import datetime

nombre_bot = "Lin"

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
    

def iniciar_agente():

def main():
    obtener_saludo(nombre_bot)
    procesar_comando_recordar("Recuérdame comprar leche")
    calcular_uptime(datetime.datetime.now())
    mostrar_ayuda()
    iniciar_agente()

if __name__ == "__main__":
    main()