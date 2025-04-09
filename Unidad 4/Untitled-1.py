def riego_automatico():
    # Leer humedad
    humedad = float(input("Ingrese el nivel de humedad (%): "))
    # Leer parámetro
    parametro = float(input("Ingrese el nivel mínimo de humedad requerido (%): "))
    
    if humedad < parametro:
        print("Abrir la llave por un tiempo determinado")
    else:
        print("La humedad es suficiente, cerrando llave")
        
riego_automatico()
