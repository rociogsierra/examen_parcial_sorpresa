
#este ejercicio no lo había entregado porque lo tenía hecho en uno de los apartados de los propuestos para el tema 2
#por si acaso lo voy a copiar y pegar aquí y enviarlo de nuevo
#muchas gracias

import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x >= 0 and self.y >= 0:
            posicion = "({}, {}) es un punto perteneciente al primer cuadrante".format(self.x, self.y)
        elif self.x <= 0 and self.y >= 0:
            posicion = "({}, {}) es un punto perteneciente al segundo cuadrante".format(self.x, self.y)
        elif self.x <= 0 and y <= 0:
            posicion = "({}, {}) es un punto perteneciente al tercer cuadrante".format(self.x, self.y)
        elif self.x >= 0 and self.y <= 0:
            posicion = "({}, {}) es un punto perteneciente al cuarto cuadrante".format(self.x, self.y)
        else:
            posicion = "el punto dado ({},{}), está en el origen y es el (0,0)".format(self.x, self.y)
        return posicion
    
    def vector(self, punto):
        x = punto.x - self.x
        y = punto.y - self.y
        return x , y  

    #optativo: crear una función denominada distancia

    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)*2 + (punto.y - self.y)*2)
        return distancia

class Rectangulo:
    
    def __init__(self, primerpunto=Punto(), segundopunto=Punto()):
        self.primerpunto = primerpunto
        self.segundopunto = segundopunto

    def Base(self):
        self.base = abs(self.segundopunto.x - self.primerpunto.x)
        return self.base

    def Altura(self):
        self.altura = abs(self.segundopunto.y - self.primerpunto.y)
        return self.altura

    def Area(self):
        area = self.base * self.altura
        return area

#EXPERIMENTACIÓN
#creamos los puntos propuestos en el enunciado 

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

#el punto A pertenece al primer cuadrante 
cuadrante_A = cuadrante(A)
#el punto B pertenece al primer cuadrante
cuadrante_B = cuadrante(B)
#el punto C pertenece al tercer cuadrante
cuadrante_C = cuadrante(C)

#el vector AB es el (3,2)
vector_AB = vector(A,B)
#el vector BA es el (-3,-2)
vector_BA = vector(B,A)

#OPCIONAL
#la distancia entre A y B es de 10 unidades
distancia_AB = distancia(A,B)
#la distancia entre B y A es de -10 unidades, aunque al ser una distancia, diremos que la la distancia es de 10 es decir, en valor absoluto ya que las distancias nunca van a ser negativas
distancia_BA = distancia(B,A)

#OPCIONAL
#el punto (0,0) es el punto D, por lo que hallaremos la distancia entre D y A, D y B, y D y C, para determinar cual es el más lejano
distancia_DA = distancia(D,A)
#la distancia entre D y A es de 10 unidades
distancia_DB = distancia(D,B)
#la distancia entre D y B es de 20 unidades
distancia_DC = distancia(D,C)
#la distancia entre D y C es de 8 unidades
#el punto que está más alejado del origen es el B

#creamos un rectángulo usando los puntos A y B
figura_rectangulo = Rectangulo(A,B)

#consultar la base, altura y area del rectángulo
figura_rectangulo.Base()
figura_rectangulo.Altura()
figura_rectangulo.Area()
