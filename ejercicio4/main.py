import json
from pathlib import Path

listado_turnos = []


archivo_turnos = Path(__file__).parent / "listado_de_turnos.json"

def crear_turno(nombre, telefono, servicio, fecha):
    
    modelo = {
        "nombre": nombre,
        "telefono": telefono,
        "servicio": servicio,
        "fecha": fecha
    }
    
    listado_turnos.append(modelo)

    with open(archivo_turnos, 'a', encoding="UTF-8") as archivo:
           
        print(archivo)



nombre = input("Nombre: ")
telefono = input("Telefonos: ")
servicio = input("Servicio: ")
fecha = input("Fecha: ")

crear_turno(nombre, telefono, servicio, fecha)