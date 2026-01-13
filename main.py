from utils import tools
import core
import time
import logging

def showMenu():
    tools.inventoryRoutine()

    connection = core.getConnection()
    
    print("Selecciona una opción:\n\n1. Ver todo.\n2. Buscar por tipo.\n3. Buscar por ID.\n")
    seleccion = input("Seleccion: ")
    match seleccion:
        case "1":
            tools.inventoryRoutine()
            core.showAllItems(connection)
        case "2":
            tipo = input("Tipo: ")
            tools.inventoryRoutine()
            core.showTypeItems(connection, tipo)
        case "3":
            try:
                id = int(input("ID: "))
                tools.inventoryRoutine()
                core.showIdItem(connection, id)
            except Exception as e:
                tools.logError(e)
        case _:
            print("Opción inválida.")
            time.sleep(1)
            return
    input("Presiona ENTER para volver.")
    core.closeConnection(connection)

def addMenu():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("=====================================")
    print("=  A G R E G A R   E L E M E N T O  =")
    print("=====================================\n")

    connection = core.getConnection()
    id = core.generateId(connection, "items")

    print("Ingrese los datos:\n")
    tipo = core.checkType(connection, input("Tipo: "))
    if not tipo:
        return
    valor = input("Valor: ")
    try:
        cantidad = int(input("Cantidad: "))
        core.saveItem(connection, id, tipo, valor, cantidad)
        core.closeConnection(connection)
    except Exception as e:
        tools.logError(e)

def deleteMenu():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("=======================================")
    print("=  E L I M I N A R   E L E M E N T O  =")
    print("=======================================\n")
    connection = core.getConnection()
    try:
        id = int(input("ID: "))
        core.deleteItem(connection, id)
    except Exception as e:
        logging.error(e)
    core.closeConnection(connection)

def editMenu():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("===================================")
    print("=  E D I T A R   E L E M E N T O  =")
    print("===================================\n")
    id = input("ID: ")
    inventario = core.getInventory()
    newInventario = core.updateItem(inventario, id)
    if (newInventario == False):
        return
    core.saveInventory(newInventario)

logging.basicConfig(filename='./logs/error.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
running = True
while running:
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n\n")
    print("Selecciona una opción:\n\n1. Ver inventario.\n2. Agregar item.\n3. Eliminar item.\n4. Editar item.\n5. Salir.\n")
    seleccion = input("Seleccion: ")
    match seleccion:
        case "1":
            showMenu()
            continue
        case "2":
            addMenu()
            continue
        case "3":
            deleteMenu()
            continue
        case "4":
            editMenu()
            continue
        case "5":
            print("Saliendo...")
            running = False
        case _:
            print("Selecciona una opción válida.")
    time.sleep(1)
tools.clearConsole()