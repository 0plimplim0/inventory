from utils import tools
import time
import json

def show_items():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("===========================")
    print("=   I N V E N T A R I O   =")
    print("===========================\n")

    with open("./data/inventario.json", "r") as json_file:
        content = json.load(json_file)
    
    for item in content:
        print(f"Tipo: {item["tipo"]}\nValor: {item["valor"]}\nCantidad: {item["cantidad"]}\n")

    input("Presiona ENTER para volver.")


def add_item():
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n")
    print("=====================================")
    print("=  A G R E G A R   E L E M E N T O  =")
    print("=====================================\n")
    print("Ingrese los datos:\n")
    tipo = input("Tipo: ")
    valor = input("Valor: ")
    cantidad = int(input("Cantidad: "))
    element = {
        "tipo": tipo,
        "valor": valor,
        "cantidad": cantidad
    }
    with open("./data/inventario.json", "r") as json_file:
        content = json.load(json_file)
    content.append(element)
    with open("./data/inventario.json", "w") as json_file:
        json.dump(content, json_file, indent=4)
    print("\nElemento agregado exitosamente.")
    time.sleep(1)
    

running = True
while running:
    tools.clearConsole()
    print("Inventario electronica v1.0.0\n\n")
    print("Selecciona una opción:\n\n1. Ver inventario\n2. Agregar item.\n3. Salir.\n")
    seleccion = input("Seleccion: ")
    match seleccion:
        case "1":
            show_items()
            continue
        case "2":
            add_item()
            continue
        case "3":
            print("Saliendo...")
            running = False
        case _:
            print("Selecciona una opción válida.")
    time.sleep(1)