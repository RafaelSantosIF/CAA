def quicksort(tarefas):   
    if len(tarefas) <= 1:
        return tarefas
    
    pivo = tarefas[0]
    menores = []
    iguais = [pivo]
    maiores = []
    
    for t in tarefas[1:]:
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

listaTarefas = [(0, 3), (0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11), (5, 10), (12, 14), (13, 16), (14, 17)]
print(agendamentoGuloso(listaTarefas))