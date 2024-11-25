class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad} años\nEspecie: {self.especie}")

class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def ladrar(self):
        print("Guau, guau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")

class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def maullar(self):
        print("Miau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")

perro1 = Perro("Martina", 4, "Perro", "Labrador")
gato1 = Gato("Gata", 3, "Gato", "Negro")

perro1.mostrar_info()
gato1.mostrar_info()
perro1.ladrar()
gato1.maullar()
