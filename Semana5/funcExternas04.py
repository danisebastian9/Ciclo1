
''' 
Definir una función inversa() que realice la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse" 
Definir una función que diga si una cadena es palindrome "Sometamos o matemos" "oso" "radar" ""
'''

# def inversa(palabra):
#     reversa = ''
#     for i in palabra: 
#         reversa = i + reversa
#     return reversa

def reves(cadena):
    longitud = len(cadena)-1
    inversa = ''
    for i in range(longitud, -1, -1):
        inversa += cadena[i]
    return inversa

def esPalindrome(nuevaPal, palabra):
    if nuevaPal == palabra:
        print('Palabra es palindrome')
    else: 
        print('palabra no es palindrome')

palabra = input('Ingrese la palabra a analizar: ')

nuevaPal = reves(palabra)
print(nuevaPal)
esPalindrome(nuevaPal, palabra)

