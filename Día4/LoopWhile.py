monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

respuesta = "s"
while respuesta == 's':
    respuesta = input("quieres seguir")
else:
    print("Gracias")

numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    else:
        pass
    numero -= 1
