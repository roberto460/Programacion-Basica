# Examen unidad 3.

# Para manejar fechas y horas
import datetime  

# Para pausas (Pausa de 2 segundos)
import time  

Jugadores = []
Equipos = []

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

#Agregar un jugador.
    if opcion == "1":
        jugador = input("Escribe un jugador:⚽️")
        print(f"jugador '{jugador}' agregado.")
        Jugadores.append(jugador)
        time.sleep(2)
        print(Jugadores)

#Agregar equipo.
    elif opcion == "2":
        equipo = input("Escribe un equipo:⚽️")
        print(f"equipo '{equipo}' agregado.")
        Equipos.append(equipo)
        time.sleep(2)
        print(Equipos)

#Ver listas completas
    elif opcion == "3":
        print("\n ✅Tu lista es:")
        time.sleep(2)
        print(Jugadores,
         Equipos)

#Eliminar jugador.
    elif opcion == "4":
        print("🔸¿Qué jugador desea eliminar?❓")
        print(Jugadores)
        jugador = input("Ingrese el jugador que desea eliminar:")
        Jugadores.remove(jugador)
        print(f"➞ El jugador {jugador} ha sido eliminado.❌")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(1)
        print(Jugadores)

#Eliminar equipo.
    elif opcion == "5":
        print("🔸¿Qué equipo desea eliminar?❓")
        print(Equipos)
        equipo = input("Ingrese el equipo que desea eliminar:")
        Equipos.remove(equipo)
        print(f"➞ El equipo {equipo} ha sido eliminado.❌")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(1)
        print(Equipos)

#Salir del programa
    elif opcion == "6":
        time.sleep(2)
        print("👋 Saliendo del programa.¡Hasta luego!💤")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        break