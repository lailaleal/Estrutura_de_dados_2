#Questão 1.– Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente. (Este
#exercício põe em prática a estratégia de escrever os testes antes de inventar algoritmos para o problema.)
#Verificar se cada elemento é menor ou igual ao próximo elemento, elementos iguais são considerados em ordem crescente. 

def ordem_crescente(v): #v = vetor ou lista 
    # situações que a lista é verdadeira: vazia, 1 elemento, todos os elementos iguais, o elemento é menor ou igual ao proximo. 
    n = len(v) # n = tamanho do vetor
    if n <= 1: return True  
    for i in range (n-1): # percorre o vetor do primeiro elemento até o penúltimo
        if v[i] > v[i+1]: return False # se o elemento atual for maior que o próximo, retorna falso
    return True # se não encontrar nenhum elemento maior que o próximo, retorna verdadeiro
print (ordem_crescente([10, 7, 5, 7, 9])) 
print (ordem_crescente([1, 2, 3, 4, 5]))
