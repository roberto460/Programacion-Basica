#Listas 4
Nombres = ["Adan", "Oswaldo", "Sabain", "Lupita", "Alexa", "Victor", "Alejandro", "Aaron", "Enrique", "Cristian", "Roberto"]
Edades = [19, 18, 19, 18, 18, 18, 18, 18, 18, 18, 18]
Libre = ["Azul", "Rojo", "Morado", "Negro", "Blanco", "Naranja", "Amarillo", "Gris", "Verde", "Cafe"]
Materias = ["Calculo", "Programación", "Algebra", "Ingles", "Ciencias e ingenierias", "Estadictica", "Calidad"]
Profesores = ["Enrique", "Marlem", "Jorge", "Eduardo", "Guillermo", "Martha", "Elizabeth"]


print(Nombres)
print(Edades)
print(Libre)
print(Materias)
print(Profesores)

#
print(len(Nombres))

#Ornenar elementos min y max
print(max(Edades))
print(min(Edades))

#Ordenar elementos
Edades.sort()
print(Edades)
Nombres.sort()
print(Nombres)
Libre.sort()
print(Libre)
Materias.sort()
print(Materias)
Profesores.sort()
print(Profesores)

#Elimanar elementos
Materias.remove("Programación")
print(Materias)

#Agregar elemento al final
Materias.append("Programación")
print(Materias)

Materias.append([1], "Programación")
print(Materias)