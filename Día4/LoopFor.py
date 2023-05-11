lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra: {numero_letra}: {letra}")

lista2 = ['pablo', 'leo', 'leonel', 'mario']
for nombre in lista2:
    if nombre[0] == 'l':
        print(nombre)
    if nombre.startswith('l'):
        print(nombre)

numeros = [1, 2, 3 , 4 , 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

palabra = "python"

for letra in palabra:
    print(letra)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1' : 'a', 'clave2' : 'b', 'clave3' : 'c'}
for item in dic.values():
    print(item)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print("Hola {}".format(nombre))
