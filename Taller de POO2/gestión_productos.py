class producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre =nombre
        self.precio = precio
        self.cantidad = cantidad


    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def ajustar_inventario(self, cantidad):
        self.cantidad += cantidad

    def mostrar_informacion(self):
        print(f"producto: {self.nombre}, precio: ${self.precio}, cantidad: {self.cantidad}")

producto1 = producto("camiseta",20.99,70)
producto2 = producto("pantalon", 21.20, 10)
producto3 = producto("zapatos",49.00, 20)

producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()