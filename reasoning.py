import re
import difflib
from practica05 import herramientas as tools
from practica05 import conocimiento as knowledge

# --- CAPA DE DECISIÓN (El Agente) ---

# 1. Catálogo de Herramientas (Toolkit)
# El agente registra las funciones que puede usar.
TOOL_CATALOG = {
    "definir": tools.buscar_en_diccionario,
    "validar": tools.validar_variable,
    "sumar": tools.ejecutar_suma,
    "multiplicar": tools.ejecutar_multiplicacion,
    "hora": tools.obtener_hora,
    "fecha": tools.obtener_fecha_completa,
    "ayuda": tools.obtener_ayuda,
    "bienvenida": tools.mostrar_bienvenida,
    "descripcion": tools.descripcion_comandos,
    "listar": tools.listar,
}

# 2. Memoria de Estado
# Guarda el perfil de aprendizaje de cada usuario.
# Por ahora, es un simple diccionario en memoria.
user_states = {}

def get_user_state(user_id):
    """Obtiene o crea el estado para un usuario."""
    if user_id not in user_states:
        user_states[user_id] = {"history": [], "learning_profile": {}}
    return user_states[user_id]

def update_user_history(user_id, message):
    """Actualiza el historial de un usuario."""
    state = get_user_state(user_id)
    state["history"].append(message)

# 3. Bucle de Razonamiento (Reasoning Loop)
def run_reasoning_loop(user_id, user_input):
    """
    El núcleo del agente. Procesa la entrada del usuario y decide qué hacer.
    """
    update_user_history(user_id, user_input)
    
    # --- PASO 1: PENSAMIENTO (Thought) ---
    # El agente analiza la intención del usuario.
    # Usamos una expresión regular simple para extraer comando y argumento.
    match = re.match(r"^\s*!(\w+)\s*(.*)", user_input)
    
    if not match:
        if user_input.strip() == "!":
             return "Por favor, escribe un comando después del '!'. Escribe '!ayuda' para ver las opciones."
        return None # No es un comando para el bot

    tool_name = match.group(1).lower()
    argument = match.group(2).strip()

    # Manejo de comandos básicos sin argumentos
    if not argument and tool_name in ["ayuda", "bienvenida", "hora", "fecha", "listar"]:
         tool_function = TOOL_CATALOG.get(tool_name)
         return tool_function()

    if tool_name not in TOOL_CATALOG:
        # Sugerir el comando más cercano si no se encuentra
        posibles_coincidencias = difflib.get_close_matches(tool_name, TOOL_CATALOG.keys(), n=1, cutoff=0.6)
        sugerencia = ""
        if posibles_coincidencias:
            sugerencia = f" ¿Quisiste decir `!{posibles_coincidencias[0]}`?"
        return f"No reconozco la herramienta '{tool_name}'.{sugerencia} Escribe `!ayuda` para ver la lista de herramientas disponibles."

    # --- PASO 2: ACCIÓN (Action) ---
    # El agente invoca la herramienta seleccionada.
    print(f"Agente: [Usuario: {user_id}] -> Invocando herramienta '{tool_name}' con argumento '{argument}'")
    tool_function = TOOL_CATALOG[tool_name]
    observation = tool_function(argument)
    
    # --- PASO 3: OBSERVACIÓN (Observation) ---
    # El agente analiza el resultado de la herramienta.
    if observation.startswith("Error:"):
        print(f"Agente: [Usuario: {user_id}] -> Herramienta '{tool_name}' devolvió un error: {observation}")
        # Si hay un error, busca una sugerencia didáctica.
        suggestion = knowledge.obtener_sugerencia(observation.strip())
        
        # --- PASO 4: SALIDA (Output - Enriquecida) ---
        # El agente formula una respuesta final combinando el error y la sugerencia.
        final_response = (
            f"🤔 **Observación:** {observation}"
            f"💡 **Sugerencia:** {suggestion}"
        )
    else:
        # --- PASO 4: SALIDA (Output - Directa) ---
        # Si no hay error, la respuesta es el resultado directo de la herramienta.
        final_response = observation
        
    print(f"Agente: [Usuario: {user_id}] -> Respuesta final: {final_response}")
    return final_response
