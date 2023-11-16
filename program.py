import sys
import tp3

AUTO_TEST = "auto"
EXECUTE = "exec"
AUTO_TEST_LINEAL = "auto_lineal"
EXECUTE_LINEAL = "exec_lineal"
AUTO_TEST_GREEDY = "auto_greedy"
EXECUTE_GREEDY = "exec_greedy"
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

def auto_test_backtracking(test_files, result_files):
    return

def auto_test_lineal_programming(test_files, result_files):
    return

def auto_test_lineal_greedy(test_files, result_files):
    return

def execute_backtracking(file_name, extra):
    subsets, a = read_data_file(file_name)
    resultado = tp3.search_for_min_hitting_set(subsets, a)
    return resultado

def execute_lineal_programming(file_name, extra):
    subsets, a = read_data_file(file_name)
    resultado = tp3.search_hs_linealp(subsets, a)
    return resultado

def execute_greedy(file_name, extra):
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
}

def program_execution():
    for line in sys.stdin:
        if line == CLOSE:
            print("Adios")
            break
        # datos = line.strip("\n").split(" ")
        result = execute_lineal_programming("15.txt", None)
        print(result)
        #MAP.get(datos[0], show_input_error())(datos[1])
