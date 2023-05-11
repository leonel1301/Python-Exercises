nombre = input("¿Cuál es tu nombre? ")
ventas = input("¿Cuánto has vendido este mes? ")
ventas = int(ventas)
comision = round((ventas * 13) / 100, 2)

print("Hola {} tu total de ventas es ${} y tus comisiones correspondientes es de ${}".format(nombre, ventas, comision))
