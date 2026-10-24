def calcular_total(preco, quantidade):
    if preco < 0 or quantidade < 0:
        raise ValueError("Valores não podem ser negativos.")
    return preco * quantidade


def normalizar_texto(texto):
    return texto.strip().lower()


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O divisor não pode ser zero.")
    return a / b


if __name__ == "__main__":
    print(7 // 2)
    print(7 % 2)
    print(normalizar_texto("  PyThOn  "))
    print(f"Total: R$ {calcular_total(4.5, 3):.2f}")
