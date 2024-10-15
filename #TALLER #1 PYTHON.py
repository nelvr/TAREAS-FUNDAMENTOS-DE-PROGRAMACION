#TALLER #1 PYTHON
#FUNDAMENTOS DE PROGRAMACIÓN
#NELSON VILLARROEL. C.I: 31423491
#ENRIQUE GODOY. C.I: 31873477

#COMIENZO PROGRAMA
#DECLARAMCIÓN DE VARIABLES
lado1 = float
lado2 = float
lado3 = float
m2_equilatero = 40
m2_isoceles = 30
m2_escaleno = 25
costo_total = float
triangulo = float
area = float
s = float
triangulovalido = float
areaprecio = float
#ENTRADA DE DATOS DEL USUARIO
lado1 = float(input("Ingrese el lado 1 del triangulo que desea: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))
#VERIFICACIÓN DEL TRIÁNGULO
if lado1 < lado2 + lado3 and lado2 < lado1 + lado1 and lado3 < lado1 + lado2:
    print("Su triángulo es válido")
else:
    print("TRIÁNGULO INVÁLIDO")
    exit()
#VERIFICACIÓN DEL TIPO DE TRIÁNGULO
if lado1 == lado2 == lado3:
    print("Su triángulo es equilátero!!")
    triangulo = m2_equilatero
elif lado1 == lado2 != lado3 or lado2 == lado1 != lado3 or lado3 == lado1 != lado2:
    triangulo = m2_isoceles
    print("Su triángulo es isóceles!!")
elif lado1 != lado2 != lado3:
    triangulo = m2_escaleno
    print("Su triángulo es escaleno!!")
else:
    print("INVALIDO")
#DETERMINACIÓN DE PERÍMETRO Y ÁREA
s = (lado1 + lado2 + lado3) / 2
print("El semiperímetro de su triángulo es:",s)
import math
area = math.sqrt((s * (s - lado1) * (s - lado2) * (s - lado3)))
print("El area de su triangulo en m2 es:",area)
areaprecio = (math.sqrt((s * (s - lado1) * (s - lado2) * (s - lado3)))) * triangulo
#SALIDA
print("El precio de su triángulo es:",areaprecio,"$")
print("Lado 1 (m):", lado1)
print("Lado 2 (m):",lado2)
print("Lado 3 (m):",lado3)
#FIN PROGRAMA