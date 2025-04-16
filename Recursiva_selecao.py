# Questão 4.– Escreva uma versão recursiva do algoritmo de ordenação por seleção.

def selecao_recursiva(vetor, inicio=0):
    
    # Caso base: quando restar apenas um elemento
    if inicio >= len(vetor) - 1:
        return vetor
    
    # Encontra o índice do menor elemento no subvetor não ordenado
    indice_menor = inicio
    for i in range(inicio + 1, len(vetor)):
        if vetor[i] < vetor[indice_menor]:
            indice_menor = i
    
    # Troca o menor elemento com o primeiro do subvetor não ordenado
    vetor[inicio], vetor[indice_menor] = vetor[indice_menor], vetor[inicio]
    
    # Chamada recursiva para o restante do vetor
    return selecao_recursiva(vetor, inicio + 1)

# Testando a função
if __name__ == "__main__":
    teste = [64, 25, 12, 22, 11]
    print("Vetor original:", teste)
    print("Vetor ordenado:", selecao_recursiva(teste.copy()))
    
    teste2 = [5, 1, 4, 2, 8]
    print("\nVetor original:", teste2)
    print("Vetor ordenado:", selecao_recursiva(teste2.copy()))