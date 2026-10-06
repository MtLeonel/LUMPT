# LUMPT

LUMPT é uma aplicação desktop em Python para aprendizado e prática de programação.

## Instalação rápida

1. Baixe o instalador único em Releases: `LUMPT_Installer.exe`
2. Execute o arquivo
3. Escolha a pasta de instalação
4. O programa instala automaticamente e abre o LUMPT

## Build do instalador único

No Windows, execute:

```powershell
python build_release.py
```

Isso gera um instalador único em:

```text
dist\LUMPT_Installer.exe
```

## Requisitos

- Windows 10/11
- Python 3.10+ (somente para build local)

## Estrutura mínima

```text
LUMPT/
├── README.md
├── .gitignore
├── main.py
├── requirements.txt
├── build_release.py
├── lumpt/
│   ├── __init__.py
│   ├── app.py
│   └── views/
└── installer/
    └── install_lumpt.py
```

## Desenvolvimento

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```
