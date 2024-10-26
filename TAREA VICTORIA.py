# DECLARACION DE VARIABLES
a = 0
b = 0
c = 0
d = 0
#ENTRADA DE DATOS
a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))
d = int(input("Presione 1 si quiere ordenar la lista de numeros pares en orden ascendente, y 2 si lo desea en orden descendente: "))
# PROCESAMIENTO DE DATOS
if d == 1:
    while a != b:
        c = a % 2
    if c == 0:
        print(a, "es par")
    a = a + 1
    if a == b:
        if b % 2 == 0:
            print(b, "es par")
elif d == 2:
    while b != a:
        c = b % 2
    if c == 0:
        print(b, "es par")
    b = b - 1
    if b == a:
        if a % 2 == 0:
            print(a, "es par")

