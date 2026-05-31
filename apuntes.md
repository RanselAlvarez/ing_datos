### ***Request***

*import requests*

*import json*

respuesta= requests.get(url_base, params=params, timeout=5)*

- La url a la que va a hacer la peticion, los parametros, timeout es el tiempo que va a esperar la peticion sin respuesta(si no se define puede quedarse colgado el script)

***Parametros para la petición HTTP GET a la API de OpenMeteo***

*params= {*

 *"latitude": 23.1136,*

 *"longitude": -82.3667,*

 *"current_weather": True,*

*}*

- ***Convertimos la respuesta de la API a json para poder trabajar con diccionarios***

*respuesta_json=respuesta.json()*

---------------------------------------------------------------------------------------------------------------------------------------

***Obtener la fecha y hora en el momento que se ejecute el script.***

*from datetime import datetime*

*fecha=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")*


***Revisamos que codigo de estado devuelve la API***

   *status_code=respuesta.status_code*

 *print(status_code)*



#### *Encabezado del archivo CSV*

*encabezados= ["fecha", "temperatura", "unidad"]*


#### Trabajando con archivo CSV, se crea el escritor y se escribe solo una vez los encabezados.

 *withopen(archivo_csv, 'a', newline="", encoding='utf-8')asarchivo:*

 *escritor= csv.DictWriter(archivo, fieldnames=encabezados)*

 *if not archivo_csv.exists()orarchivo_csv.stat().st_size==0:*

 *escritor.writeheader()*

 *escritor.writerow({"fecha": fecha, "temperatura": temperatura, "unidad": celsius})*
