import time
import json

def getInventory():
    try:
        with open("./data/inventario.json", "r") as json_file:
            content = json.load(json_file)
        return content
    except FileNotFoundError:
        print("No se ha encontrado el archivo inventario.json.")
        time.sleep(1)
        return False
    
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

def searchType(inventario, type):
    lista = []
    for item in inventario:
        if (item["tipo"] == type):
            lista.append(item)
    if (len(lista) == 0):
        print("No hay ningún item con ese tipo asignado.\n")
        return
    else:
        for item in lista:
            showItem(item)
def searchId(inventario, id):
    lista = []
    for item in inventario:
        if (item["id"] == id):
            lista.append(item)
    if (len(lista) == 0):
        print("No hay ningún item con ese ID asignado.\n")
        return
    else:
        for item in lista:
            showItem(item)

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