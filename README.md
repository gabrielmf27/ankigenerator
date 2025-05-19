# ankigenerator
Resolvi um problema pessoal nos estudos criando essa ferramenta: ela converte arquivos .csv, .xls, .xlsx ou .ods em baralhos Anki .apkg, com visualização da tabela e interface intuitiva.

REQUISITOS PARA RODAR ESTE PROGRAMA (.py)

Este programa converte arquivos de tabelas (.csv, .xls, .xlsx, .ods) em baralhos do Anki (.apkg).
Ele possui uma interface gráfica e funciona em sistemas Windows, macOS e linux (se você usa linux, provavelmente não precisa que eu te diga como rodar um programa em python).

Siga os passos abaixo conforme o seu sistema:

============================================================
1. INSTALAR O PYTHON
============================================================

WINDOWS:
- Baixe em: https://www.python.org/downloads/windows/
- Durante a instalação, marque a opção "Add Python to PATH"
- Finalize normalmente

MACOS:
- Baixe em: https://www.python.org/downloads/macos/
- Ou instale via Homebrew (caso saiba usar):
  brew install python

============================================================
2. INSTALAR OS PACOTES NECESSÁRIOS
============================================================

Abra o terminal:

WINDOWS:
- Pressione `Win + R`, digite `cmd` e pressione Enter.

MACOS:
- Use o Terminal (Aplicativos > Utilitários > Terminal)

Execute o seguinte comando:

pip install pandas genanki odfpy

============================================================
3. EXECUTAR O PROGRAMA
============================================================

WINDOWS:
- Clique duas vezes no arquivo "ankigenerator.bat"
- OU abra o terminal, navegue até a pasta do projeto e rode:
  python ankigenerator.py

MACOS:
- Abra o terminal, navegue até a pasta do projeto e rode:
  python3 ankigenerator.py

Observação: no macOS, pode ser necessário usar `python3` em vez de `python`.

============================================================
4. USO
============================================================

- O programa abrirá uma janela gráfica.
- Clique em "Selecionar Arquivo" para carregar um arquivo com perguntas e respostas.
- Veja a visualização da tabela.
- Clique em "Gerar Arquivo Anki (.apkg)" para salvar o baralho.

============================================================
5. FORMATOS SUPORTADOS
============================================================

- CSV (valores separados por vírgula ou ponto e vírgula)
- XLS / XLSX (Microsoft Excel)
- ODS (LibreOffice ou Planilhas compatíveis)

============================================================
6. ESTRUTURA ESPERADA DA TABELA
============================================================

- A primeira coluna deve conter as perguntas.
- A segunda coluna deve conter as respostas.
- Linhas extras ou vazias são ignoradas.

============================================================
7. IMPORTAR NO ANKI
============================================================

- O arquivo gerado será salvo com a extensão `.apkg`.
- Abra o Anki e use a opção "Importar" para adicionar o baralho.

Download oficial do Anki: https://apps.ankiweb.net/

