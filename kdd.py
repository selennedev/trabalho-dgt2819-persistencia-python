"""
Trabalho Prático - DGT2819: Persistência de dados com Python
Objetivo: ler um arquivo TXT, separar palavras, comparar métodos de ordenação
e gravar o resultado ordenado em um novo arquivo.
"""

from time import perf_counter


def bubble_sort(lista):
    """Ordena uma lista em ordem crescente usando Bubble Sort."""
    resultado = lista.copy()
    n = len(resultado)

    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if resultado[j].casefold() > resultado[j + 1].casefold():
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                houve_troca = True
        if not houve_troca:
            break

    return resultado


def selection_sort(lista):
    """Ordena uma lista em ordem crescente usando Selection Sort."""
    resultado = lista.copy()
    n = len(resultado)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if resultado[j].casefold() < resultado[menor].casefold():
                menor = j
        resultado[i], resultado[menor] = resultado[menor], resultado[i]

    return resultado


def ler_palavras(nome_arquivo):
    """Lê o arquivo linha por linha e reúne as palavras em uma lista."""
    palavras = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.extend(linha.split())
    return palavras


def medir_tempo(funcao, palavras):
    """Executa uma função de ordenação e retorna o resultado e o tempo."""
    inicio = perf_counter()
    ordenadas = funcao(palavras)
    fim = perf_counter()
    return ordenadas, fim - inicio


def main():
    arquivo_entrada = "texto.txt"
    arquivo_saida = "palavras_ordenadas.txt"

    try:
        palavras = ler_palavras(arquivo_entrada)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")
        print("Coloque texto.txt na mesma pasta que kdd.py e tente novamente.")
        return

    if not palavras:
        print(f"O arquivo '{arquivo_entrada}' está vazio. Adicione algum texto.")
        return

    print(f"Total de palavras lidas: {len(palavras)}")
    print("\n--- Comparação dos métodos de ordenação ---")

    bubble, tempo_bubble = medir_tempo(bubble_sort, palavras)
    selection, tempo_selection = medir_tempo(selection_sort, palavras)
    nativo, tempo_nativo = medir_tempo(
        lambda itens: sorted(itens, key=str.casefold), palavras
    )

    print(f"\nBubble Sort ({tempo_bubble:.8f} segundos):")
    print(" ".join(bubble))

    print(f"\nSelection Sort ({tempo_selection:.8f} segundos):")
    print(" ".join(selection))

    print(f"\nMétodo nativo sort/sorted ({tempo_nativo:.8f} segundos):")
    print(" ".join(nativo))

    # Escolha do método nativo por sua eficiência prática.
    with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(nativo))
        arquivo.write("\n")

    print(f"\nMétodo escolhido: ordenação nativa do Python (sorted).")
    print(f"Resultado salvo em '{arquivo_saida}'.")


if __name__ == "__main__":
    main()
