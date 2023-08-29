class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        # return f'ou eu sou uma garrafa de tamanho {self.tamanho}'
        return f'ou eu sou uma garrafa {self.marca}'
    
    #eq: Compara se as marcas são iguais, no caso shopee e Stanley e é printado no garrafa==stanley
    def __eq__(self, obj):
        if self.marca == obj.marca:
            return True
        else:
            return False
    
    def encher(self):
        print('estou enchida')
    
    def esvaziar(self):
        print('estou vazia')

garrafa = Garrafa(500, 'preto', 'shopee')
print(garrafa)
stanley = Garrafa(200, 'preto', 'Stanley')
print(stanley)

print(garrafa == stanley)

stanley.encher()
stanley.esvaziar()