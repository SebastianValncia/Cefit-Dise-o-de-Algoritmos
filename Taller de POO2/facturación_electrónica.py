class factura:
    def __init__(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = 0
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        self.items.append((descripcion, cantidad, precio_unitario))
        self.monto_total += cantidad * precio_unitario

    def mostrar_detalles(self):
        print(f"Factura {self.numero} - Cliente: {self.cliente} - Fecha: {self.fecha} - Monto Total: ${self.monto_total}")
        print("Items:")
        for item in self.items:
            print(f"{item[0]} - {item[1]} x ${item[2]}")

    def aplicar_descuento(self, porcentaje):
        self.monto_total -= self.monto_total * (porcentaje / 100)


factura1 = factura(1, "Sebastian", "2024-10-22")
factura1.agregar_item("Camiseta", 3, 19.99)
factura1.agregar_item("Pantalón", 2, 28.50)

factura1.mostrar_detalles()
factura1.aplicar_descuento(10)
factura1.mostrar_detalles()
