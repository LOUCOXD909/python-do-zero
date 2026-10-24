def calcular_media(notas):
    if not notas:
        raise ValueError("Informe pelo menos uma nota.")
    return sum(notas) / len(notas)


def formatar_mensagem(nome, mensagem="Bom estudo"):
    nome_limpo = nome.strip()
    if not nome_limpo:
        raise ValueError("O nome não pode ficar vazio.")
    return f"{mensagem}, {nome_limpo}!"


def aplicar_desconto(preco, percentual=0):
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    if not 0 <= percentual <= 100:
        raise ValueError("O percentual deve ficar entre 0 e 100.")
    return preco * (1 - percentual / 100)


if __name__ == "__main__":
    print(calcular_media([8, 9, 10]))
    print(formatar_mensagem("Estudante"))
    print(aplicar_desconto(100, 15))
