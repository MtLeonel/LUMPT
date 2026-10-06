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


def run(cmd):
    """Execute command."""
    print("$ " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def main():
    """Build the installer."""
    print("Instalando PyInstaller...")
    run([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])

    print("Limpando artefatos antigos...")
    for path in (DIST, BUILD):
        if path.exists():
            shutil.rmtree(path)
    if SPEC.exists():
        SPEC.unlink()

    print("Gerando instalador...")
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
        print("\n✓ Instalador gerado com sucesso!")
        print("  Arquivo: {}".format(str(output)))
        print("  Tamanho: {:.2f} MB".format(output.stat().st_size / (1024 * 1024)))
    else:
        raise FileNotFoundError("Arquivo não encontrado: {}".format(str(output)))


if __name__ == "__main__":
    main()
