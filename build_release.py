"""Build a single-file Windows installer for LUMPT."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILD = ROOT / "build"
SPEC = ROOT / "build" / "install_lumpt.spec"


def run(cmd: list[str]) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    print("Instalando dependências do empacotamento...")
    run([sys.executable, "-m", "pip", "install", "pyinstaller"])

    print("Removendo artefatos antigos...")
    for path in (DIST, BUILD):
        if path.exists():
            shutil.rmtree(path)
    if SPEC.exists():
        SPEC.unlink()

    pyinstaller_cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--name",
        "LUMPT_Installer",
        "--distpath",
        str(DIST),
        "--workpath",
        str(BUILD),
        "--specpath",
        str(BUILD),
        "--collect-all",
        "lumpt",
        "--add-data",
        str(ROOT / "main.py") + os.pathsep + ".",
        "--add-data",
        str(ROOT / "README.md") + os.pathsep + ".",
        "--add-data",
        str(ROOT / "requirements.txt") + os.pathsep + ".",
        "--add-data",
        str(ROOT / "lumpt") + os.pathsep + "lumpt",
        str(ROOT / "installer" / "install_lumpt.py"),
    ]

    run(pyinstaller_cmd)
    output = DIST / "LUMPT_Installer.exe"
    if output.exists():
        print(f"Instalador pronto: {output}")
    else:
        raise FileNotFoundError(f"Arquivo não encontrado após build: {output}")


if __name__ == "__main__":
    main()
