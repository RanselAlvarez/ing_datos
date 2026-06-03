import requests
import json
from datetime import datetime


url_base = "http://ipwho.is/"

parametros = {
            "fields": "ip,country,city",
            # "ip": "",
            # "lang": "es"
}


respuesta = requests.get(url_base, params=parametros, timeout=5)

respuesta_json = respuesta.json()
ip = respuesta_json.get("ip", "IP Desconocido")
pais = respuesta_json.get("country", "Pais Desconocido")
ciudad = respuesta_json.get("city", "Ciiudad Desconocida")

print(f"Tu ip es: {ip}")
print(f"Pais: {pais}")
print(f"Ciudad: {ciudad}")


