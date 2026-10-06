# 7. Sabemos que as listas possuem funções que ajudam a construir programas
# sem escrever muito código. Vimos as funções: max(), min(), sum() e enumerate().

T = [-10, -8, 0, 1, 2, 20, -2, -4]

soma = 0

for i in range(len(T)):
    soma += T[i]

print(f"A soma total da lista é {soma}")

# O código acima faz a soma de todos os números da lista sem utilizar a função
# sum(). Utilizando o código como base, faça:

# a) Um código para descobrir o maior número da lista

T = [-10, -8, 0, 1, 2, 20, -2, -4]

maior = max(T)
print(f"O maior número da lista é {maior}")

# b) Um código para descobrir o menor número da lista

T = [-10, -8, 0, 1, 2, 20, -2, -4]

menor = min(T)
print(f"O menor número da lista é {menor}")

# c) Um código para mostrar endereço e elemento na lista

T = [-10, -8, 0, 1, 2, 20, -2, -4]

for endereco, elemento in enumerate(T):
    print(f"Endereço: {endereco} | Elemento: {elemento}")

