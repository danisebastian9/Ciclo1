'''Leer una edad en el intervalo [18 a 24]. 
Si la persona está por fuera del intervalo siendo menor que 18, 
se debe pedir el número del registro civil y la partida de bautizo. 
Si la persona está por encima del rango mayor a 24 se debe pedir 
certificado de supervivencia. Si la persona está dentro del intervalo, 
solo se debe pedir la cedula.
'''

edad = int(input(" Ingrese su edad: "))

if edad >= 18 and edad <= 24:
    documento = 'Por favor ingrese número de cédula.'
elif edad < 18 and edad >= 0: 
    documento = 'Por favor ingrese número de regístro civil y partida de bautízo.'
elif edad > 24 and edad < 120:
    documento = 'Por favor ingrese certificado de supervivencia.'
else:
    documento = 'Rango de edad no válido'

print(documento)


    