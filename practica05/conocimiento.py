# Base de Conocimiento Pedagógico

DIDACTIC_SUGGESTIONS = {
    "Error: El nombre de una variable no puede empezar con un número.": 
        "¡Buen intento! En Python, las variables son como etiquetas para guardar información. "
        "Una regla importante es que estas etiquetas no pueden comenzar con un número. "
        "Prueba con un nombre que empiece con una letra, como 'numero1' en lugar de '1numero'.",

    "Error: El nombre contiene caracteres no permitidos o es una palabra reservada.":
        "Parece que has usado un símbolo que no está permitido o una palabra que Python se reserva para sus propias instrucciones (como 'if', 'for', 'while'). "
        "Los nombres de variables solo pueden contener letras, números y guiones bajos (_). "
        "¡Inténtalo de nuevo con una combinación diferente!",

    "Error: Ambos argumentos deben ser números.":
        "¡Casi lo tienes! La operación que intentas hacer (como sumar o multiplicar) necesita números para funcionar. "
        "Asegúrate de que los valores que me pasas son numéricos. Por ejemplo: 'sumar 10 5'.",
    
    "Error: La suma requiere exactamente dos números separados por espacio.":
        "¡Estás cerca! Para realizar una suma, necesito que me des exactamente dos números, ni más ni menos, separados por un espacio. "
        "Por ejemplo, si quieres sumar 10 y 5, escribe: 'sumar 10 5'.",

    "Error: La multiplicación requiere exactamente dos números separados por espacio.":
        "¡Ya casi! Para poder multiplicar, es importante que me proporciones justo dos números, separados por un espacio. "
        "Por ejemplo, para multiplicar 7 por 3, el formato sería: 'multiplicar 7 3'."

}

def obtener_sugerencia(error_message):
    """
    Busca una sugerencia didáctica para un mensaje de error específico.
    """
    return DIDACTIC_SUGGESTIONS.get(error_message, 
                                   "Parece que algo no salió como esperábamos. Revisa bien el comando y tus argumentos.")
