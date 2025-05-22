# Ejercicio: Gestión Sencilla de Tareas Pendientes

# 1. Crea una lista vacía para almacenar las tareas
tareas_pendientes = []

def mostrar_tareas():
    """Función auxiliar para mostrar las tareas actuales."""
    if not tareas_pendientes: # Comprueba si la lista está vacía
        print("\n--- No hay tareas pendientes ---")
    else:
        print("\n--- Tus Tareas Pendientes ---")
        # Usamos enumerate para obtener tanto el índice como el elemento
        # El 'start=1' hace que la numeración empiece desde 1 en lugar de 0
        for i, tarea in enumerate(tareas_pendientes, start=1):
            print(f"{i}. {tarea}")
        print("----------------------------")

# 2. Bucle principal del menú
while True:
    print("\n--- Menú de Tareas ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    print("----------------------")

    opcion = input("Elige una opción (1-4): ")

    if opcion == '1':
        # Opción 1: Añadir tarea
        nueva_tarea = input("Introduce el nombre de la nueva tarea: ")
        tareas_pendientes.append(nueva_tarea)
        print(f"'{nueva_tarea}' ha sido añadida a tus tareas.")

    elif opcion == '2':
        # Opción 2: Ver tareas
        mostrar_tareas()

    elif opcion == '3':
        # Opción 3: Marcar tarea como completada
        mostrar_tareas() # Primero, muestra las tareas para que el usuario pueda elegir

        if not tareas_pendientes: # Si la lista está vacía después de mostrarla
            print("No hay tareas para marcar como completadas.")
            continue # Vuelve al inicio del bucle

        try:
            # Pedimos el número de la tarea
            num_tarea_completar = int(input("Introduce el NÚMERO de la tarea a completar: "))

            # Verificamos si el número de tarea es válido
            # Recuerda: el usuario ve 1, 2, 3... pero las listas usan índices 0, 1, 2...
            # Por eso restamos 1 al número del usuario para obtener el índice real.
            if 1 <= num_tarea_completar <= len(tareas_pendientes):
                indice_tarea = num_tarea_completar - 1
                # Usamos pop() para eliminar la tarea por su índice y obtener su valor
                tarea_completada = tareas_pendientes.pop(indice_tarea)
                print(f"Tarea '{tarea_completada}' marcada como completada y eliminada.")
            else:
                print("Número de tarea inválido. Por favor, introduce un número de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
        except IndexError: # Aunque la verificación 'if' ya ayuda, esto es un extra
            print("Número de tarea fuera de rango.")

    elif opcion == '4':
        # Opción 4: Salir
        print("¡Gracias por usar el gestor de tareas! ¡Adiós!")
        break # Sale del bucle while y termina el programa

    else:
        # Manejo de opciones inválidas
        print("Opción no válida. Por favor, elige un número del 1 al 4.")