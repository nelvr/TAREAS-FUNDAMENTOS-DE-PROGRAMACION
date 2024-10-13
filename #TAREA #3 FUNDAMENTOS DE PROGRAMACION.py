#TAREA #3 FUNDAMENTOS DE PROGRAMACION. NELSON VILLARROEL. PROF. RICARDO SALVATORELLI
# DECLARACION DE VARIABLES
tarifa = float
plan = int
plan_basico = 50
plan_intermedio = 80
plan_premium = 120
impuesto_igtf = 0.3
impuesto_iva = 0.16
frecuencia_de_pago = int
descuento = float
informacion_de_precios = """
Por favor, indique el plan al que desea suscribirse
1- plan basico (50$ precio base sin incluir el '16%' de iva)
2- plan intermedio (80$precio base sin incluir el '16%' de iva)
3- plan premium (120$ precio base sin incluir el '16%' de iva)
"""
metodos_de_pago = """
Por favor, marcar el numero correspondiente del 1 al 3 para seleccionar su metodo de pago
1- efectivo (Aplica el 3'%' de impuesto del IGTF)
2- pago movil
3- tarjeta de debito o credito
"""
frecuenciadepago = """
Por favor, marcar el numero correspondiente del 1 al 3 para seleccionar su frecuencia de pago
1- Anual
2- Semestral
3- Mensual
"""
#ENTRADA DE DATOS DEL USUARIO POR FRECUENCIA DE PAGO
print("Bienvenido al sistema de suscripciones del gimnasio!!")
medio_de_pago = int(input(metodos_de_pago))
match medio_de_pago:
    case 1:
        print("usted ha seleccionado pago movil como su metodo de pago")
        medio_de_pago = impuesto_igtf
    case 2:
        medio_de_pago = 0
        print("usted ha seleccionado efectivo como su medio de pago")
    case 3:
        print("usted ha seleccionado tarjeta como medio de pago")
        medio_de_pago = 0
#CIERRE CONDICIONAL DEL VALOR DEL METODO DE PAGO
#COMIENZO DE LA DETERMINACION DE LA FRECUENCIA DE PAGO
frecuencia_de_pago = int(input(frecuenciadepago))
match frecuencia_de_pago:
    case 1:
        frecuencia_de_pago = 0.15
        print("Usted ha seleccionado la modalidad anual por lo tanto tiene un descuento del 10%")
    case 2:
        frecuencia_de_pago = 0.10
        print("Usted ha seleccionado la modalidad semestral, por lo tanto tiene un descuento del 15%")
    case 3:
        print("Usted ha seleccionado la modalidad mensual")
        frecuencia_de_pago = 0
# FIN CONDICIONAL FRECUENCIA DE PAGO, COMIENZO ENTRADA DE DATOS
plan = int(input(informacion_de_precios))
if plan == 1:
    print("Usted ha seleccionado el plan basico!")
    tarifa = plan_basico + (plan_basico * medio_de_pago) + (plan_basico * impuesto_iva) - (frecuencia_de_pago * plan_basico)
    print("Usted tiene acceso a la zona de cardio!")
elif plan == 2:
    tarifa = plan_basico + (plan_basico * medio_de_pago) + (plan_basico * impuesto_iva) - (frecuencia_de_pago * plan_basico)
    print("Usted tiene acceso a las clases grupales!")
elif plan == 3:
    tarifa = plan_basico + (plan_basico * medio_de_pago) + (plan_basico * impuesto_iva) - (frecuencia_de_pago * plan_basico)
    print("Usted tiene acceso habilitado tanto al cardio como a las clases grupales!")
else:
    print("ENTRADA INVALIDA")
descuento_promocion = input("Si sabe cual es el codigo promocional, insertelo ahora. En caso de no ternerlo, puede insertar cualquier valor o palabra: ")
if descuento_promocion == "DESC25":
    descuento = (tarifa * 0.25)
else:
    descuento = 0
    print("Usted introdujo un codigo invalido, o en su defecto no  lo tiene")
#CIERRE DE ENTRADA DE DATOS
#OUTPUT
tarifa = tarifa - descuento
print("Su total a pagar con los impuestos correspondientes es $",tarifa)
#CIERRE ALGORITMO