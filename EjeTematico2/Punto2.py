nombres = input("escriba el nombres separados por comas: ")
lista_nombres = [nombre.strip() for  nombre  in nombres.split(',')]
lista_nombres.sort()
print(" nombre en orden alfabetico: ")
for nombre in lista_nombres:
    print(nombre)