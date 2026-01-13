import time
import json
import sqlite3
    
def getConnection():
    connection = sqlite3.connect('./data/inventario.db')
    return connection

def getTypeIds(connection):
    cursor = connection.cursor()
    lista = {}
    cursor.execute('select * from tipos')
    tipos = cursor.fetchall()
    for tipo in tipos:
        lista[tipo[0]] = tipo[1]
    return lista

def showAllItems(connection):
    cursor = connection.cursor()

    tipos = getTypeIds(connection)
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
    tipos = getTypeIds(connection)
    cursor.execute('select * from items where id = ?', (id,))
    item = cursor.fetchone()
    if not item:
        print('No existe ningún item con ese id.\n')
        return
    print(f'ID: {item[0]}\nTipo: {tipos[item[1]]}\nValor: {item[2]}\nCantidad: {item[3]}\n')
    

def closeConnection(connection):
    connection.close()    
  
def generateId(connection, table):
    cursor = connection.cursor()
    if (table == 'items'):
        cursor.execute('select id from items')
    elif (table == 'tipos'):
        cursor.execute('select id from tipos')
    items = cursor.fetchall()
    if not items:
        return 1
    length = len(items) - 1
    item = items[length]
    id = item[0] + 1
    return id

def saveItem(connection, id, tipoid, valor, cantidad):
    cursor = connection.cursor()
    cursor.execute('insert into items values(?, ?, ?, ?)', (id, tipoid, valor, cantidad))
    connection.commit()

def checkType(connection, type):
    cursor = connection.cursor()
    cursor.execute('select * from tipos')
    tipos = cursor.fetchall()
    for tipo in tipos:
        if (type == tipo[1]):
            return tipo[0]
    while True:
        select = input('Ese tipo aun no está registrado. Deseas registrarlo? (Y/n): ').upper()
        match select:
            case "Y":
                id = generateId(connection, 'tipos')
                cursor.execute('insert into tipos values(?, ?)', (id, type))
                connection.commit()
                return id
            case "N":
                return False
            case _:
                print("Opción inválida.")