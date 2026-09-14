"""Aba Microcontroladores - Conteúdo educativo sobre microcontroladores."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class MicrocontrollersTab(ttk.Frame):
    """Aba para conteúdo sobre microcontroladores."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Microcontroladores."""
        title = ttk.Label(self, text="Microcontroladores", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Aprenda sobre programação em microcontroladores e sistemas embarcados.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        placeholder = ttk.Label(self, text="Funcionalidade em desenvolvimento...")
        placeholder.pack(padx=16, pady=16)