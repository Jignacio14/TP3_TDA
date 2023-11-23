import pulp

def search_for_min_hitting_set(subsets, a):
    return  _search_for_min_hitting_set(subsets, [], [], 0)

def is_solution(hitting_set, subsets):
    for subset in subsets:
        flag = False
        for element in subset:
            if element in hitting_set: 
                flag = True
                break
    if not flag: return False 
    return True

def has_a_player(subset, act_sol):
    for player in subset:
        if player in act_sol:
            return True
    return False


def _search_for_min_hitting_set(subsets, best_sol, act_sol, act_sub): 

    if is_solution(act_sol, subsets) and (len(best_sol) == 0 or len(act_sol) < len(best_sol)):
        best_sol = act_sol[:]
        return best_sol
    
    if len(best_sol) > 0 and len(act_sol) > len(best_sol) and not is_solution(act_sol, subsets):
        return best_sol

    if act_sub > len(subsets) - 1: 
        return best_sol

    if has_a_player(subsets[act_sub], act_sol):
        return _search_for_min_hitting_set(subsets, best_sol, act_sol, act_sub + 1)
    
    for player in subsets[act_sub]:
        act_sol.append(player)
        best_sol = _search_for_min_hitting_set(subsets, best_sol, act_sol, act_sub + 1)
        act_sol.pop()

    return best_sol

def search_hs_linealp(subsets, set):
    dict_variables = {elem: pulp.LpVariable(f"{elem}", cat="Binary") for elem in set}

    problem = pulp.LpProblem("hitting_set_problem", pulp.LpMinimize)
    problem += pulp.lpSum(dict_variables[elem] for elem in set)
    for subset in subsets:
        problem += pulp.lpSum(dict_variables[elem] for elem in subset) >= 1
    
    pulp.LpSolverDefault.msg = 0
    problem.solve()
    
    hitting_set_solution = {var.name for var in dict_variables.values() if pulp.value(var) == 1}
    return hitting_set_solution