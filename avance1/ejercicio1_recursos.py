# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: [Nombre Apellido 1], [Nombre Apellido 2], [Nombre Apellido 3]
# Fecha: 15/10/2026 Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

#Declaración de constantes ------------------------------------------------------------------------------------------------------------------
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
RESERVA_PROVISIONES = 3

#Entrada de datos --------------------------------------------------------------------------------------------------------------------------
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días estimados para llegar al destino: "))
