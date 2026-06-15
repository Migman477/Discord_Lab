import discord
import os
import re
from dotenv import load_dotenv
import datetime
from practica01.gestor_comandos import buscar_en_diccionario, validar_variable, analizar_comando





def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "\n"
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Esccriba !Exit para salir del Agente:"
        "📜 Escriba el termino para buscar en el diccionario:"
    )

def historial_comandos ():
    historial_comandos = []
    return historial_comandos


def ejecutar_suma(argumento):
    """
    Procesa la suma de dos números recibidos como texto.
    Demuestra la Unidad 2.2.3 (Tipos de datos simples).
    """
    try:
        nums = argumento.split(" ")
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"La suma de {n1} + {n2} es: {n1 + n2}"
    except:
        return "Uso correcto: '!sumar 10 5'"

def buscar_en_diccionario(termino):
    if not termino: return " ¿Qué término buscas?"
    
    conocimiento = {

        #CONCEPTOS DE ESTRUCTURA DE CONTROL
        "if": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición.",
        "else": "Estructura de control que permite ejecutar un bloque de código si no se cumple una condición.",
        "elif": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición adicional después de un if.",
        "for": "Estructura de control que permite ejecutar un bloque de código un número determinado de veces.",
        "while": "Estructura de control que permite ejecutar un bloque de código mientras se cumpla una condición.",
        "break": "Instrucción que permite salir de un bucle antes de que se cumpla la condición de finalización.",
        "continue": "Instrucción que permite saltar a la siguiente iteración de un bucle sin ejecutar el código restante en la iteración actual.",
        
        #CONCEPTOS DE FUNCIONES
        "def": "Palabra clave que se utiliza para definir una función en Python.",
        "return": "Palabra clave que se utiliza para devolver un valor desde una función.",
        "import": "Palabra clave que se utiliza para importar módulos en Python.",
        "class": "Palabra clave que se utiliza para definir una clase en Python.", 

        #Tipos de datos
        "int": "Tipo de dato que representa números enteros.",
        "float": "Tipo de dato que representa números con decimales.",
        "str": "Tipo de dato que representa cadenas de caracteres.",
        "bool": "Tipo de dato que representa valores booleanos (verdadero o falso).",
        "list": "Tipo de dato que representa una lista de valores.",
        "tuple": "Tipo de dato que representa una tupla de valores.",
        "dict": "Tipo de dato que representa un diccionario de valores.",
        "set": "Tipo de dato que representa un conjunto de valores.",

        #Operadores de sintaxis
        "print": "Función que se utiliza para mostrar información en la consola.",
        "input": "Función que se utiliza para recibir información del usuario a través de la consola.",
        "len": "Función que se utiliza para obtener la longitud de un objeto.",
        "type": "Función que se utiliza para obtener el tipo de un objeto.",
        "range": "Función que se utiliza para generar una secuencia de números.",

        #Conceptos de programacion estruturada
        "programacion estructurada": "Paradigma de programación que se basa en la división de un programa en bloques de código que realizan tareas específicas, utilizando estructuras de control y funciones para organizar el código de manera clara y eficiente."
        ,
        "variable": "Espacio en memoria reservado para almacenar un valor que puede cambiar durante la ejecución del programa.",
        "operadores": "Símbolos que permiten realizar operaciones matemáticas, lógicas o de comparación entre valores.",
        "comentario": "Texto en el código que no se ejecuta y sirve para explicar el funcionamiento del programa.",
        "indentacion": "Espacios al inicio de una línea de código que definen la jerarquía y pertenencia a bloques de control en Python."
        
    }

    return conocimiento.get(termino.lower(), f"El término '{termino}' no se encuentra en el diccionario.")

def validar_variable(nombre):
    if not nombre: return "Indica el nombre."
    if nombre[0].isdigit(): return "No puede empezar con número."
    if not nombre.isidentifier(): return "Caracteres no permitidos."
    return f"{nombre} es válido."


def ejecutar_multiplicacion(argumento):
    """
    Procesa la multiplicación de dos números recibidos como texto.
    """
    try:
        nums = argumento.split(" ")
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"La multiplicación de {n1} x {n2} es: {n1 * n2}"
    except:
        return "Uso correcto: '!multiplicar 10 5'"

# --- FUNCIÓN EXTRA: Fecha y hora completa ---
def obtener_fecha_completa():
    """
    Devuelve la fecha y hora actual en formato completo.
    """
    ahora = datetime.datetime.now()
    return ahora.strftime("%A, %d de %B de %Y, %H:%M:%S")

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
        
        if comando == "ayuda":
            return (" Comandos disponibles:\n"
                    "1. '!inicio' - Muestra la bienvenida.\n"
                    "2. '!ayuda' - Muestra esta ayuda.\n"
                    "3. '!exit' - Sale del agente.\n"
                    "4. '!definir <termino>' - Busca conceptos de Python.\n"
                    "5. '!validar <nombre>' - Revisa si un nombre de variable es válido.\n"
                    "6. '!hora' - Muestra la hora del sistema.\n"
                    "7. '!fecha' - Muestra la fecha y hora completa.\n"
                    "8. '!historial' - Muestra los últimos comandos ejecutados.\n"
                    "9. '!sumar <n1> <n2>' - Suma dos números.\n"
                    "10. '!multiplicar <n1> <n2>' - Multiplica dos números.")
        
        elif comando == "hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" La hora actual del servidor es: {ahora}"
        elif comando == "definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "validar":
            return validar_variable(argumento)
            
        elif comando == "hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" Hora actual: {ahora}"
        
        elif comando == "historial":
            # UNIDAD 3.2: Estructuras de repetición
            res = "Últimos comandos:\n"
            for i, cmd in enumerate(historial_comandos, 1):
                res += f"{i}. {cmd}\n"
            return res

        elif comando == "sumar":
            # UNIDAD 4.3: Parámetros de entrada
            return ejecutar_suma(argumento)
        
        elif comando == "fecha":
            return obtener_fecha_completa()
        
        elif comando == "multiplicar":
            return ejecutar_multiplicacion(argumento)
            
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)

def comandos(entrada):
    
        PREFIJO = "!"
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "ayuda":
            return (" Comandos disponibles:\n"
                    "1. '!inicio' - Muestra la bienvenida.\n"
                    "2. '!ayuda' - Muestra esta ayuda.\n"
                    "3. '!exit' - Sale del agente.\n"
                    "4. '!definir <termino>' - Busca conceptos de Python.\n"
                    "5. '!validar <nombre>' - Revisa si un nombre de variable es válido.\n"
                    "6. '!hora' - Muestra la hora del sistema.\n"
                    "7. '!fecha' - Muestra la fecha y hora completa.\n"
                    "8. '!historial' - Muestra los últimos comandos ejecutados.\n"
                    "9. '!sumar <n1> <n2>' - Suma dos números.\n"
                    "10. '!multiplicar <n1> <n2>' - Multiplica dos números.")
        elif comando == "hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" La hora actual del servidor es: {ahora}"
        elif comando == "definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "validar":
            return validar_variable(argumento)
            
        elif comando == "hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" Hora actual: {ahora}"
        
        elif comando == "historial":
            # UNIDAD 3.2: Estructuras de repetición
            res = "Últimos comandos:\n"
            for i, cmd in enumerate(historial_comandos, 1):
                res += f"{i}. {cmd}\n"
            return res

        elif comando == "sumar":
            # UNIDAD 4.3: Parámetros de entrada
            return ejecutar_suma(argumento)
        
        elif comando == "fecha":
            return obtener_fecha_completa()
        
        elif comando == "multiplicar":
            return ejecutar_multiplicacion(argumento)
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

    
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")