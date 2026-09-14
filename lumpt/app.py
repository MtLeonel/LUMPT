"""Interface principal do LUMPT com abas de funcionalidades."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

# Imports dos módulos de view
from lumpt.views.editor import EditorTab
from lumpt.views.minigames import MinigamesTab
from lumpt.views.courses import CoursesTab
from lumpt.views.free_code import FreeCodeTab
from lumpt.views.credits import CreditsTab
from lumpt.views.microcontrollers import MicrocontrollersTab
from lumpt.views.profile import ProfileTab


class LumptApp(tk.Tk):
    """Aplicação principal do LUMPT com interface de abas."""

    def __init__(self) -> None:
        super().__init__()
        self.title("LUMPT - Educação em Lógica de Programação")
        self.geometry("900x600")
        self.resizable(True, True)
        
        # Configurar estilo
        self.configure(bg="#f0f0f0")
        
        # Criar frame principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Criar notebook (abas)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill="both", expand=True, padx=4, pady=4)
        
        # Inicializar abas
        self._create_tabs()
        
    def _create_tabs(self) -> None:
        """Criar e adicionar todas as abas do aplicativo."""
        try:
            # Aba 1: Tradutor de Lógica (principal)
            editor_tab = EditorTab(self.notebook)
            self.notebook.add(editor_tab, text="Tradutor de Lógica")
            
            # Aba 2: Código Livre
            free_code_tab = FreeCodeTab(self.notebook)
            self.notebook.add(free_code_tab, text="Código Livre")
            
            # Aba 3: Mini-games
            minigames_tab = MinigamesTab(self.notebook)
            self.notebook.add(minigames_tab, text="Mini-games")
            
            # Aba 4: Cursos
            courses_tab = CoursesTab(self.notebook)
            self.notebook.add(courses_tab, text="Cursos")
            
            # Aba 5: Microcontroladores
            microcontrollers_tab = MicrocontrollersTab(self.notebook)
            self.notebook.add(microcontrollers_tab, text="Microcontroladores")
            
            # Aba 6: Perfil
            profile_tab = ProfileTab(self.notebook)
            self.notebook.add(profile_tab, text="Perfil")
            
            # Aba 7: Créditos
            credits_tab = CreditsTab(self.notebook)
            self.notebook.add(credits_tab, text="Créditos")
            
        except Exception as exc:
            # Se alguma aba falhar ao carregar, exibir erro mas continuar
            error_label = ttk.Label(self.notebook, text=f"Erro ao carregar interface: {exc}")
            error_label.pack(padx=16, pady=16)
            raise

    def run(self) -> None:
        """Iniciar o loop principal da aplicação."""
        self.mainloop()


def run() -> None:
    """Função de entrada: criar e executar a aplicação LUMPT."""
    try:
        app = LumptApp()
        app.run()
    except Exception as exc:
        # Fallback: mensagem de erro em terminal se GUI falhar completamente
        print(f"Erro ao executar LUMPT: {exc}")
        raise