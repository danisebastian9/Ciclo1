'''
En una empresa de 1000 trabajadores, se hará un aumento al salario
de acuerdo al tiempo de servicio, para este aumento se tomará en
cuenta lo siguiente:
Tiempo de servicio: de 1 a 5 años Aumento: 10%
Tiempo de servicio: de 5 a 10 años Aumento: 15%
Tiempo de servicio: de 10 a 20 años Aumento: 20%
Tiempo de servicio: de 20 años a más Aumento: 35%
'''

tiempoServicio = int(input('Ingrese la cantidad de años que lleva laborando en la empresa: '))
salario = int(input('Ingrese su salario actual: '))

if tiempoServicio >= 1 and tiempoServicio <= 5:
    porcAumento = '10%'
    aumento = salario * 10 / 100
    salarioFinal = salario + aumento

elif tiempoServicio >= 6 and tiempoServicio <= 10:
    porcAumento = '15%'
    aumento = salario * 15 / 100
    salarioFinal = salario + aumento

elif tiempoServicio >= 11 and tiempoServicio <= 20:
    porcAumento = '20%'
    aumento = salario * 20 / 100
    salarioFinal = salario + aumento

elif tiempoServicio > 20:
    porcAumento = '35%'
    aumento = salario * 35 / 100
    salarioFinal = salario + aumento

else: 
    porcAumento = 'invalido'
    aumento = 'NA'
    salarioFinal = 0


print('Su aumento anual es', porcAumento, aumento, ' y su nuevo salario va a ser:', salarioFinal)