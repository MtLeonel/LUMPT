"""Aba Perfil - Informações e preferências do usuário."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class ProfileTab(ttk.Frame):
    """Aba para perfil e preferências do usuário."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Perfil."""
        title = ttk.Label(self, text="Perfil", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Gerencie suas preferências e informações de perfil.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        placeholder = ttk.Label(self, text="Funcionalidade em desenvolvimento...")
        placeholder.pack(padx=16, pady=16)