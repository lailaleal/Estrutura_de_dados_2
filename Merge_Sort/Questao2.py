# Questão 2.– Implemente um programa que utilize a função merge_sort(array) e realize testes ex-
# perimentais para verificar sua correção. Gere vetores de inteiros aleatórios de vários tamanhos (por
# exemplo, 10, 100, 1000 elementos). Após a ordenação, verifique automaticamente se o vetor está, de
# fato, em ordem crescente. Exiba o resultado de cada teste.

import random

# Função Merge (Intercalação) – ordena duas sublistas já ordenadas
def merge(left, right):
    result = []
    i = j = 0

    # Compara elementos das duas listas até que uma seja completamente percorrida
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # menor elemento entra primeiro (ordem crescente)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adiciona o restante dos elementos da lista esquerda (se sobrar)
    result.extend(left[i:])
    # Adiciona o restante dos elementos da lista direita (se sobrar)
    result.extend(right[j:])

    return result  # retorna lista mesclada e ordenada

# Função Recursiva do Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:  # Caso base: lista com 0 ou 1 elemento já está ordenada
        return arr

    mid = len(arr) // 2  # Divide no meio para aplicar "dividir para conquistar"
    left = merge_sort(arr[:mid])    # Recursivamente ordena metade esquerda
    right = merge_sort(arr[mid:])   # Recursivamente ordena metade direita

    return merge(left, right)       # Intercala as duas metades ordenadas

# Função de verificação automática
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))  # Verifica se cada elemento é menor ou igual ao próximo

# Testes com diferentes tamanhos
for size in [10, 100, 1000]:
    vetor = [random.randint(1, 1000) for _ in range(size)]  # Gera vetor aleatório
    ordenado = merge_sort(vetor)  # Aplica Merge Sort
    print(f"Teste com {size} elementos:", "OK" if is_sorted(ordenado) else "FALHOU")
