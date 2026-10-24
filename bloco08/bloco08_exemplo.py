from pathlib import Path


def ler_texto(caminho):
    return Path(caminho).read_text(encoding="utf-8")


def contar_linhas(caminho):
    texto = ler_texto(caminho)
    if not texto:
        return 0
    return len(texto.splitlines())


def salvar_texto(caminho, conteudo):
    Path(caminho).write_text(conteudo, encoding="utf-8")


if __name__ == "__main__":
    exemplo = Path(__file__).with_name("consulta.txt")
    print(ler_texto(exemplo))
    print(f"Linhas: {contar_linhas(exemplo)}")
