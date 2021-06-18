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
    filter = input('Ingrese letra a filtrar -> ').upper()
    for i in list:
        if i[0] == filter:
            position = list.index(i)
            print(list[position])
            print(list[position + 1])
            print(list[position + 2])

def addData():
    file = open('Archivos/agenda.txt','a')
    user = input('Ingrese Nombre y Apellido del beneficiario -> ').title()
    userId = input('Ingrese Numero de cedula del beneficiario -> ')
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
        list.pop(position - 1)
        list.pop(position)
        list.pop(position)
        file = open('Archivos/agenda.txt','a')
        for i in list:
            file.write(i + '\n')
        file.close()


    





list = viewData()
