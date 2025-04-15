import time  # Biblioteca para medir tempo de execução

# Função que executa o Insertion Sort otimizado com exibição de cada passo
def insertion_sort_otimizado(array):
    n = len(array)  # Pega o tamanho do vetor
    print("\n=== PASSO A PASSO DA ORDENAÇÃO ===")  # Título da seção
    
    for i in range(1, n):  # Começa do segundo elemento até o último
        aux = array[i]  # Elemento que será inserido na posição correta
        j = i - 1  # Posição anterior ao elemento atual

        # Loop para encontrar a posição correta de 'aux' no vetor
        while j >= 0 and aux < array[j]:  # Enquanto aux for menor que os anteriores
            array[j + 1] = array[j]  # Move o elemento maior uma posição à frente
            j -= 1  # Volta uma posição para comparar o próximo anterior

        array[j + 1] = aux  # Insere o elemento na posição correta
        print(f"Iteração {i}: {array}")  # Exibe o vetor após a iteração

# Função principal que controla a execução do programa
def main():
    print("=== INSERTION SORT OTIMIZADO ===")  # Título do programa

    # Solicita ao usuário o número de elementos do vetor
    while True:
        try:
            n = int(input("\nDigite o número de elementos: ").strip())  # Lê o número
            if n <= 0:  # Verifica se é positivo
                print("Por favor, digite um número positivo!")
                continue
            break  # Entrada válida
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Solicita os elementos do vetor ao usuário
    print(f"\nDigite os {n} elementos (separados por espaço):")
    while True:
        entrada = input("> ").strip()  # Lê a linha e remove espaços extras
        elementos = entrada.split()  # Divide pelos espaços

        if len(elementos) != n:  # Verifica se a quantidade está correta
            print(f"Erro: Você deve digitar exatamente {n} elementos!")
            continue

        try:
            vetor = [int(num) for num in elementos]  # Converte todos os valores para inteiros
            break  # Sai do loop se tudo estiver certo
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    # Processamento de ordenação
    print("\n=== PROCESSO DE ORDENAÇÃO ===")  # Título
    inicio = time.time()  # Marca o tempo de início
    vetor_ordenado = vetor.copy()  # Cria uma cópia do vetor original
    insertion_sort_otimizado(vetor_ordenado)  # Executa a ordenação
    tempo = time.time() - inicio  # Calcula o tempo de execução

    # Exibe os resultados
    print("\n=== RESULTADOS ===")
    print("Vetor original:", vetor)  # Exibe o vetor original
    print("Vetor ordenado:", vetor_ordenado)  # Exibe o vetor ordenado
    print(f"Tempo de execução: {tempo:.6f} segundos")  # Mostra o tempo decorrido

# Início do programa
if __name__ == "__main__":
    main()  # Executa a função principal
