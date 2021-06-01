# funciones externas: Creadas.

def saludo():
    print('Hola Muchachos.......')

def saludoNombre(nombre):
    print(f'Hola.... {nombre}')

saludo()
saludo()
nom = 'Juan'
saludoNombre(nom)
saludoNombre('Maria')
saludoNombre(5)

def nombreCompleto(nombre, apellido):
    print(f'Hola, bienvenido {nombre} {apellido}')

nombreCompleto('Sebastian','Cubides')

nombre = input('Digite su nombre: ')
apellido = input('Digite su apellido: ')
nombreCompleto(nombre, apellido)

# Ejercicio funcion suma: 

def suma(num1, num2):
    total = num1 + num2
    print(f'la suma de {num1} y {num2} es igual a {total}')

num1 = int(input('Ingrese numero 1 a sumar: '))
num2 = int(input('Ingrese numero 2 a sumar: '))
suma(num1, num2)

