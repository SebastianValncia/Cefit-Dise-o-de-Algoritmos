def filtrar_palabras(palabras, letra):
    return [palabra for palabra in palabras if palabra.lower().startswith(letra.lower())]

inicio = input("escriba una lista de palabras separadas por comas: ")
letra = input("escriba la letra con la que deben comenzar las palabras: ")

lista_palabras = [palabra.strip() for palabra in inicio.split(",")]

resultado = filtrar_palabras(lista_palabras, letra)

print("Palabras que comienzan con '{}':".format(letra))
print(resultado)

