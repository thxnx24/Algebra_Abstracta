#Pregunta 3
#Cree una función que permita calcular la sumatoria de:

def sumatoria(ini, fin):
    suma = 0
    for i in range (ini, fin + 1):
        suma += i
    return suma
ini = int(input("Ingrese el primer numero por favor: "))
fin = int(input("Ingrese el segundo numero por favor: "))

resultado = sumatoria(ini, fin)

print(f"La suma de los numeros entre {ini} y {fin} es {resultado}")