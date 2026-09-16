#Ejercicio 4

class Calcular_Edades:

  @staticmethod
  def calcular_edalber(edjuan):
      return (2 * edjuan) / 3

  @staticmethod
  def calcular_edana(edjuan):
      return (4 * edjuan) / 3

  @staticmethod
  def calcular_edmama(edjuan, edalber, edana):
      return edjuan + edalber + edana

edjuan = 9
edalber = Calcular_Edades.calcular_edalber(edjuan)
edana = Calcular_Edades.calcular_edana(edjuan)
edmama = Calcular_Edades.calcular_edmama(edjuan, edalber, edana)

# Resultado formateado
print(f"Las edades son: Alberto = {edalber}, Juan = {edjuan}, Ana = {edana}, Mamá = {edmama}")