# Bloco 8 — Arquivos e erros

Para ler texto, use pathlib.Path.read_text(encoding="utf-8") ou with open(caminho, "r", encoding="utf-8"). O with fecha o arquivo automaticamente.

Caminhos relativos dependem do diretório de trabalho. O modo r lê, w escreve sobrescrevendo e a acrescenta ao final. FileNotFoundError indica caminho ausente; PermissionError indica falta de permissão. Trate erros esperados e não esconda falhas com except vazio.

Os testes usam arquivos temporários para evitar alterar arquivos pessoais. Rode python -m pytest bloco08 -q.