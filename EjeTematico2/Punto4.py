def suma_numeros_pares():
    numeros = input("escribe una lista de numeros separados por espacios: ")

    lista_numeros = list(map(int, numeros. split()))
    suma_pares = sum(num for num in lista_numeros if num % 2==0)
    print("la suma de los numeros pares es:", suma_pares)

suma_numeros_pares()
