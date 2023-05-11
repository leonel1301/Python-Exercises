precios_cafe = [('Capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]


def cafe_mas_caro(lista):
    mayor = 0
    coffe = ''

    for item, value in lista:
        if value > mayor:
            mayor = value
            coffe = item
        else:
            pass
    return coffe, mayor


cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El cafe mas caro es {cafe} cuyo precio es {precio}')
