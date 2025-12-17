def quicksort(tarefas):   
    if len(tarefas) <= 1:
        return tarefas
    
    pivo = tarefas[len(tarefas) // 2]
    menores = []
    iguais = [pivo]
    maiores = []
    
    for t in tarefas[:len(tarefas) // 2] + tarefas[len(tarefas) // 2 + 1:]:
        if t[1] < pivo[1]:
            menores.append(t)
        elif t[1] > pivo[1]:
            maiores.append(t)
        else:
            iguais.append(t)            
    
    return quicksort(menores) + iguais + quicksort(maiores)

def agendamentoGuloso(tarefas):
    
    ordenadas = quicksort(tarefas)
    
    agendados = []
    ultimo_fim = -1
    
    for inicio, fim in ordenadas:        
        if inicio >= ultimo_fim:
            agendados.append((inicio, fim))
            ultimo_fim = fim  
            
    return agendados

if __name__ == "__main__":
    listaTarefas = [(0, 3), (0, 6), (1, 2), (1, 4), (3, 5), (3, 8), (4, 7), (4, 12), (5, 9), (5, 16), (6, 10), (8, 11), (5, 10), (12, 14), (13, 16), (14, 17)]
    print(agendamentoGuloso(listaTarefas))