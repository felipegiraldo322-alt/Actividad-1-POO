#Ejercicio 5

import math

class Calculos:
    @staticmethod
    def calcular_x(x,y):
        return x + math.pow(y,2)


suma = 0
x = 20
y = 40

suma = suma + x
x = Calculos.calcular_x(x, y)

suma = suma + (x / y)

print(f"El valor de x es : {x}")
print(f"El valor de y es : {y}")
print(f"El valor de la suma es: {suma}")