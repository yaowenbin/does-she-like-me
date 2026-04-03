#!/usr/bin/env python3
"""Lightweight redaction for pasted chat logs — offline, stdlib only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_PHONE = re.compile(
    r"(?<!\d)(?:\+?86[\s-]?)?1[3-9]\d{9}(?!\d)",
)
_WXID = re.compile(r"(?i)\bwxid_[a-z0-9_-]{6,}\b")
_LONG_DIGITS = re.compile(r"\b\d{11,}\b")
_EMAIL = re.compile(r"(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b")


def redact(text: str) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    out, counts["phone"] = _PHONE.subn("[REDACTED-PHONE]", text)
    out, counts["wxid"] = _WXID.subn("[REDACTED-WXID]", out)
    out, counts["email"] = _EMAIL.subn("[REDACTED-EMAIL]", out)
    out, counts["digits"] = _LONG_DIGITS.subn("[REDACTED-DIGITS]", out)
    return out, counts


def main() -> int:
    p = argparse.ArgumentParser(description="Redact phones / long digits / wxid / email.")
    p.add_argument("--input", "-i", required=True, help="Input text file")
    group = p.add_mutually_exclusive_group()
    group.add_argument("--output", "-o", help="Output file")
    group.add_argument("--inplace", action="store_true", help="Rewrite input file")
    p.add_argument("--summary", action="store_true", help="Print replacement summary to stderr")
    args = p.parse_args()
    path = Path(args.input)
    if not path.is_file():
        print(f"not a file: {path}", file=sys.stderr)
        return 1
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"read failed: {exc}", file=sys.stderr)
        return 1
    done, counts = redact(raw)
    try:
        if args.inplace:
            path.write_text(done, encoding="utf-8", newline="\n")
        elif args.output:
            Path(args.output).write_text(done, encoding="utf-8", newline="\n")
        else:
            sys.stdout.write(done)
    except OSError as exc:
        print(f"write failed: {exc}", file=sys.stderr)
        return 1
    if args.summary:
        print(
            "replaced "
            + ", ".join(
                [
                    f"phone={counts['phone']}",
                    f"wxid={counts['wxid']}",
                    f"email={counts['email']}",
                    f"digits={counts['digits']}",
                ]
            ),
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
