"""Aba Tradutor de Lógica - Tradutor de lógica para múltiplas linguagens."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class EditorTab(ttk.Frame):
    """Aba para tradução de lógica entre linguagens."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Tradutor."""
        # Título
        title = ttk.Label(self, text="Tradutor de Lógica", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        # Descrição
        description = ttk.Label(
            self,
            text="Traduza sua lógica entre múltiplas linguagens de programação.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        # Frame para entrada
        input_frame = ttk.LabelFrame(self, text="Entrada", padding=12)
        input_frame.pack(fill="both", expand=True, padx=16, pady=8)

        self.input_text = tk.Text(input_frame, height=10, width=50)
        self.input_text.pack(fill="both", expand=True)

        # Frame para saída
        output_frame = ttk.LabelFrame(self, text="Saída", padding=12)
        output_frame.pack(fill="both", expand=True, padx=16, pady=8)

        self.output_text = tk.Text(output_frame, height=10, width=50, state="disabled")
        self.output_text.pack(fill="both", expand=True)

        # Botão de tradução
        button_frame = ttk.Frame(self)
        button_frame.pack(padx=16, pady=16)

        ttk.Button(button_frame, text="Traduzir").pack(side="left", padx=4)
        ttk.Button(button_frame, text="Limpar").pack(side="left", padx=4)