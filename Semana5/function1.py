# str()
# int()
# float()
# str.lower()
# str.upper()
# print()
# len('cadena')
# range(20)
# input()
# ord()

#string.join(lista)
z = '____'
lista = ['a','b','c','d']
print(z.join(lista))

# string.split('_') fragmentar un text de acuerdo a un patron
texto = 'La_vida_es_bella'
miLista = list(texto.split('_'))
print(miLista)

nums = '8 9 4 1 2 4 7 5 7 5 7 1 4 4'
miLista2 = list(nums.split())
print(miLista2)

print('______________________________________________')
#range

li = list(range(20))
li1 = list(range(10,20))
li2 = list(range(10,20,3))
print(li)
print(li1)
print(li2)

print('______________________________________________')

# max devuelve el maximo de un conjunto de datos. 

listaNum = [5,4,9,8,4,5,67,4,5,6,55,5,5,4,8,68,84]
print(max(listaNum))

# min devuelve el minimo de un conjunto de datos. 

print(min(listaNum))

#suma de todos los elementos: 

print(sum(listaNum))


print('______________________________________________')
# promedio de datos de un conjunto de datos
import statistics

promedio = statistics.mean(listaNum)
print(promedio)
# El que mas se repite mode: 
print(statistics.mode(listaNum))

print('______________________________________________')
# Matematica: 
import math
print(math.pi) # pi
print(math.sin(45)) # seno
print(math.pow(2,2)) # potencia
print(math.factorial(4)) # factorial
print(math.sqrt(25)) # raiz cuadrada
print(math.trunc(45.99999999)) # truncar decimales, se los quita
print(round(45.99999999)) # redondea

print('______________________________________________')
# aleatorios
import random
print(random.randint(10,20)) # numero aleatorio entre el rango dado
print(random.random()) # numeros aleatorios entre 0 y 1
print(random.randbytes(5)) # los bytes

print('______________________________________________')
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





