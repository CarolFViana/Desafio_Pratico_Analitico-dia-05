
# 1. Observe o código apresentado a seguir e veja outras formas de inserir dados em uma lista.

numeros = [0, 0, 0, 0, 0]

x = 0

while x < 5:
    numeros[x] = float(input("Digite um número qualquer: "))
    x += 1

y = 0

while y < 5:
    print(f"{numeros[y]}")
    y += 1

# a) Refaça o código utilizando a estrutura FOR

numeros = [0, 0, 0, 0, 0]

for x in range(5):
    numeros[x] = float(input("Digite um número qualquer: "))

for y in range(5):
    print(numeros[y])

# b) O que acontece se colocarmos while <= 4: ? Justifique.
# Se a condição for alterada de x < 5 para x <= 4, o resultado será o mesmo,
# pois em ambos os casos o laço executará enquanto x assumir os valores
# de 0 a 4, totalizando cinco repetições.

# c) Esse código funcionaria caso quiséssemos inserir mais de 5 elementos?
# Justifique.
# Não. O código foi construído para trabalhar com apenas cinco elementos, pois a lista possui cinco
# posições e a condição do while também limita a repetição a cinco vezes. Para inserir mais elementos
# seria necessário alterar o código.

# d) Qual a problemática da alternativa anterior (c) para a realidade dos códigos?
# A problemática é que o código fica limitado a uma quantidade fixa de elementos. Sempre que a
# quantidade de dados mudar, será necessário alterar manualmente o programa, tornando-o pouco
# flexível, pouco reutilizável e mais difícil de manter.

# e) Refaça o código melhorando os problemas encontrados na alternativa (c e d)

numeros = []

quantidade = int(input("Quantos números deseja inserir? "))

for x in range(quantidade):
    numero = float(input("Digite um número qualquer: "))
    numeros.append(numero)

for numero in numeros:
    print(numero)