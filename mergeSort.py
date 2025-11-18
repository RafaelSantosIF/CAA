def mergeSort(arr):    
    if len(arr) > 1:
        meio = len(arr) // 2
        sub_lista_esquerda = arr[:meio]
        sub_lista_direita = arr[meio:]

        mergeSort(sub_lista_esquerda)
        mergeSort(sub_lista_direita)

        i = j = k = 0
        
        while i < len(sub_lista_esquerda) and j < len(sub_lista_direita):
            if sub_lista_esquerda[i] < sub_lista_direita[j]:
                arr[k] = sub_lista_esquerda[i]
                i += 1
            else:
                arr[k] = sub_lista_direita[j]
                j += 1
            k += 1

        while i < len(sub_lista_esquerda):
            arr[k] = sub_lista_esquerda[i]
            i += 1
            k += 1

        while j < len(sub_lista_direita):
            arr[k] = sub_lista_direita[j]
            j += 1
            k += 1

if __name__ == "__main__":
    vetor1 = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {vetor1}")
    mergeSort(vetor1)
    print(f"Lista ordenada: {vetor1}")