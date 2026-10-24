import pytest
from bloco08_exemplo import ler_texto, contar_linhas, salvar_texto


def test_leitura(tmp_path):
    arquivo = tmp_path / "texto.txt"
    arquivo.write_text("Olá\nPython\n", encoding="utf-8")
    assert ler_texto(arquivo) == "Olá\nPython\n"


def test_contar_linhas(tmp_path):
    arquivo = tmp_path / "linhas.txt"
    arquivo.write_text("uma\nduas\n", encoding="utf-8")
    assert contar_linhas(arquivo) == 2


def test_arquivo_ausente():
    with pytest.raises(FileNotFoundError):
        ler_texto("arquivo_que_nao_existe_123.txt")


def test_salvar(tmp_path):
    arquivo = tmp_path / "novo.txt"
    salvar_texto(arquivo, "conteúdo")
    assert arquivo.read_text(encoding="utf-8") == "conteúdo"
