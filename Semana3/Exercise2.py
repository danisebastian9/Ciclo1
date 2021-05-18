'''
Hacer un algoritmo donde se ingrese dos números y realice una 
operación matemática de acuerdo al siguiente menú (Debe mostrarse el menú): 
MENU PRINCIPAL a. SUMA b. RESTA c. MULTIPLICACION d. DIVISION
'''

numero1 = int(input('Ingrese numero 1 para la operación: '))
numero2 = int(input('Ingrese numero 2 para la operación: '))

operacion = str(input('''
Seleccione la operacion a realizar, responda A, B, C o D respectivamente:
A - SUMA
B - RESTA
C - MULTIPLICACION
D - DIVISION
 '''))

if operacion.upper() == "A":
    resultado = numero1 + numero2
    operSelect = "SUMA"
elif operacion.upper() == "B":
    resultado = numero1 - numero2
    operSelect = "RESTA"
elif operacion.upper() == "C":
    resultado = numero1 * numero2
    operSelect = "MULTIPLICACION"
elif operacion.upper() == "D": 
    resultado = numero1 / numero2
    operSelect = "DIVISION"
else:
    print("Respuesta no valida, responda solo A, B, C, D")

print('El resultado de la operacion', operSelect, 'entre ', numero1, 'y ', numero2, ' es', resultado)