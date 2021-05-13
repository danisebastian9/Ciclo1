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

