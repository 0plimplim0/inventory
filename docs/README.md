# INVENTARIO v1.0

## Estado del proyecto
En desarrollo activo

## Qué es?
Es basicamente un programa de inventario en consola.
Mas que un proyecto es una herramienta que desarrolle y desarrollo para uso propio.

## Cómo se usa?
1. Tener python instalado.
2. Clonar repo
    ```
    git clone https://github.com/0plimplim0/inventory
    ```
3. Ejecutar
    ````
    python ./main.py
    ```

## Formato para archivos txt
Para meter varios elementos de golpe se puede usar un archivo txt junto a la funcion **txtToJson** del archivo **tools.py** en la carpeta **utils** con el siguiente formato:
```
tipo | valor | cantidad
```

## Roadmap

### v1.0
- Base del proyecto funcional.
- Guardado de inventario en *json*.
- 3 propiedades basicas por elemento.

### v1.1
- Manejo de errores.
- Filtrado por tipo.
- Implementacion de IDs para elementos.
- Busqueda de elementos por ID.
- Manipulación basica de items (CRUD).

### v1.2
- Cambio de *json* a *sqlite*.
- Mejora en el manejo de errores (Logs).

### v1.3
- Interfaz grafica con *Tkinter*.