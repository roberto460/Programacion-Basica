from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv
# Nombre del archivo a leer y de la función a importar

archivo = "ExamenUnidad3.py"

Jugadores = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

guardar_diccionarios_en_csv(archivo, jugadores)

leer_diccionarios_de_csv(archivo)

    # Leer los diccionarios desde el archivo CSV
    datos_leidos = leer_diccionarios_de_csv(archivo)
    print("Datos leídos del archivo CSV:")
    print(datos_leidos)