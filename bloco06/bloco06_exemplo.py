def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]


def resumir_notas(notas):
    if not notas:
        return {"quantidade": 0, "media": None, "maior": None}
    return {"quantidade": len(notas), "media": sum(notas) / len(notas), "maior": max(notas)}


def buscar_pessoa(pessoas, nome):
    for pessoa in pessoas:
        if pessoa.get("nome", "").casefold() == nome.casefold():
            return pessoa
    return None


if __name__ == "__main__":
    print(filtrar_pares([1, 2, 3, 4, 5, 6]))
    print(resumir_notas([8, 7, 10]))
