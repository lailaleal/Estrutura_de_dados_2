#Questão 5.– Utilize a versão iterativa do Merge Sort e compare-a com a versão recursiva. Faça testes
#com vetores de tamanhos variados, meça o tempo de execução de ambas as versões e apresente os
#resultados em uma tabela. Em seguida, discuta as vantagens e desvantagens observadas entre as duas
#abordagens.

import time
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Versão Iterativa
def merge_sort_iterativo(arr):
    n = len(arr)
    step = 1

    while step < n:
        for i in range(0, n, 2 * step):
            left = arr[i:i+step]
            right = arr[i+step:i+2*step]
            merged = merge(left, right)
            arr[i:i+len(merged)] = merged
        step *= 2
    return arr

# Função para medir tempo de execução
def medir_tempo(algoritmo, array):
    inicio = time.time()
    algoritmo(array.copy())
    fim = time.time()
    return fim - inicio

# Testes 
tamanhos = [100, 1000, 10000, 50000]
print(f"{'Tamanho':>10} | {'Recursivo (s)':>15} | {'Iterativo (s)':>15}")
print("-" * 45)
for tam in tamanhos:
    vetor = [random.randint(1, 10000) for _ in range(tam)]
    t1 = medir_tempo(merge_sort, vetor)
    t2 = medir_tempo(merge_sort_iterativo, vetor)
    print(f"{tam:>10} | {t1:>15.5f} | {t2:>15.5f}")
