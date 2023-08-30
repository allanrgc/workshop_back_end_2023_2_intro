#polimorfism Crie uma classe base chamada Animal com métodos para emitir um som e mostrar informações gerais. Crie 
#subclasses como Cachorro e Gato que herdam de Animal e implementam seus próprios métodos para emitir sons específicos.

class Animal:
    def __init__(self, tipo, nome, cor, patas):
        self.tipo = tipo
        self.nome = nome
        self.cor = cor
        self.patas = patas

    def __str__(self):
        return f'O {self.tipo} se chama {self.nome} e tem a cor {self.cor}.'
    

class Gato(Animal):
    def __init__(self,tipo, nome, cor, patas, som):
        super().__init__(tipo, nome, cor, patas)
        self.som = som  

    def somEmitido(self):
        return f'O gato faz {self.som}'
    def miar(self):
        return f'{self.som}'
    
class Cachorro(Animal):
    def __init__(self,tipo, nome, cor, patas, som):
        super().__init__(tipo, nome, cor, patas)
        self.som = som  

    def somEmitido(self):
        return f'O cachorro faz {self.som}'
    
    def latir(self):
        return f'{self.som}'

gato = Gato('gato','Gatuno', 'preto', 4, 'Miau')
print(gato.__str__())
print(gato.somEmitido())

print('')

cachorro = Cachorro('cachorro','Pekiskis', 'marrom', 4, 'Rolf ')
print(cachorro.__str__())
print(cachorro.somEmitido())
print(cachorro.latir()*4)
print(cachorro.latir())