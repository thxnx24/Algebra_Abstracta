#Cree una funcion que permita calcular Suma de los enteros positivos d tales que d|n

def suma_div(x):
    suma = 0
    for i in range(1, x + 1):
        if (x % i == 0):
            suma += i
    return suma

x = 6
print(f"La suma de los divisores de: {x} es {suma_div(x)}")