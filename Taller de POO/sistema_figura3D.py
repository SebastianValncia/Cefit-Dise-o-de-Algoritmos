class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado")

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        volumen = self.lado ** 3
        print(f"El volumen del cubo es: {volumen}")

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        volumen = (4/3) * 3.1416 * (self.radio ** 3)
        print(f"El volumen de la esfera es: {volumen}")

cubo1 = Cubo(3)
esfera1 = Esfera(5)

cubo1.calcular_volumen()
esfera1.calcular_volumen()

