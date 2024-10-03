def eliminar_duplicados(lista):
    nueva_lista =[]
    see = set()
    for elemento in lista :
        if elemento not in see :
            nueva_lista.append(elemento)
            see.add(elemento)
    return nueva_lista

lista_original =  [1, 1, 2, 3, 3, 4, 5, 6, 6, 7]
resultado = eliminar_duplicados(lista_original)
print(resultado)