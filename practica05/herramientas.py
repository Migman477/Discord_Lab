import datetime

# Base de conocimiento para la herramienta de búsqueda.
# Se define a nivel de módulo para que otras funciones puedan acceder a ella.
_CONOCIMIENTO = {
    "if": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición.",
    "else": "Estructura de control que permite ejecutar un bloque de código si no se cumple una condición.",
    "elif": "Estructura de control que permite ejecutar un bloque de código si se cumple una condición adicional después de un if.",
    "for": "Estructura de control que permite ejecutar un bloque de código un número determinado de veces.",
    "while": "Estructura de control que permite ejecutar un bloque de código mientras se cumpla una condición.",
    "break": "Instrucción que permite salir de un bucle antes de que se cumpla la condición de finalización.",
    "continue": "Instrucción que permite saltar a la siguiente iteración de un bucle sin ejecutar el código restante en la iteración actual.",
    "def": "Palabra clave que se utiliza para definir una función en Python.",
    "return": "Palabra clave que se utiliza para devolver un valor desde una función.",
    "import": "Palabra clave que se utiliza para importar módulos en Python.",
    "class": "Palabra clave que se utiliza para definir una clase en Python.",
    "int": "Tipo de dato que representa números enteros.",
    "float": "Tipo de dato que representa números con decimales.",
    "str": "Tipo de dato que representa cadenas de caracteres.",
    "bool": "Tipo de dato que representa valores booleanos (verdadero o falso).",
    "list": "Tipo de dato que representa una lista de valores.",
    "tuple": "Tipo de dato que representa una tupla de valores.",
    "dict": "Tipo de dato que representa un diccionario de valores.",
    "set": "Tipo de dato que representa un conjunto de valores.",
    "print": "Función que se utiliza para mostrar información en la consola.",
    "input": "Función que se utiliza para recibir información del usuario a través de la consola.",
    "len": "Función que se utiliza para obtener la longitud de un objeto.",
    "type": "Función que se utiliza para obtener el tipo de un objeto.",
    "range": "Función que se utiliza para generar una secuencia de números.",
    "programacion estructurada": "Paradigma de programación que se basa en la división de un programa en bloques de código que realizan tareas específicas, utilizando estructuras de control y funciones para organizar el código de manera clara y eficiente.",
    "variable": "Espacio en memoria reservado para almacenar un valor que puede cambiar durante la ejecución del programa.",
    "operadores": "Símbolos que permiten realizar operaciones matemáticas, lógicas o de comparación entre valores.",
    "comentario": "Texto en el código que no se ejecuta y sirve para explicar el funcionamiento del programa.",
    "indentacion": "Espacios al inicio de una línea de código que definen la jerarquía y pertenencia a bloques de control en Python."
}

def mostrar_bienvenida():
    """Retorna un mensaje de bienvenida."""
    return (
        "📜 ¡Hola! Soy tu Agente Tutor de Python. 📜"

        "Puedes pedirme que resuelva problemas de programación estructurada."
        "Por ejemplo: !resolver 'Crea una variable valida con el nombre mi_variable'"
    )

def obtener_ayuda():
    """Devuelve una lista de las herramientas que el agente puede usar."""
    return ("Mis herramientas disponibles son:\n"
            "- definir <termino>**: Busco conceptos de Python.\n"
            "- validar <nombre_variable>**: Reviso si un nombre de variable es válido.\n"
            "- sumar <n1> <n2>**: Sumo dos números.\n"
            "- multiplicar <n1> <n2>**: Multiplico dos números.\n"
            "- hora**: Muestro la hora del sistema.\n"
            "- fecha**: Muestro la fecha y hora completa.\n"
            "- listar**: Muestro todos los términos que conozco.\n"
            "- descripcion <termino>**: Explico cómo usar los comandos de búsqueda.")

def ejecutar_suma(argumento):
    """
    Suma dos números.
    Devuelve un resultado o un mensaje de error.
    """
    try:
        nums = argumento.split(" ")
        if len(nums) != 2:
            return "Error: La suma requiere exactamente dos números separados por espacio."
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"Resultado: {n1} + {n2} = {n1 + n2}"
    except ValueError:
        return "Error: Ambos argumentos deben ser números."
    except Exception as e:
        return f"Error inesperado en suma: {e}"

def buscar_en_diccionario(termino):
    """Busca un término en la base de conocimiento."""
    if not termino: return "Error: Necesito un término para buscar."
    return _CONOCIMIENTO.get(termino.lower(), f"Error: El término '{termino}' no se encuentra.")

def validar_variable(nombre):
    """Valida si un nombre de variable sigue las reglas de Python."""
    if not nombre: return "Error: Indica el nombre de la variable a validar."
    if nombre[0].isdigit(): return "Error: El nombre de una variable no puede empezar con un número."
    if not nombre.isidentifier(): return "Error: El nombre contiene caracteres no permitidos o es una palabra reservada."
    return f"'{nombre}' es un nombre de variable válido."

def ejecutar_multiplicacion(argumento):
    """

    Multiplica dos números.
    Devuelve un resultado o un mensaje de error.
    """
    try:
        nums = argumento.split(" ")
        if len(nums) != 2:
            return "Error: La multiplicación requiere exactamente dos números separados por espacio."
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"Resultado: {n1} x {n2} = {n1 * n2}"
    except ValueError:
        return "Error: Ambos argumentos deben ser números."
    except Exception as e:
        return f"Error inesperado en multiplicación: {e}"

def obtener_hora():
    """Devuelve la hora actual."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def obtener_fecha_completa():
    """Devuelve la fecha y hora actual en formato completo."""
    ahora = datetime.datetime.now()
    return ahora.strftime("%A, %d de %B de %Y, %H:%M:%S")

def descripcion_comandos(termino: str) -> str:
    """
    Enseña la estructura y el funcionamiento de los comandos de búsqueda.
    """
    if not termino:
        return "Error: Necesito un término para darte una descripción de los comandos."
    
    return (
        f"Para buscar información sobre '{termino}', puedes usar los siguientes comandos:\n"
        "- `!definir <termino>`: Para buscar el término directamente en el diccionario.\n"
        "- `!listar`: Para listar todas las entradas disponibles en el diccionario.\n"
        "- `!ayuda`: Para obtener más información sobre cómo usar estos comandos."
    )

def listar() -> str:
    """
    Lista las posibles opciones seleccionables en el diccionario de conocimiento.
    """
    if not _CONOCIMIENTO:
        return "El diccionario de conocimiento está vacío."
    
    claves = ', '.join(sorted(_CONOCIMIENTO.keys()))
    return f"Las entradas disponibles en el diccionario son: {claves}."
