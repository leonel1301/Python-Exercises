def reverseString(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return reverseString(cadena[1:]) + cadena[0]


string = input("Ingresa una cadena: ")
resultado = reverseString(string)
print(f"Cadena invertida: {resultado}")
