nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
dni = ['73171570', '12345678', '23456791']

comprimido = list(zip(nombres, edades, dni))

print(comprimido)

for nombre, edad, dni in comprimido:
    print(f"{nombre} tiene {edad} y su DNI: {dni}")

espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)