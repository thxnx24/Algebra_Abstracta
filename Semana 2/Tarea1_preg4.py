#Pregunta 4
#Cree una funcion que permita calcular Suma de los enteros positivos d tales que d|n

def suma_div(x):
    suma = 0
    for i in range(1, x + 1):
        if (x % i == 0):
            suma += i
    return suma

x = int(input("Ingrese el numero por favor: "))

resultado = suma_div(x)
print(f"La suma de los divisores de: {x} es {resultado}")