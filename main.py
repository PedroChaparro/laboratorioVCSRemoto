import math

a = int(input("Ingrese la \"a\" de la fórmula cuadrática teniendo en cuenta su forma ax^2 + bx +c: "))
b = int(input("Ingrese la \"b\" de la fórmula cuadrática teniendo en cuenta su forma ax^2 + bx +c: "))
c = int(input("Ingrese la \"c\" de la fórmula cuadrática teniendo en cuenta su forma ax^2 + bx +c: "))

d = b**2 -4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)

    print("Las soluciones de la ecuación cuadrática ingresada son: {} y {}".format(x1, x2))

elif d == 0:
    solucion = (-b)/(2*a)
    print("Para la ecuación cuadrática ingresada, x1 y x2 son iguales y corresponden a: ", solucion)

else:
    print("No existe solución a la ecuación cuadrática dentro del dominio de los número reales")