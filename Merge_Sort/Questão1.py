## Questão 1.– Escreva uma versão recursiva do algoritmo Merge Sort que ordene um vetor v[incio..f im]
## em ordem decrescente. Sua função deve conter o código da intercalação, considerando que os sub-
## vetores v[incio..meio] e v[meio + 1..f im] já estejam ordenados de forma decrescente. O resultado final
## também deve ser um vetor decrescente.

def merge_decrescente(v, inicio, meio, fim):

    # Criar cópias das duas metades do vetor
    D = v[inicio:meio+1] # vetor da esquerda (D)
    E = v[meio+1:fim+1] # vetor da direita (E)
    
    i = 0  # índice para Esquerda (D)
    j = 0  # índice para Direita (E)
    j = 0  # índice para R
    k = inicio  # índice para o vetor original
    
    # Intercalar em ordem decrescente ( >= Descrecente / <= Crescente)
    # Enquanto houver elementos em ambas as metades
    while i < len(E) and j < len(D):
        if E[i] >= D[j]:  
            v[k] = E[i]
            i += 1
        else:
            v[k] = D[j]
            j += 1
        k += 1
    
    # Copiar os elementos restantes da esquerda
    while i < len(E):
        v[k] = E[i]
        i += 1
        k += 1
    
    # Copiar os elementos restantes de direita
    while j < len(D):
        v[k] = D[j]
        j += 1
        k += 1