import requests
from requests.exceptions import RequestException, HTTPError
import json
from datetime import datetime
import logging
import csv
from pathlib import Path

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='API_ip_whois.log',
                    filemode='a',
                    encoding='utf-8',

)

# URL de la API
url_base = "http://ipwho.is/"

# Parametros de la API
parametros = {
            "fields": "ip,country,city",
            # "ip": "",
            # "lang": "es"
}

# Fecha actual del script
fecha = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


# PARA EL CSV
# Encabezado del archivo CSV
encabezados_csv = ["Fecha", "IP", "Pais", "Ciudad"]

# Path del archivo CSV
ruta_archivo_csv = Path(__file__).parent / "registro_api_whois.csv"



try:
    # Haciendo requests a la API
    respuesta = requests.get(url_base, params=parametros, timeout=5)
    # Comprobar codigo de estado
    codigo_estado = respuesta.status_code
    respuesta_json = respuesta.json()
    ip = respuesta_json.get("ip", "IP Desconocido")
    pais = respuesta_json.get("country", "Pais Desconocido")
    ciudad = respuesta_json.get("city", "Ciiudad Desconocida")
    print(f"Tu ip es: {ip}")
    print(f"Pais: {pais}")
    print(f"Ciudad: {ciudad}")
    with open(ruta_archivo_csv, "a", newline="") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados_csv)
        if not ruta_archivo_csv.exists() or ruta_archivo_csv.stat().st_size == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow({"Fecha": fecha, "IP": ip, "Pais": pais, "Ciudad": ciudad})
    logging.info("Se ha obtenido la información de la IP correctamente.")
except HTTPError as e:           
    logging.error(f"{e}")                
except requests.exceptions.RequestException as e:
    logging.error(f"Error al obtener la información de la IP: {e}")
except Exception as e:            
    logging.error(f"{e}")                
    