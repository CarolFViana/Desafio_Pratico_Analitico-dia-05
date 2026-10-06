#8. Escreva um código que receba números ou palavras. O código deve
# armazenar cada situação em listas diferentes, ou seja, uma lista só para as
# palavras e outra só para os números. O programa deve encerrar quando o
# usuário digitar o x ou X. No fim, mostre o que foi inserido nas duas listas, a
# quantidade total de coisas digitadas pelo usuário. (Dica: métodos em Python)

numeros = []
palavras = []

while True:
    valor = input("Digite um número, uma palavra ou X para sair: ")

    if valor.lower() == "x":
        break

    if valor.isnumeric():
        numeros.append(int(valor))
    else:
        palavras.append(valor)

total = len(numeros) + len(palavras)

print("Números:", numeros)
print("Palavras:", palavras)
print("Quantidade total digitada:", total)