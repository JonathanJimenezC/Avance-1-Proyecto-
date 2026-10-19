# ============================================================
# Archivo: ejercicio2.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariana Chacón Quirós, Jonathan Jimenes Carmona, Jorge Alfaro Vargas
# Fecha: 18 de octubre, 2026. Versión: 1.0
# # Descripción: Calcula la cantidad de combustible necesario para la misión y el combustible adicional 
# ============================================================




#Aquí le indicamos al usuario que ingrese los datos requeridos.
combustible_disponible = int(input("Ingrese la cantidad de combustible necesaria para la mision: "))
combustible_ida = int(input("Ingrese la cantidad de combustible necesaria para llegar al destino: "))
combustible_regreso = int(input("Ingrese la cantidad de combustible necesaria para regresar del destino: "))




#Aquí realizamos las formulas que nos ayudaran a calcular el combustible de la mision.
RESERVA_EMERGENCIA = 10
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA
combustible_adicional = combustible_disponible - combustible_total_requerido




#Finalmente imprimimos los datos y una advertencia en caso de que el combustible adicional sea menor a 10.
print("--Verificación del combustible:--")
print("Combustible disponible: ", combustible_disponible)
print("Combustible necesario para llegar al destino: ", combustible_ida)
print("Combustible necesario para regresar: ", combustible_regreso)
print("Reserva de emergencia: ", RESERVA_EMERGENCIA)
print("Combustible total requerido: ", combustible_total_requerido)
print("Combustible adicional disponible: ", combustible_adicional)

if combustible_adicional<10:
    print("Advertencia: el margen adicional de combustible es bajo.")


