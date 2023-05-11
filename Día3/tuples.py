mi_tuple =(1, 2, (10, 20), 4)
mi_tuple = list(mi_tuple)
mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))
"""al tener 3 valores y 3 variables donde reemplazar se asigna uno a cada uno"""
t = (1, 2, 3)

x, y, z = t
print(x, y ,z)


lista = ['a', 'b', 'c']
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])

lista_indices = list(enumerate("Python"))
print(lista_indices)