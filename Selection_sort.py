# Questão 5.– Escreva uma função que permute os elementos de um vetor inteiro v[0..n-1] de modo que
# eles fiquem em ordem decrescente. Inspire-se no algoritmo Selectionsort.

def ordena_decrescente(v):
 
    n = len(v)
    for i in range(n):
        # Encontra o índice do maior elemento no restante do vetor
        indice_maior = i
        for j in range(i + 1, n):
            if v[j] > v[indice_maior]:  # Comparação modificada para ordem decrescente
                indice_maior = j
        
        # Troca o elemento atual com o maior encontrado
        v[i], v[indice_maior] = v[indice_maior], v[i]
    
    return v
vetor = [5, 2, 9, 1, 5, 6]
print("Original:", vetor)
print("Decrescente:", ordena_decrescente(vetor.copy()))