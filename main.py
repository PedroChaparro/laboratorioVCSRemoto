import math

b = int(input("Ingrese un número para calcular su cuadrado: "))
d = int(input("Ingrese un número para calcular su raíz cuadrada: "))

cuadrado = b**2
print("El cuadrado del número {} es {}".format(b, cuadrado))

raiz = math.sqrt(d)
print("La raíz del número {} es {}".format(d, raiz))
