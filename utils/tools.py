import json
import os

# Los argumentos tienen que ser la ruta al archivo desde donde se ejecuta la funcion, no solo el nombre :p
def txtToJson(txtFileName, jsonFileName):
    with open(txtFileName, "r") as txt_file:
        content = txt_file.read()

    lista = []

    items = content.split("\n")
    for item in items:
        item_content = item.split(" | ")
        dic = {
            "id": item_content[0],
            "tipo": item_content[1],
            "valor": item_content[2],
            "cantidad": item_content[3]
        }
        lista.append(dic)
    
    with open(jsonFileName, "w") as json_file:
        json.dump(lista, json_file, indent=4)

    print("Operacion completada con exito.")

def clearConsole():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")