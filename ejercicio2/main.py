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
url_base = "http://ipwho.is/8.8.8.8"

# Parametros de la API
parametros = {
            "fields": "ip,country,city",
            # "country": "",
            # "city": "",
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
    respuesta = requests.get(url_base,  timeout=5)
    
    # Verificando que la solicitud fue exitosa.
    respuesta.raise_for_status()

    # Transformamos la respuesta JSON en un diccionario
    respuesta_json = respuesta.json()


    # Imprimiendo la URL de la petición
    print(f"Url de la peticion: {respuesta.url}")
    print(f"Toda la info: {respuesta_json}")



    # Extraemos la información relevante
    # La IP, el país y la ciudad con get, si no se necuentra la informacion se devuelve un string por defecto
    ip = respuesta_json.get("ip", "IP Desconocido")
    pais = respuesta_json.get("country", "Pais Desconocido")
    ciudad = respuesta_json.get("city", "Ciiudad Desconocida")
    print(f"Tu ip es: {ip}")
    print(f"Pais: {pais}")
    print(f"Ciudad: {ciudad}")

    # Guardar la información en un CSV
    with open(ruta_archivo_csv, "a", newline="") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados_csv)
        
        if not ruta_archivo_csv.exists() or ruta_archivo_csv.stat().st_size == 0:
            escritor_csv.writeheader()
        
        escritor_csv.writerow({"Fecha": fecha, "IP": ip, "Pais": pais, "Ciudad": ciudad})
    
    # Aqui guandamos la informacion en el log (Mensaje exitoso)    
    logging.info("Se ha obtenido la información de la IP correctamente.")
# El orden de los Excepts es importante para que se capturen los errores en el orden correcto
except HTTPError as e:           
    # Aqui guardamos el error en el log (Mensaje de error)    
    logging.error(f"Error HTTP al obtener la información de la IP:{e}")                
except RequestException as e:
    # Aqui guardamos el error en el log (Mensaje de error)    
    logging.error(f"Error al obtener la información de la IP: {e}")
except Exception as e:            
    # Aquí guardamos el error en el log (e)
    logging.error(f"Error general al obtener la información de la IP: {e}")
                    
    