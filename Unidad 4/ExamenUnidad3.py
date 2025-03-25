# Examen unidad 3.
from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv

import csv
import datetime  
import time  

archivo = "ExamenUnidad3.py" 

Jugadores = {}
Equipos = {}

# Función para cargar los jugadores y equipos desde CSV
def cargar_datos():
    try:
        # Cargar jugadores desde archivo CSV
        with open('jugadores.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Jugadores[row['Nombre']] = {'Edad': row['Edad'], 'Posición': row['Posición']}
        
        # Cargar equipos desde archivo CSV
        with open('equipos.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Equipos[row['Nombre']] = {'País': row['País'], 'Liga': row['Liga']}
    except FileNotFoundError:
        print("No se encontró el archivo CSV. Se iniciarán las listas vacías.")

# Función para guardar los jugadores y equipos en CSV
def guardar_datos():
    # Guardar jugadores en archivo CSV
    with open('jugadores.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Nombre', 'Edad', 'Posición'])
        writer.writeheader()
        for jugador, detalles in Jugadores.items():
            writer.writerow({'Nombre': jugador, 'Edad': detalles['Edad'], 'Posición': detalles['Posición']})

    # Guardar equipos en archivo CSV
    with open('equipos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Nombre', 'País', 'Liga'])
        writer.writeheader()
        for equipo, detalles in Equipos.items():
            writer.writerow({'Nombre': equipo, 'País': detalles['País'], 'Liga': detalles['Liga']})

# Cargar los datos desde los archivos CSV al inicio
cargar_datos()

print("💡Bienvenido.👋")
print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
time.sleep(1)

while True:
    print("Menú Principal")
    print("1. Agregar jugador")
    print("2. Agregar equipo")
    print("3. Ver lista")
    print("4. Eliminar jugador")
    print("5. Eliminar equipo")
    print("6. Salir")

    opcion = input("Elige una opción:✍️")

    # Agregar un jugador.
    if opcion == "1":
        jugador_nuevo = input("⚽️Escribe el nombre del jugador:")
        edad = input("📅Escribe la edad del jugador:")
        posicion = input("🔄Escribe la posición del jugador:")
        Jugadores[jugador_nuevo] = {"Edad": edad, "Posición": posicion}  
        print(f"Jugador '{jugador_nuevo}' agregado.")
        time.sleep(1)
        print(Jugadores)
        # Guardar los datos después de agregar un jugador
        guardar_datos()

    # Agregar equipo.
    elif opcion == "2":
        equipo = input("⚽️Escribe el nombre del equipo:")
        pais = input("🌍Escribe el país del equipo:")
        liga = input("🏆Escribe la liga del equipo:")
        Equipos[equipo] = {"País": pais, "Liga": liga}  
        print(f"Equipo '{equipo}' agregado.")
        time.sleep(1)
        print(Equipos)
        # Guardar los datos después de agregar un equipo
        guardar_datos()

    # Ver listas completas
    elif opcion == "3":
        print("\n ✅Tu lista es:")
        time.sleep(1)
        print("Jugadores:")
        for jugador, detalles in Jugadores.items():
            print(f"- {jugador}: {detalles}")
        print("\nEquipos:")
        for equipo, detalles in Equipos.items():
            print(f"- {equipo}: {detalles}")

    # Eliminar jugador.
    elif opcion == "4":
        print("🔸¿Qué jugador desea eliminar?❓")
        print(Jugadores)
        jugador = input("Ingrese el nombre del jugador que desea eliminar:")
        if jugador in Jugadores:
            del Jugadores[jugador]  
            print(f"➞ El jugador {jugador} ha sido eliminado.❌")
        else:
            print(f"➞ El jugador {jugador} no existe en la lista.⚠️")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(1)
        print(Jugadores)
        # Guardar los datos después de eliminar un jugador
        guardar_datos()

    # Eliminar equipo.
    elif opcion == "5":
        print("🔸¿Qué equipo desea eliminar?❓")
        print(Equipos)
        equipo = input("Ingrese el nombre del equipo que desea eliminar:")
        if equipo in Equipos:
            del Equipos[equipo]  
            print(f"➞ El equipo {equipo} ha sido eliminado.❌")
        else:
            print(f"➞ El equipo {equipo} no existe en la lista.⚠️")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(1)
        print(Equipos)
        # Guardar los datos después de eliminar un equipo
        guardar_datos()

    # Salir del programa
    elif opcion == "6":
        time.sleep(1)
        print("👋 Saliendo del programa.¡Hasta luego!💤")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        break

 # Guardar los diccionarios en un archivo CSV
guardar_diccionarios_en_csv(archivo, Jugadores)

# Leer los diccionarios desde el archivo CSV
jugadores_leidos = leer_diccionarios_de_csv(archivo)
print("Jugadores leídos del archivo CSV:")
print(Jugadores_leidos)