import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una tarea a la lista de tareas si cumple con los requisitos.
    """
    if  len(descripcion) > 3:
        return "Error: La descripción de la tarea debe tener más de 3 caracteres."
    
    #crear formato para tarea

    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nueva_tarea = f"{descripcion} (Agregada el {fecha})"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):

    """
    Devuelve una lista de tareas formateada o un mensaje si no hay tareas.
    """

    if not lista_tareas:
        return "No hay tareas en la lista."
    #agrer una variable llamada resultado
    resultado = "\n"

    # iterar sobre la lista de tareas y agregar cada tarea al resultado con un formato numerado

    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return f"Tareas actuales:\n{resultado}"

def elminar_tarea(lista_tareas, indice):
    """
    Elimina una tarea de la lista por su indice si es valido.
    """
    indice = int(indice)

    if not indice.isdigit():
        return "Error: El indice debe ser un numero."

    if indice < 1 or indice > len(lista_tareas):
        
        tarea_eliminada = lista_tareas.pop(indice - 1)
        return f"Tarea eliminada: {tarea_eliminada}"
    
    else:
        return "Error: Indice fuera de rango."


def main ():
    lista_tareas = []

    Prefijo = "!"
    print("-----Bienvenido al gestor de tareas-----")
    activa = True

    while activa:
        entrada= input(">>>"). strip()
        if not entrada.startswith(prefijo):
            print("error:comndo no reconocido")
            continue
        #procediiento de la entrada
        cuerpo= entrada[len(prefijo):].split(maxsplit=1)
        comando= cuerpo[0].lower()
        argumento= cuerpo[1] if len(cuerpo)> 1 else ""

        #seleccion d accion
        if comando=="add":
            resultado=agregar_tarea(tareas, argumento)
            print
