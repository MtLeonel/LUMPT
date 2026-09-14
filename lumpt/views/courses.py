"""Aba Cursos - Espaço para divulgação de cursos e conteúdos."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class CoursesTab(ttk.Frame):
    """Aba para divulgação de cursos e conteúdos educativos."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Cursos."""
        title = ttk.Label(self, text="Cursos", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Espaço reservado para divulgação de cursos, empresas e conteúdos parceiros.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        placeholder = ttk.Label(self, text="Em breve: integração com parceiros educacionais.")
        placeholder.pack(padx=16, pady=16)