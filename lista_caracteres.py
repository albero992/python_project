lista_caracteres = input("Escribe una lista de numeros separados por coma: ").split(",")
resultado = 0

for i in range(len(lista_caracteres)):
    resultado += int(lista_caracteres[i])

    print(lista_caracteres)
