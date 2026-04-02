#!/usr/bin/env python3
"""Split a long chat log into chunk files — offline, stdlib only."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def chunk_by_lines(text: str, lines_per_chunk: int) -> list[str]:
    lines = text.splitlines()
    if lines_per_chunk <= 0:
        return [text]
    out: list[str] = []
    for i in range(0, len(lines), lines_per_chunk):
        block = "\n".join(lines[i : i + lines_per_chunk])
        out.append(block)
    return out if out else [""]


def main() -> int:
    p = argparse.ArgumentParser(description="Split text into fixed line-count chunks.")
    p.add_argument("--input", "-i", required=True)
    p.add_argument("--lines", "-n", type=int, default=80, help="Lines per chunk")
    p.add_argument("--out-dir", "-d", required=True, help="Directory for chunk-NNN.txt")
    args = p.parse_args()
    src = Path(args.input)
    if not src.is_file():
        print(f"not a file: {src}", file=sys.stderr)
        return 1
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw = src.read_text(encoding="utf-8", errors="replace")
    chunks = chunk_by_lines(raw, args.lines)
    for idx, block in enumerate(chunks, start=1):
        (out_dir / f"chunk-{idx:03d}.txt").write_text(
            block + ("\n" if block and not block.endswith("\n") else ""),
            encoding="utf-8",
            newline="\n",
        )
    print(f"wrote {len(chunks)} file(s) to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
