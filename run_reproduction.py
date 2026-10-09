#!/usr/bin/env python3
"""Verify and execute the frozen R15 Tetouan reproducibility archive."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ARCHIVE_NAME = "CERT_Bench_ESWA_R15_Anonymous_Reproducibility_Package.zip"
ARCHIVE_SHA256 = "19f894d6e0772e3971eb26c5ca91cc796955ffa9c9b5ca647cd65e609e30163e"


def main() -> None:
    archive = Path(__file__).resolve().parent / "artifacts" / ARCHIVE_NAME
    if not archive.is_file():
        raise SystemExit(f"Missing archive: {archive}")
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != ARCHIVE_SHA256:
        raise SystemExit("Reproducibility archive SHA-256 does not match frozen R15")

    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise SystemExit("ZIP integrity check failed")
        checks = z.read("SHA256SUMS.txt").decode("utf-8").splitlines()
        for line in checks:
            digest, relative_path = line.split("  ", 1)
            if hashlib.sha256(z.read(relative_path)).hexdigest() != digest:
                raise SystemExit(f"Manifest mismatch: {relative_path}")
        with tempfile.TemporaryDirectory(prefix="cert_bench_r15_") as folder:
            z.extractall(folder)
            print(f"Archive and manifest verified ({len(checks)} entries)", flush=True)
            subprocess.run(
                [sys.executable, "reproduce_tetouan_sensitivity.py"],
                cwd=folder,
                check=True,
            )


if __name__ == "__main__":
    main()
