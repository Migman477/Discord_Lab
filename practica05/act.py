

def Descripción_comandos(término: str) -> str:
    """
    Función que recibe un término y devuelve una descripción de los comandos disponibles
    para buscar información en el diccionario.
    
    Parámetros:
    término (str): El término para el cual se desea obtener la descripción de los comandos.
    
    Retorna:
    str: Una descripción de los comandos disponibles para buscar información en el diccionario.
    """
    descripción = (
        f"Para buscar información sobre '{término}', puedes usar los siguientes comandos:\n"
        "- 'buscar': Para buscar el término directamente en el diccionario.\n"
        "- 'listar': Para listar todas las entradas disponibles en el diccionario.\n"
        "- 'ayuda': Para obtener más información sobre cómo usar estos comandos."
    )
    return descripción

def listar(diccionario: dict) -> str:
    """
    Función que recibe un diccionario y devuelve una lista de sus claves como un string.
    
    Parámetros:
    diccionario (dict): El diccionario del cual se desea listar las claves.
    
    Retorna:
    str: Una lista de las claves del diccionario, separadas por comas.
    """
    claves = ', '.join(diccionario.keys())
    return f"Las entradas disponibles en el diccionario son: {claves}."