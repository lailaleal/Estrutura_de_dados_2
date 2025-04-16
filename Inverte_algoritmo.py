# Questão 6.– Invente um algoritmo de ordenação que seja mais rápido que o de inserção e o de seleção.
# Explique como consegue

def select_insert_sort(vetor):
    n = len(vetor)
    divisao = int(0.8 * n)  

    # Fase 1: Selection Sort modificado (ordena os 80% maiores no final)
    for i in range(divisao, n):
        indice_maior = 0
        for j in range(1, n - i):
            if vetor[j] > vetor[indice_maior]:
                indice_maior = j
        vetor[n - i - 1], vetor[indice_maior] = vetor[indice_maior], vetor[n - i - 1]

    # Fase 2: Insertion Sort nos 20% restantes
    for i in range(1, n):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

    return vetor

# Teste
vetor = [12, 3, 7, 22, 45, 1, 8, 15, 33, 6]
print("Original:", vetor)
print("Ordenado:", select_insert_sort(vetor.copy()))