"""
Tarea: múltiplo de 10
Autor: Priscila Cervantes 
Fecha de entrega: -
Grupo: ESI-5
Profesor: Jorge Zaldívar

Descripción:
Diseñar un programa para determinar si un número entero es múltiplo de 10.
"""

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
if numero % 10 == 0:
    print(f"El número {numero} es múltiplo de 10")

else:
    print(f"El número {numero} no es múltiplo de 10")
