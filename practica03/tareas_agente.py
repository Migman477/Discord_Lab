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


    lista_tareas.append(tarea)
    return f"Tarea agregada: {descripcion}"
