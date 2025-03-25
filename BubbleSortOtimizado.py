import random                             # Importa biblioteca para geração de números aleatórios
import time                               # Importa biblioteca para medição de tempo

def gera_vetor(n):                        # Função Gerar vetor aleatório
    return [random.randint(0, n-1) for _ in range(n)]  # Retorna lista com n números aleatórios entre 0 e n-1

def troca(v, a, b):                       # Função Troca elementos de posição
    v[a], v[b] = v[b], v[a]               # Realiza troca direta entre posições a e b do vetor 

def bubble_sort(v):                       # Função Bubble Sort (não otimizado)
    n = len(v)                            # Obtém tamanho do vetor
    for i in range(n - 1):                # Loop externo (n-1 passagens)
        for j in range(n - 1):            # Loop interno (compara todos os pares)
            if v[j] > v[j + 1]:           # Se elemento atual > próximo elemento
                troca(v, j, j + 1)        # Troca os elementos de posição

def bubble_sort_otimizado(v):             # Função Bubble Sort otimizado
    n = len(v)                            # Obtém tamanho do vetor
    print("Vetor original:", v)           # Mostra vetor antes de ordenar                           
    for i in range(n - 1):                # Loop externo (n-1 passagens)
        houve_troca = False               # Flag para verificar trocas na passagem
        print(f"Iteração {i}:", v)        # Mostra vetor a cada iteração
        for j in range(n - 1 - i):        # Loop interno (reduz a cada passagem)
            if v[j] > v[j + 1]:           # Se elemento atual > próximo elemento
                troca(v, j, j + 1)        # Troca os elementos de posição
                houve_troca = True        # Marca que houve troca nesta passagem
        if not houve_troca:               # Se não houve trocas nesta passagem
             break                        # Sai do loop se não houve trocas
    
    print("Vetor ordenado:", v)           # Mostra resultado final    
    return v                             # Termina função (vetor já ordenado)

def imprimir_vetor(v):                    # Função para imprimir vetor
    print(" ".join(map(str, v)))          # Converte elementos para string e imprime separados por espaço

def main():                               # Função main
    inicio = time.time()                  # Marca tempo inicial de execução

    n = 10                                # Define tamanho do vetor
    v = gera_vetor(n)                     # Gera vetor aleatório de tamanho n
    print("\n=== Bubble Sort Otimizado ===")
    # bubble_sort(v)                      # Chamada comentada para versão não otimizada
    bubble_sort_otimizado(v)              # Chama versão otimizada do Bubble Sort

    fim = time.time()                     # Marca tempo final de execução
    tempo_execucao = fim - inicio         # Calcula tempo total de execução
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")  # Imprime tempo formatado

if __name__ == "__main__":                # Verifica se é o módulo principal
    main()                                # Chama função principal para executar o programa