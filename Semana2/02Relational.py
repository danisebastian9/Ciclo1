# Operaciones Relacionales

a = True
b = False

x = 5
y = 3
print( x > y )  # True 
print( x >= y ) # True
print( x <= y ) # False
print( x != y ) # True
print( x == y ) # False

c = "A"
d = "B" 
print(ord("A")) # Encontrar el codigo decimal ascii de un caracter
print( c < d) 

#Operadores logicos

dia = "Lunes"
mes = "Mayo"
año = 2021
# 1 not
# 2 and
# 3 or
print(dia != "Martes" or mes == "Junio" and año < 2020) # True
print(not(dia != "Martes" or mes == "Junio" and año < 2020)) # False, not niega la respuesta

# Manejo de cadenas de caracteres. 

cadena1 = "Hola"
cadena2 = " "
cadena3 = "Mundo"

frase = cadena1 + cadena2 + cadena3
print(frase)

repetir = frase * 5
print(repetir)

print(len(frase))

print(cadena1[0])

print(cadena1[1:3])

print(cadena1[2:])

buscar = frase.find("M")
print(buscar)

buscar1 = frase.find("es")
print(buscar1) # -1 no encontro resultado. 

nombre = "MARIA"
print(nombre.lower())

apellido = "Sanchez"
print(apellido.upper())

reemplazar = cadena3.replace("d","HOLA")
print(reemplazar)

reemplazar1 = frase.replace("o", "Hi")
print(reemplazar1)



