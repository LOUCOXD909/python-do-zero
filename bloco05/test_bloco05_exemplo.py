from bloco05_exemplo import somar_ate, contar_vogais, contagem_regressiva


def test_soma():
    assert somar_ate(5) == 15
    assert somar_ate(0) == 0


def test_vogais():
    assert contar_vogais("Abacaxi") == 4
    assert contar_vogais("") == 0


def test_contagem():
    assert contagem_regressiva(3) == [3, 2, 1, "Fim!"]
    assert contagem_regressiva(0) == ["Fim!"]
