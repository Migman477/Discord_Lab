from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import re

# ==============================================================================
# 1. BASE DE CONOCIMIENTOS (DATOS DE ENTRENAMIENTO Y RESPUESTAS)
# ==============================================================================

datos_entrenamiento = [
    # --- SALUDOS Y DESPEDIDAS ---
    ("hola", "saludo"), ("hola que tal", "saludo"), ("buenas", "saludo"), ("que tal", "saludo"), ("buenos dias", "saludo"),
    ("adios", "despedida"), ("chao", "despedida"), ("hasta luego", "despedida"), ("nos vemos", "despedida"),

    # --- CAPACIDADES DEL BOT ---
    ("que puedes hacer", "capacidades"), ("cuales son tus capacidades", "capacidades"), ("de que temas sabes", "capacidades"),
    ("que conceptos me puedes definir", "capacidades"), ("ayudame", "capacidades"),

    # --- CONCEPTOS DE PROGRAMACIÓN ---
    ("palabras reservadas", "palabras_reservadas"), ("que son las palabras reservadas", "palabras_reservadas"), ("dime las palabras reservadas", "palabras_reservadas"),
    ("identificador", "identificadores"),("identificadores", "identificadores"), ("que es un identificador", "identificadores"), ("como nombrar una variable", "identificadores"),
    ("datos simples", "datos_simples"), ("tipos de datos simples", "datos_simples"), ("que son los tipos de datos simples", "datos_simples"),
    ("datos compuestos", "datos_compuestos"), ("tipos de datos compuestos", "datos_compuestos"), ("que son los tipos de datos compuestos", "datos_compuestos"),
    ("lista", "datos_compuestos"), ("listas", "datos_compuestos"), ("que es una lista", "datos_compuestos"),
    ("variable", "variables_constantes"), ("variables", "variables_constantes"), ("constante", "variables_constantes"), ("que es variable", "variables_constantes"),("definicion de variable", "variables_constantes"), ("explicame que es una variable", "variables_constantes"), ("que es una variable", "variables_constantes"), ("que es una constante", "variables_constantes"), ("variables y constantes", "variables_constantes"), ("diferencia entre variable y constante", "variables_constantes"), ("que es una varible", "variables_constantes"),
    ("operadores aritmeticos", "operadores_aritmeticos"), ("que son los operadores aritmeticos", "operadores_aritmeticos"), ("cuales son los operadores aritmeticos", "operadores_aritmeticos"),
    ("operadores logicos", "operadores_logicos"), ("que son los operadores logicos", "operadores_logicos"), ("cuales son los operadores logicos", "operadores_logicos"),
    ("if", "sentencia_if"), ("sentencia if", "sentencia_if"), ("que es if", "sentencia_if"), ("estructura condicional if", "sentencia_if"),
    ("if then", "sentencia_if_then"), ("sentencia if then", "sentencia_if_then"), ("que es if then", "sentencia_if_then"),
    ("switch", "switch_case"), ("case", "switch_case"), ("switch case", "switch_case"), ("seleccion multiple switch case", "switch_case"), ("sentencia switch case", "switch_case"),

    # --- CICLOS / BUCLES ---
    ("for", "ciclo_for"),("ciclo for", "ciclo_for"), ("bucle for", "ciclo_for"), ("que es el ciclo for", "ciclo_for"), ("como funciona el ciclo for", "ciclo_for"),
    ("while", "ciclo_while"),("ciclo while", "ciclo_while"), ("bucle while", "ciclo_while"), ("que es el ciclo while", "ciclo_while"), ("estructura de control while", "ciclo_while"),
    ("do while", "ciclo_do_while"),("ciclo do while", "ciclo_do_while"), ("bucle do while", "ciclo_do_while"), ("que es el ciclo do while", "ciclo_do_while"), ("hacer mientras do while", "ciclo_do_while"),

    # --- PROCEDIMIENTOS Y FUNCIONES ---
    ("funciones", "def_funciones"), ("procedimientos", "def_funciones"), ("definicion de procedimientos y funciones", "def_funciones"), ("que es un procedimiento o funcion", "def_funciones"),
    ("diferencia funcion", "dif_proc_func"), ("diferencia procedimiento", "dif_proc_func"), ("diferencias entre procedimientos y funciones", "dif_proc_func"), ("diferencia funcion procedimiento", "dif_proc_func"),
    ("invocacion", "invocacion_funciones"), ("llamar funcion", "invocacion_funciones"), ("invocacion de procedimientos y funciones", "invocacion_funciones"), ("como llamar invocar una funcion", "invocacion_funciones"),
    ("parametro", "parametros_general"), ("parametros", "parametros_general"), ("que son los parametros en programacion", "parametros_general"),
    ("parametros de entrada", "parametros_entrada"), ("parametro de entrada", "parametros_entrada"), ("que es un parametro de entrada", "parametros_entrada"),
    ("parametros de salida", "parametros_output"), ("parametro de salida", "parametros_output"), ("que es un parametro de salida", "parametros_output"),
    ("funciones externas", "funciones_externas"), ("que son las funciones externas", "funciones_externas"),
    ("bibliotecas", "funciones_biblioteca"), ("librerias", "funciones_biblioteca"), ("procedimientos y funciones definidos en bibliotecas", "funciones_biblioteca"), ("librerias bibliotecas funciones", "funciones_biblioteca"),
    ("funciones de usuario", "funciones_usuario"), ("procedimientos y funciones definidas por el usuario", "funciones_usuario"), ("funciones creadas por el usuario", "funciones_usuario"),

    # --- ARREGLOS ---
    ("arreglos", "def_arreglos"), ("array", "def_arreglos"), ("definicion de arreglos", "def_arreglos"), ("que es un arreglo array", "def_arreglos"),
    ("declaracion de arreglos", "decl_arreglos"), ("como se declara un arreglo", "decl_arreglos"),
    ("vector", "vectores"), ("vectores", "vectores"), ("que es un vector", "vectores"), ("que es un vector unidimensional", "vectores"),
    ("matriz", "matrices"), ("matrices", "matrices"), ("que es una matriz", "matrices"), ("que es una matriz bidimensional", "matrices"),
    ("leer arreglos", "lectura_escritura_arreglos"), ("escribir arreglos", "lectura_escritura_arreglos"), ("lectura y escritura de arreglos", "lectura_escritura_arreglos"), ("leer escribir datos en un arreglo", "lectura_escritura_arreglos"),
    ("operaciones con arreglos", "operaciones_arreglos"), ("operaciones sobre arreglos", "operaciones_arreglos"), ("que operaciones se hacen con arreglos", "operaciones_arreglos")
]

respuestas = {
    # --- RESPUESTAS DE CONTROL ---
    "saludo": "¡Hola! Soy tu asistente de Fundamentos de Programación.  ¿De qué concepto te gustaría aprender hoy?",
    "despedida": "¡Hasta luego! Éxito con tus líneas de código. ¡Regresa pronto si tienes más dudas! ",
    "capacidades": "Puedo definirte conceptos básicos de programación como: variables, operadores, condicionales (if, switch), ciclos (for, while), funciones, arreglos (vectores, matrices) y más. ¡Solo pregunta!",

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


# ==============================================================================
# 2. MOTOR DE PROCESAMIENTO DE LENGUAJE NATURAL (NLP)
# ==============================================================================

class NLPEngine:
    """
    Clase que encapsula el entrenamiento y la predicción de intenciones.
    """
    def __init__(self):
        self.modelo = None
        self.vectorizador = None
        self._entrenar()

    def _entrenar(self):
        """
        Entrena el modelo de NLP con los datos definidos.
        """
        frases, etiquetas = zip(*datos_entrenamiento)
        self.vectorizador = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
        X_entrenamiento = self.vectorizador.fit_transform(frases)
        
        self.modelo = LogisticRegression()
        self.modelo.fit(X_entrenamiento, etiquetas)
        print(f"Modelo NLP entrenado. Total de intenciones: {len(respuestas)}")

    def predecir_intencion(self, user_input):
        """
        Toma la entrada del usuario y devuelve una respuesta formateada si
        la intención es reconocida con suficiente confianza.
        """
        # Limpieza del texto
        texto_limpio = re.sub(r'[^a-z0-9\s]', '', user_input.lower()).strip()

        if not texto_limpio:
            return (
                "**Lo siento, por el momento no sé o no tengo esa información.**"
                "Recuerda que estoy especializado en conceptos de fundamentos de programación (variables, ciclos, funciones, arreglos, etc.). "
                "También puedes usar comandos que empiezan con `!` (escribe `!ayuda` para verlos)."
            )

        # Predicción NLP
        X_usuario = self.vectorizador.transform([texto_limpio])
        probabilidades = self.modelo.predict_proba(X_usuario)[0]
        max_prob_idx = np.argmax(probabilidades)
        intencion_detectada = self.modelo.classes_[max_prob_idx]
        certeza = probabilidades[max_prob_idx]

        # Umbral de confianza
        if certeza > 0.1:  
            respuesta_bot = respuestas.get(intencion_detectada, "No encontré una respuesta para eso.")
            # Opcional: Mostrar la certeza solo en temas académicos
            if intencion_detectada in ["saludo", "despedida", "capacidades"]:
                return respuesta_bot
            else:
                return f"{respuesta_bot}*(Confianza: {certeza:.2%})*"
        else:
            return (
                "**Lo siento, por el momento no sé o no tengo esa información.**"
                "Recuerda que estoy especializado en conceptos de fundamentos de programación (variables, ciclos, funciones, arreglos, etc.). "
                "También puedes usar comandos que empiezan con `!` (escribe `!ayuda` para verlos)."
            )
