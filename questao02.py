# 2. Observe o código a seguir e analise as questões pedidas

L = [1, 2, 3]

x = 0

while x < 3:
    print(L[x])
    x += 1

# a) Qual a saída final da variável x?
# O valor final da variável x será 3, pois ela inicia em 0 e é incrementada 
# em 1 a cada repetição até que a condição x < 3 se torne falsa.

# b) Podemos considerar o resultado final da variável x como o tamanho da lista? Justifique.
# Neste caso, o valor final de x coincide com o tamanho da lista, pois ambos são 3.
# Porém, não podemos considerar x uma forma geral de obter o tamanho da lista,
# pois o limite 3 foi definido diretamente na condição do while. Se o tamanho da lista mudar,
# o valor utilizado no laço também precisará ser alterado.

# c) O que aconteceria se atualizarmos a lista para L=[7,8,9,10,11,12]? Justifique
# O código mostrará apenas os valores 7, 8 e 9, pois a condição x < 3 permite somente três repetições,
# independentemente de a lista possuir seis elementos. Os demais valores não serão percorridos.

# d) Reescreva o código para que o mesmo possa funcionar para qualquer lista L

L = [7, 8, 9, 10, 11, 12]

x = 0

while x < len(L):
    print(L[x])
    x += 1