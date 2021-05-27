
for i in [8,5,7,2,1,3,4]: 
    print(i)

for i in ['Juan','Carlos', 'Jose', 'Luisa', 'Maria']: 
    print(i, 'tiene', len(i), 'caracteres')

for i in ['Juan','Carlos', 'Jose', 'Luisa', 'Maria']:
    contador = 0
    for j in i:
        contador += 1
    print(i, 'tiene', contador, 'caracteres')
    