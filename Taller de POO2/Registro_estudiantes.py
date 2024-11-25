class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materias(self, materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        print(f"materias de {self.nombre}: {', '.join(self.materias)}")

    def actualizar_grado(self, nuevo_grado):
        self.grado = nuevo_grado

estudiante1 = estudiante("sebastian", 19, "10°")
estudiante2 = estudiante("carlos", 15, "8°")
estudiante3 = estudiante("maria", 17, "11°")

estudiante1.inscribir_materias("matematicas")
estudiante1.inscribir_materias("etica")
estudiante1.mostrar_materias()

estudiante2.inscribir_materias("educacion fisica")
estudiante2.inscribir_materias("español")
estudiante2.mostrar_materias()

estudiante3.inscribir_materias("fisica")
estudiante3.mostrar_materias()