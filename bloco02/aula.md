# Bloco 2 — Variáveis e tipos

Uma variável associa um nome a um valor; `=` atribui, não compara. Tipos básicos: `str` texto, `int` inteiro, `float` decimal e `bool` verdadeiro/falso. Use `type(valor)` para inspecionar.

`input()` sempre devolve texto. `int("12")` converte, mas `int("doze")` gera `ValueError`. Valide entradas externas. Execute o exemplo e rode `python -m pytest bloco02 -q`.