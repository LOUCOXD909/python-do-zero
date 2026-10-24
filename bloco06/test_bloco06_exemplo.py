from bloco06_exemplo import filtrar_pares, resumir_notas, buscar_pessoa


def test_pares():
    assert filtrar_pares([1, 2, 3, 4]) == [2, 4]
    assert filtrar_pares([]) == []


def test_resumo():
    assert resumir_notas([8, 10]) == {"quantidade": 2, "media": 9, "maior": 10}


def test_vazio():
    assert resumir_notas([]) == {"quantidade": 0, "media": None, "maior": None}


def test_busca():
    pessoas = [{"nome": "Bia", "idade": 20}]
    assert buscar_pessoa(pessoas, "bia") == pessoas[0]
    assert buscar_pessoa(pessoas, "ninguém") is None
