import json
import os

# Nombre del archivo donde se guardará el inventario
INVENTORY_FILE = 'inventory.json'


def cargar_inventario():
    """Carga el inventario desde el archivo JSON."""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return {}


def guardar_inventario(inventario):
    """Guarda el inventario en el archivo JSON."""
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventario, file, indent=4)


def añadir_producto(inventario):
    """Añade un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio unitario: "))

    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    guardar_inventario(inventario)
    print(f"Producto '{nombre}' añadido al inventario.")


def actualizar_producto(inventario):
    """Actualiza un producto existente en el inventario."""
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        cantidad = int(
            input("Ingrese la nueva cantidad (dejar vacío para no cambiar): ") or inventario[nombre]['cantidad'])
        precio = float(input("Ingrese el nuevo precio (dejar vacío para no cambiar): ") or inventario[nombre]['precio'])

        inventario[nombre]['cantidad'] = cantidad
        inventario[nombre]['precio'] = precio
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' actualizado.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


def mostrar_inventario(inventario):
    """Muestra todos los productos en el inventario."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for nombre, info in inventario.items():
            print(f"- {nombre}: Cantidad = {info['cantidad']}, Precio = {info['precio']}")


def main():
    """Función principal de la aplicación."""
    inventario = cargar_inventario()

    while True:
        print("\nMenú de opciones:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            añadir_producto(inventario)
        elif opcion == '2':
            actualizar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario(inventario)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()
