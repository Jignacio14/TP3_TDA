def search_for_min_hitting_set(subsets, set):
    return  _search_for_min_hitting_set(set, subsets, [], [])

def is_solution(hitting_set, subsets):
    for subset in subsets:
        flag = False
        for element in subset:
            if element in hitting_set: 
                flag = True
                break
        if not flag: return False 
    return True


def _search_for_min_hitting_set(set,subsets, best_sol, act_sol): 

    if is_solution(act_sol, subsets) and (len(best_sol) == 0 or len(act_sol) < len(best_sol)):
        best_sol = act_sol[:]  
        
    if len(best_sol) > 0 and len(act_sol) > len(best_sol) and not is_solution(act_sol, subsets):
        return



    return best_sol