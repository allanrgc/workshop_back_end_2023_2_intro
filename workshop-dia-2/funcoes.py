def calculadora():
    def soma(a,b):
        print(a+b)

    def sub (a,b):
        print(a-b)
    
    def mult (a,b):
        print(a*b)
    
    def div (a,b):
        print(a/b)

    func = input("Operação: ")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if (func == 'soma'):
        soma(num1,num2)

    elif (func == 'sub'):
        sub(num1,num2)

    elif (func == 'mult'):
        mult(num1,num2)

    elif (func == 'div'):
        div(num1,num2)
        
    else:
        print("Opção inválida")

calculadora()