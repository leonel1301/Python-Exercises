from random import *

# Lista Inicial
palitos = ['-', '--', '---', '----']


# Mezclar Palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle Intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Ingrese el numero: ")
    return int(intento)


# Comprobar intento
def chekingintento(lista, intento):
    if lista[intento - 1] == ['-']:
        print("A lavar los platos")
    else:
        print("Esta ves te haz salvado")
    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chekingintento(palitos_mezclados, seleccion)

probar_suerte()
