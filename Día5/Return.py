def multiplicar(numero1, numero2):
    total = numero1 * numero2
    return total


resultado = multiplicar(5, 4)
print(resultado)


def invertir_palabra(palabra):
    invertido = palabra[::-1].upper()
    return invertido


resultado = invertir_palabra('python')
print(resultado)