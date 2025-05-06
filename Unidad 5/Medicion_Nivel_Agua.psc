Algoritmo Medicion_Nivel_Agua

	Definir nivel_agua Como Real	
	Definir umbral_bajo Como Real
	Definir umbral_alto Como Real
	Definir alerta Como Cadena
	
	umbral_bajo = 20.0
	umbral_alto = 80.0
	
	Escribir "Checando el nivel de agua..."
	Leer nivel_agua
	
	Si nivel_agua < umbral_bajo Entonces
		alerta = "El nivel de agua es bajo."
	FinSi
	
	Si nivel_agua > umbral_alto Entonces
		alerta = "El nivel de agua es alto."
	Sino 
		alerta = "El nivel de agua está dentro del rango."
	FinSi
	Escribir alerta
FinAlgoritmo
