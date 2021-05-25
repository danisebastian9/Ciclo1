# Buscar una letra que este dentro frase, que me indique cuantas veces lo encontro. 

frase = input('Digite una frase: ')
letra = input('Digite la letra a buscar: ')
longitud = len(frase)

# print(frase.count(letra))

i = 0
cont = 0 
while i < longitud :
    if frase [i] == letra:
        cont = cont + 1 # cont += 1
        i += 1

print('Cantidad encontrada es: ', cont)
