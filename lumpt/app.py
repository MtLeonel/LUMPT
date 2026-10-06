"""Interface principal do LUMPT com abas de funcionalidades."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from lumpt.views.editor import EditorTab
    from lumpt.views.minigames import MinigamesTab
    from lumpt.views.courses import CoursesTab
    from lumpt.views.free_code import FreeCodeTab
    from lumpt.views.credits import CreditsTab
    from lumpt.views.microcontrollers import MicrocontrollersTab
    from lumpt.views.profile import ProfileTab
except ImportError as e:
    raise SystemExit("Erro ao importar módulos: {}".format(str(e)))


class LumptApp(tk.Tk):
    """Aplicação principal do LUMPT com interface de abas."""

    def __init__(self):
        super(LumptApp, self).__init__()
        self.title("LUMPT - Educação em Lógica de Programação")
        self.geometry("900x600")
        self.resizable(True, True)
        self.configure(bg="#f0f0f0")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill="both", expand=True, padx=4, pady=4)

        self._create_tabs()

    def _create_tabs(self):
        """Criar e adicionar todas as abas do aplicativo."""
        try:
            editor_tab = EditorTab(self.notebook)
            self.notebook.add(editor_tab, text="Tradutor de Lógica")

            free_code_tab = FreeCodeTab(self.notebook)
            self.notebook.add(free_code_tab, text="Código Livre")

            minigames_tab = MinigamesTab(self.notebook)
            self.notebook.add(minigames_tab, text="Mini-games")

            courses_tab = CoursesTab(self.notebook)
            self.notebook.add(courses_tab, text="Cursos")

            microcontrollers_tab = MicrocontrollersTab(self.notebook)
            self.notebook.add(microcontrollers_tab, text="Microcontroladores")

            profile_tab = ProfileTab(self.notebook)
            self.notebook.add(profile_tab, text="Perfil")

            credits_tab = CreditsTab(self.notebook)
            self.notebook.add(credits_tab, text="Créditos")

        except Exception as exc:
            error_label = ttk.Label(
                self.notebook,
                text="Erro ao carregar interface: {}".format(str(exc))
            )
            error_label.pack(padx=16, pady=16)
            raise

    def run(self):
        """Iniciar o loop principal da aplicação."""
        self.mainloop()


def run():
    """Função de entrada: criar e executar a aplicação LUMPT."""
    try:
        app = LumptApp()
        app.run()
    except Exception as exc:
        print("Erro ao executar LUMPT: {}".format(str(exc)))
        raise
