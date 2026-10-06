# LUMPT - Learning Universal Multidisciplinary Programming Tool

LUMPT é uma plataforma educacional interativa desenvolvida em Python com interface gráfica Tkinter.

## Instalação Rápida

1. Baixe o arquivo `LUMPT-Installer.exe` na seção [Releases](https://github.com/MtLeonel/LUMPT/releases)
2. Clique duas vezes no arquivo para abrir o instalador
3. Escolha a pasta onde deseja instalar
4. Clique em "Instalar"
5. O programa será instalado e um atalho será criado na sua área de trabalho

## Requisitos

- Windows 7 ou superior
- Python 3.7+ (o instalador gerencia as dependências)
- Acesso à internet para primeira execução

## Funcionalidades

- **Cursos**: Módulos de aprendizado estruturado
- **Editor**: Ambiente de codificação integrado
- **Microcontroladores**: Simulação e programação
- **Minigames**: Exercícios práticos e gamificados
- **FreeCode**: Ambiente livre para experimentos
- **Créditos**: Informações sobre desenvolvedor

## Estrutura do Projeto

```
LUMPT/
├── README.md              # Este arquivo
├── .gitignore            # Configuração Git
├── main.py               # Ponto de entrada
├── requirements.txt      # Dependências
└── lumpt/                # Pacote principal
    ├── __init__.py
    ├── app.py           # Aplicação principal
    └── views/           # Módulos de interface
        ├── courses.py
        ├── editor.py
        ├── microcontrollers.py
        └── ...
```

## Desenvolvimento

Para configurar o ambiente de desenvolvimento:

```bash
# Clone o repositório
git clone https://github.com/MtLeonel/LUMPT.git
cd LUMPT

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python main.py
```

## Construindo o Instalador

Para gerar um novo instalador executável:

```bash
pip install pyinstaller
pyinstaller --onefile installer/install_lumpt.py
```

O arquivo `install_lumpt.exe` será gerado em `dist/`.

## Licença

Projeto em desenvolvimento.

## Autor

[MtLeonel](https://github.com/MtLeonel)
