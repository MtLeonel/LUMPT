"""Aba Código Livre - Exemplos de código em múltiplas linguagens."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class FreeCodeTab(ttk.Frame):
    """Aba com exemplos de código em múltiplas linguagens."""

    LANGUAGE_EXAMPLES = {
        "Python": 'print("Olá, Mundo!")',
        "JavaScript": 'console.log("Olá, Mundo!");',
        "C++": '#include <iostream>\nusing namespace std;\nint main() {\n  cout << "Olá, Mundo!";\n  return 0;\n}',
        "Java": 'public class Main {\n  public static void main(String[] args) {\n    System.out.println("Olá, Mundo!");\n  }\n}',
        "C#": 'using System;\nclass Program {\n  static void Main() {\n    Console.WriteLine("Olá, Mundo!");\n  }\n}',
        "Go": 'package main\nimport "fmt"\nfunc main() {\n  fmt.Println("Olá, Mundo!")\n}',
        "Ruby": 'puts "Olá, Mundo!"',
    }

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        self._create_widgets()

    def _create_widgets(self) -> None:
        """Criar widgets da aba Código Livre."""
        title = ttk.Label(self, text="Código Livre", font=("Arial", 14, "bold"))
        title.pack(padx=16, pady=(16, 8))

        description = ttk.Label(
            self,
            text="Exemplos de código em múltiplas linguagens de programação.",
            wraplength=500,
        )
        description.pack(padx=16, pady=(0, 16))

        # Seletor de linguagem
        language_frame = ttk.Frame(self)
        language_frame.pack(padx=16, pady=(0, 8))

        ttk.Label(language_frame, text="Linguagem:").pack(side="left", padx=(0, 8))

        self.language_var = tk.StringVar(value="Python")
        language_combo = ttk.Combobox(
            language_frame,
            textvariable=self.language_var,
            values=list(self.LANGUAGE_EXAMPLES.keys()),
            state="readonly",
            width=20,
        )
        language_combo.pack(side="left")
        language_combo.bind("<<ComboboxSelected>>", self._update_code)

        # Exibição de código
        code_frame = ttk.LabelFrame(self, text="Exemplo", padding=12)
        code_frame.pack(fill="both", expand=True, padx=16, pady=8)

        self.code_text = tk.Text(code_frame, height=15, width=60)
        self.code_text.pack(fill="both", expand=True)
        
        self._update_code()

    def _update_code(self, *args) -> None:
        """Atualizar código exibido conforme linguagem selecionada."""
        language = self.language_var.get()
        code = self.LANGUAGE_EXAMPLES.get(language, "")
        self.code_text.delete("1.0", "end")
        self.code_text.insert("1.0", code)
        self.code_text.config(state="disabled")