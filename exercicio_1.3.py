
''' Crie  um programa que receba os três lados de um triângulo - s1, s2, e s3 -
 calcule sua área. Compare a resposta com o exercico anterior, dada as mesmas entradas. 
 Os resultados devem ser idênticos'''

import math


s1 = float(input("Informe o valor do primeiro lado do triângulo: "))
s2 = float(input("Informe o valor do segundo lado do triângulo: "))
s3 = float(input("Informe o valor do terceiro lado do triângulo: "))
soma = (s1 + s2 + s3) / 2
#area = (soma* (soma-s1) * (soma-s2) * (soma-s3))**(1/2)
area = math.sqrt(soma* (soma-s1) * (soma-s2) * (soma-s3)) 
print((area))