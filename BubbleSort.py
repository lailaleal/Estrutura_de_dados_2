import random
import time

def gera_vetor(n):
    return [random.randint(0, n-1) for _ in range(n)]

def bubble_sort(array):
    n = len(array)  # Armazena o tamanho da lista na variável 'n'
    print("Vetor original:", array)  # Imprime o vetor original antes de começar a ordenação
    for i in range(n - 1):  # Loop externo: controla o número de iterações
        print("Iteração:", i, array)  # Imprime o vetor em cada iteração
        for j in range(n - 1 - i):  # Loop interno: compara elementos
            if array[j] > array[j + 1]:  # Verifica se o elemento atual é maior
                array[j], array[j + 1] = array[j + 1], array[j]  # Troca os elementos
    print("Vetor ordenado:", array)  # Imprime o vetor após a ordenação
    return array

def main():
    # Inicia a contagem do tempo
    inicio = time.time()

    n = 10  # Reduzi para 10 para facilitar a visualização das impressões
    v = gera_vetor(n)
    bubble_sort(v)

    # Finaliza a contagem do tempo
    fim = time.time()

    # Calcula o tempo de execução em segundos
    tempo_execucao = fim - inicio
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    main()