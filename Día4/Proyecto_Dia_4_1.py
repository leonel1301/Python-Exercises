from random import *

nombre = input("Hola y bienvenido al juego, dime tu nombre para continuar: ")
print(f'Bueno {nombre} he pensado en un número entre 1 y 100, y solo tienes 8 intentos para adivinar cuál '
                   f'crees que es el número...')
numpc = randint(1, 100)
print(numpc)
count = 1
while count <= 8:
    numero = int(input('¿Cuál es el número? '))
    count += 1
    if numero < 1 or numero > 100:
        print('Usted eligió el numero {} , el cual no está permitido'.format(numero))
    elif numero < numpc:
        print('<<El numero que usted ha elegido es menor al número secreto>>')
    elif numero > numpc:
        print('<<El número que usted ha elegido es mayor al número secreto>>')
    else:
        print("Usted descubrió el número secreto"
              "Le tomó {} intentos descubrirlo".format(count))
        break
if count > 8:
    print("Eres un perdedor :D")