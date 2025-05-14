#Questão 3.– No código do Merge Sort, o meio é calculado como: meio = (inicio + fim) \ 2.
#Refaça a implementação utilizando as seguintes variações:
#• (inicio + fim - 1) \ 2
#• (inicio + fim + 1) \ 2
#Em seguida, responda:

#a) Houve diferença nos resultados?
#  Há pequenas diferenças nos valores de meio, mas não nos resultados finais

#b) O algoritmo ainda funciona corretamente?
#  Sim, o algoritmo continua funcionando corretamente, pois todas as variações de meio ainda
#  garantem que o vetor seja dividido em duas partes, mesmo que as divisões sejam ligeiramente diferentes.

#c) Alguma das variações provoca falhas? Justifique.
#  Nenhuma das variações provoca falhas, pois todas garantem que o vetor seja dividido em duas partes.
#  No entanto, a variação (inicio + fim - 1) \ 2 pode levar a um ligeiro desbalanceamento em
#  relação ao tamanho das duas partes, especialmente quando o vetor tem um número ímpar de elementos.
#  Isso pode afetar o desempenho em casos extremos, mas não provoca falhas no algoritmo.


# Versão padrão: meio = (inicio + fim) // 2
def meio_normal(inicio, fim):
    return (inicio + fim) // 2

# Variação 1: meio = (inicio + fim - 1) // 2
def meio_var1(inicio, fim):
    return (inicio + fim - 1) // 2

# Variação 2: meio = (inicio + fim + 1) // 2
def meio_var2(inicio, fim):
    return (inicio + fim + 1) // 2

# Teste comparativo
for inicio, fim in [(0, 9), (0, 10), (5, 15), (1, 8)]:
    print(f"início={inicio}, fim={fim}")
    print("meio normal:", meio_normal(inicio, fim))
    print("meio -1   :", meio_var1(inicio, fim))
    print("meio +1   :", meio_var2(inicio, fim))
    print("------")
