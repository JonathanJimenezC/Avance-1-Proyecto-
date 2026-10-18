# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Jorge Alfaro Vargas, Jonathan Jimenez Carmona, Mariana Chacón Quirós
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

#Calculos ----------------------------------------------------------------------------------------------------------------------------------
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA# El regreso dura los mismos días que la ida y consume lo mismo por día
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA# La nave debe poder regresar, por eso se suma el regreso y la reserva de emergencia
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE# Oxígeno y provisiones se consumen solo en el viaje de ida
oxigeno_requerido = dias_viaje * tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + RESERVA_OXIGENO
energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIA + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA + RESERVA_PROVISIONES

#Salida de datos ----------------------------------------------------------------------------------------------------------------------------
print("Misión:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
