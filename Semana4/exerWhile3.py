#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

num = int(input('Digite un numero: '))
suma = 0

while num != 0: 
    if num > 0:
        suma += num
    num = int(input('Digite un numero: '))
    
print('La suma de los numeros positivos es: ', suma)
