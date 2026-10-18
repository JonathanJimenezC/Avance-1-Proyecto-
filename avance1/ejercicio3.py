# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariana Quiros, Jorge Alfaro y Jonathan Jimenez.
# Fecha: 17/10/2026
# Versión: 1.0
# Descripción: Verifica si el oxígeno y las provisiones son suficientes
# para mantener a la tripulación durante el viaje.

# Se solicitan los recursos disponibles y los necesarios, en unidades.
oxigeno_disponible = int(input("Oxígeno disponible (unidades): "))
oxigeno_requerido = int(input("Oxígeno requerido (unidades): "))
provisiones_disponibles = int(input("Provisiones disponibles (unidades): "))
provisiones_requeridas = int(input("Provisiones requeridas (unidades): "))

# Ambos recursos deben alcanzar lo requerido, incluida la igualdad.
if (oxigeno_disponible >= oxigeno_requerido
        and provisiones_disponibles >= provisiones_requeridas):
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
