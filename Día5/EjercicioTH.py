print("Bienvenidos a la Calculadora\nPara salir escribe Salir")
print("Las operaciones son suma, multi, div y resta\n")
verificate = False
resultado = 0
if not verificate:
    num = int(input("Ingresar número << "))
    verificate = True
while verificate:
    operacion = input("Ingrese operación << ")
    match operacion:
        case 'suma':
            num2 = int(input("Ingresa el siguiente número << "))
            resultado = num + num2
            print(f'El resultado es {resultado}')
        case 'mult':
            num2 = int(input("Ingresa el siguiente número << "))
            resultado = num * num2
            print(f'El resultado es {resultado}')
        case 'div':
            num2 = int(input("Ingresa el siguiente número << "))
            resultado = num/num2
            print(f'El resultado es {resultado}')
        case 'resta':
            num2 = int(input("Ingresa el siguiente número << "))
            resultado = num - num2
            print(f'El resultado es {resultado}')
        case 'salir':
            break
        case _:
            print("Error al digitar la operación >>")

    num = resultado