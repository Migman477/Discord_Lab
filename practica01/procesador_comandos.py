import datetime



def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """

    return f"Hola, soy {nombre_bot}. ¿En qué puedo ayudarte hoy?"

def procesar_comando_recordar(comando):
    """
    Valida y procesa la accion de recordar un dato
    """

    if not comando:
        return "Error: El comando no puede estar vacío."
    return f"Entendido, te recordaré: {comando}"



def calcular_uptime(hora_inicio):

    """
    Calcula el tiempo de actividad del agente
    """

    hora_actual = datetime.datetime.now()
    uptime = hora_actual - hora_inicio
    return f"Tiempo de actividad: {uptime}"

  
def mostrar_ayuda():
    """
    Muestra una lista de comandos disponibles
    """

    comandos_disponibles = [
        "!saludo - Muestra un saludo del bot",
        "!recordar [Nombre] - El bot recordara el nombre proporcionado",
        "!uptime - Muestra el tiempo de actividad del agente",
        "!ayuda - Muestra esta ayuda"
    ]
    return "Comandos disponibles:\n" + "\n".join(comandos_disponibles)


def iniciar_agente():
    #Funcion principal para iniciar el agente
    NOMBRE_BOT = "Lin"
    PREFIJO = "!"
    hora_inicio = datetime.datetime.now()
    
    print(obtener_saludo(NOMBRE_BOT))
    print("Escribe '!ayuda' para ver los comandos disponibles.")

    ejecutando = True
    while ejecutando:
        entrada =input(f"{NOMBRE_BOT}> : ").strip()

        if not entrada.startswith(PREFIJO):
            print("Error: Comando debe comenzar con '!'")
            continue

        partes = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
        elif comando == "recordar":
            print(procesar_comando_recordar(argumento))
        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        elif comando == "salir":
            print("¡Hasta luego!")
            ejecutando = False
        else:
            print(f"Comando desconocido: {comando}. Escribe '!ayuda' para ver los comandos disponibles.")



def main():
    iniciar_agente()

if __name__ == "__main__":
    main()