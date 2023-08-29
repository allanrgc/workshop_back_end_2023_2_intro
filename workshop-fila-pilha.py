tarefas = []

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Executar Fila de tarefas")
    print("3. Sair")

    num = int(input("\nEscolha uma opção: "))

    if num == 1:
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
    elif num == 2:
        if tarefas:
            print("\nExecutando:", tarefas.pop(0))
        else:
            print("Fila de tarefas vazia")
    elif num == 3:
        print("Fim do programa")
        break
    else:
        print("Opção inválida")
