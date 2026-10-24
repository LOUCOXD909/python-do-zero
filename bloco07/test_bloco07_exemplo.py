import pytest
from bloco07_exemplo import calcular_media, formatar_mensagem, aplicar_desconto


def test_media():
    assert calcular_media([8, 10]) == 9


def test_media_vazia():
    with pytest.raises(ValueError):
        calcular_media([])


def test_padrao():
    assert formatar_mensagem("Ana") == "Bom estudo, Ana!"


def test_nome_vazio():
    with pytest.raises(ValueError):
        formatar_mensagem("   ")


def test_desconto():
    assert aplicar_desconto(100, 15) == 85


def test_desconto_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
