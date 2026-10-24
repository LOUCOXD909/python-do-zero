def classificar_nota(nota):
    if not 0 <= nota <= 10:
        return "Nota inválida"
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def pode_entrar(idade, acompanhado=False):
    return idade >= 18 or acompanhado


if __name__ == "__main__":
    for nota in (10, 8, 6, 3, 12):
        print(f"{nota}: {classificar_nota(nota)}")
