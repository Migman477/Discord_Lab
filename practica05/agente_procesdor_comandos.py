import ast
import inspect
import importlib
import os
import sys
from pathlib import Path

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "\n"
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Esccriba !Exit para salir del Agente:"
        "📜 Escriba el termino para buscar en el diccionario:"
    )

def load_comandos_module():
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    return importlib.import_module("practica02.procesador_comandos")

def get_functions(module):
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__ == module.__name__ and not name.startswith("_")
    }

def parse_arguments(args):
    parsed = []
    for arg in args:
        try:
            parsed.append(ast.literal_eval(arg))
        except (ValueError, SyntaxError):
            parsed.append(arg)
    return parsed

def print_help(functions):
    print("Comandos disponibles:")
    print("  list                - Lista las funciones disponibles en procesador_comandos")
    print("  help                - Muestra esta ayuda")
    print("  exit                - Sale del procesador")
    print("  <funcion> [args...] - Llama a la funcion de procesador_comandos con argumentos opcionales")
    print("\nFunciones disponibles:")
    for name, func in sorted(functions.items()):
        signature = str(inspect.signature(func))
        print(f"  {name}{signature}")

def execute_command(functions, command, args):
    if command == "list":
        print("Funciones disponibles:")
        for name in sorted(functions):
            print(f"  {name}")
        return
    if command == "help":
        print_help(functions)
        return
    if command == "exit":
        sys.exit(0)
    if command not in functions:
        print(f"Funcion no encontrada: {command}")
        return
    func = functions[command]
    parsed_args = parse_arguments(args)
    try:
        result = func(*parsed_args)
        if result is not None:
            print(result)
    except Exception as err:
        print(f"Error al ejecutar {command}: {err}")

def main():
    try:
        module = load_comandos_module()
    except ModuleNotFoundError:
        print("No se encontro el modulo procesador_comandos. Asegurese de que la ruta sea correcta.")
        return
    
    functions = get_functions(module)
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]
        execute_command(functions, command, args)
        return

    print("Procesador de comandos cargado. Escriba 'help' para ver los comandos.")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        execute_command(functions, parts[0], parts[1:])

if __name__ == "__main__":
    main()
