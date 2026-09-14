"""Testes para validar a estrutura e funcionamento básico do LUMPT."""

from __future__ import annotations

import sys
from pathlib import Path

# Adicionar raiz ao path para importações
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def test_lumpt_package_exists() -> None:
    """Verificar se pacote lumpt/ existe e pode ser importado."""
    lumpt_dir = PROJECT_ROOT / "lumpt"
    assert lumpt_dir.exists(), f"Pasta 'lumpt/' não encontrada em {PROJECT_ROOT}"
    assert (lumpt_dir / "__init__.py").exists(), "lumpt/__init__.py não encontrado"


def test_lumpt_app_module_exists() -> None:
    """Verificar se app.py existe em lumpt/."""
    app_file = PROJECT_ROOT / "lumpt" / "app.py"
    assert app_file.exists(), f"Arquivo 'lumpt/app.py' não encontrado em {PROJECT_ROOT}"


def test_lumpt_views_package_exists() -> None:
    """Verificar se pacote views/ existe."""
    views_dir = PROJECT_ROOT / "lumpt" / "views"
    assert views_dir.exists(), f"Pasta 'lumpt/views/' não encontrada em {PROJECT_ROOT}"
    assert (views_dir / "__init__.py").exists(), "lumpt/views/__init__.py não encontrado"


def test_lumpt_views_files_exist() -> None:
    """Verificar se todos os arquivos de view estão presentes."""
    views_dir = PROJECT_ROOT / "lumpt" / "views"
    required_views = [
        "editor.py",
        "minigames.py",
        "courses.py",
        "free_code.py",
        "credits.py",
        "microcontrollers.py",
        "profile.py",
    ]
    
    for view_file in required_views:
        view_path = views_dir / view_file
        assert view_path.exists(), f"Arquivo 'lumpt/views/{view_file}' não encontrado"


def test_lumpt_can_import() -> None:
    """Verificar se a aplicação pode ser importada sem erros."""
    try:
        from lumpt.app import run, LumptApp  # noqa: F401
    except ImportError as exc:
        raise AssertionError(f"Falha ao importar lumpt: {exc}") from exc


def test_installer_files_exist() -> None:
    """Verificar se arquivos do instalador existem."""
    installer_file = PROJECT_ROOT / "installer" / "install_lumpt.py"
    assert installer_file.exists(), "Arquivo 'installer/install_lumpt.py' não encontrado"
    
    cmd_file = PROJECT_ROOT / "installer" / "install_lumpt.cmd"
    assert cmd_file.exists(), "Arquivo 'installer/install_lumpt.cmd' não encontrado"


def test_main_entry_point_exists() -> None:
    """Verificar se main.py existe e contém função main()."""
    main_file = PROJECT_ROOT / "main.py"
    assert main_file.exists(), "Arquivo 'main.py' não encontrado na raiz"
    
    # Verificar se contém 'def main()'
    main_content = main_file.read_text()
    assert "def main()" in main_content, "main.py não contém função main()"


def test_ai_context_file_exists() -> None:
    """Verificar se arquivo de contexto de IA existe."""
    ai_context_dir = PROJECT_ROOT / "ai_context"
    assert ai_context_dir.exists(), f"Pasta 'ai_context/' não encontrada em {PROJECT_ROOT}"
    
    ai_context_file = ai_context_dir / "ai_context.txt"
    assert ai_context_file.exists(), "Arquivo 'ai_context/ai_context.txt' não encontrado"


def test_requirements_exists() -> None:
    """Verificar se requirements.txt existe."""
    requirements_file = PROJECT_ROOT / "requirements.txt"
    assert requirements_file.exists(), "Arquivo 'requirements.txt' não encontrado na raiz"


if __name__ == "__main__":
    # Executar testes simples
    test_lumpt_package_exists()
    test_lumpt_app_module_exists()
    test_lumpt_views_package_exists()
    test_lumpt_views_files_exist()
    test_lumpt_can_import()
    test_installer_files_exist()
    test_main_entry_point_exists()
    test_ai_context_file_exists()
    test_requirements_exists()
    
    print("✅ Todos os testes de estrutura passaram!")