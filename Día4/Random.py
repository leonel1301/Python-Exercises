from random import *

aleatorio = randint(1, 11)


aleatorio = randint(1, 50)
aleatorio2 = round(uniform(1,5), 2)
aleatorio3 = random()

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)
print(numeros)
print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)