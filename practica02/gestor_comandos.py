

def analiar_comand0(entrada_usuario):
    """
    Analiza el comando ingresado por el usuario y devuelve el comando y su argumento
    """

    if not entrada_usuario.startswith("!"):
        return None, None

    partes = entrada_usuario[1:].split(maxsplit=1)
    comando = partes[0].lower()
    argumento = partes[1] if len(partes) > 1 else ""
    return comando, argumento

def buscar_en_diccionario(termino):

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
    
    if termino.lower() in conocimiento:
        return conocimiento[termino.lower()]
    else:
        return "Lo siento, no tengo información sobre ese término."
    

def validar_variable(nombre):
   
   """
   Valida si una variable comple con los estandares de la programacion estructurada
   """ 

   if not nombre:
         return "Error: El nombre de la variable no puede estar vacío."
   if not nombre[0].isalpha() and nombre[0] != "_":
         return "Error: El nombre de la variable debe comenzar con una letra o un guion bajo."
   if not all(c.isalnum() or c == "_" for c in nombre):
         return "Error: El nombre de la variable solo puede contener letras, números y guiones bajos."
   if  " " in nombre:
         return "Error: El nombre de la variable no puede contener espacios."
   
   return f"El nombre de la variable '{nombre}' es válido."