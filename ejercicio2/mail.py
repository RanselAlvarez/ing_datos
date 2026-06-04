import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

# 1. Encontrar la carpeta donde vive este script
DIRECTORIO_ACTUAL = Path(__file__).parent

# 2. Apuntar al archivo .env que está en esa misma carpeta
RUTA_ENV = DIRECTORIO_ACTUAL / ".env"

# 3. Cargar las variables en memoria
load_dotenv(dotenv_path=RUTA_ENV)

# 4. Leer las variables de forma segura
REMITENTE = os.getenv("EMAIL_REMITENTE")
CONTRASENA_APP = os.getenv("EMAIL_CONTRASENA")
DESTINATARIO = os.getenv("EMAIL_DESTINATARIO", REMITENTE) # Si no hay destinatario, usa el remitente

# Configuración del servidor (Cartero)
SERVIDOR_SMTP = "smtp.gmail.com"
PUERTO = 587  # Puerto estándar para conexiones seguras (TLS)


# 1. Creamos el objeto mensaje
mensaje = EmailMessage()

# 2. Le asignamos los campos básicos
mensaje['Subject'] = "🚨 Prueba de Alerta desde Python"
mensaje['From'] = REMITENTE
mensaje['To'] = DESTINATARIO

# 3. Le asignamos el contenido (puede ser texto plano o HTML)
mensaje.set_content("¡Hola! Este es un mensaje de prueba enviado automáticamente desde mi script de ingeniería de datos.")


try:
    # 1. Nos conectamos al servidor y al puerto
    with smtplib.SMTP(SERVIDOR_SMTP, PUERTO) as servidor:
        
        # 2. Iniciamos la seguridad (encripta la conexión)
        servidor.starttls()
        
        # 3. Nos identificamos (¡Ojo! Aquí va tu contraseña de APP, no la normal)
        servidor.login(REMITENTE, CONTRASENA_APP)
        
        # 4. Enviamos el mensaje
        servidor.send_message(mensaje)
        
    print("✅ ¡Correo enviado con éxito!")

except Exception as e:
    print(f"❌ Error al enviar el correo: {e}")