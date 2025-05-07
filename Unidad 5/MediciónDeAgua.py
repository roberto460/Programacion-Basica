#Medición de nivel del agua.

def medicion_nivel_agua():
    # Definir umbrales
    umbral_bajo = 20.0
    umbral_alto = 80.0
    
    print("Checando el nivel de agua...")
    nivel_agua = float(input("Ingrese el nivel de agua: "))
    
    if nivel_agua < umbral_bajo:
        alerta = "El nivel de agua es bajo."
    elif nivel_agua > umbral_alto:
        alerta = "El nivel de agua es alto."
    else:
        alerta = "El nivel de agua está dentro del rango."
    
    print(alerta)

medicion_nivel_agua()
