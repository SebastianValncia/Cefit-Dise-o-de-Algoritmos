import json
import os

CONTACTS_FILE = 'contacts.json'


def cargar_contactos():
    """Carga los contactos desde el archivo JSON."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}  # Devuelve un diccionario vacío


def guardar_contactos(contactos):
    """Guarda la lista de contactos en el archivo JSON."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contactos, file, indent=4)


def añadir_contacto(contactos):
    """Añade un nuevo contacto a la lista."""
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    contactos[nombre] = {'telefono': telefono, 'correo': correo}
    guardar_contactos(contactos)
    print(f"Contacto {nombre} añadido.")


def actualizar_contacto(contactos):
    """Actualiza un contacto existente."""
    nombre = input("Nombre del contacto a actualizar: ")
    if nombre in contactos:
        telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
        correo = input("Nuevo correo electrónico (dejar en blanco para no cambiar): ")
        if telefono:
            contactos[nombre]['telefono'] = telefono
        if correo:
            contactos[nombre]['correo'] = correo
        guardar_contactos(contactos)
        print(f"Contacto {nombre} actualizado.")
    else:
        print("Contacto no encontrado.")


def eliminar_contacto(contactos):
    """Elimina un contacto de la lista."""
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")


def mostrar_contactos(contactos):
    """Muestra todos los contactos registrados."""
    if contactos:
        print("Lista de contactos:")
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Correo: {info['correo']}")
    else:
        print("No hay contactos registrados.")


def menu():
    """Muestra el menú y gestiona la interacción con el usuario."""
    contactos = cargar_contactos()

    while True:
        print("\nOpciones:")
        print("1. Añadir contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            añadir_contacto(contactos)
        elif opcion == '2':
            actualizar_contacto(contactos)
        elif opcion == '3':
            eliminar_contacto(contactos)
        elif opcion == '4':
            mostrar_contactos(contactos)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()
