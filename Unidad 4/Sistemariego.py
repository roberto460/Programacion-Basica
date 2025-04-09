# Sistema de riego automatico.

import random

def menu_riego():
    opcion = 0
    while opcion != 2:
        print("---- MENÚ ----")
        print("1. Medir humedad")
        print("2. Salir")
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            humedad = random.randint(10, 100)
            print(f"Humedad actual: {humedad}%")
            if humedad < 40:
                print("Humedad baja. Activando riego...")
            else:
                print("Humedad suficiente. No se activa riego.")
        elif opcion != 2:
            print("Opción no válida.")
    
    print("Fin del programa.")

menu_riego()
        