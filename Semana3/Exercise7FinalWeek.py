edad = int(input('Edad: '))
puntaje = int(input('Puntaje: '))
ingreso = float(input('Ingreso: '))

if edad >= 15 and edad <= 18: 
    descuentoEdad = 25
elif edad >= 19 and edad <= 21:
    descuentoEdad = 15
elif edad >= 22 and edad <= 25:
    descuentoEdad = 10
else: 
    descuentoEdad = 0

if ingreso <= 1: 
    descuentoIngreso = 30
elif ingreso > 1 and ingreso <= 2:
    descuentoIngreso = 20
elif ingreso > 2 and ingreso <= 3:
    descuentoIngreso = 10
elif ingreso > 3 and ingreso <= 4:
    descuentoIngreso = 5
else:
    descuentoIngreso = 0


if puntaje >= 80 and puntaje < 86:
    descuentoPuntaje = 30
elif puntaje >= 86 and puntaje < 91:
    descuentoPuntaje = 35
elif puntaje >= 91 and puntaje < 96:
    descuentoPuntaje = 40
elif puntaje >= 96:
    descuentoPuntaje = 45
else:
    descuentoPuntaje = 0


descuentoTotal = descuentoEdad + descuentoIngreso + descuentoPuntaje 

print(descuentoEdad)
print(descuentoPuntaje)
print(descuentoIngreso)
print(descuentoTotal)


