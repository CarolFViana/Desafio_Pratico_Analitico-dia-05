# 6. Observe o código a seguir e analise as questões pedidas

L = []

while True:
    n = int(input("Digite um número ou 0 para sair: "))

    if n == 0:
        break

    L.append(n)

x = 0

while x < len(L):
    print(L[x])
    x = x + 1

# a) Modifique o código usando a estrutura FOR para as duas repetições.

L = []

quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    n = int(input("Digite um número ou 0 para sair: "))

    if n == 0:
        break

    L.append(n)

for n in L:
    print(n)

    # b) A alternativa anterior teve êxito? Justifique.
    #Parcialmente. A segunda repetição pôde ser substituída pelo for sem alterar sua finalidade, 
    # pois ela apenas percorre os elementos já armazenados na lista. Entretanto, na primeira repetição foi necessário
    # definir previamente uma quantidade de execuções. No código original, o while True permite inserir uma quantidade
    # indefinida de valores e só encerra quando o usuário digita 0. Portanto, a substituição
    # pelo for altera o comportamento original do programa.