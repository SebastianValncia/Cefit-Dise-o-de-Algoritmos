def suma_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma

lista = [1, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(lista)
print(resultado)