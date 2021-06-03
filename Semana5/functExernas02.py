def suma(num1 = 0, num2 = 0):
    if num1 == 0 and num2 == 0:
        print('No envio parametros, no se realizo la suma')
    else:
        total = num1 + num2
        print(f'la suma de {num1} y {num2} es igual a {total}')

num1 = int(input('Ingrese numero 1 a sumar: '))
num2 = int(input('Ingrese numero 2 a sumar: '))

suma(num1, num2)
suma(9,num2)
suma()
