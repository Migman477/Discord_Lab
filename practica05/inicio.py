import discord
import os
from dotenv import load_dotenv
from practica05 import agente

# --- CAPA DE PERCEPCIÓN (DISCORD) ---

# 1. Configuración del entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Configuración de los permisos (Intents) de Discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Se ejecuta cuando el bot se conecta a Discord."""
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    """
    Se ejecuta cada vez que se recibe un mensaje en cualquier canal.
    """
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return

    # Extraer la intención del usuario (ID y contenido del mensaje)
    user_id = message.author.id
    user_input = message.content
    
    print(f"Percibido: [Usuario: {user_id}] -> Mensaje: '{user_input}'")

    # Pasar la intención a la Capa de Decisión (el Agente)
    if user_input.startswith('!'):
        # El agente procesa la entrada y devuelve una respuesta final
        final_response = agente.run_reasoning_loop(user_id, user_input)
        
        # Si el agente genera una respuesta, la capa de percepción actúa
        if final_response:
            print(f"Actuando: [Usuario: {user_id}] -> Enviando respuesta.")
            # La capa de actuación se limita a enviar el mensaje formateado por el agente
            await message.channel.send(final_response)

# --- Punto de entrada ---
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN de Discord en el archivo .env")