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


print(len(Nombres))

Materias.insert(0,"Programación")#Inserta en dato en la posicion deseada (primero posición).
print(Materias)

for Materia in Materias: 
    print(Materia)