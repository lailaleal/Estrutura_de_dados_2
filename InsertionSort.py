import time  # Importa módulo para medir tempo de execução

def insertion_sort(array): # Função de ordenação por inserção
    n = len(array)
    print("\n=== INSERTION SORT ===")
    print("Array original:", array)  # Mostra array antes da ordenação
    
    for i in range(1, n):  # Começa do segundo elemento (índice 1)
        aux = array[i]     # Elemento atual a ser posicionado
        j = i - 1          # Índice do elemento anterior
        
        # Move elementos maiores que 'aux' para a direita
        while j >= 0 and aux < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = aux  # Insere 'aux' na posição correta
        
        print(f"Iteração {i}: {array}")  # Mostra progresso a cada iteração
    
    print("Array ordenado:", array)  # Mostra resultado final
    return array

def main():  # Função principal (idêntica à sua estrutura)
    print("=== INSERTION SORT ===")
    
    # 1. Solicita o número de elementos
    while True:
        try:
            n = int(input("\nDigite o número de elementos: "))
            if n <= 0:
                print("Por favor, digite um número positivo!")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    # 2. Solicita os elementos do array
    print(f"\nDigite os {n} elementos (separados por espaço):")
    while True:
        elementos = input().split()  # Recebe os elementos como strings
        
        # Verifica se a quantidade corresponde ao informado
        if len(elementos) != n:
            print(f"Erro: Você deve digitar exatamente {n} elementos!")
            print("Por favor, digite novamente:")
            continue
        
        # Converte para inteiros
        try:
            array = [int(num) for num in elementos]
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    
    # 3. Processamento da ordenação
    print("\n=== PROCESSO DE ORDENAÇÃO ===")
    inicio = time.time()
    array_ordenado = insertion_sort(array.copy())  # Ordena uma cópia
    tempo = time.time() - inicio
    
    # 4. Exibição dos resultados
    print("\n=== RESULTADOS ===")
    print("Array original:", array)
    print("Array ordenado:", array_ordenado)
    print(f"Tempo de execução: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()