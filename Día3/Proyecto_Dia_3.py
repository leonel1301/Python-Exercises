mi_texto = input("Ingrese un texto: ")
mi_lista_2 = [input("Ingrese la primera letra: ").lower(), input("Ingrese la segunda letra: ").lower(),
              input("Ingrese la tercera letra: ").lower()]
mi_texto_2 = mi_texto.lower()
count1 = mi_texto_2.count(mi_lista_2[0])
count2 = mi_texto_2.count(mi_lista_2[1])
count3 = mi_texto_2.count(mi_lista_2[2])

print(f"Hemos encontrado la letra '{mi_lista_2[0]}' repetida {count1} veces")
print(f"Hemos encontrado la letra '{mi_lista_2[1]}' repetida {count2} veces")
print(f"Hemos encontrado la letra '{mi_lista_2[2]}' repetida {count3} veces")

palabras = mi_texto_2.split()
print(f"La cantidad de palabras es: {len(palabras)}\n")
