import pytest
from bloco09_exemplo import calcular_imc, classificar_imc


def test_calculo():
    assert calcular_imc(70, 1.75) == pytest.approx(22.857142857)


@pytest.mark.parametrize("peso,altura", [(0, 1.7), (-2, 1.7), (70, 0), (70, -1)])
def test_medidas_invalidas(peso, altura):
    with pytest.raises(ValueError):
        calcular_imc(peso, altura)


def test_classificacao():
    assert classificar_imc(17) == "Abaixo da faixa de referência"
    assert classificar_imc(22) == "Dentro da faixa de referência"
    assert classificar_imc(27) == "Acima da faixa de referência"
    assert classificar_imc(32) == "Faixa elevada"
