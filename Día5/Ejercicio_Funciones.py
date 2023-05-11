    from random import *


    def lanzar_dados():
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        return dado1, dado2


    def evaluar_jugada(dado1, dado2):
        suma_dados = dado1 + dado2
        if suma_dados <= 6:
            return f"La suma de tus dados es {suma_dados}. Lamentable"
        elif 6 < suma_dados < 10:
            return f"La suma de tus dados es {suma_dados}. Tienen buenas chances"
        else:
            return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


intento1, intento2 = lanzar_dados()
print(intento1, intento2)

