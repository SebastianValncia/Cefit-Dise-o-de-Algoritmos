class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Marca: {self.marca}")


class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de batería: {self.capacidad_bateria} mAh")


class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de pantalla: {self.tamano_pantalla} pulgadas")


telefono = TelefonoMovil("Iphone 11", 2999, "Apple", 5000)
laptop = Laptop("MacBook Pro", 4999, "Apple", 16)

telefono.mostrar_info()
print()
laptop.mostrar_info()
