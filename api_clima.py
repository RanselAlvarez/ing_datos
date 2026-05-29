# Línea 1: Importamos la herramienta que sabe hablar HTTP
import requests  # ← Completa: ¿qué librería usamos para peticiones?
import json
from datetime import datetime
import logging
from con_logging import con_logging


con_logging()

# Línea 2: Definimos la dirección base de la API
url_base = "https://api.open-meteo.com/v1/forecast"
fecha = datetime.now().strftime("%Y-%m-%dT%H:%M")



# Línea 3-5: Definimos los parámetros que queremos enviar
mis_parametros = {
    "latitude": 23.1136,
    "longitude": -82.3667,
    "current_weather": True,
}


try:
    respuesta = requests.get(url_base, params=mis_parametros, timeout=5)
    codigo_estado = respuesta.status_code
    print(f"\nCodigo de estado: {codigo_estado}\n")
    print(respuesta.text)
    print()

    respuesta_json = respuesta.json()

    for clave, valor in respuesta_json.items():
        print(f"{clave}: {valor}")

    print()
    unidad_temperatura = respuesta_json['current_weather_units']['temperature']
    print(f"Temperatura: {respuesta_json['current_weather']['temperature']} {unidad_temperatura}")
    print()

    with open('logs_de_temperatura.log', 'a', encoding='utf-8') as logs:
        logging.info(f"Temperatura: {respuesta_json['current_weather']['temperature']} {unidad_temperatura}")

except Exception as e:
    print("Error al obtener la temperatura:", e)
    with open('logs_de_temperatura.log', 'a', encoding='utf-8') as logs:
        logging.error(f"Error al obtener la temperatura: {e}")
        
        
        
        