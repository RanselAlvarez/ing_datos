import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv


def enviar_alerta(asunto: str, mensjae: str) -> bool:
        """
    Envía un correo con el asunto y mensaje proporcionados.
    Retorna True si se envió correctamente, False si hubo error.
    """
    
    