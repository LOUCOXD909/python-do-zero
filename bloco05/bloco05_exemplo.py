def somar_ate(limite):
    total = 0
    for numero in range(1, limite + 1):
        total += numero
    return total


def contar_vogais(texto):
    vogais = "aeiouáéíóúâêôãõ"
    return sum(1 for caractere in texto.lower() if caractere in vogais)


def contagem_regressiva(inicio):
    resultado = []
    while inicio > 0:
        resultado.append(inicio)
        inicio -= 1
    resultado.append("Fim!")
    return resultado


if __name__ == "__main__":
    print(somar_ate(5))
    print(contar_vogais("Python é legal"))
    print(contagem_regressiva(3))
