def invertir_lista(lista):
    nueva_lista =[]
    for i in range(len(lista) -1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista

lista_original = [1, 2, 3, 4, 5, 6, 7]
resultado = invertir_lista(lista_original)
print(resultado)