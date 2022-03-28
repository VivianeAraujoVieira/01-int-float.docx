
"""Escreva um programa que leia do usuário um número de 4 digitos e imprima a soma desses digitos.
exemplo, se o usuario digitar 3141, seu programa deverá imprimir na tela 3+1+4+1 = 9"""

num = input("Digite um número de 4 digitos: ")
soma = 0
for c in num:
    soma += int(c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
print(f"{num[0]} + {num[1]} + {num[2]} + {num[3]} = {soma}")
