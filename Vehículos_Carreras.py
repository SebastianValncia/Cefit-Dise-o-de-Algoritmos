class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nVelocidad Máxima: {self.velocidad_maxima} km/h")

class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")

class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")


coche1 = CocheF1("Ferrari", "S-30", 350, "Suave")
moto1 = MotoGP("Yamaha", "YZ", 320, "Aérodinámico")

coche1.mostrar_info()
moto1.mostrar_info()
