import grafo

def search_for_min_hitting_set(subsets, set):
    _search_for_min_hitting_set(set, subsets, [], [], subsets)
    return

def is_solution(hitting_set, subsets):
    for subset in subsets:
        flag = False
        for element in subset:
            if element in hitting_set: continue
        if not flag: return False 
    return True

def _search_for_min_hitting_set(set,subsets, best_sol, act_sol):

    if is_solution(act_sol, subsets) and len(act_sol) < len(best_sol):
        best_sol = act_sol[:]

    if not is_solution(act_sol, subsets) and len(act_sol) >= len(best_sol):
        return 
    
    for element in set:
        if element in act_sol: continue
        act_sol.append(element)
        _search_for_min_hitting_set(set, subsets, best_sol, act_sol)
        act_sol.pop()

    return best_sol

        
            
        
