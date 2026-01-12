import time
import json
import sqlite3
    
def getConnection():
    connection = sqlite3.connect('./data/inventario.db')
    return connection

def getTypes(connection):
    cursor = connection.cursor()
    lista = {}
    cursor.execute('select * from tipos')
    tipos = cursor.fetchall()
    for tipo in tipos:
        lista[tipo[0]] = tipo[1]
    return lista

def showAllItems(connection):
    cursor = connection.cursor()

    tipos = getTypes(connection)
    cursor.execute('select * from items')
    items = cursor.fetchall()
    
    for item in items:
        print(f'ID: {item[0]}\nTipo: {tipos[item[1]]}\nValor: {item[2]}\nCantidad: {item[3]}\n')

def showTypeItems(connection, type):
    cursor = connection.cursor()
    cursor.execute('select id from tipos where nombre = ?', (type,))
    id = cursor.fetchone()
    if not id:
        print('No existe ningún item con ese tipo.\n')
        return
    cursor.execute('select * from items where tipoid = ?', (id[0],))
    items = cursor.fetchall()
    for item in items:
        print(f'ID: {item[0]}\nTipo: {type}\nValor: {item[2]}\nCantidad: {item[3]}\n')

def showIdItem(connection, id):
    cursor = connection.cursor()
    tipos = getTypes(connection)
    cursor.execute('select * from items where id = ?', (id,))
    item = cursor.fetchone()
    if not item:
        print('No existe ningún item con ese id.\n')
        return
    print(f'ID: {item[0]}\nTipo: {tipos[item[1]]}\nValor: {item[2]}\nCantidad: {item[3]}\n')
    

def closeConnection(connection):
    connection.close()
    
def saveInventory(inventario):
    try:
        with open("./data/inventario.json", "w") as json_file:
            json.dump(inventario, json_file, indent=4)
            print("Inventario actualizado correctamente.")
            time.sleep(1)
    except:
        print("Ha ocurrido un error al guardar.")
        time.sleep(1)
        return

# Mas adelante cambiar a formateo con f-strings
# Aviso: El tope de items es de 999.   
def generateId(inventario):
    index = len(inventario) - 1
    lastItem = inventario[index]
    num = int(lastItem["id"]) + 1
    length = len(str(num))
    match length:
        case 1:
            id = "00" + str(num)
            return id
        case 2:
            id = "0" + str(num)
            return id
        case 3:
            return str(num)

def showItem(item):
    id = item["id"]
    tipo = item["tipo"]
    valor = item["valor"]
    cantidad = item["cantidad"]

    print(f"ID: {id}\nTipo: {tipo}\nValor: {valor}\nCantidad: {cantidad}\n")

def deleteItem(inventario, id):
    for item in inventario:
        if (item["id"] == id):
            inventario.remove(item)
            return inventario
    print("No existe ningún item con ese ID asignado.")
    time.sleep(1)
    return False

def updateItem(inventario, id):
    for item in inventario:
        if (item["id"] == id):
            try:
                newCantidad = int(input("Nueva cantidad: "))
                item["cantidad"] = newCantidad
                return inventario
            except ValueError:
                print("Cantidad inválida.")
                time.sleep(1)
                return False
    print("No existe ningún item con ese ID asignado.")
    time.sleep(1)
    return False