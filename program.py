import sys
import os
import tp3

LECTURA = 'r'
PREFIX = "resultado_"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
AUTO_TEST = "auto"
EXECUTE = "exec"
AUTO_TEST_LINEAL = "auto_lineal"
EXECUTE_LINEAL = "exec_lineal"
EXECUTE_GREEDY = "exec_greedy"
EXEC_LINEALC = "exec_linealc"
CLOSE = "close\n"

def read_data_file(file):
    subconjuntos = []
    a = set()
    with open(file) as origen:
        for linea in origen:
            datos = linea.strip("\n").split(",")
            nuevo_subconjunto = set()
            nuevo_subconjunto.update(datos)
            a.update(datos)
            subconjuntos.append(nuevo_subconjunto)
    return subconjuntos, a

def _auto_test_volumn(test_files_path, solutions, function):
    for file in os.listdir(test_files_path):
        solution = solutions.get(file, None)
        subsets, a = read_data_file(os.path.join(test_files_path, file))
        result = function(subsets, a)
        if(len(result) != solution):
            print(RED, f"Ha ocurrido un error con el algoritmo ! En el archivo: {file}")
            print(f"El resultado del algoritmo fue: {len(result)} y se esperaba {solution}", RESET)
            break

        print(GREEN, "TODO OK", RESET, end="\n\n")
        print(f"El obtenido fue conseguido fue: {len(result)}")
        print("La secuencia de jugadores es: ")
        print(result)     
    return

def read_solutions(file):
    solutions = {}
    with open(file) as origen:
        for linea in origen:
            datos = linea.strip("\n").split(":")
            solutions[datos[0]] = int(datos[1])
    return solutions

def auto_test_backtracking(files: list):
    if not os.path.exists(files[0]) or not os.path.exists(files[1]):
        print("Some path is not available")
        return
    _auto_test_volumn(files[0], read_solutions(files[1]), tp3.search_for_min_hitting_set)
    return

def auto_test_lineal_programming(files: list):
    if not os.path.exists(files[0]) or not os.path.exists(files[1]):
        print("Some path is not available")
        return 
    _auto_test_volumn(files[0], read_solutions(files[1]), tp3.search_hs_linealp)
    return

def execute_algorithm(files: list, function):
    subsets, a = read_data_file(files[0])
    print(function(subsets, a))
    return 

def execute_backtracking(file_name: list):
    return execute_algorithm(file_name, tp3.search_for_min_hitting_set)

def execute_lineal_programming(file_name: list):
    return execute_algorithm(file_name, tp3.search_hs_linealp)

def execute_continous_lineal_programming(file_name: list):
    return execute_algorithm(file_name, tp3.aprox_hs_by_contlp)

def execute_greedy(file_name: list):
    return execute_algorithm(file_name, tp3.aprox_hs_by_greedy)

def show_input_error():
    print("No has pasado los parametros solicitados")

def prepare_data(data):
    file_two = None
    split_data = data.split(" ")
    file_one = split_data[0]
    if len(split_data) == 2:
        file_two = split_data[1]
    return file_one, file_two

MAP = {
    AUTO_TEST: auto_test_backtracking, 
    AUTO_TEST_LINEAL: auto_test_lineal_programming,
    EXECUTE: execute_backtracking,
    EXECUTE_LINEAL: execute_lineal_programming, 
    EXECUTE_GREEDY: execute_greedy,
    EXEC_LINEALC: execute_continous_lineal_programming
}

def program_execution():
    try:
        for line in sys.stdin:
            if line == CLOSE:
                print("Bye bye")
                break
            data = line.strip("\n").split(" ")
            command = data[0]
            MAP.get(command, show_input_error)(data[1:])
    except Exception as e:
        print(f"An error occurred: {str(e)}")



    


        