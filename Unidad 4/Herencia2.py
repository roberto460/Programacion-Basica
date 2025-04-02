# Herencia2.
#clase base o padre.
class Computadoras:
    def __init__(self, marca, modelo, color, procesador):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.procesador = procesador

    def presentarse(self):
        return f"Mi computadora es una {self.marca}; modelo {self.modelo}, de color {self.color} y tiene un procesador {self.procesador}."

# Clase derivada o hija
class Computadora_de_escritorio(Computadoras):
    def __init__(self, marca, modelo, color, procesador, monitor):
        super().__init__(marca, modelo, color, procesador)  # Llamada al constructor de la clase padre
        self.monitor = monitor

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Mi computadora es una {self.marca}, modelo {self.modelo}, de color {self.color}, y tiene un monitor {self.monitor}."

# Otra clase derivada
class Laptop(Computadoras):
    def __init__(self, marca, modelo, color, procesador, bateria, portabilidad):
        super().__init__(marca, modelo, color, procesador)
        self.bateria = bateria
        self.portabilidad = portabilidad

    def presentarse(self):
        return f"Mi computadora es una {self.marca}; modelo {self.modelo}, de color {self.color}, con un procesador {self.procesador}, batería {self.bateria} y excelente portabilidad {self.portabilidad}."

# Programa principal
if __name__ == "__main__":
    computadoras = Computadoras("HP", "HP 250 G10", "blanca", "Intel Core i5")
    computadora_de_escritorio = Computadora_de_escritorio("Dell", "Inspiron 3671", "plateado", "Intel Core i5", "LED de 22 pulgadas")
    laptop = Laptop("Lenovo", "Slim 3 15RH8", "gris", "Intel Core i7", "45Wh", "alta")

    print(computadoras.presentarse())
    print(computadora_de_escritorio.presentarse())
    print(laptop.presentarse())