import pulp

def search_for_min_hitting_set(subsets, set):
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
    return _search_hs_linealp(subsets, set)

def _search_hs_linealp(subsets, set):

    aux = list(set)
    y = []
    dict_variables = {}

    for i in range(len(aux)):
        y.append(pulp.LpVariable("x" + str(i), cat="Binary"))
        dict_variables[aux[i]] = "x" + str(i)
    
    problem = pulp.LpProblem("hitting_set_problem", pulp.LpMinimize)

    for subset in subsets:
        variables = []
        for elem in subset:
            variables.append(dict_variables[elem])
        problem += pulp.LpAffineExpression(variables) >= 1

    problem.solve()
    return list(map(lambda xi: pulp.value(xi), y))


