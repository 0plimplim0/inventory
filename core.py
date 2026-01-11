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
    
def saveItem(item):
    try:
        with open("./data/inventario.json", "w") as json_file:
            json.dump(item, json_file, indent=4)
            print("Elemento agregado correctamente.")
            time.sleep(1)
    except:
        print("Ha ocurrido un error al agregar el item.")
        time.sleep(1)
        return

# Mas adelante cambiar a formateo con f-strings
# Aviso: El tope de items es de 999.   
def generateId(inventario):
    num = len(inventario) + 1
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