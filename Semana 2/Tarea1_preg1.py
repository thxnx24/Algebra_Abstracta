#Crea una función que permita ingresar el radio R y la altura H de un cilindro y que"
#retorne su area de la superficie

import math

def cal_area_superficie(radio, altura):
    if radio <= 0 or altura <= 0:
        return "El radio y la altura deben tener valores positivos."
    
    area_lateral = 2 * math.pi *radio *altura
    area_base = 2 *math.pi *radio ** 2
    area_total = area_lateral + area_base
    
    return area_total

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingres la altura del cilindro: "))

area_superficie = cal_area_superficie(radio, altura)
print(f"El area de la superficie es: {area_superficie}")