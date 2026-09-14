"""Aba Mini-games - Perguntas e respostas educativas."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class MinigamesTab(ttk.Frame):
    """Aba para mini-games educativos."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Mini-games."""
        title = ttk.Label(self, text="Mini-games", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Teste seus conhecimentos com perguntas e respostas interativas.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        # Placeholder para futuras questões
        placeholder = ttk.Label(self, text="Funcionalidade em desenvolvimento...")
        placeholder.pack(padx=16, pady=16)