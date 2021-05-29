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

minTemperatura = float(input('Add minimum temperature: '))
maxTemperatura = float(input('Add Maximum temperature: '))

totalMinTemp = 0
totalMaxTemp = 0
errorMin = 0
errorMax = 0

while minTemperatura != 0 and maxTemperatura != 0:
    if minTemperatura < 5:
        errorMin += 1
    elif maxTemperatura > 35:
        errorMax += 1
    elif minTemperatura >= 5 and minTemperatura <= 35: 
        totalMinTemp = totalMinTemp + minTemperatura
    elif maxTemperatura >= 5 and maxTemperatura <= 35:
        totalMaxTemp = totalMaxTemp + minTemperatura

    
