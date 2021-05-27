#Hacer que cambie las vocales 

frase = input('Digite una frase: ').lower()
vocal = input('ingrese la vocal a cambiar del texto').lower()
a = 0
e = 0
i = 0
o = 0
u = 0




for x in frase: 
    if x == 'a' or x == 'á':
        a += 1
    elif x == 'e' or x == 'é':
        e += 1
    elif x == 'i' or x == 'í':
        i += 1
    elif x == 'o' or x == 'ó':
        o += 1
    elif x == 'u' or x == 'ú':
        u += 1

total = a+e+i+o+u

print('Vocal A: ', a)
print('Vocal E: ', e)
print('Vocal I: ', i)
print('Vocal O: ', o)
print('Vocal U: ', u)
print('Total Vocales = ', total)
