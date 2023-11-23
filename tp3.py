import pulp

def search_for_min_hitting_set(subsets, a):
    return  _search_for_min_hitting_set(subsets, set(), set(), 0, set())

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


def _search_for_min_hitting_set(subsets: list, best_sol: set, act_sol: set, act_sub: int, used_players: set): 

    if len(best_sol) > 0 and len(act_sol) > len(best_sol): 
        return best_sol

    if act_sub == len(subsets) - 1 and (len(best_sol) == 0 or len(act_sol) < len(best_sol)) and is_solution(act_sol, subsets):
        best_sol = act_sol.copy()
        return best_sol
    
    if act_sub > len(subsets) - 1: 
        return best_sol

    if has_a_player(subsets[act_sub], act_sol):
        return _search_for_min_hitting_set(subsets, best_sol, act_sol, act_sub + 1, used_players)
    
    selected_players = set()

    for player in subsets[act_sub]:
        if player in used_players: 
            continue
        act_sol.add(player)
        selected_players.add(player)
        used_players.add(player)
        best_sol = _search_for_min_hitting_set(subsets, best_sol, act_sol, act_sub + 1, used_players)
        act_sol.remove(player)

    used_players.difference_update(selected_players)
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