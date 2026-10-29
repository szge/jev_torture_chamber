#!/usr/bin/env python3
"""Send a request file to the TypeSafe API and save the raw response beside it.

Usage: python3 run.py <group_dir>/<name>.json

Writes <group_dir>/<name>.<timestamp>.response.json containing the response
body byte-for-byte, and prints it to stdout. Non-2xx responses are saved as
<name>.<timestamp>.error.json and exit non-zero.
"""
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://api.typesafe.ai/v1/systemone"


def load_key() -> str:
    key = os.environ.get("TYPESAFE_API_KEY")
    if key:
        return key
    for line in (Path(__file__).parent / ".env").read_text().splitlines():
        name, _, value = line.partition("=")
        if name.strip() == "TYPESAFE_API_KEY":
            return value.strip().strip("\"'")
    sys.exit("TYPESAFE_API_KEY not found in environment or .env")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    request_file = Path(sys.argv[1])
    payload = request_file.read_bytes()
    req = urllib.request.Request(
        URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {load_key()}",
            "Content-Type": "application/json",
        },
    )
    status = 0
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body, suffix = resp.read(), "response"
    except urllib.error.HTTPError as e:
        body, suffix, status = e.read(), "error", 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = request_file.with_name(f"{request_file.stem}.{stamp}.{suffix}.json")
    out.write_bytes(body)
    sys.stdout.buffer.write(body + b"\n")
    print(f"saved: {out}", file=sys.stderr)
    sys.exit(status)


if __name__ == "__main__":
    main()
