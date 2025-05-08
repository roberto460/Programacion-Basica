# Examen unidad 3.

import time
from reader import feed

def main():
    """Imprime el último tutorial de Python"""
tic = time.perf_counter()
    
   
# Para manejar fechas y horas
import datetime  

# Para pausas (Pausa de 2 segundos)
import time  

Jugadores = {}  
Equipos = {}    

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

    # Agregar equipo.
    elif opcion == "2":
        equipo = input("⚽️Escribe el nombre del equipo:")
        pais = input("🌍Escribe el país del equipo:")
        liga = input("🏆Escribe la liga del equipo:")
        Equipos[equipo] = {"País": pais, "Liga": liga}  
        print(f"Equipo '{equipo}' agregado.")
        time.sleep(1)
        print(Equipos)

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

    # Salir del programa
    elif opcion == "6":
        time.sleep(1)
        print("👋 Saliendo del programa.¡Hasta luego!💤")
        print("Fecha y hora actual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        break

toc = time.perf_counter()
print(f"El tutorial ha sido descargado en {toc - tic:0.4f} segundos")

if __name__ == "__main__":
    main()
