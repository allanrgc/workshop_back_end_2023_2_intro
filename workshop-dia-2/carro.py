#Classe Carro Crie uma classe chamada Carro com atributos como marca, 
#modelo e ano. Crie um método para acelerar o carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
    
    def acelerar(self):
        print('Acelerando')
    
yaris = Carro('Toyota', 'Yaris', 2021)
print(yaris)
x3 = Carro('BMW', 'X3', 2021)
print(x3)

yaris.acelerar()
