#Cree una función que permita Ingresar la base mayor( B ), 
#base menor( b ) y la altura( h ) de un trapecio y hallar su area

def area_trapecio(b_menor, b_mayor, altura):
    if b_mayor <= 0 or b_menor <= 0 or altura <= 0:
        return "Los valores deben ser numeros positivos."
    
    area_trapecio_ = (b_menor + b_mayor)/2 * altura
    return area_trapecio_

b_menor = float(input("Ingrese la base menor: "))
b_mayor = float(input("Ingrese la base mayor: "))
altura = float(input("Ingrese la altura: "))

area_total = area_trapecio(b_menor, b_mayor, altura)
print(f"El area total del trapecio es: {area_total}")