# Diversão de carnaval
"""Faça um programa que receba dois números do usuário,
 A e B  e imprima na tela as seguintes operações:

    A soma de A e B;
    A diferença quando subtrai B de A;
    O produto (multiplicação) entre A e B;
    O quociente (parte inteira da divisão) quando se divide A por B;
    O resto da divisão entre A e B;
    O resto de log10 de A;
    O resto de A elevado a B"""

import math
n1 = int(input("\033[1;34mInforme o primeiro número:\033[m "))
n2 = int(input("\033[1;34mInforme o segundo número:\033[m "))
som = n1 + n2
dif = n1 - n2
prod = n1 * n2 
quoc = n1 // n2
rest = n1 % n2
log =  math.log10(n1)
pot = n1**n2
print(f"\n\033[1;34mResultado das operações:\033[m\n\n \033[1;33mSoma:\033[m {som}\n \033[1;33mSubtração:\033[m {dif}\n \033[1;33mMultiplicação:\033[m {prod} \n \033[1;33mQuociente:\033[m {quoc}")
print(f"\033[1;33m Resto da divisão:\033[m {rest}\n \033[1;33mLogaritmo10:\033[m {log:.2f}\n \033[1;33mPotência:\033[m {pot:.2f} \033[m")