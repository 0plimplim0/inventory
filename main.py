from utils import tools
import core
import time

def showMenu():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("===========================")
    print("=   I N V E N T A R I O   =")
    print("===========================\n")

    inventario = core.getInventory()
    if (inventario == False):
        return
    
    for item in inventario:
        core.showItem(item)

    input("Presiona ENTER para volver.")

def addMenu():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("=====================================")
    print("=  A G R E G A R   E L E M E N T O  =")
    print("=====================================\n")

    inventario = core.getInventory()
    if (inventario == False):
        return
    id = core.generateId(inventario)

    print("Ingrese los datos:\n")
    tipo = input("Tipo: ")
    valor = input("Valor: ")
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Por favor introduce una cantidad válida.")
        time.sleep(1)
        return
    element = {
        "id": id,
        "tipo": tipo,
        "valor": valor,
        "cantidad": cantidad
    }
    
    inventario.append(element)
    core.saveItem(inventario)    

running = True
while running:
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n\n")
    print("Selecciona una opción:\n\n1. Ver inventario\n2. Agregar item.\n3. Salir.\n")
    seleccion = input("Seleccion: ")
    match seleccion:
        case "1":
            showMenu()
            continue
        case "2":
            addMenu()
            continue
        case "3":
            print("Saliendo...")
            running = False
        case _:
            print("Selecciona una opción válida.")
    time.sleep(1)