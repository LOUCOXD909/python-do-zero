"""Modelo auxiliar do bloco final, não é a solução do projeto."""


def validar_titulo(titulo):
    titulo_limpo = titulo.strip()
    if not titulo_limpo:
        raise ValueError("O título não pode ficar vazio.")
    return titulo_limpo


def calcular_total(valores):
    if any(valor < 0 for valor in valores):
        raise ValueError("Os valores não podem ser negativos.")
    return sum(valores)


def procurar_por_id(registros, identificador):
    for registro in registros:
        if registro.get("id") == identificador:
            return registro
    return None


if __name__ == "__main__":
    print("Crie seu projeto final em outra pasta.")
