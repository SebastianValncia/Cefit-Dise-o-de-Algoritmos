class animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1

    def cambiar_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre} - Especie: {self.especie} - Edad: {self.edad} años - Hábitat: {self.habitat}")


animal1 = animal("León", "Panthera leo", 5, "Sabana")
animal2 = animal("Tigre", "tigris", 3, "Bosque")

animal1.mostrar_detalles()
animal2.cumplir_años()
animal2.mostrar_detalles()
