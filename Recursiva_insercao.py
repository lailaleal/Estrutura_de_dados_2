# Questão 3.– Escreva uma versão recursiva do algoritmo de ordenação por inserção.

def ordenacao_insercao_recursiva(vetor, n=None):

    # Caso base: quando n é None = Null ou <= 1
    if n is None:
        n = len(vetor)
    if n <= 1:
        return vetor
    
    # Ordena recursivamente o subvetor de tamanho n-1
    ordenacao_insercao_recursiva(vetor, n-1)
    
    # Insere o último elemento na posição correta
    ultimo = vetor[n-1]
    i = n-2
    
    while i >= 0 and vetor[i] > ultimo:
        vetor[i+1] = vetor[i]
        i -= 1
    
    vetor[i+1] = ultimo
    
    return vetor

# Testando a função
if __name__ == "__main__":
    teste = [12, 11, 13, 5, 6]
    print("Vetor original:", teste)
    print("Vetor ordenado:", ordenacao_insercao_recursiva(teste.copy()))
    
    teste2 = [4, 3, 2, 1]
    print("\nVetor original:", teste2)
    print("Vetor ordenado:", ordenacao_insercao_recursiva(teste2.copy()))