inicio = input("escriba una palabra o frase: ").lower()
conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }

for letra in inicio:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

for vocal, conteo in conteo_vocales.items():
    print(f"vocal '{vocal} : {conteo}")
