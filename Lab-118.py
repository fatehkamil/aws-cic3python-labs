#!/usr/bin/env python3
"""Lab-118.py
Clean preproinsulin-seq.txt and extract insulin segments into files.

Creates:
- preproinsulin-seq-clean.txt (contains: preproinsulin = "<sequence>")
- lsinsulin-seq.txt, binsulin-seq.txt, ainsulin-seq.txt, cinsulin-seq.txt
"""

import re
from pathlib import Path
import sys

ROOT = Path(__file__).parent
INPUT = ROOT / "preproinsulin-seq.txt"
CLEAN = ROOT / "preproinsulin-seq-clean.txt"
LS_OUT = ROOT / "lsinsulin-seq.txt"
B_OUT = ROOT / "binsulin-seq.txt"
A_OUT = ROOT / "ainsulin-seq.txt"
C_OUT = ROOT / "cinsulin-seq.txt"

def clean_sequence(text: str) -> str:
	parts = re.findall(r"[A-Za-z]+", text)
	parts = [p for p in parts if p.lower() != "origin"]
	return "".join(parts).lower()

def write_assignment(path: Path, name: str, seq: str) -> None:
	path.write_text(f'{name} = "{seq}"\n')

def write_sequence(path: Path, seq: str) -> None:
	path.write_text(seq + "\n")

def main() -> None:
	if not INPUT.exists():
		print(f"Input file not found: {INPUT}", file=sys.stderr)
		sys.exit(1)

	raw = INPUT.read_text()
	seq = clean_sequence(raw)
	write_sequence(CLEAN, seq)

	# Known segment lengths for human preproinsulin
	LS_LEN = 24
	B_LEN = 30
	C_LEN = 35
	A_LEN = 21

	total_expected = LS_LEN + B_LEN + C_LEN + A_LEN
	if len(seq) < total_expected:
		print(f"Cleaned sequence too short ({len(seq)}); expected at least {total_expected}", file=sys.stderr)
		sys.exit(1)

	lsinsulin = seq[0:LS_LEN]
	binsulin = seq[LS_LEN:LS_LEN+B_LEN]
	cinsulin = seq[LS_LEN+B_LEN:LS_LEN+B_LEN+C_LEN]
	ainsulin = seq[LS_LEN+B_LEN+C_LEN:LS_LEN+B_LEN+C_LEN+A_LEN]

	write_sequence(LS_OUT, lsinsulin)
	write_sequence(B_OUT, binsulin)
	write_sequence(A_OUT, ainsulin)
	write_sequence(C_OUT, cinsulin)

	print(f"Wrote cleaned sequence to: {CLEAN}")
	print("Wrote segment files:")
	for p in (LS_OUT, B_OUT, A_OUT, C_OUT):
		print(" -", p.name)

if __name__ == "__main__":
	main()
