import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

# Definición de funciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Clase de la aplicación con PyQt5
class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora y Conversión")
        self.setGeometry(100, 100, 300, 250)
        
        self.initUI()

    def initUI(self):
        # Crear widgets
        self.label_num1 = QLabel("Número 1:", self)
        self.input_num1 = QLineEdit(self)

        self.label_num2 = QLabel("Número 2:", self)
        self.input_num2 = QLineEdit(self)

        self.button_suma = QPushButton("Suma", self)
        self.button_resta = QPushButton("Resta", self)
        self.button_multiplicacion = QPushButton("Multiplicación", self)
        self.button_division = QPushButton("División", self)
        self.button_convert = QPushButton("Convertir Número 1 a Float", self)

        self.result_label = QLabel("Resultado:", self)

        # Conectar botones con funciones
        self.button_suma.clicked.connect(lambda: self.calculate("suma"))
        self.button_resta.clicked.connect(lambda: self.calculate("resta"))
        self.button_multiplicacion.clicked.connect(lambda: self.calculate("multiplicacion"))
        self.button_division.clicked.connect(lambda: self.calculate("division"))
        self.button_convert.clicked.connect(self.convert_to_float)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_num1)
        layout.addWidget(self.input_num1)
        layout.addWidget(self.label_num2)
        layout.addWidget(self.input_num2)
        layout.addWidget(self.button_suma)
        layout.addWidget(self.button_resta)
        layout.addWidget(self.button_multiplicacion)
        layout.addWidget(self.button_division)
        layout.addWidget(self.button_convert)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self, operation):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())

            if operation == "suma":
                resultado = suma(num1, num2)
            elif operation == "resta":
                resultado = resta(num1, num2)
            elif operation == "multiplicacion":
                resultado = multiplicacion(num1, num2)
            elif operation == "division":
                resultado = division(num1, num2)

            self.result_label.setText(f"Resultado: {resultado}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos.")

    def convert_to_float(self):
        texto = self.input_num1.text()
        try:
            numero = float(texto)
            self.result_label.setText(f"Conversión a float: {numero}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa un número válido.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculatorApp()
    ventana.show()
    sys.exit(app.exec_())
