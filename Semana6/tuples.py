# TUPLES -> INMUTABLES

myTuple = ('Juan',32,'3124856751','Bogota')
print(myTuple[1])

# myTuple[1] = 50 # Can't be performed

a = 'Maria'
b = 'Medellin'
c = '35'
d = '3158467494'

newTuple = a, b, c, d # Empaquetado
print(newTuple)

w, x, y, z = myTuple # Desempaquetado

print(w)
print(x)
print(y)
print(z)

for i in newTuple:
    print(i)
    
