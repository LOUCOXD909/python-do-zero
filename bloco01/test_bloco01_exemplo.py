from bloco01_exemplo import saudacao, mensagem_curso


def test_saudacao():
    assert saudacao("Ana") == "Olá, Ana!"


def test_nome_composto():
    assert saudacao("João Silva") == "Olá, João Silva!"


def test_mensagem():
    assert "Python" in mensagem_curso()
