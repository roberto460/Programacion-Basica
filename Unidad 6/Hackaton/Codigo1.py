#Codigo 1.

programa = input("Introduce el nombre del programa:")
print("Has iniciado el progrma,", programa)

Frase_texto = input("Escribe una frase o texto:")

palabras = Frase_texto.split()

cantidad_palabras = len(palabras)
print(f"El texto contiene {cantidad_palabras} palabras.")