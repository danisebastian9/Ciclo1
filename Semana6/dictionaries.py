# Diccionarios: 

alimentos = {}
alimentos['Frutas']=['Fresa','Naranja','Piña']
alimentos['Vegetales']=['Lechuga','Espinaca']
alimentos['Lacteos']=['Yogurt','Queso']

print(alimentos)
print(alimentos['Frutas'])
print(alimentos['Frutas'][1])
alimentos['Frutas'][2] = 'Manzana'


for i in alimentos:
    print(i)

for i in alimentos['Frutas']:
    print(i)

for key, valores in alimentos.items():
    print(key, valores)
    for i in valores:
        print(i)


