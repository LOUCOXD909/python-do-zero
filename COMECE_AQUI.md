# Comece aqui

1. Instale Python 3.11+: https://www.python.org/downloads/
2. Instale VS Code e a extensão Python: https://code.visualstudio.com/
3. Abra a pasta do repositório.
4. Confira a instalação: Windows `py --version`; macOS/Linux `python3 --version`.

## Ambiente de testes
Windows: `py -m venv .venv`, depois `.venv\\Scripts\\Activate.ps1`, depois `py -m pip install -r requirements-dev.txt`.
macOS/Linux: `python3 -m venv .venv`, depois `source .venv/bin/activate`, depois `python -m pip install -r requirements-dev.txt`.

## Como estudar
Leia aula.md e consulta.txt, execute o exemplo, resolva exercicios.txt num arquivo Python separado e rode `python -m pytest bloco01 -q`. Curso inteiro: `python -m pytest -q`.

Use `py` ou `python3` se `python` não for reconhecido. TXT é material de leitura. No bloco 10, crie um projeto independente na sua IDE e envie à IA os arquivos e a saída real dos testes para avaliação.