class habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"habitación {self.numero} reservada.")
        else:
            print(f"habitación {self.numero} no está disponible.")

    def liberar(self):
        self.disponible = True
        print(f"habitación {self.numero} liberada.")

    def mostrar_informacion(self):
        estado = "disponible" if self.disponible else "no disponible"
        print(f"habitación {self.numero} - tipo: {self.tipo} - precio: ${self.precio} - estado: {estado}")


habitacion1 = habitacion(101, "Individual", 100)
habitacion2 = habitacion(102, "Doble", 150)

habitacion1.mostrar_informacion()
habitacion2.reservar()
habitacion2.mostrar_informacion()
