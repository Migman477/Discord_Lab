import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del agente: Procesamiento de comandos y lógica dinamica.
    Aquí el alumno aprende a separar la 'accion' de los 'datos'.
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulacion de comandos prefijados
    if mensaje.startswith("!recordar"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else ""
        
        # Logica de comando
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        elif comando == "!validar":
            return validar_variable(argumento)
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidro es: {ahora}"
        elif comando == "!ayuda":
            return (" **Comandos disponibles:**\n"
                    "1. !definir [termino] - Busca la definición de una palabra.\n"
                    "2. !validar [nombre] - Valida el valor de una variable.\n"
                    "3. !hora - Muestra la hora actual del servidor.\n")


def buscar_en_diccionario(argumento):


    if not argumento:
        return "Por favor, proporciona un término para definir."

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
    return conocimiento.get(argumento, "Lo siento, no tengo información sobre ese término.")


def validar_variable(nombre):

    if not nombre:
        return "Por favor, proporciona un nombre de variable para validar. Eh: !validar mi_variable"
    
    if nombre [0].isdigit():
        return "El nombre de la variable no puede comenzar con un número."
    
    if " " in nombre:
        return "El nombre de la variable no puede contener espacios."
    
    if not nombre.isidentifier():
        return "El nombre de la variable contiene caracteres no válidos."
    
    return f"La variable '{nombre}' es válida."

def main():
    print("Bienvenido al gestor de comandos. Escribe '!ayuda' para ver los comandos disponibles.")
    entrada =input(f"BOT> : ").strip()
    analizar_comando(entrada)

if __name__ == "__main__":
    main()

