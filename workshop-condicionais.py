#crie um programa que receba uma idade e retorne se pode obter carteira de
#motorista(CNH)
idade = int(input("Qual a sua idade? "))
if(idade >= 18):
    print("Já pode tirar CNH")
else:
    print("Não tem idade para tirar carteira")

print("")
#crie um programa que leia uma velocidade de um carro e multe se passar com
#velocidade maior que 80km/h. mostre que ele foi multado. a multa é de 7R$ por
#cada km acima do limite
velo = int(input("Qual a velodidade do carro? "))
if(velo > 80):
    multa = (velo - 80)*7
    print("Você foi multado em: ", multa)
else:
    print("safe")

print("")
#crie um programa que leia tres numeros e mostre qual deles e o maior e o menor
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite só mais um número: "))
if(num1>num2 and num1>num3):
    if(num2>num3):
        print(num1," é o maior e ",num3," é o menor")
    else:
        print(num1," é o maior e ",num2," é o menor")
elif(num2>num1 and num2>num3):
    if(num1>num3):
        print(num2," é o maior e ",num3," é o menor")
    else:
        print(num2," é o maior e ",num1," é o menor")
elif(num3>num1 and num3>num2):
    if(num1>num2):
        print(num3," é o maior e ",num2," é o menor")
    else:
        print(num3," é o maior e ",num1," é o menor")
else:
    print("Acho que os números são iguais")

print("")
#crie um programa que receba uma quantidade de canetas pretas e azuis.
#A caneta azul vale R$2.00, a caneta preta vale R$2.50. Mostre a quantidade
#final a ser paga.
cazul = 2.0
cpret = 2.5
qazul = int(input("Quantas canetas azuis você quer? "))
qpret = int(input("Quantas canetas pretas você quer? "))
print("Canetas azuis: ",qazul,"x",cazul," = ",qazul*cazul)
print("Canetas Pretas: ",qpret,"x",cpret," = ",qpret*cpret)
print("Total: ",qazul*cazul + qpret*cpret)

print("")
#crie um programa que leia o nome de tres pessoas: João Maia, João Abrantes e
#Pedro. Para os respectivos nomes imprima:'oi eu sou joao maia', 'oi eu sou
#joao abrantes', 'oi eu sou pedro', e caso o nome nao seja nenhum dos
#tres imprima 'oi meu nome é {nome}'
nome = str(input("Qual seu nome? "))
if(nome == "João Maia"):
    print("oi eu sou joao maia")
elif(nome == "João Abrantes"):
    print("oi eu sou joao abrantes")
elif(nome == "Pedro"):
    print("oi eu sou pedro")
else:
    print("oi meu nome é ",nome)


