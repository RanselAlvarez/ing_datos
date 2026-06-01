import requests
import json
from datetime import datetime


url_base = "http://ipwho.is/"

parametros = {
            "ip": "",
            "lang": "es"
}


respuesta = requests.get(url_base, params=parametros, timeout=5)

respuesta_json = respuesta.json()
print(respuesta_json)

