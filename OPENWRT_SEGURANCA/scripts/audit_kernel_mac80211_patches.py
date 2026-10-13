#!/usr/bin/env python3
"""Auditoria diferencial de patches OpenWrt para cinco fixes Linux CVE.

Não determina explorabilidade nem homologação. Regista alterações por caminho e
pesquisa marcadores do fix mac80211 no pacote backports fixado pela release.
"""
from __future__ import annotations
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(os.environ.get("OPENWRT_TREE", "/tmp/openwrt"))
OUT = Path(os.environ.get("AUDIT_OUT", "audit-output"))
OUT.mkdir(parents=True, exist_ok=True)
TARGETS = {
    "CVE-2026-63810": "block/bdev.c",
    "CVE-2026-74665": "net/core/dev.c",
    "CVE-2026-89995": "kernel/dma/direct.c",
    "CVE-2026-98211": "drivers/mmc/host/mmci.c",
}
MAC_TARGET = "net/mac80211/spectmgmt.c"
MAC_MARKERS = [
    "new_chan_no", "new_op_class", "ieee80211_parse_ch_switch_ie",
]
patch_roots = [
    ROOT / "target/linux/generic/backport-6.12",
    ROOT / "target/linux/generic/pending-6.12",
    ROOT / "package/kernel/mac80211/patches",
]
# Include target-specific 6.12 patch directories available in the pinned tree.
for p in (ROOT / "target/linux").glob("*/patches-6.12"):
    patch_roots.append(p)
for p in (ROOT / "target/linux").glob("*/patches-6.12/*"):
    if p.is_dir():
        patch_roots.append(p)

patch_files = sorted({f for base in patch_roots if base.exists() for f in base.rglob("*.patch")})
target_hits = {cve: [] for cve in TARGETS}
mac_overlay_hits = []
for patch in patch_files:
    try:
        text = patch.read_text(errors="replace")
    except OSError:
        continue
    paths = set(re.findall(r"^diff --git a/(.*?) b/.*$", text, re.M))
    paths.update(re.findall(r"^--- a/(\\S+)", text, re.M))
    for cve, target in TARGETS.items():
        if target in paths:
            target_hits[cve].append({
                "patch": str(patch.relative_to(ROOT)),
                "target_path": target,
                "sha256": hashlib.sha256(patch.read_bytes()).hexdigest(),
            })
    if MAC_TARGET in paths or any(marker in text for marker in MAC_MARKERS):
        mac_overlay_hits.append({
            "patch": str(patch.relative_to(ROOT)),
            "changes_spectmgmt": MAC_TARGET in paths,
            "markers": [m for m in MAC_MARKERS if m in text],
            "sha256": hashlib.sha256(patch.read_bytes()).hexdigest(),
        })

makefile = ROOT / "package/kernel/mac80211/Makefile"
make_text = makefile.read_text(errors="replace") if makefile.exists() else ""
def match(pattern):
    m = re.search(pattern, make_text, re.M)
    return m.group(1).strip() if m else None
pin = {
    "version": match(r"^PKG_VERSION:=(.+)$"),
    "source": match(r"^PKG_SOURCE_URL:=(.+)$"),
    "filename": match(r"^PKG_SOURCE:=(.+)$"),
    "sha256": match(r"^PKG_HASH:=(.+)$"),
}
tarball = Path(os.environ.get("BACKPORTS_TARBALL", "/tmp/backports-6.18.26.tar.zst"))
tarball_result = {"downloaded": tarball.exists(), "expected_sha256": pin["sha256"], "actual_sha256": None, "hash_matches": False, "spectmgmt_checked": False, "markers_found": [], "archive_paths": []}
if tarball.exists():
    actual = hashlib.sha256(tarball.read_bytes()).hexdigest()
    tarball_result["actual_sha256"] = actual
    tarball_result["hash_matches"] = bool(pin["sha256"] and actual == pin["sha256"])
    if tarball_result["hash_matches"]:
        listing = subprocess.run(["tar", "--zstd", "-tf", str(tarball)], capture_output=True, text=True)
        if listing.returncode == 0:
            paths = listing.stdout.splitlines()
            matches = [p for p in paths if p.endswith("/spectmgmt.c") or p == "net/mac80211/spectmgmt.c"]
            tarball_result["archive_paths"] = matches[:20]
            extracted = ""
            for member in matches:
                proc = subprocess.run(["tar", "--zstd", "-xOf", str(tarball), member], capture_output=True, text=True)
                if proc.returncode == 0:
                    extracted += proc.stdout
            tarball_result["spectmgmt_checked"] = bool(matches)
            tarball_result["markers_found"] = [m for m in MAC_MARKERS if m in extracted]

result = {
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "upstream_tag": "v25.12.5",
    "patch_roots_scanned": [str(p.relative_to(ROOT)) for p in patch_roots if p.exists()],
    "generic_patch_count": sum(1 for base in patch_roots[:2] if base.exists() for _ in base.rglob("*.patch")),
    "all_patch_count_scanned": len(patch_files),
    "target_file_patch_hits": target_hits,
    "mac80211_overlay_candidates": mac_overlay_hits,
    "mac80211_pin": pin,
    "backports_tarball": tarball_result,
    "interpretation": {
        "target_file_hits": "Patch path-level hits only; each hit requires semantic hunk review. No hit does not prove equivalent changes cannot be implemented through other files.",
        "mac80211": "Markers are indicators, not a full semantic proof. A checksum mismatch or unavailable archive means the tarball result is inconclusive.",
        "hardware": "No router target is inferred; target-specific applicability requires a verified hardware model/revision.",
    },
}
(OUT / "kernel-mac80211-audit.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
lines = [
    "# OpenWrt kernel/mac80211 differential scan",
    "",
    f"- Generated UTC: {result['generated_utc']}",
    f"- OpenWrt tag: `{result['upstream_tag']}`",
    f"- Generic patches scanned: {result['generic_patch_count']}",
    f"- Total patches scanned (generic + discovered target-specific): {result['all_patch_count_scanned']}",
    f"- mac80211 pin version: {pin['version']}",
    f"- Backports archive downloaded: {tarball_result['downloaded']}",
    f"- Backports SHA-256 matches Makefile: {tarball_result['hash_matches']}",
    f"- Archive `spectmgmt.c` inspected: {tarball_result['spectmgmt_checked']}",
    f"- CSA fix markers found: {', '.join(tarball_result['markers_found']) if tarball_result['markers_found'] else 'none detected / inconclusive if source not inspected'}",
    "",
    "## Exact target-path patch hits",
]
for cve, hits in target_hits.items():
    lines.append(f"### {cve} — `{TARGETS[cve]}`")
    if hits:
        lines.extend(f"- `{h['patch']}` (SHA-256 `{h['sha256']}`)" for h in hits)
    else:
        lines.append("- No patch changes this exact path in the scanned patch set.")
        lines.append("- This is not, by itself, proof that no semantically equivalent fix exists.")
lines.extend(["", "## mac80211 overlay candidates"])
if mac_overlay_hits:
    lines.extend(f"- `{h['patch']}`: spectmgmt={h['changes_spectmgmt']}; markers={h['markers']}" for h in mac_overlay_hits)
else:
    lines.append("- No exact-file/marker candidate found in scanned patch files.")
lines.extend(["", "## Limitations", "- Path-level scan is a triage aid, not a semantic equivalence proof.", "- CVE states must remain inconclusive until relevant hunks/source are reviewed.", "- No device-specific target, firmware build, router modification, or lab/homologation test is implied.", "- Zabbix remains paused."])
(OUT / "kernel-mac80211-audit.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
