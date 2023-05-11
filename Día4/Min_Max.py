menor = min(12, 45, 67, 78, 87)
mayor = max(12, 45, 67, 78, 87)

lista = [58, 96, 72, 64, 35]

listnombre = ['juan', 'pablo', 'alicia', 'carlos']
nombre = 'Carlos'
nombre2 = 'carlos'

dic = {'C1': 45, 'C2': 11}


print(dic["C2"])
print(min(dic.keys()))
print(min(dic.values()))
print(min(nombre))
print(min(nombre2))
print(min(listnombre))
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')
print(mayor)
print(max(lista))

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)
print(edad_minima)