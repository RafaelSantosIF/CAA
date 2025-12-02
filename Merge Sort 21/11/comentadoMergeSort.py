def merge_sort(lista):
    """
    Função principal que implementa o algoritmo Merge Sort.
    Recebe uma lista de inteiros e retorna a lista ordenada.
    """
    
    # Caso base: Se a lista tiver 0 ou 1 elemento, já está ordenada.
    if len(lista) <= 1:
        return lista

    # --- ETAPA DE DIVISÃO ---
    # Encontra o índice do meio da lista para dividi-la em duas partes
    meio = len(lista) // 2
    
    # Divide a lista em esquerda e direita
    # O fatiamento (slicing) cria cópias das sub-listas
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Chamada recursiva para ordenar cada metade
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    # --- ETAPA DE CONQUISTA (MERGE) ---
    # Chama a função auxiliar para intercalar as duas metades ordenadas
    return merge(esquerda_ordenada, direita_ordenada)


def merge(esquerda, direita):
    """
    Função auxiliar responsável por intercalar (merge) duas listas ordenadas
    em uma única lista ordenada.
    """
    lista_ordenada = []  # Lista auxiliar para armazenar o resultado
    i = j = 0 # Índices para percorrer as listas da esquerda (i) e direita (j)

    # Enquanto houver elementos em ambas as listas, comparamos e inserimos o menor
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    # Se sobrarem elementos na lista da esquerda, adicionamos ao final
    lista_ordenada.extend(esquerda[i:])

    # Se sobrarem elementos na lista da direita, adicionamos ao final
    lista_ordenada.extend(direita[j:])

    return lista_ordenada

# --- Exemplo de Uso ---
if __name__ == "__main__":
    numeros = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {numeros}")
    
    resultado = merge_sort(numeros)
    print(f"Lista ordenada: {resultado}")