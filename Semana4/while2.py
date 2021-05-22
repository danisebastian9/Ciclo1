edad = int(input("Digite su edad: "))

while edad < 0 or edad > 120:
    print('La edad no puede ser menor a 0 ni mayor a 120')
    edad=int(input('Digite su edad: '))

print('Su edad es: ', edad)