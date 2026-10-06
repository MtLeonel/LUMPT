"""Aba Cursos - Espaço para divulgação de cursos e conteúdos."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class CoursesTab(ttk.Frame):
    """Aba para cursos e conteúdos educacionais."""

    def __init__(self, parent):
        super(CoursesTab, self).__init__(parent)
        self._create_widgets()

    def _create_widgets(self):
        """Criar widgets da aba Cursos."""
        title = ttk.Label(self, text="Cursos", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Espaço reservado para divulgação de cursos, empresas e conteúdos educacionais.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        placeholder = ttk.Label(self, text="Conteúdo em breve...")
        placeholder.pack(padx=16, pady=16)
