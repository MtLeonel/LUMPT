"""Instalador do LUMPT - copia e configura a aplicação no computador do usuário."""

import argparse
import os
import shutil
import subprocess
import sys
import tkinter as tk
import zipfile
from pathlib import Path
from tkinter import BooleanVar, StringVar, filedialog, ttk

INSTALLER_DIR = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
PROJECT_ROOT = INSTALLER_DIR.parent
DEFAULT_INSTALL_DIR = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "LUMPT"
DESKTOP_DIR = Path.home() / "Desktop"
START_MENU_DIR = (
    Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    / "Microsoft"
    / "Windows"
    / "Start Menu"
    / "Programs"
    / "LUMPT"
)


def resolve_bundle_dir():
    """Resolver o diretório do bundle do programa."""
    candidates = [
        PROJECT_ROOT / "lumpt",
        INSTALLER_DIR / "lumpt",
    ]

    for candidate in candidates:
        if candidate.exists() and (candidate / "app.py").exists():
            return candidate

    return PROJECT_ROOT / "lumpt"


APP_BUNDLE_DIR = resolve_bundle_dir()


def ensure_python_dependency():
    """Verificar se Tkinter está disponível."""
    try:
        import tkinter
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Python com Tkinter não encontrado. "
            "Instale o Python 3.7+ com Tcl/Tk habilitado."
        ) from exc


def create_shortcut(target_path, shortcut_path):
    """Criar atalho para executável (Windows)."""
    shortcut_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import win32com.client
    except ModuleNotFoundError:
        fallback_path = shortcut_path.with_suffix(".cmd")
        fallback_path.write_text(
            "@echo off\nstart \"\" \"{}\"\n".format(str(target_path)),
            encoding="utf-8",
        )
        return

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.Targetpath = str(target_path)
    shortcut.WorkingDirectory = str(target_path.parent)
    shortcut.IconLocation = str(target_path)
    shortcut.save()


def create_desktop_shortcut(target_path):
    """Criar atalho na área de trabalho."""
    DESKTOP_DIR.mkdir(parents=True, exist_ok=True)
    create_shortcut(target_path, DESKTOP_DIR / "LUMPT.lnk")


def create_start_menu_shortcut(target_path):
    """Criar atalho no menu Iniciar."""
    START_MENU_DIR.mkdir(parents=True, exist_ok=True)
    create_shortcut(target_path, START_MENU_DIR / "LUMPT.lnk")


def copy_bundle_contents(bundle_dir, install_dir):
    """Copiar conteúdo do programa para diretório de instalação."""
    install_dir.mkdir(parents=True, exist_ok=True)

    lumpt_dest = install_dir / "lumpt"
    if lumpt_dest.exists():
        shutil.rmtree(lumpt_dest)

    shutil.copytree(bundle_dir, lumpt_dest, dirs_exist_ok=True)


def create_zip_bundle(install_dir):
    """Criar arquivo ZIP do programa para backup."""
    archive_path = install_dir / "LUMPT_Backup.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(install_dir):
            dirs[:] = [d for d in dirs if d not in {"__pycache__"}]
            for file_name in files:
                if file_name == archive_path.name:
                    continue
                file_path = Path(root) / file_name
                archive.write(file_path, file_path.relative_to(install_dir).as_posix())


def install_app(install_dir, create_shortcut_flag):
    """Instalar a aplicação LUMPT."""
    if not APP_BUNDLE_DIR.exists():
        raise FileNotFoundError(
            "A pasta do programa não foi encontrada no instalador."
        )

    install_dir.mkdir(parents=True, exist_ok=True)
    copy_bundle_contents(APP_BUNDLE_DIR, install_dir)

    main_py_src = PROJECT_ROOT / "main.py"
    if main_py_src.exists():
        shutil.copy2(main_py_src, install_dir / "main.py")

    launcher_path = install_dir / "LUMPT.cmd"
    launcher_path.write_text(
        "@echo off\nsetlocal\ncd /d \"%~dp0\"\npython main.py\nendlocal\n",
        encoding="utf-8",
    )

    create_zip_bundle(install_dir)

    if create_shortcut_flag:
        create_desktop_shortcut(launcher_path)
        create_start_menu_shortcut(launcher_path)


def parse_args():
    """Parser de argumentos da linha de comando."""
    parser = argparse.ArgumentParser(description="Instalador do LUMPT")
    parser.add_argument("--install-dir", default=None, help="Pasta de instalação")
    parser.add_argument("--no-shortcut", action="store_true", help="Sem atalhos")
    return parser.parse_args()


def build_gui():
    """Construir e exibir interface gráfica do instalador."""
    ensure_python_dependency()

    root = tk.Tk()
    root.title("Instalador LUMPT")
    root.geometry("600x360")
    root.resizable(False, False)

    install_dir_var = StringVar(value=str(DEFAULT_INSTALL_DIR))
    shortcut_var = BooleanVar(value=True)
    status_var = StringVar(value="Clique em Instalar para começar.")

    ttk.Label(root, text="Instalador LUMPT", font=("MS Sans Serif", 14, "bold")).pack(
        anchor="w", padx=16, pady=(16, 8)
    )
    ttk.Label(
        root,
        text="Um clique para instalar o LUMPT em seu computador.",
        wraplength=560,
    ).pack(anchor="w", padx=16, pady=(0, 8))

    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Pasta de instalação:").grid(row=0, column=0, sticky="w")
    entry = ttk.Entry(frame, textvariable=install_dir_var, width=56)
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(4, 8))
    ttk.Button(
        frame,
        text="Procurar",
        command=lambda: install_dir_var.set(
            filedialog.askdirectory(initialdir=str(DEFAULT_INSTALL_DIR)) or install_dir_var.get()
        ),
    ).grid(row=1, column=2, padx=(8, 0), sticky="w")

    ttk.Checkbutton(frame, text="Criar atalho na área de trabalho", variable=shortcut_var).grid(
        row=2, column=0, columnspan=3, sticky="w", pady=(4, 12)
    )

    status_label = ttk.Label(frame, textvariable=status_var, wraplength=560)
    status_label.grid(row=3, column=0, columnspan=3, sticky="w", pady=(0, 8))

    def install():
        install_dir = Path(install_dir_var.get()).expanduser().resolve()
        if not str(install_dir):
            status_var.set("Selecione uma pasta válida.")
            return

        try:
            install_app(install_dir, bool(shortcut_var.get()))
            status_var.set("Instalação concluída! Instale em: {}".format(str(install_dir)))
            root.update_idletasks()
            try:
                subprocess.Popen([str(install_dir / "LUMPT.cmd")], shell=True)
            except Exception:
                pass
        except Exception as exc:
            status_var.set("Erro ao instalar: {}".format(str(exc)))

    ttk.Button(frame, text="Instalar", command=install).grid(row=4, column=0, sticky="w", pady=(8, 0))
    ttk.Button(frame, text="Fechar", command=root.destroy).grid(
        row=4, column=1, padx=(8, 0), sticky="w", pady=(8, 0)
    )

    frame.columnconfigure(0, weight=1)
    root.mainloop()


def main():
    """Função principal: parse argumentos e executa instalação."""
    args = parse_args()
    if args.install_dir or args.no_shortcut:
        install_dir = (
            Path(args.install_dir).expanduser().resolve()
            if args.install_dir
            else DEFAULT_INSTALL_DIR
        )
        install_app(install_dir, not args.no_shortcut)
        print("Instalação concluída em: {}".format(str(install_dir)))
        return
    build_gui()


if __name__ == "__main__":
    main()
