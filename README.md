# LUMPT

LUMPT é uma aplicação educativa em Python com interface Tkinter para aprender lógica de programação.

Estrutura ativa do projeto:

```text
LUMPT/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── build_release.py
├── lumpt/
│   ├── __init__.py
│   ├── app.py
│   └── views/
├── installer/
│   ├── install_lumpt.py
│   └── install_lumpt.cmd
├── ai_context/
│   └── ai_context.txt
├── tests/
│   └── test_lumpt_structure.py
└── dist/   (gerado ao empacotar)
```

Arquivos antigos e duplicados no nível raiz foram removidos da estrutura ativa e ficam ignorados no `.gitignore`.

## Executar localmente

```powershell
python main.py
```

## Gerar instalador único

No Windows, com Python 3.9+:

```powershell
python build_release.py
```

Isso gera o instalador em:

```text
dist\LUMPT_Installer.exe
```

## Requisitos

- Windows 10/11
- Python 3.9+ (somente para build local)
- Nenhuma dependência externa obrigatória no projeto em execução

## Observações

- O programa usa Tkinter, que acompanha a instalação padrão do Python no Windows.
- O instalador é pensado para ser simples, em um único arquivo, e instalar o projeto em uma pasta escolhida pelo usuário.
- O contexto de IA principal está em `ai_context/ai_context.txt` e referencia o modelo `Qwen 1.5B`.
