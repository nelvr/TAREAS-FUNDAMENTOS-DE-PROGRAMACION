#TAREA #3 FUNDAMENTOS DE PROGRAMACION. NELSON VILLARROEL. PROF. RICARDO SALVATORELLI
# DECLARACION DE VARIABLES
tarifa = 0.00
plan = 0.00
plan_basico = 50
plan_intermedio = 80
plan_premium = 120
cardio = bool
clases_grupales = bool
impuesto_igtf = plan * 0,3
impuesto_iva = plan * 0,16
descuento_promocion = str
descuento_promocion = plan * 0,25
medio_de_pago = str
#ENTRADA DE DATOS
print("Bienvenido al sistema de suscripciones del gimnasio!!")
medio_de_pago = input("Por favor, seleccione su metodo de pago, sea efectivo, pago movil, tarjeta de credito o debito")
    match medio_de_pago == "pago movil"
plan = int(input("Por favor, seleccione un plan, marque 1 si desea el plan basico, 2 si desea el plan intermedio y 3 si desea el plan premium "))
if plan == 1:
    plan = plan_basico
    print("usted ha seleccionado el plan basico!")
    cardio = True
    descuento_promocion = ("Si lo tiene, ingrese el codigo promocional")
    if descuento_promocion == "DESC25":
        tarifa = plan - descuento_promocion
    else: print("Su precio SIN IMPUESTOS es:",tarifa)
elif plan == 2:
    plan = plan_intermedio
    print("usted ha seleccionado el plan intermedio!")
    clases_grupales = True
    descuento_promocion = ("Si lo tiene, ingrese el codigo promocional")
    if descuento_promocion == "DESC25":
        tarifa = plan - (plan * 0.25)
        print("")
    else: print("Su precio SIN IMPUESTOS es:",tarifa)
elif plan == 3:
    plan = plan_premium
    print("Usted ha seleccionado el plan premium!")
    cardio = True
    clases_grupales = True
    descuento_promocion = input(("Si lo tiene, ingrese el codigo promocional: "))
    if descuento_promocion == "DESC25":
        tarifa = plan_premium - (plan * 0.25)
        print("su precio SIN IMPUESTOS es:",tarifa)
    else: print("Su precio es:",plan)
    if cardio == True: print("Usted tiene el acceso a la sala de cardio habilitado")
    if clases_grupales == True: print("Usted tiene el acceso a las clases grupales habilitado")
else: print("Entrada invalida")