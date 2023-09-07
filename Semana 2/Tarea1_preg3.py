#Cree una función que permita calcular la sumatoria de:

def sumatoria(ini, fin):
    suma = 0
    for i in range (ini, fin + 1):
        suma += i
    return suma

ini = 1
fin = 56

print(sumatoria(ini, fin))
