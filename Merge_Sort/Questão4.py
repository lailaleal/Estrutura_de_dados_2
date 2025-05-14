#Questão 4. Implemente o algoritmo Merge Sort para listas encadeadas simples (estrutura de nó
#com campo de valor e ponteiro para o próximo). A função deve ordenar a lista em ordem crescente
#sem alocar novas células, apenas manipulando os ponteiros existentes.

# Estrutura de nó de lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Função que divide a lista ao meio
def dividir_lista(head):
    if not head or not head.proximo:
        return head, None

    slow = head
    fast = head.proximo  # ponteiro rápido anda 2x

    while fast and fast.proximo:
        slow = slow.proximo
        fast = fast.proximo.proximo

    meio = slow.proximo
    slow.proximo = None  # separa a lista

    return head, meio

# Função merge para intercalar listas encadeadas
def merge_listas(l1, l2):
    dummy = Node(0)
    atual = dummy

    while l1 and l2:
        if l1.valor <= l2.valor:
            atual.proximo = l1
            l1 = l1.proximo
        else:
            atual.proximo = l2
            l2 = l2.proximo
        atual = atual.proximo

    atual.proximo = l1 if l1 else l2  # anexa o restante
    return dummy.proximo

# Merge Sort para lista encadeada
def merge_sort_lista(head):
    if not head or not head.proximo:
        return head  # lista com 0 ou 1 elemento já está ordenada

    esquerda, direita = dividir_lista(head)
    esquerda_ordenada = merge_sort_lista(esquerda)
    direita_ordenada = merge_sort_lista(direita)

    return merge_listas(esquerda_ordenada, direita_ordenada)

# Função auxiliar para criar lista encadeada
def criar_lista(valores):
    head = Node(valores[0])
    atual = head
    for val in valores[1:]:
        atual.proximo = Node(val)
        atual = atual.proximo
    return head

# Função auxiliar para imprimir lista encadeada
def imprimir_lista(head):
    while head:
        print(head.valor, end=' ')
        head = head.proximo
    print()

# Teste
valores = [7, 2, 9, 4, 3, 8, 6, 1]
lista = criar_lista(valores)
print("Original:")
imprimir_lista(lista)
ordenada = merge_sort_lista(lista)
print("Ordenada:")
imprimir_lista(ordenada)
