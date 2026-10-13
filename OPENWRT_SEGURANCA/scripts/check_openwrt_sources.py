#!/usr/bin/env python3
"""Validate the XFI OpenWrt source catalog and check approved official URLs.

The report records source metadata and HTTP reachability. Reachability is not a
content, freshness, applicability, or security assessment.
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "OPENWRT_SEGURANCA" / "FONTES_OFICIAIS.md"
REPORT = ROOT / "openwrt-source-check-report.json"
URL_RE = re.compile(r"https://[^\s|)<>]+", re.IGNORECASE)
USER_AGENT = "XFI-OpenWrt-SourceCatalogCheck/1.1 (+https://github.com/carlos-andrade/XFI)"
TIMEOUT_SECONDS = 15
PAUSE_SECONDS = 0.5


def official_url(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https":
        return False
    if host == "openwrt.org" or host.endswith(".openwrt.org"):
        return True
    # Limit GitHub checks to the upstream OpenWrt organization/repository.
    return host == "github.com" and parsed.path.lower().startswith("/openwrt/")


def parse_catalog(content: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for line_number, line in enumerate(content.splitlines(), start=1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in {"tema", "---"}:
            continue
        if set(cells[0]) <= {"-", ":"}:
            continue
        match = URL_RE.search(cells[1])
        if not match:
            continue
        url = match.group(0).rstrip(".,;")
        records.append({
            "category": cells[0],
            "url": url,
            "purpose": cells[2],
            "catalog_line": str(line_number),
        })
    # De-duplicate by canonical URL while retaining the first catalog record.
    unique: dict[str, dict[str, str]] = {}
    for record in records:
        unique.setdefault(record["url"], record)
    return list(unique.values())


def check_url(url: str) -> dict[str, object]:
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            status = int(response.status)
            return {
                "url": url,
                "status": status,
                "final_url": response.geturl(),
                "result": "reachable" if 200 <= status < 400 else "http_error",
                "detail": "",
            }
    except HTTPError as exc:
        return {
            "url": url,
            "status": int(exc.code),
            "final_url": exc.geturl(),
            "result": "http_error",
            "detail": str(exc.reason),
        }
    except (URLError, TimeoutError, OSError) as exc:
        return {
            "url": url,
            "status": None,
            "final_url": None,
            "result": "network_error",
            "detail": str(exc)[:300],
        }


def main() -> int:
    if not CATALOG.is_file():
        print(f"ERROR: source catalog not found: {CATALOG}", file=sys.stderr)
        return 2

    content = CATALOG.read_text(encoding="utf-8")
    sources = parse_catalog(content)
    if not sources:
        print("ERROR: no source-table URLs found in catalog", file=sys.stderr)
        return 2

    invalid = [source["url"] for source in sources if not official_url(source["url"])]
    if invalid:
        print("ERROR: non-allowlisted URL(s): " + ", ".join(invalid), file=sys.stderr)
        return 2

    results_by_url: dict[str, dict[str, object]] = {}
    for index, source in enumerate(sources):
        results_by_url[source["url"]] = check_url(source["url"])
        if index + 1 < len(sources):
            time.sleep(PAUSE_SECONDS)

    results = []
    for source in sources:
        result = results_by_url[source["url"]]
        results.append({
            **source,
            **result,
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "review_status": "reachability_checked_content_review_pending",
        })

    reachable = sum(1 for item in results if item["result"] == "reachable")
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalog": str(CATALOG.relative_to(ROOT)),
        "schema_version": "1.0",
        "total_unique_urls": len(results),
        "reachable": reachable,
        "http_errors": sum(1 for item in results if item["result"] == "http_error"),
        "network_errors": sum(1 for item in results if item["result"] == "network_error"),
        "note": "HTTP reachability is not content/security validation. Review each source for freshness, relevance, affected versions, and remediation.",
        "sources": results,
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = {key: report[key] for key in (
        "generated_at_utc", "catalog", "schema_version", "total_unique_urls",
        "reachable", "http_errors", "network_errors"
    )}
    summary["failures"] = [
        {"url": item["url"], "status": item["status"], "result": item["result"], "detail": item["detail"]}
        for item in results if item["result"] != "reachable"
    ]
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
