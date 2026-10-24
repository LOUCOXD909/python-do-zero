from bloco04_exemplo import classificar_nota, pode_entrar


def test_limites():
    assert classificar_nota(10) == "Excelente"
    assert classificar_nota(7) == "Aprovado"
    assert classificar_nota(5) == "Recuperação"
    assert classificar_nota(4.9) == "Reprovado"


def test_nota_invalida():
    assert classificar_nota(-1) == "Nota inválida"
    assert classificar_nota(10.1) == "Nota inválida"


def test_or():
    assert pode_entrar(20)
    assert not pode_entrar(15)
    assert pode_entrar(15, acompanhado=True)
