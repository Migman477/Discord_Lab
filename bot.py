import discord
import re
import numpy as np

# Importaciones absolutas desde la nueva estructura del proyecto
import reasoning
from reconocimiento_intenciones import NLPEngine

# Instanciamos el motor de NLP, que se entrena automáticamente al crearse
nlp_engine = NLPEngine()
# --- CAPA DE PERCEPCIÓN (DISCORD) ---

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

    # --- CAPA DE DECISIÓN ---
    # Si el mensaje es un comando, lo procesa el agente de herramientas.
    if user_input.startswith('!'):
        final_response = reasoning.run_reasoning_loop(user_id, user_input)
        if final_response:
            print(f"Actuando: [Usuario: {user_id}] -> Enviando respuesta.")
            await message.channel.send(final_response)
    # Si no es un comando, intenta usar el reconocimiento de lenguaje natural.
    else:
        # La lógica de predicción ahora está centralizada en el módulo de intenciones
        respuesta_bot = nlp_engine.predecir_intencion(user_input)
        await message.reply(respuesta_bot)