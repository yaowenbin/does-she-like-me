#!/usr/bin/env python3
"""Lightweight redaction for pasted chat logs — offline, stdlib only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# CN mobile rough pattern (11 digits, 1[3-9]...)
_PHONE = re.compile(
    r"(?<!\d)(?:\+?86[\s-]?)?1[3-9]\d{9}(?!\d)",
)
# loose WeChat-style wxid (not exhaustive)
_WXID = re.compile(r"(?i)\bwxid_[a-z0-9_-]{6,}\b")
# consecutive digits that look like phone fragments
_LONG_DIGITS = re.compile(r"\b\d{11,}\b")


def redact(text: str) -> str:
    out = _PHONE.sub("[REDACTED-PHONE]", text)
    out = _WXID.sub("[REDACTED-WXID]", out)
    out = _LONG_DIGITS.sub("[REDACTED-DIGITS]", out)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Redact phones / long digit runs / wxid-like tokens.")
    p.add_argument("--input", "-i", required=True, help="Input text file")
    p.add_argument("--output", "-o", help="Output file (default: stdout)")
    args = p.parse_args()
    path = Path(args.input)
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 1
    raw = path.read_text(encoding="utf-8", errors="replace")
    done = redact(raw)
    if args.output:
        Path(args.output).write_text(done, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(done)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
