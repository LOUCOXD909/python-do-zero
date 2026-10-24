import pytest
from bloco10_exemplo import validar_titulo, calcular_total, procurar_por_id


def test_titulo():
    assert validar_titulo("  Minha tarefa ") == "Minha tarefa"


def test_titulo_vazio():
    with pytest.raises(ValueError):
        validar_titulo("   ")


def test_total():
    assert calcular_total([2.5, 3, 4]) == 9.5
    assert calcular_total([]) == 0


def test_total_negativo():
    with pytest.raises(ValueError):
        calcular_total([5, -1])


def test_busca():
    registros = [{"id": 1, "nome": "A"}, {"id": 2, "nome": "B"}]
    assert procurar_por_id(registros, 2) == {"id": 2, "nome": "B"}
    assert procurar_por_id(registros, 3) is None
