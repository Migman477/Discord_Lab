import discord
from discord.ext import commands
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# ==============================================================================
# 1. BASE DE CONOCIMIENTOS Y ENTRENAMIENTO NLP
# ==============================================================================

datos_entrenamiento = [
    # --- SALUDOS Y DESPEDIDAS ---
    ("hola", "saludo"), ("buenas", "saludo"), ("que tal", "saludo"), ("buenos dias", "saludo"),
    ("adios", "despedida"), ("chao", "despedida"), ("hasta luego", "despedida"), ("nos vemos", "despedida"),

    # --- CONCEPTOS DE PROGRAMACIÓN ---
    ("palabras reservadas", "palabras_reservadas"), ("que son las palabras reservadas", "palabras_reservadas"),
    ("identificadores", "identificadores"), ("como nombrar una variable identificador", "identificadores"),
    ("tipos de datos simples", "datos_simples"), ("enteros flotantes booleanos datos simples", "datos_simples"),
    ("tipos de datos compuestos", "datos_compuestos"), ("listas arrays estructuras compuestos", "datos_compuestos"),
    ("variables y constantes", "variables_constantes"), ("diferencia entre variable y constante", "variables_constantes"),
    ("operadores aritmeticos", "operadores_aritmeticos"), ("suma resta multiplicacion division", "operadores_aritmeticos"),
    ("operadores logicos", "operadores_logicos"), ("and or not operadores logicos", "operadores_logicos"),
    ("sentencia if", "sentencia_if"), ("estructura condicional if", "sentencia_if"),
    ("sentencia if then", "sentencia_if_then"), ("condicional si entonces if then", "sentencia_if_then"),
    ("seleccion multiple switch case", "switch_case"), ("sentencia switch case", "switch_case"),

    # --- CICLOS / BUCLES ---
    ("ciclo for", "ciclo_for"), ("bucle for", "ciclo_for"), ("como funciona el ciclo for", "ciclo_for"),
    ("ciclo while", "ciclo_while"), ("bucle while", "ciclo_while"), ("estructura de control while", "ciclo_while"),
    ("ciclo do while", "ciclo_do_while"), ("bucle do while", "ciclo_do_while"), ("hacer mientras do while", "ciclo_do_while"),

    # --- PROCEDIMIENTOS Y FUNCIONES ---
    ("definicion de procedimientos y funciones", "def_funciones"), ("que es un procedimiento o funcion", "def_funciones"),
    ("diferencias entre procedimientos y funciones", "dif_proc_func"), ("diferencia funcion procedimiento", "dif_proc_func"),
    ("invocacion de procedimientos y funciones", "invocacion_funciones"), ("como llamar invocar una funcion", "invocacion_funciones"),
    ("parametros", "parametros_general"), ("que son los parametros en programacion", "parametros_general"),
    ("parametros de entrada", "parametros_entrada"), ("que es un parametro de entrada", "parametros_entrada"),
    ("parametros de salida", "parametros_output"), ("que es un parametro de salida", "parametros_output"),
    ("funciones externas", "funciones_externas"), ("que son las funciones externas", "funciones_externas"),
    ("procedimientos y funciones definidos en bibliotecas", "funciones_biblioteca"), ("librerias bibliotecas funciones", "funciones_biblioteca"),
    ("procedimientos y funciones definidas por el usuario", "funciones_usuario"), ("funciones creadas por el usuario", "funciones_usuario"),

    # --- ARREGLOS ---
    ("definicion de arreglos", "def_arreglos"), ("que es un arreglo array", "def_arreglos"),
    ("declaracion de arreglos", "decl_arreglos"), ("como se declara un arreglo", "decl_arreglos"),
    ("vectores", "vectores"), ("que es un vector unidimensional", "vectores"),
    ("matrices", "matrices"), ("que es una matriz bidimensional", "matrices"),
    ("lectura y escritura de arreglos", "lectura_escritura_arreglos"), ("leer escribir datos en un arreglo", "lectura_escritura_arreglos"),
    ("operaciones sobre arreglos", "operaciones_arreglos"), ("que operaciones se hacen con arreglos", "operaciones_arreglos")
]

respuestas = {
    # --- RESPUESTAS DE CONTROL ---
    "saludo": "¡Hola! Soy tu asistente de Fundamentos de Programación.  ¿De qué concepto te gustaría aprender hoy?",
    "despedida": "¡Hasta luego! Éxito con tus líneas de código. ¡Regresa pronto si tienes más dudas! ",

    # --- CONCEPTOS DE PROGRAMACIÓN ---
    "palabras_reservadas": " **Palabras reservadas:** Son términos internos del lenguaje (como `if`, `while`) que no puedes usar para nombrar tus variables.",
    "identificadores": " **Identificadores:** Son los nombres que asignas a variables, funciones o clases bajo ciertas reglas léxicas.",
    "datos_simples": " **Tipos de datos simples:** Valores atómicos básicos: enteros (`int`), reales/flotantes (`float`), booleanos (`bool`) y caracteres (`char`).",
    "datos_compuestos": " **Tipos de datos compuestos:** Estructuras complejas que agrupan datos, como strings, listas o registros.",
    "variables_constantes": " **Variables y Constantes:** Las variables cambian su valor en el tiempo; las constantes mantienen un valor fijo inmutable.",
    "operadores_aritmeticos": " **Operadores aritméticos:** Símbolos para operaciones matemáticas básicas (`+`, `-`, `*`, `/`, `%`).",
    "operadores_logicos": " **Operadores lógicos:** Conectores booleanos (`AND`, `OR`, `NOT`) para evaluar múltiples condiciones juntas.",
    "sentencia_if": " **Sentencia IF:** Estructura condicional que ejecuta un bloque de código **si** la condición evaluada es verdadera.",
    "sentencia_if_then": "↪ **Sentencia IF/THEN:** Representación clásica de 'Si ocurre X, Entonces haz Y'. En muchos lenguajes modernos el 'Then' es implícito.",
    "switch_case": " **SWITCH/CASE:** Control de selección múltiple que evalúa una variable contra una lista de casos permitidos de forma limpia.",

    # --- CICLOS ---
    "ciclo_for": " **Ciclo FOR:** Estructura iterativa que se utiliza cuando sabemos de antemano el número exacto de veces que queremos repetir un bloque de código.",
    "ciclo_while": " **Ciclo WHILE:** Ejecuta un bloque de código repetidamente **mientras** una condición sea verdadera. Evalúa la condición al inicio.",
    "ciclo_do_while": " **Ciclo DO WHILE:** Ejecuta el bloque de código **al menos una vez**, ya que evalúa la condición de repetición al final de la iteración.",

    # --- FUNCIONES ---
    "def_funciones": " **Procedimientos y Funciones:** Bloques de código reutilizables diseñados para realizar una tarea específica, permitiendo modularizar el programa.",
    "dif_proc_func": " **Diferencia entre Procedimientos y Funciones:** Una **Función** realiza un cálculo y **siempre devuelve un valor** (`return`). Un **Procedimiento** ejecuta instrucciones pero **no devuelve ningún valor**.",
    "invocacion_funciones": " **Invocación:** Significa 'llamar' o activar una función escribiendo su nombre seguido de paréntesis y pasándole los argumentos necesarios.",
    "parametros_general": " **Parámetros:** Variables locales declaradas en la definición de una función para recibir los datos desde el exterior.",
    "parametros_entrada": " **Parámetros de entrada:** Datos que la función recibe para trabajar; sus modificaciones no alteran las variables externas (paso por valor).",
    "parametros_output": " **Parámetros de salida:** Permiten a una función modificar variables externas directamente y devolver resultados a través de ellas (paso por referencia).",
    "funciones_externas": " **Funciones Externas:** Funciones que pertenecen a otros módulos o archivos del sistema y se importan al código actual.",
    "funciones_biblioteca": " **Funciones de Biblioteca:** Funciones prefabricadas que ya vienen incluidas en el lenguaje (ej: `math.sqrt()` o `print()`).",
    "funciones_usuario": " **Funciones del usuario:** Funciones personalizadas que tú diseñas y programas desde cero para cubrir una necesidad específica.",

    # --- ARREGLOS ---
    "def_arreglos": " **Definición de Arreglos (Arrays):** Estructura homogénea que almacena una colección de elementos del mismo tipo en posiciones de memoria continuas.",
    "decl_arreglos": " **Declaración de Arreglos:** Instrucción donde indicamos al compilador el nombre del arreglo, tipo de datos y su tamaño máximo.",
    "vectores": " **Vectores:** Arreglos **unidimensionales** (una sola fila). Se accede a sus elementos mediante un único índice: `vector[i]`.",
    "matrices": " **Matrices:** Arreglos **bidimensionales** (filas y columnas). Requieren dos índices para acceder a un dato: `matriz[f][c]`.",
    "lectura_escritura_arreglos": " **Lectura/Escritura:** Proceso de ingresar o mostrar valores de un arreglo, generalmente usando bucles que recorren sus posiciones secuencialmente.",
    "operaciones_arreglos": " **Operaciones:** Acciones estándar sobre arrays como: Búsqueda de elementos, Ordenamiento, Inserción, Eliminación o Modificación."
}

# --- ENTRENAMIENTO DEL MODELO ---
frases, etiquetas = zip(*datos_entrenamiento)
vectorizador = TfidfVectorizer(ngram_range=(1, 4), lowercase=True)
X_entrenamiento = vectorizador.fit_transform(frases)

modelo = LogisticRegression()
modelo.fit(X_entrenamiento, etiquetas)
print(f" Modelo académico entrenado. Total de intenciones: {len(respuestas)}")

# ==============================================================================
# 2. CONFIGURACIÓN DEL BOT DE DISCORD
# ==============================================================================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f" Bot de Fundamentos listo y activo como: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Limpieza del texto
    texto_usuario = message.content.lower().replace("/", " ").replace("-", " ").strip()

    # Predicción NLP
    X_usuario = vectorizador.transform([texto_usuario])
    probabilidades = modelo.predict_proba(X_usuario)[0]
    max_prob_idx = np.argmax(probabilidades)
    intencion_detectada = modelo.classes_[max_prob_idx]
    certeza = probabilidades[max_prob_idx]

    # Umbral de confianza
    if certeza > 0.38:  
        respuesta_bot = respuestas[intencion_detectada]
        # Opcional: Mostrar la certeza solo en temas académicos, no en saludos/despedidas
        if intencion_detectada in ["saludo", "despedida"]:
            await message.reply(respuesta_bot)
        else:
            await message.reply(f"{respuesta_bot}\n\n*(Confianza: {certeza:.2%})*")
    else:
        # RESPUESTA POR DEFECTO SI NO ENTIENDE LA INTENCIÓN
        await message.reply(
            " **Lo siento, por el momento no sé o no tengo esa información.**\n"
            "Recuerda que estoy especializado en conceptos de fundamentos de programación (variables, ciclos, funciones, arreglos, etc.). "
            "¿Podrías intentar reformular tu pregunta?"
        )

    await bot.process_commands(message)

bot.run('TU_BOT_TOKEN_AQUI')