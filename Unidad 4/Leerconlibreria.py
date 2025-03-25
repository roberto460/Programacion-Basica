import csv

def leer_diccionarios_de_csv(nombre_archivo):

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return [fila for fila in lector]
