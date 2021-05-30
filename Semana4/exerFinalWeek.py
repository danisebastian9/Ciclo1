'''
El programa de Ingeniería ambiental de la Universidad 
El Bosque en una de sus salidas de campo, ha registrado 
un par de temperaturas diarias (máxima, mínima) para todos 
los días que permanecieron en campo. 
Dadas las condiciones del terreno donde se encontraban, no era
posible tener temperaturas menores de 5 grados ni mayores 
de 35 grados, que se consideraron errores, pero igual se 
registraron para su estudio posterior. 
La pareja de temperaturas (0,0) indicará que se han terminado 
los datos de la salida de campo. El director del programa le 
ha solicitado a usted como programador, que le desarrolle un
programa en lenguaje Python que le permita:
• Leer desde el teclado todos los datos registrados en 
    la salida de campo.
• Mostrar en consola el número total de días que duró la 
    salida de campo.
• Mostrar en consola cuantos días en total se tuvieron 
    temperaturas con error, de los cuales se debe informar 
    cuántos fueron por temperaturas menores de 5 grados, 
    cuántos fueron por temperaturas mayores de 35 grados y 
    cuántos por ambos errores.
• Mostrar en consola la temperatura media mínima y máxima, 
    sin tener en cuenta los días en que se reportaron errores.
• Mostrar en consola el porcentaje de días que se reportaron 
    errores respecto del total de días reportados.
'''

Temperatura_Max = int(input('Ingrese temperatura maxima hoy: '))
Temperatura_Min = int(input('Ingrese temperatura minima hoy: '))

Contador_Dias = 0
Dias_Error = 0
Contador_Min = 0
Contador_Max = 0  

while Temperatura_Min != 0 or Temperatura_Max != 0:
    Contador_Dias += 1
    print('Dias',Contador_Dias)
    if Temperatura_Min < 5 or Temperatura_Max > 35: 
        Dias_Error += 1 
        print('Error cualquier dia',Dias_Error)
        if Temperatura_Min < 5:
            Contador_Min += 1
            print('error minimo', Contador_Min)
        elif Temperatura_Max > 35:
            Contador_Max += 1
            print('error maximo', Contador_Max)
    Temperatura_Max = int(input('Ingrese temperatura maxima hoy: '))
    Temperatura_Min = int(input('Ingrese temperatura minima hoy: '))


    
