# Ejercicio: Datos Personales Simples

# 1. Pedir al usuario su nombre completo
nombre_completo = input("Buenos días dígame su nombre!?  ")

# 2. Pedir al usuario su edad y convertirla a entero
# Usamos int() para convertir la cadena de texto obtenida por input() a un número entero
edad_str = input("Introduce tú edad BRO!  ")
edad = int(edad_str) # Convertimos la cadena de texto a un entero

# 3. Pedir al usuario su ciudad de residencia
ciudad = input("¿En qué ciudad resides? ")

# 4. Mostrar la información de forma ordenada
print("\n--- Resumen de Datos ---")
print(f"Nombre: {nombre_completo}") # Usando una f-string para insertar la variable
print(f"Edad: {edad} años")         # También usando f-string
print(f"Ciudad: {ciudad}")
print("------------------------")

# También se podría hacer concatenando cadenas (menos común hoy en día, pero válido):
# print("Nombre: " + nombre_completo)
# print("Edad: " + str(edad) + " años") # Convertimos la edad a cadena para concatenar
# print("Ciudad: " + ciudad)