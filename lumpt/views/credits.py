"""Aba Créditos - Informações sobre desenvolvedores."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class CreditsTab(ttk.Frame):
    """Aba com créditos e informações dos desenvolvedores."""

    TEAM = [
        ("Desenvolvedor Principal", "MtLeonel"),
        ("Arquitetura", "Equipe LUMPT"),
        ("Interface", "Tkinter"),
        ("Versão", "1.0.0"),
    ]

    def __init__(self, parent):
        super(CreditsTab, self).__init__(parent)
        self._create_widgets()

    def _create_widgets(self):
        """Criar widgets da aba Créditos."""
        title = ttk.Label(self, text="Créditos", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="LUMPT - Learning Universal Multidisciplinary Programming Tool",
            wraplength=500,
            font=("Arial", 10, "italic")
        )
        description.pack(padx=16, pady=(0, 16))

        content_frame = ttk.Frame(self)
        content_frame.pack(padx=16, pady=16, fill="both", expand=True)

        for role, name in self.TEAM:
            row_frame = ttk.Frame(content_frame)
            row_frame.pack(fill="x", pady=4)

            ttk.Label(row_frame, text=role + ":", font=("Arial", 10, "bold")).pack(side="left", anchor="w")
            ttk.Label(row_frame, text=name, font=("Arial", 10)).pack(side="left", padx=(16, 0))

        separator = ttk.Separator(content_frame, orient="horizontal")
        separator.pack(fill="x", pady=16)

        footer = ttk.Label(
            content_frame,
            text="Obrigado por usar o LUMPT!\nContribua em: github.com/MtLeonel/LUMPT",
            wraplength=500,
            justify="center",
            font=("Arial", 9)
        )
        footer.pack(padx=16, pady=16)
