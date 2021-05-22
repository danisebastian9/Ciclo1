n = int(input('Digite limite inferior: '))
m = int(input('Digite limite superior: '))

while n > m: 
    print('El limite inferior debe ser menor que el superior, vuelva a ingresarlos')
    n = int(input('Digite limite inferior: '))
    m = int(input('Digite limite superior: '))

while n <= m:
    if n % 2 == 0:
        print(n)
    n = n + 1
