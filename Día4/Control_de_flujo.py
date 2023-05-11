num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual a {num2}")
else:
    print(f"{num2} es mayor que {num1}")

nombre = 'leonel'
edad = 18
dni = '73171570'
if nombre == 'leonel':
    if edad == 18:
        if dni == '73171570':
            print("Tu nombre es {}, tu edad es {} y tu DNI, {}".format(nombre, edad, dni))