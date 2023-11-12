import sys

AUTO_TEST = "auto"
EXECUTE = "exec"
AUTO_TEST_LINEAL = "auto_lineal"
EXECUTE_LINEAL = "exec_lineal"
AUTO_TEST_GREEDY = "auto_greedy"
EXECUTE_GREEDY = "exec_greedy"
CLOSE = "close\n"

def auto_test_backtracking(test_files, result_files):
    print("Paso por aca 1")
    print(test_files, result_files)
    return

def auto_test_lineal_programming(test_files, result_files):
    print("Paso por aca 2")
    print(test_files, result_files)
    return

def auto_test_lineal_greedy(test_files, result_files):
    print("Paso por aca 3")
    print(test_files, result_files)
    return

def execute_backtracking(file_name, extra):
    print("Paso por aca 4")
    print(file_name, extra)
    return

def execute_lineal_programming(file_name, extra):
    print("Paso por aca 5")
    print(file_name, extra)
    return

def execute_greedy(file_name, extra):
    print("Paso por aca 6")
    print(file_name, extra)
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
    try:
        for line in sys.stdin:
            if line == CLOSE:
                print("Adios")
                break
            command, data = line.strip().split(" ", 1)
            file_one, file_two = prepare_data(data)
            MAP.get(command, show_input_error())(file_one, file_two)
    except (ValueError, TypeError) as e:
        show_input_error()