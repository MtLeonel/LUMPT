"""Aba Créditos - Nomes dos integrantes e funções."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class CreditsTab(ttk.Frame):
    """Aba com créditos e informações dos contribuidores."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Créditos."""
        title = ttk.Label(self, text="Créditos", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Conheça os integrantes da equipe LUMPT.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        # Frame de créditos
        credits_frame = ttk.Frame(self)
        credits_frame.pack(fill="both", expand=True, padx=16, pady=8)

        self.credits_text = tk.Text(credits_frame, height=20, width=60)
        self.credits_text.pack(fill="both", expand=True)

        credits_content = """LUMPT - Educação em Lógica de Programação

Projeto educativo desenvolvido para ensinar conceitos
básicos de programação e desenvolvimento.

Equipe de Desenvolvimento:
- Coordenação e Arquitetura
- Desenvolvimento da Interface (Tkinter)
- Exemplos de Código
- Testes e Validação

Agradecimentos especiais a todos os colaboradores
e à comunidade educacional.

Versão 1.0.0
"""
        self.credits_text.insert("1.0", credits_content)
        self.credits_text.config(state="disabled")