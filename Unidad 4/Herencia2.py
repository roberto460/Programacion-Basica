# Herencia2
# Clase base o padre
class Computadoras:
    def __init__(self, marca, modelo, color, peso):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.procesador = procesador

    def presentarse(self):
        return f"Mi computadora es una {self.marca}; modelo {self.modelo} de color {self.color} y un procesador {self.procesador}." 

# Clase derivada o hija
class Computadora_de_escritorio(Computadoras):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo, color)  # Llamada al constructor de la clase padre
        self.monitor = monitor

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Mi computadora es una {self.marca}, modelo {self.modelo} de color {self.color} y contiene un monitor {self.monitor}."

# Otra clase derivada
class Laptop(Computadoras):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo, color)
        self.portabilidad = portabilidad
        self.bateria = bateria

    def presentarse(self):
        return f"Mi computadora es una {self.marca}; modelo {self.modelo}, procesador {self.procesador} de color {self.color} que contiene una bateria {self.bateria} con buena {self.portabilidad}." 

# Programa principal
if __name__ == "__main__":
    Computadoras = Computadoras("hp", "HP 250 G10", "blanca", "inter core i5")
    Computadora_de_escritorio = Computadora_de_escritorio("Ana", 20, "3er año de Ingeniería")
    Laptop = Profesor("Luis", 50, "Matemáticas")

    print(Computadoras.presentarse())
    print(Computadora_de_escritorio.presentarse())
    print(Laptop.presentarse())