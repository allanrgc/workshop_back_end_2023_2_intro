#utilize estrutura de repeticao for para imprimir numeros de 0 a 10.
print("printando de 0 a 10")
for x in range (0,10):
    print(x)

print("")
#utilize estrutura de repeticao for para imprimir numeros de 10 a 0.
print("printando de 10 a 0")
for y in range (10,0):
    print(y)

print("")
#utilize estrutura de repeticao for para imprimir numeros pares de 0 a 10.
print("Printando os pares")
for z in range (10):
    if(z%2 == 0):
        print(z)

print("")
#utilize estrutura de repeticao for para fazer a tabuada de adição de 0 a 10
#de um numero digitado no terminal.
print("printando tabu")
numero = int(input("Digite um numero: "))
for num in range (10):
    print(numero+num)

#utilizando estrutura de repeticao while crie um programa que peça varios
#nomes e só pare quando for digitado "parar"
nome = str(input("Digite um nome: "))
while(nome != "parar"):
    print(nome)
    nome = str(input("Digite outro nome: "))

print("")
#utilizando estrutura de repeticao while crie um programa que faça a soma de
#todos os numeros digitados. o loop so devera parar quando for digitado 0
numero = int(input("Digite um número: "))
while(numero != 0):
    numero += numero
    print("A soma dos números digitados foi: ", numero)
    numero = int(input("Digite um número: "))

print("")
#utilizando estrutura de repeticao while crie um programa que leia
#exclusivamente o sexo como 'F' e 'M' e o loop so deve terminar quando
#sexo for = sair. ao fim mostre a quantidade e mulheres e homens
sexo = str(input("Digite o sexo 'M' para Masculino e 'F' para Feminino: "))
while(sexo != "sair"):
    if(sexo == "M" or sexo == "F"):
        print(sexo)
        sexo = str(input("Digite o sexo 'M' ou 'F': "))
    else:
        print("Assim não pode")
        sexo = str(input("Digite o sexo 'M' ou 'F': "))
