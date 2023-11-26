import sys
import os
import tp3
import time

LECTURA = 'r'
PREFIX = "resultado_"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
AUTO_TEST = "auto"
EXECUTE = "exec"
AUTO_TEST_LINEAL = "auto_lineal"
EXECUTE_LINEAL = "exec_lineal"
AUTO_TEST_GREEDY = "auto_greedy"
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

def _auto_test_volumn(test_files_path, result_files_path, function, flag = True):
    result_files_path = result_files_path + "/"
    test_files_path = test_files_path + "/"

    for file in os.listdir(test_files_path):

        path = os.path.join(test_files_path, file)
        if not os.path.isfile(path): continue

        subsets, a_set = read_data_file(path)
        result = function(subsets, a_set)
        ruta_resultado = test_files_path + PREFIX + path
        
        if not os.path.isfile(ruta_resultado): continue
        
        #expected_result = read_result(ruta_resultado)
        expected_result = None

        if(len(result) != expected_result):
            print(RED, f"Ha ocurrido un error con el algoritmo ! En el archivo: {path}")
            print(f"El resultado del algoritmo fue: {len(result)} y se esperaba {expected_result}", RESET)
            break
        
        print(GREEN, "TODO OK", RESET, end="\n\n")
        print(f"El obtenido fue conseguido fue: {len(result)}")
        print("La secuencia de jugadores es: ")
        print(result)

def auto_test_backtracking(files: list):
    if not os.path.exists(files[0]) or not os.path.exists(files[1]):
        print("Alguna de las rutas no es valida")
        return 
    _auto_test_volumn(files[0], files[1], tp3.search_for_min_hitting_set)
    return

def auto_test_lineal_programming(files: list):
    if not os.path.exists(files[0]) or not os.path.exists(files[1]):
        print("Alguna de las rutas no es valida")
        return 
    _auto_test_volumn(files[0], files[1], tp3.search_hs_linealp)
    return

def auto_test_lineal_greedy(files: list):
    return

def execute_backtracking(file_name: list):
    subsets, a = read_data_file(file_name[0])
    print(tp3.search_for_min_hitting_set(subsets, a))
    return 

def execute_lineal_programming(file_name: list):
    subsets, a = read_data_file(file_name[0])
    print(tp3.search_hs_linealp(subsets, a))
    return

def execute_continous_lineal_programming(file_name: list):
    subsets, a = read_data_file(file_name[0])
    print(tp3.aprox_hs_by_contlp(subsets, a))
    return

def execute_greedy(file_name: list):
    subsets, a = read_data_file(file_name[0])
    print(tp3.aprox_greedy(subsets, a))
    return

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
    AUTO_TEST_GREEDY: auto_test_lineal_greedy,
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



    


        