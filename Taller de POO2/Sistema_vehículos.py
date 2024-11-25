class vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, km):
        self.kilometraje += km

    def mostrar_detalles(self):
        print(f"{self.marca} {self.modelo} {self.año} - kilometraje: {self.kilometraje} km")

    def es_vehiculo_antiguo(self):
        return 2024- self.año > 20


vehiculo1 = vehiculo("chevrolet", "cruze", 2000, 50000)
vehiculo2 = vehiculo("toyota", "corolla", 2005, 1500000)

vehiculo1.mostrar_detalles()
vehiculo2.mostrar_detalles()