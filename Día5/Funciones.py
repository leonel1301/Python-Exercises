def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


def todos_positivos(lista):
    count = 0
    for n in lista:
        if n >= 0:
            count += 1

    if count == len(lista):
        return True
    else:
        return False


def suma_menores(lista):
    suma = 0
    for n in lista:
        if 0 < n < 100:
            suma += n
    return suma








lista_numeros = [1, 50, 5000, 750]
resultado = cantidad_pares(lista_numeros)
print(resultado)

resultado = chequear_3_cifras([550, 99, 6000])
print(resultado)
