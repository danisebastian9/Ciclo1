# Menu con while

def createFile():
    file = open('Archivos/agenda.txt','w')
    file.close()

def viewData():
    file = open('Archivos/agenda.txt','r')
    data = file.readlines()
    file.close()
    count = 0 
    for i in data:
        data[count] = i.replace('\n','')
        count += 1
    return data

def filterData(list):
    filter = input('Digite la letra por la que empiezan los beneficiaros: ').upper()
    print('Listado filtrado de beneficiarios: \n')
    for i in list:
        if i[0] == filter:
            position = list.index(i)
            print(list[position])
            print(list[position + 1])
            print(list[position + 2])

def addData(list):
    file = open('Archivos/agenda.txt','a')
    user = input('Ingrese Nombre y Apellido del beneficiario -> ').title()
    userId = input('Ingrese Numero de cedula del beneficiario -> ')
    if userId in list:
        print('Usuario ya existe')
        return
    userPhone = input('Ingrese Numero telefonico -> ')
    file.write(user + '\n')
    file.write(userId + '\n')
    file.write(userPhone + '\n')
    file.close()

def searchData(list):
    user = input('Ingrese Nombre y Apellido a buscar -> ').title()
    if user in list:
        position = list.index(user)
        print(list[position])
        print(list[position + 1])
        print(list[position + 2])

def deleteData(list):
    userID = input('Ingrese Numero de Cedula de beneficiario a eliminar -> ')
    if userID in list:
        position = list.index(userID)
        list.pop(position)
        list.pop(position)
        list.pop(position - 1)
        file = open('Archivos/agenda.txt','w')
        for i in list:
            file.write(i + '\n')
        file.close()

# MAIN PROGRAM 

createFile()

menu = int(input('''
Menu Principal
1. Ver listado
2. Ver listado filtrado
3. Agregar beneficiario
4. Buscar beneficiario
5. Borrar beneficiario
6. Salir
'''))

while menu != 6:
    if menu == 1:
        print(viewData())
        
    elif menu == 2:
        filterData(viewData())
       
    elif menu == 3:
        addData(viewData())
    
    elif menu == 4:
        searchData(viewData())
    
    elif menu == 5:
        deleteData(viewData())
    
    else:
        print('Opcion invalida')
    menu = int(input('''
Menu Principal
1. Ver listado
2. Ver listado filtrado
3. Agregar beneficiario
4. Buscar beneficiario
5. Borrar beneficiario
6. Salir
'''))
print('Hasta pronto')

    
