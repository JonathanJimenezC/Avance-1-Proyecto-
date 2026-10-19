# ============================================================
# Archivo: ejercicio4.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariana Chacón Quirós, Jonathan Jimenes Carmona, Jorge Alfaro Vargas
# Fecha: 18 de octubre, 2026. Versión: 1.0
# # Descripción: Muestra la verificación general antes de la autorización inicial del lanzamiento.
# ============================================================




#Aquí se solicitan los datos necesarios.
combustible_disponible = int(input("Ingrese la cantidad de combustible necesaria para la mision: "))
combustible_ida = int(input("Ingrese la cantidad de combustible necesaria para llegar al destino: "))
combustible_regreso = int(input("Ingrese la cantidad de combustible necesaria para regresar del destino: "))

oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible en la nave: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido para la mmisión: "))

energia_disponible = int(input("Ingrese la cantidad de energía disponible en la nave: "))
energia_requerida = int(input("Ingrese la cantidad de energía requerida para la mmisión: "))

provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponible en la nave: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas para la mmisión: "))




#Aquí se realizan las operaciones para los resultados finales
RESERVA_EMERGENCIA=10
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA





#Aquí se imprime si la nave puede o no despegar
print("--Autorización del lanzamiento:--")
print("Combustible disponible: ", combustible_disponible)
print("Combustible necesario para llegar al destino: ", combustible_ida)
print("Combustible necesario para regresar: ", combustible_regreso)
print("Reserva de emergencia: ", RESERVA_EMERGENCIA)
print("Combustible total requerido: ", combustible_total_requerido)
print("Oxígeno disponible: ", oxigeno_disponible)
print("Oxígeno requerido: ", oxigeno_requerido)
print("Energía disponible: ", energia_disponible)
print("Energía requerida: ", energia_requerida)
print("Provisionnes disponible: ", provisiones_disponibles)
print("Provisionnes requerido: ", provisiones_requeridas)

if combustible_disponible>=combustible_total_requerido:
    if oxigeno_disponible>=oxigeno_requerido:
        if energia_disponible>=energia_requerida:
            if provisiones_disponibles>=provisiones_requeridas:
                print("Lanzamiento autorizado.")
            else:
                print("Lanzamiento no autorizado. La misión debe ser revisada.")
        else:
                print("Lanzamiento no autorizado. La misión debe ser revisada.")
    else:
                print("Lanzamiento no autorizado. La misión debe ser revisada.")
else:
                print("Lanzamiento no autorizado. La misión debe ser revisada.")