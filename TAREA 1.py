#ALGORITMO CALCULADOR NELSON VILLARROEL 
#FUNDAMENTOS DE PROGRAMACION UCAB PRIMER SEMESTRE
# PROF. RICARDO SALVATORELLI#
a = int(input('inserte su primera cifra: '))
operacion = input('introduzca el signo de la operacion a realizar: ')
b = int(input('inserte su segunda cifra: '))
if operacion == '+':
    print ('su resultado es:',a + b)
elif operacion == '-':
    print ('su resultado es:', a - b)
elif operacion == '*':
    print('su resultado es:', a * b)
elif operacion == '/':
    print('su resultado es:', a / b)
elif operacion == '**':
    print('su resultado es:', a ** b)
elif operacion == '%':
    print('su resultado es:', a % b)
else: print('invalido')

