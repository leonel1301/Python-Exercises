dic = {'clave1' : 100, 'clave2' : 500}

a = dic.popitem()
print(dic)
print(a)

palabra = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(palabra.lstrip(",:%_#"))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert("naranja")


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
