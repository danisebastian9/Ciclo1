# Hacer la tabla de multiplicar desde N hasta M 
n = int(input('Digite limite inferior: '))
m = int(input('Digite limite superior: '))

while n > m: 
    print('El limite inferior debe ser menor que el superior, vuelva a ingresarlos')
    n = int(input('Digite limite inferior: '))
    m = int(input('Digite limite superior: '))

contador = 1

while n <= m: 
    mult = contador * n 
    print(n,'X', m, '=', mult)
    contador = contador + 1

