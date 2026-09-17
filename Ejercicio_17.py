#Ejercicio 17

import math

class Calculos:
    @staticmethod
    def calcular_longitud_circunferencia(radio):
        return 2 * math.pi * radio

    @staticmethod
    def calcular_area_circulo(radio):
        return math.pi * math.pow(radio,2)

radio = 3.0

longitud_circunferencia = Calculos.calcular_longitud_circunferencia(radio)
area_circulo = Calculos.calcular_area_circulo(radio)

print("Longitud circunferencia: ", longitud_circunferencia)
print("Área círculo: ", area_circulo)