#import random                            # Importa biblioteca para geração de números aleatórios
import time                               # Importa biblioteca para medição de tempo

#def gera_vetor(n):                        # Função Gerar vetor aleatório
 #   return [random.randint(0, n-1) for _ in range(n)]  # Retorna lista com n números aleatórios entre 0 e n-1

def troca(v, a, b):                       # Função Troca elementos de posição
    v[a], v[b] = v[b], v[a]               # Realiza troca direta entre posições a e b do vetor 

#def bubble_sort(v):                       # Função Bubble Sort (não otimizado)
   # n = len(v)                            # Obtém tamanho do vetor
   # for i in range(n - 1):                # Loop externo (n-1 passagens)
   #     for j in range(n - 1):            # Loop interno (compara todos os pares)
         #   if v[j] > v[j + 1]:           # Se elemento atual > próximo elemento
         #       troca(v, j, j + 1)        # Troca os elementos de posição

def bubble_sort_otimizado(v):             # Função Bubble Sort otimizado
    n = len(v)                            # Obtém tamanho do vetor
    print("\n=== BUBBLE SORT OTIMIZADO ===")
    print("Vetor original:", v)           # Mostra vetor antes de ordenar                           
    for i in range(n - 1):                # Loop externo (n-1 passagens)
        houve_troca = False               # Flag para verificar trocas na passagem
        #print(f"Iteração {i}:", v)        # Mostra vetor a cada iteração
        for j in range(n - 1 - i):        # Loop interno (reduz a cada passagem)
            if v[j] > v[j + 1]:           # Se elemento atual > próximo elemento
                troca(v, j, j + 1)        # Troca os elementos de posição
                houve_troca = True        # Marca que houve troca nesta passagem
        # Exibe o estado do vetor após cada passagem completa
        print(f"Iteração {i+1}: {v}")
        if not houve_troca:               # Se não houve trocas nesta passagem
             break                        # Sai do loop se não houve trocas
    
    print("Vetor ordenado:", v)           # Mostra resultado final    
    return v                              # Termina função (vetor já ordenado)

#def imprimir_vetor(v):                    # Função para imprimir vetor
 #   print(" ".join(map(str, v)))          # Converte elementos para string e imprime separados por espaço

def main():                               # Função main
     # Entrada do número de elementos
    while True:
        try:
            n = int(input("\nDigite o número de elementos: "))
            if n <= 0:
                print("Por favor, digite um número positivo!")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    # Entrada dos elementos
    print(f"\nDigite os {n} elementos (separados por espaço):")
    while True:
        elementos = input().split()
        if len(elementos) != n:
            print(f"Erro: Você deve digitar exatamente {n} elementos!")
            print("Por favor, digite novamente:")
            continue
        
        try:
            vetor = [int(num) for num in elementos]  # Converte para inteiros
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    
    # Processamento
    print("\n=== PROCESSO DE ORDENAÇÃO ===")
    inicio = time.time()
    vetor_ordenado = bubble_sort_otimizado(vetor.copy())
    tempo = time.time() - inicio
    
    # Resultados
    print("\n=== RESUMO ===")
    print("Vetor original:", vetor)
    print("Vetor ordenado:", vetor_ordenado)
    print(f"Tempo de execução: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()