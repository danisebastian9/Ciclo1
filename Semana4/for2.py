frase = input('Digite una frase: ').lower()
letra = input('Digite la letra a buscar: ').lower()

cont = 0
for i in frase: 
    if i == letra:
        cont += 1

print('Cantidad encontrada', cont)


