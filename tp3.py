import grafo

def search_for_min_hitting_set(subconjuntos):
    _search_for_min_hitting_set(subconjuntos, [], [], subconjuntos)
    return

def _search_for_min_hitting_set(subconjuntos, mejor_sol, sol_act, conjuntos_no_cubiertos):

    if len(conjuntos_no_cubiertos) == 0:
        return sol_act 
    
    if len(mejor_sol) < len(sol_act):
        return 

    # selecciono algun elemento de a

    #_search_for_min_hitting_set(subconjuntos, mejor_sol, sol_act.add(nuevo_elemento), conjuntos_no_cubiertos.elimino_los_que_tengan(nuevo_elemento))

    return


        
            
        
