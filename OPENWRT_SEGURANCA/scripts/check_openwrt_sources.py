#!/usr/bin/env python3
"""Validate the OpenWrt source catalog and check official links.

Network failures and HTTP error responses are reported but do not fail the job:
wiki pages can rate-limit automated clients. Invalid catalog entries do fail.
Only URLs on openwrt.org and its subdomains are accepted by this first version.
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
URL_RE = re.compile(r"https://openwrt\.org[^\s|)]+", re.IGNORECASE)
USER_AGENT = "XFI-OpenWrt-SourceCatalogCheck/1.0 (+https://github.com/carlos-andrade/XFI)"
TIMEOUT_SECONDS = 15
PAUSE_SECONDS = 0.5


def official_url(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and (host == "openwrt.org" or host.endswith(".openwrt.org"))


def check_url(url: str) -> dict[str, object]:
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return {
                "url": url,
                "status": int(response.status),
                "final_url": response.geturl(),
                "result": "reachable" if 200 <= response.status < 400 else "http_error",
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
    urls = sorted(set(URL_RE.findall(content)))
    if not urls:
        print("ERROR: no official OpenWrt URLs found in catalog", file=sys.stderr)
        return 2

    invalid = [url for url in urls if not official_url(url)]
    if invalid:
        print("ERROR: non-allowlisted URL(s): " + ", ".join(invalid), file=sys.stderr)
        return 2

    results = []
    for index, url in enumerate(urls):
        results.append(check_url(url))
        if index + 1 < len(urls):
            time.sleep(PAUSE_SECONDS)

    reachable = sum(1 for item in results if item["result"] == "reachable")
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalog": str(CATALOG.relative_to(ROOT)),
        "total_unique_urls": len(urls),
        "reachable": reachable,
        "http_errors": sum(1 for item in results if item["result"] == "http_error"),
        "network_errors": sum(1 for item in results if item["result"] == "network_error"),
        "note": "Reachability is not a content/security validation. HTTP/network errors may reflect rate limiting; review manually.",
        "results": results,
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "generated_at_utc", "catalog", "total_unique_urls", "reachable",
        "http_errors", "network_errors"
    )}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
