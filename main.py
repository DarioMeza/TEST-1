import os
import math
import globales
import json
import random


def asignar_ventas():
    trabajadores = globales.leer_archivo_json("trabajadores.json")
    ventas = []
    for trabajador in trabajadores:
        nueva_venta = {
            "nombre": trabajador["nombre"],
            "venta": random.randint(1500000, 5000000)
        }
        ventas.append(nueva_venta)
    
    globales.guardar_archivo_json("ventas.json", ventas)


def ver_estadisticas():
    if  not os.path.exists("ventas.json"):
        print("No hay ventas registradas...")
        return
    
    trabajadores = globales.leer_archivo_json("ventas.json")
    ventas_empleados = [trabajador["venta"] for trabajador in trabajadores]

    venta_max = max(ventas_empleados)
    venta_min = min(ventas_empleados)
    promedio_ventas = sum(ventas_empleados) / len(ventas_empleados)
    media_geo = math.exp(sum(math.log(v) for v in ventas_empleados) / len(ventas_empleados))

    print(venta_max)
    print(venta_min)
    print(promedio_ventas)
    print(media_geo)

def iniciar_programa():
    while True:
        print("1. Asignar Ventas")
        print("2. Ver Estadisticas")
        print("3. Salir")

        try:
            opcion = int(input("Ingrese una de las opciones >> "))
        except:
            "Error, intente nuevamente"

        if opcion < 1 or opcion > 3:
            print("Opcion invalida, intente nuevamente")
        
        if opcion == 1:
            asignar_ventas()
        elif opcion == 2:
            ver_estadisticas()
        elif opcion == 3:
            break
    

__name__ == "__main__"
iniciar_programa()


    