import pytest
from bloco03_exemplo import calcular_total, normalizar_texto, dividir


def test_total():
    assert calcular_total(4, 3) == 12


def test_negativos():
    with pytest.raises(ValueError):
        calcular_total(-1, 2)


def test_normalizar():
    assert normalizar_texto("  PyThOn  ") == "python"


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
