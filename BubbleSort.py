# Importa bibliotecas necessárias
#import random  # Para gerar números aleatórios
import time    # Para medir tempo de execução

# Função que gera um vetor de tamanho 'n' com valores aleatórios entre 0 e n-1
#def gera_vetor(n):
    #return [random.randint(0, n-1) for _ in range(n)]
    # random.randint(a, b) → retorna um número aleatório entre a e b (inclusive)
    # A list comprehension cria uma lista com 'n' elementos aleatórios

# Função Bubble Sort
def bubble_sort(array):
    n = len(array)  # Obtém o tamanho do vetor
    
    print("Vetor original:", array)  # Mostra o vetor antes da ordenação
    
    # Loop externo: controla quantas vezes o vetor será percorrido
    # Executa n-1 vezes pois o último elemento já estará ordenado
    for i in range(n - 1):
        
        
        # Loop interno: compara elementos adjacentes e os troca se estiverem fora de ordem
        # A cada iteração externa, diminui o limite pois os maiores elementos já estão no final
        for j in range(n - 1 - i):  # A cada iteração, o maior elemento já está no final
            if array[j] > array[j + 1]:  # Se o elemento atual > próximo elemento...
                array[j], array[j + 1] = array[j + 1], array[j]  # Troca os dois elementos
    
        # Exibe o estado do array após cada passagem completa
        print(f"Iteração {i+1}: {array}")
    print("\nVetor ordenado:", array)  # Exibe o resultado final
    return array  # Retorna o array ordenado

# Função principal 
def main():
    """Função principal que gerencia a execução do programa"""
    
    print("=== BUBBLE SORT ===")  # Título do programa
    
    # 1. Solicitação do número de elementos com tratamento de erros
    while True:
        try:
            n = int(input("\nDigite o número de elementos: "))  # Recebe o tamanho do array
            if n <= 0:
                print("Por favor, digite um número positivo!")  # Valida número positivo
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")  # Trata erros de tipo
    
    # 2. Solicitação dos elementos do array
    print(f"\nDigite os {n} elementos (separados por espaço):")
    while True:
        elementos = input().split()  # Recebe os elementos como strings separadas por espaço
        
        # Verifica se a quantidade de elementos digitados corresponde ao n informado
        if len(elementos) != n:
            print(f"Erro: Você deve digitar exatamente {n} elementos!")
            print("Por favor, digite novamente:")
            continue
        
        # Converte os elementos para inteiros com tratamento de erros
        try:
            array = [int(num) for num in elementos]  # List comprehension para conversão
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    
    # 3. Processamento da ordenação
    print("\n=== PROCESSO DE ORDENAÇÃO ===")
    inicio = time.time()  # Marca o início do cronômetro
    array_ordenado = bubble_sort(array.copy())  # Ordena uma cópia para preservar o original
    tempo = time.time() - inicio  # Calcula o tempo decorrido
    
    # 4. Exibição dos resultados finais
    print("\n=== RESULTADO FINAL ===")
    print("Vetor original:", array)  # Mostra o array antes da ordenação
    print("Vetor ordenado:", array_ordenado)  # Mostra o array após ordenação
    print(f"Tempo de execução: {tempo:.6f} segundos")  # Exibe o tempo com 6 casas decimais


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal