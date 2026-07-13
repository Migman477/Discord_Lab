import os
from dotenv import load_dotenv

from bot import client

def main():
    """Punto de entrada principal para ejecutar el bot."""
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN de Discord en el archivo .env")

if __name__ == "__main__":
    main()