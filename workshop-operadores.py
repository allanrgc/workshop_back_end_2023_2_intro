#crie um programa que peça um numero e mostre o seu sucessor e antecessor
numero = float(input("Digite um número: "))
print("O antecessor de ",numero," é ",numero-1," e seu sucessor é ",numero+1)

print("")
#crie um programa que leia dois numeros e exiba a soma dos dois numeros,
#a subtracao, multiplicacao e divisao
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
print("A soma dos dois número é: ",num1+num2)
print("A subtração dos dois número é: ",num1-num2)
print("A subtração dos dois número é: ",num1/num2)
print("A multiplicação dos dois número é: ",num1*num2)

print("")
#crie um programa que leia dois numeros e que exiba True se o primeiro
#numero for maiorque o primeiro e False se o primeiro numero for menor ou
#igual ao segundo numero
if(num1>num2):
    print("True")
elif(num1<=num2):
    print("False")
else:
    print("Inválido")


#crie um programa que leia uma temperatura em celsius e a
#converta para fahrenheit
temp = float(input("Qual é a temperatura atual(ºC)?"))
fah = 32 + (temp*9/5)
print(temp,"ºC em Fahrenheit é ",fah,"F")
