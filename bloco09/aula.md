# Bloco 9 — Módulos e testes

Um arquivo Python pode ser importado por outro. Coloque funções reutilizáveis em módulos e deixe demonstrações sob if __name__ == "__main__": para que não rodem durante a importação.

pytest encontra arquivos test_*.py e funções test_*. Use assert para comparar resultado e esperado. Para erros esperados, use pytest.raises. Teste casos comuns, limites e entradas inválidas.

Comandos: python -m pytest bloco09 -q e python -m pytest -q. Testes ajudam a detectar regressões, mas não provam ausência total de erros.