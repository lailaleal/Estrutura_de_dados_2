#Questão 2.– Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem
#crescente e insira x no vetor de modo a manter a ordem crescente.
# O objetivo do exercício é inserir um número em uma lista ordenada, mantendo ela ordenada.
# def insere_x(x, v): # x = valor a ser inserido e v = vetor.


# Função para verificar se o vetor está ordenado
def esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True

# Pede ao usuário para digitar um vetor ordenado
while True:
    entrada = input("Digite um vetor ordenado (números separados por espaço): ")
    try:
        vetor = [int(num) for num in entrada.split()]
        if esta_ordenado(vetor):
            break
        else:
            print("O vetor não está ordenado! Digite novamente.")
    except ValueError:
        print("Por favor, digite apenas números separados por espaços.")

# Pede o número a ser inserido
while True:
    try:
        numero = int(input("Digite o número a ser inserido: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.")

# Encontra a posição correta para inserir o número
posicao = 0
for i in range(len(vetor)):
    if vetor[i] < numero:
        posicao = i + 1
    else:
        break

# Insere o número na posição correta
vetor.insert(posicao, numero)

# Mostra o resultado
print("\nVetor original:", entrada)
print("Número inserido:", numero)
print("Vetor ordenado com o novo número:", vetor)