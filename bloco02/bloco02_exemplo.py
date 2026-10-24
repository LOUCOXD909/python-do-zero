def descrever_pessoa(nome, idade, altura):
    return f"{nome} tem {idade} anos e {altura:.2f} m de altura."


def converter_idade(texto):
    return int(texto)


def eh_maior_de_idade(idade):
    return idade >= 18


if __name__ == "__main__":
    nome = "Alex"
    idade = 20
    altura = 1.75
    estudante = True
    print(descrever_pessoa(nome, idade, altura))
    print(f"Estudante? {estudante}")
    print(type(altura).__name__)
