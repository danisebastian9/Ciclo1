'''
Generar password con longitud variable: 
generarPassword(): genera la contraseña del objeto con la longitud que tenga. 
esFuerte(): 
 devuelve un booleano si es fuerte o no,
 para que sea fuerte debe tener más de 2 mayúsculas,
 más de 1 minúscula y 
 más de 5 números.
'''

import random

def generarPassword(longitud):
    password = ''
    for i in range(longitud): 
        cadena= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz0123456789'
        letra = random.choice(cadena)
        password += letra
    return password

def esFuerte(password):
    contMay = 0
    contMin = 0
    contNum = 0
    for i in password:
        if i.isupper():
            contMay += 1
        elif i.islower():
            contMin += 1
        elif i.isdigit():
            contNum += 1
    if contMay > 2 and contMin > 1 and contNum > 5:
        return True
    else:
        return False

#Main Program
longitud = int(input('Digite longitud de la contraseña: '))
cantidad = int(input('Digite la cantidad de contraseñas: '))

while longitud < 11:
    print('La longitud debe ser mayor que 10')
    longitud = int(input('Digite longitud de la contraseña: '))

cantidad = int(input('Digite la cantidad de contraseñas: '))

for i in range(cantidad):
    contra = generarPassword(longitud)
    if esFuerte(contra):
        print(contra, 'Es Fuerte')
    else: 
        print(contra, 'No es fuerte')




