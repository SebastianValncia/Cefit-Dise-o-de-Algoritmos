class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El material '{self.titulo}' ha sido prestado.")
        else:
            print(f"El material '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El material '{self.titulo}' ha sido devuelto.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nCódigo: {self.codigo}\nDisponible: {'Sí' if self.disponible else 'No'}")

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Páginas: {self.numero_paginas}\nGénero: {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Edición: {self.numero_edicion}\nFecha de Publicación: {self.fecha_publicacion}")


libro1 = Libro("No Rules Clan", "Sison Beats", "023", 100, "Musica")
revista1 = Revista("La viña", "N Wise Allah", "005", 35, "2023-10-08")

libro1.mostrar_info()
revista1.mostrar_info()
libro1.prestar()
libro1.devolver()
