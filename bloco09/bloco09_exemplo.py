def calcular_imc(peso_kg, altura_m):
    if peso_kg <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    if altura_m <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso_kg / (altura_m ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo da faixa de referência"
    if imc < 25:
        return "Dentro da faixa de referência"
    if imc < 30:
        return "Acima da faixa de referência"
    return "Faixa elevada"


if __name__ == "__main__":
    valor = calcular_imc(70, 1.75)
    print(f"IMC demonstrativo: {valor:.1f}")
    print(classificar_imc(valor))
