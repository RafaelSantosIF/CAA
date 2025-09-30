def bubble_sort(vetor):   
    n = len(vetor)    
    comp = 0
    
    for i in range(n - 1):        
        for j in range(n - i - 1):
            comp += 1            
            if vetor[j] > vetor[j + 1]:
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux    
    
    print("Vetor ordenado:", end=" ")
    for i in range(n):
        print(vetor[i], end=" ")
    print("Comparações Feitas: ", comp) 
    
def early_exit(vetor):   
    n = len(vetor)    
    comp = 0
    swap = False
    
    for i in range(n - 1):        
        for j in range(n - i - 1):
            comp += 1            
            if vetor[j] > vetor[j + 1]:
                swap = True
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux
                
        if (not swap):
            break                
    
    print("Vetor ordenado:", end=" ")
    for i in range(n):
        print(vetor[i], end=" ")
    print("Comparações Feitas: ", comp)     

def last_swap(vetor):   
    n = len(vetor)    
    comp = 0    
    
    i = 0
    while i < n - 1:
        last_swap = 0          
        
        for j in range(n - i - 1):   
            comp += 1          
            if vetor[j] > vetor[j + 1]:
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux
                last_swap = j + 1        
        
        if last_swap == 0:
            break        
        
        n = last_swap + 1
        i += 1                
    
    print("Vetor ordenado:", end=" ")
    for i in range(n):
        print(vetor[i], end=" ")
    print("Comparações Feitas: ", comp) 


if __name__ == "__main__":
    
    vetor1 = [1, 2, 3, 4, 5]
    vetor2 = [5, 4, 3, 2, 1]
    vetor3 = [1, 2, 4, 5, 3]
    
    print("Sort Simples")
    print("="*30)
    print("Melhor Caso:", vetor1)
    bubble_sort(vetor1)
    print("Pior Caso:", vetor2)
    bubble_sort(vetor2)
    print("Médio Caso:", vetor3)
    bubble_sort(vetor3)
    print()
    
    vetor1 = [1, 2, 3, 4, 5]
    vetor2 = [5, 4, 3, 2, 1]
    vetor3 = [1, 2, 4, 5, 3]
    
    print("Otimizado com Early Exit")
    print("="*30)
    print("Melhor Caso:", vetor1)
    early_exit(vetor1)
    print("Pior Caso:", vetor2)
    early_exit(vetor2)
    print("Médio Caso:", vetor3)
    early_exit(vetor3)
    print()
    
    vetor1 = [1, 2, 3, 4, 5]
    vetor2 = [5, 4, 3, 2, 1]
    vetor3 = [1, 2, 4, 5, 3]
    
    print("Otimizado com Last-Swap")
    print("="*30)
    print("Melhor Caso:", vetor1)
    last_swap(vetor1)
    print("Pior Caso:", vetor2)
    last_swap(vetor2)
    print("Médio Caso:", vetor3)
    last_swap(vetor3)
    print()
   