# 5. Observe o código a seguir e analise as questões pedidas

L = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))

x = 0

while x < len(L) and L[x] != p:
    x += 1

if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")

# a) Explique a função das linhas 20, 24, 25 e 27
# Linha 20: inicializa a variável booleana achou com False, indicando que o valor ainda não foi encontrado.
# Linha 24: altera achou para True quando o valor procurado é encontrado na lista.
# Linha 25: o comando break interrompe o laço de repetição assim que o valor é encontrado.
# Linha 27: verifica o valor da variável achou para decidir se será exibida a mensagem de valor encontrado ou não encontrado.

# b) Refaça o código de forma a realizar a mesma tarefa, mas sem utilizar a variável achou

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))

x = 0

while x < len(L) and L[x] != p:
    x += 1

if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")

