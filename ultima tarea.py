oracion = input("Introduzca una cadena mayor de 5 caracteres y menor de 255: ")
oracion_invertida = ""
palabra = ""
while len(oracion) < 5 or len(oracion) > 255:
    print("CADENA INVALIDA")
    oracion = input("Introduzca una cadena mayor de 5 caracteres y menor de 255: ")
for caracter in oracion:
    if caracter == " ":
        oracion_invertida = " " + palabra + oracion_invertida
        palabra = ""
    else:
        palabra += caracter
oracion_invertida = palabra + oracion_invertida
print(oracion_invertida)