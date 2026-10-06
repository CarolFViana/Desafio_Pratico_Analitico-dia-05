# 4. Faça um programa que percorra duas listas, A e B, e gere uma terceira sem
# elementos repetidos.
# A = [‘Python’, ‘Java’, ‘C’, ‘PHP’, ‘JavaScript’, ‘Dart’]
# B = [‘C++’, ‘Python’, ‘Java’, ‘Julia’, ‘Go’, ‘JavaScript’]

A = ["Python", "Java", "C", "PHP", "JavaScript", "Dart"]
B = ["C++", "Python", "Java", "Julia", "Go", "JavaScript"]

C = []

for linguagem in A:
    if linguagem not in C:
        C.append(linguagem)

for linguagem in B:
    if linguagem not in C:
        C.append(linguagem)

print(C)