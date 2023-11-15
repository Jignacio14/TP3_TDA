from copy import deepcopy

def search_for_min_hitting_set(subsets, set):
    return  _search_for_min_hitting_set(set, subsets, [], [])

def validar_hitting_set(h: set, lista_subconjuntos: list):
    for sub in lista_subconjuntos:
        alguno = False
        for elemento in sub: 
            if elemento in h: 
                alguno = True
        if alguno == False: return False
    return True

def is_solution(hitting_set, subsets):
    for subset in subsets:
        flag = False
        for element in subset:
            if element in hitting_set: 
                flag = True
                continue
        if not flag: return False 
    return True


def _search_for_min_hitting_set(set,subsets, best_sol, act_sol): 

    if is_solution(act_sol, subsets) and len(act_sol) < len(best_sol):
        best_sol = act_sol[::]
    
    if len(act_sol) > len(best_sol) and not is_solution(act_sol, subsets):
        return 
    
    for element in set:
        if element in act_sol or element in best_sol: 
            continue
        act_sol.append(element)
        _search_for_min_hitting_set(set, subsets, best_sol, act_sol)
        act_sol.pop()

    
    return best_sol