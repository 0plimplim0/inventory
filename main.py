from utils import tools
import core
import time

def showMenu():
    tools.inventoryRoutine()

    inventario = core.getInventory()
    if (inventario == False):
        return
    
    print("Selecciona una opción:\n\n1. Ver todo.\n2. Buscar por tipo.\n3. Buscar por ID.\n")
    seleccion = input("Seleccion: ")
    match seleccion:
        case "1":
            for item in inventario:
                core.showItem(item)
        case "2":
            tipo = input("Tipo: ").strip()
            if not tipo:
                print("Por favor introduce un tipo válido.")
                time.sleep(1)
                return
            tools.inventoryRoutine()
            core.searchType(inventario, tipo)
        case "3":
            id = input("ID: ").strip()
            if not id:
                print("Por favor introduce un ID válido.")
                time.sleep(1)
                return
            tools.inventoryRoutine()
            core.searchId(inventario, id)
        case _:
            print("Opción inválida.")
            time.sleep(1)
            return
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
            pass
        case "4":
            pass
        case "5":
            print("Saliendo...")
            running = False
        case _:
            print("Selecciona una opción válida.")
    time.sleep(1)
tools.clearConsole()