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
if a > b:
    a, b = b, a

# BUCLE PARA LA RECOLECCION DE NUMEROS
for num in range(a, b + 1):
    if num % 2 == 0:
        pares.append(num)

# ORDEN SEGUN LA ELECCION DEL USUARIO
if d == 1:
    pares.sort()
elif d == 2:
    pares.sort(reverse=True)

# SALIDA
print("Números pares ordenados:", pares)
