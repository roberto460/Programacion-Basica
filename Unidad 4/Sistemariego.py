# Sistema de riego automatico.

import random

def menu_riego():
    opcion = 0  # Definir la opción como entero
    humedad = 0.0  # Definir la humedad como real
    
    while opcion != 2:  # Repetir hasta que opción sea 2
        print("MENÚ")
        print("1. Medir humedad")
        print("2. Salir")
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:  # Si opción es 1
            humedad = random.randint(10, 100)  # Generar humedad aleatoria entre 10 y 100
            print(f"Humedad actual: {humedad}%")
            
            if humedad < 40:  # Si humedad es menor que 40
                print("Humedad baja. Activando riego...")
            else:  # Sino
                print("Humedad suficiente. No se activa riego.")
        
        elif opcion != 1 and opcion != 2:  # Si opción no es válida
            print("Opción no válida.")
    
    print("Fin del programa.")  # Fin del programa

menu_riego()