import discord
import os
import re
from dotenv import load_dotenv

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "\n"
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Esccriba !Exit para salir del Agente:"
    )

def main(entrada):
    
        PREFIJO = "!"
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."
                        
        elif comando == "inicio":
            print(mostrar_bienvenida())
            return mostrar_bienvenida()
            
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")

import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del Agente: Procesamiento de comandos y lógica dinámica.    
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulación de comandos prefijados (como se usan en Discord: !ayuda, !ejemplo)
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None
        
        # Lógica de Comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
            
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" La hora actual del servidor es: {ahora}"
            
        elif comando == "!ayuda":
            return (" Comandos disponibles:\n"
                    "1. '!definir <termino>' - Busca conceptos de Python.\n"
                    "2. '!validar <nombre>' - Revisa si un nombre de variable es válido.\n"
                    "3. '!hora' - Muestra la hora del sistema.")
        
        else:
            return f" El comando '{comando}' no existe. Usa '!ayuda'."
            
    return " Recuerda usar el prefijo '!' para darme órdenes, o pregunta algo directamente."

def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir qué término quieres definir. Ej: '!definir list'"
    
    # Base de datos simplificada (puedes reutilizar la de la práctica anterior)
    conocimiento = {
        "variable": "Un espacio en memoria para almacenar datos.",
        "lista": "Colección mutable de elementos.",
        "tupla": "Colección inmutable de elementos (no se puede cambiar)."
    }
    return conocimiento.get(termino, f" No encontré '{termino}' en mi base de datos.")

def validar_variable(nombre):
    """
    Lógica pedagógica: Enseña a los alumnos las reglas de nombrado en Python.
    """
    if not nombre:
        return " Indica el nombre a validar. Ej: `!validar mi_variable`"
    
    # Reglas básicas de Python
    if nombre[0].isdigit():
        return f" '{nombre}' no es válido: ¡No puede empezar con un número!"
    if " " in nombre:
        return f" '{nombre}' no es válido: No puede contener espacios."
    if not nombre.isidentifier():
        return f" '{nombre}' contiene caracteres no permitidos (solo letras, números y _)."
        
    return f" '{nombre}' es un nombre de variable válido en Python."

# --- Simulación de ejecución ---
if __name__ == "__main__":
    print("--- Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")
    
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
        
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")