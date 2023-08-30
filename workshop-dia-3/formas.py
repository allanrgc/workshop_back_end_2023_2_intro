#Herança de Formas Geométricas Crie uma classe base chamada FormaGeometrica 
#com um método para calcular a área. Em seguida, crie subclasses como 
#Retangulo e Circulo que herdam de FormaGeometrica e implementam seus 
#próprios métodos para calcular a área.

class FormaGeometrica:
    def calcularArea(self, raio):
        return 3.14*(raio**2)

    
class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcularArea(self, b,h):
        return b*h

circulo = Circulo()
area = circulo.calcularArea(20)
print(area)

retangulo = Retangulo()
area = retangulo.calcularArea(30, 40)
print(area)

