import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

# PASO 1: Configuración (se ejecuta una sola vez al iniciar)
# Buscamos dónde está este archivo para encontrar el .env
DIRECTORIO_ACTUAL = Path(__file__).parent
RUTA_ENV = DIRECTORIO_ACTUAL / ".env"

# Cargamos las contraseñas y correos del archivo .env
load_dotenv(dotenv_path=RUTA_ENV)

# 4. Leer las variables de forma segura
REMITENTE = os.getenv("EMAIL_REMITENTE")
CONTRASENA_APP = os.getenv("EMAIL_CONTRASENA")
DESTINATARIO = os.getenv("EMAIL_DESTINATARIO", REMITENTE) # Si no hay destinatario, usa el remitente

SERVIDOR_SMTP = "smtp.gmail.com"
PUERTO = 587


# PASO 2: La Función (La "receta" que podemos usar muchas veces)
def enviar_alerta(asunto, mensaje):
    """
    Esta función envía un correo. 
    Necesita que le pasemos dos cosas: el 'asunto' y el 'mensaje'.
    """
    
    # 2.1. Armamos el correo con los datos que nos pasaron
    email = EmailMessage()
    email['Subject'] = asunto       # Aquí ponemos el asunto que recibimos
    email['From'] = REMITENTE       # El remitente ya lo sabemos (viene del .env)
    email['To'] = DESTINATARIO      # El destinatario ya lo sabemos
    email.set_content(mensaje)      # Aquí ponemos el texto del mensaje que recibimos

    # 2.2. Intentamos enviarlo
    try:
        # Nos conectamos al servidor de correo
        with smtplib.SMTP(SERVIDOR_SMTP, PUERTO) as servidor:
            servidor.starttls() # Activamos la seguridad
            servidor.login(REMITENTE, CONTRASENA_APP) # type: ignore # Nos identificamos
            servidor.send_message(email) # ¡Enviamos!
        
        print("✅ Correo enviado correctamente")
        return True  # Le avisamos al programa principal que SÍ funcionó

    # 2.3. Si algo falla, lo atrapamos aquí
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
        return False # Le avisamos al programa principal que NO funcionó