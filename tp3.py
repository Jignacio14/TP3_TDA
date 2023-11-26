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
    players = {player: pulp.LpVariable(f"{player}", cat=pulp.LpBinary) for player in set}

    problem = pulp.LpProblem("hitting_set_problem", pulp.LpMinimize)
    problem += pulp.lpSum(players[player] for player in set)
    for subset in subsets:
        problem += pulp.lpSum(players[player] for player in subset) >= 1
    
    pulp.LpSolverDefault.msg = 0
    problem.solve()
    
    hitting_set_solution = {player.name for player in players.values() if pulp.value(player) == 1}
    return hitting_set_solution


def _aprox_hs_by_contlp(subsets: set, total_players: set, b: float):
    players = {player: pulp.LpVariable(f"{player}", lowBound=0, upBound=1, cat=pulp.LpContinuous) for player in total_players}
    problem = pulp.LpProblem("hitting_set_problem_c", pulp.LpMinimize)
    problem += pulp.lpSum(players[player] for player in total_players)

    for subset in subsets:
        problem += pulp.lpSum(players[player] for player in subset) >= 1
    
    pulp.LpSolverDefault.msg = 0
    problem.solve()
    hitting_set_solution = {player.name for player in players.values() if pulp.value(player) >= b}
    if len(hitting_set_solution) == 0:
        return []
    return hitting_set_solution

def aprox_hs_by_contlp(subsets: set, set: set):
    max_length = max(len(subset) for subset in subsets)
    result = _aprox_hs_by_contlp(subsets, set, 1/max_length)
    return result

def aprox_greedy(subsets: set, a: set):
    aprox_sol = set()
    missing_sets = set(range(len(subsets)))
    subsets = list(subsets)
    return _aprox_greedy(subsets, aprox_sol, missing_sets)

def _aprox_greedy(subsets: list, aprox_sol: set, missing_sets: set):
    while(not is_solution(aprox_sol, subsets)):
        diference = set()
        player = find_most_frequent_player(missing_sets, subsets)
        for i in missing_sets: 
            if has_a_player(subsets[i], player):
                diference.add(i)
        aprox_sol.add(player)
        missing_sets.difference_update(diference)
    return aprox_sol

def find_most_frequent_player(missing_sets: set, subsets: list):
    frequency = dict()
    for subset_index in missing_sets:
        for player in subsets[subset_index]:
            frequency[player] = frequency.get(player, 0) + 1
    most_frequent_player = max(frequency, key=frequency.get)
    return most_frequent_player