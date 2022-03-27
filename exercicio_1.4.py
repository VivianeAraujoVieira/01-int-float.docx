 
'''Faça um programa que receba do usuário o seu peso em kg e altura em metros e imprima o
índice de massa corporal (IMC) do usuario.'''

nome = str(input("Qual o seu nome: "))
print(f"Olá {nome}, espero que esteja tudo bem com você! ")
peso = float(input("Me informe o seu peso:  "))
alt = float(input("Agora informe a sua altura:  "))
imc = peso / alt**2

if (imc<=18.5):
    print(f" {nome} seu imc foi {imc:.2f} você esta abaixo do peso. ")
if (imc>=19) and (imc<24.9):
        print(f"Parabéns {nome}, seu imc é {imc:.2f}, você esta dentro do peso ideal. ")
if (imc>=25) and (imc<=29.9):
    print(f"{nome}, seu imc é {imc:.2f}, esta um pouco acima do peso, cuide-se! ")
if (imc>=30):
    print (f"{nome}, seu imc é {imc:.2f}, você esta obeso! ")
if (imc>=40):
    print(f"{nome}, seu imc é {imc}, você esta com obesidade morbida! ")
