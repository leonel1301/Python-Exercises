lista = ['a', 'b', 'c']

for indice, item in enumerate(range(50, 55)):
    print(indice, item)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, item in list(enumerate(lista_nombres)):
    if item.startswith('M'):
        print(indice)
    else:
        pass