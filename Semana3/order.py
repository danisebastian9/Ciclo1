# Que lea tres números y los imprima en forma ascendente.

num1 = int(input("Ingrese numero a ordenar Nro 1: "))
num2 = int(input("Ingrese numero a ordenar Nro 2: "))
num3 = int(input("Ingrese numero a ordenar Nro 3: "))

if num1 <= num2 <= num3:
    menor = num1
    medio = num2
    mayor = num3 
elif num1 <= num3 <= num2:
    menor = num1
    medio = num3
    mayor = num2 
elif num2 <= num1 <= num3:
    menor = num2
    medio = num1
    mayor = num3 
elif num2 <= num3 <= num1:
    menor = num2
    medio = num3
    mayor = num1 
elif num3 <= num1 <= num2:
    menor = num3
    medio = num1
    mayor = num2 
elif num3 <= num2 <= num1:
    menor = num3
    medio = num2
    mayor = num1 
else: 
    print("Numeros no son validos ")

print("El orden ascendente es:", menor,'-', medio,'-', mayor)