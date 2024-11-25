class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Tipo de transporte: {self.tipo}, Capacidad: {self.capacidad} pasajeros")


class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ruta: {self.ruta}")


class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de vagones: {self.numero_vagones}")


autobus = Autobus("Autobús", 40, "Ruta 23")
tren = Tren("Tren", 300, 20)

autobus.mostrar_info()
print()
tren.mostrar_info()
