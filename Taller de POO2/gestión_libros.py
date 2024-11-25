class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def mostrar_informacion(self):
        print(f"{self.titulo} - Autor: {self.autor} - Género: {self.genero} - Precio: ${self.precio}")

    def es_mas_caro_que(self, otro_libro):
        return self.precio > otro_libro.precio

# Instanciación de libros
libro1 = Libro("El Principito", "Antoine de Saint", "historia", 50)
libro2 = Libro("1984", "George Orwell", "Ficción", 15)


libro1.mostrar_informacion()
libro1.aplicar_descuento(10)
libro2.mostrar_informacion()