import requests
import logging
import json
import csv
from datetime import datetime
from pathlib import Path



logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='app.log',
        filemode='a',
        encoding='utf-8'
)

# Guardamos la fecha en que se ejecuta el script con la hora
fecha = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


# Datos para requests
url_base = "https://api.open-meteo.com/v1/forecast"

# Parametros para la petición HTTP GET a la API de OpenMeteo
params = {
        "latitude": 23.1136,
        "longitude": -82.3667,
        "current_weather": True,
}

# Encabezado del archivo CSV
encabezados = ["fecha", "temperatura", "unidad"]


try:
    # Peticion a la API de OpenMeteo para obtener datos del clima
    respuesta = requests.get(url_base, params=params, timeout=5)

    # Revisamos que codigo de estado devuelve la API
    status_code = respuesta.status_code
    print(status_code)
    print()

    # Imprimimos los datos obtenidos en formato texto(sin el .text imprime la respuesta en codigo HTML)
    # print(respuesta.text)

    # Convertimos la respuesta en JSON
    respuesta_json = respuesta.json()
    for clave, valor in respuesta_json.items():
        print(f"{clave}: {valor}")


    temperatura = respuesta_json["current_weather"]["temperature"]
    celsius = respuesta_json["current_weather_units"]["temperature"]

    # nivel = '[INFO]'
    
    archivo_csv = Path(__file__).parent / "datos_temperatura.csv"

    
    
    with open(archivo_csv, 'a', newline="", encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        
        if not archivo_csv.exists() or archivo_csv.stat().st_size == 0:
            escritor.writeheader()
        
        escritor.writerow({"fecha": fecha, "temperatura": temperatura, "unidad": celsius})    
        
        
        logging.info(f"Temperatura: {temperatura} {celsius}")
        # archivo.write(f"{nivel}  -- {fecha} -- Temperatura: {temperatura} {celsius}\n")

    print(f"{temperatura} {celsius}")


except Exception as e:
    # nivel = '[ERROR]'
    logging.error(f"Error al obtener la temperatura: {e}")
    # with open('app.log', 'a') as archivo:
        # archivo.write(f"{nivel} -- {fecha} -- Error al obtener la temperatura: {e}\n")