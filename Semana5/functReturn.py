def operacion(num1 = 0, num2 = 0):
    if num1 == 0 and num2 == 0:
        total = num1 + num2
        resta = 0
    else:
        total = num1 + num2
        resta = num1 - num2
    return total, resta

num1 = int(input('Ingrese numero 1 a sumar: '))
num2 = int(input('Ingrese numero 2 a sumar: '))

print('la suma es ', operacion(9,5))
sumar3 = operacion(num1, num2)
print(f'la suma es{sumar3}')

sumar, resta = operacion(10,7)
print(f'la suma es: {sumar}')
print(f'la resta es: {resta}')