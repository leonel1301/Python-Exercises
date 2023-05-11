palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

palabra = 'leonel'
lista = [letra for letra in palabra]
lista = lista[::-1]
print(lista)

lista = []
for n in range(0, 21, 2):
    lista.append(n)
print(lista)

lista = [n for n in range(0, 21, 2) if n * 2 > 10]
lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [m * 3.281 for m in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [num for num in valores if num % 2 == 0]
print(valores_pares)

palabra = "agua"
palabra = list(palabra)
print(palabra)
