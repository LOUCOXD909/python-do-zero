import pytest
from bloco02_exemplo import descrever_pessoa, converter_idade, eh_maior_de_idade


def test_descricao():
    assert descrever_pessoa("Bia", 16, 1.6) == "Bia tem 16 anos e 1.60 m de altura."


def test_conversao():
    assert converter_idade("42") == 42


def test_conversao_invalida():
    with pytest.raises(ValueError):
        converter_idade("quarenta")


def test_maioridade():
    assert eh_maior_de_idade(18) is True
    assert eh_maior_de_idade(17) is False
