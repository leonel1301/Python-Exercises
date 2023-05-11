import string


def descifrar(cadena):
    if len(cadena) > 10:
        print("La contraseña debe tener menos de 10 caracteres")
        return

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenia_posible = ''
    i = 0

    while i < len(cadena):
        for caracter in caracteres:
            print(contrasenia_posible + caracter)

            if cadena[i] == caracter:
                contrasenia_posible += caracter
                i += 1
                break


clave = input("Ingrese Contraseña: ")
descifrar(clave)


"""
La técnica que realicé en este ejercicio es Fuerza Bruta,  este código utiliza un 
conjunto de caracteres que incluye letras mayúsculas y minúsculas, dígitos y signos 
de puntuación para coincidir con la contraseña dada. Comparamos cada caracter con el
caracter correspondiente a la contraseña ingresada, si es que hay coincidencia, este 
caracter se agrega a la variable "contrasenia_posible" y continúa el ciclo.
"""