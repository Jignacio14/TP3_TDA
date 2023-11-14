# Informe 

### Enunciado

Scaloni ya está armando la lista de 43 jugadores que van a ir al mundial 2026. 
Hay mucha presión por parte de la prensa para bajar línea de cuál debería ser 
el 11 inicial. Lo de siempre. 
Algunos medios quieren que juegue Roncaglia, otros quieren que juegue 
Mateo Messi, y así. Cada medio tiene un subconjunto de
jugadores que quiere que jueguen. A Scaloni esto no le importa, no va a dejar
que la prensa lo condicione, pero tiene jugadores jóvenes a los que esto
puede afectarles. 

Justo hay un partido amistoso contra Burkina Faso la semana que viene. Oportunidad
ideal para poner un equipo que contente a todos, baje la presión y poder 
aislar al equipo. 

El problema es, ¿cómo elegir el conjunto de jugadores que jueguen ese partido 
(entre titulares y suplentes que vayan a entrar)? Además, Scaloni quiere poder
usar ese partido para probar cosas aparte. No puede gastar el amistoso
para contentar a un periodista mufa que habla mal de Messi, por ejemplo. 
Quiere definir el conjunto más pequeño de jugadores necesarios para contentarlos 
y poder seguir con la suya. Con elegir
un jugador que contente a cada periodista/medio, le es suficiente. 

Ante este problema, Bilardo se sentó con Scaloni para explicarle que en realidad 
este es un problema conocido (viejo zorro como es, ya se comió todas las operetas 
de prensa así que se conoce este problema de memoria). Se sirvió una copa de _Gatorei_ 
y le comentó:

"Esto no es más que un caso particular del Hitting-Set Problem. El cual es: Dado un conjunto 
$A$ de $n$ elementos y $m$ subconjuntos $B_1, B_2, ..., B_m$ de $A$
($B_i \subseteq A \forall i$) , queremos el subconjunto $C \subseteq A$ de menor tamaño tal 
que $$C$$ tenga al menos un elemento de cada
$B_i$ (es decir, $C \cap B_i \neq \emptyset$). En nuestro caso, $A$ son los jugadores 
convocados, los $$B_i$$ son los deseos de la
prensa, y $C$ es el conjunto de jugadores que deberían jugar contra Burkina Faso 
si o si". 

Bueno, ahora con un poco más claridad en el tema, Scaloni necesita de nuestra 
ayuda para ver si obtener este subconjunto se puede hacer de forma eficiente 
(polinomial) o, si no queda otra, con qué alternativas contamos. 

### Hitting Set se encuentra en NP

Para demostrar que hitting set se encuentra en NP bastaria con tener una solución del problema: un conjunto $H$ y y el set de datos de entrada al mismo, un conjunto de subconjuntos $B = B_1, B_2, ... B_m$ ($B_i \subseteq A \forall i$) de manera que, simplemente, se debe iterar sobre el conjunto de subconjuntos y sobre cada subconjunto validando si alguno de los elementos $b_j \in B_i$ ciertamente pertenece a $H$. En caso de haber probado con todos los elementos de un $B_i$ y ninguno de sus elementos $b_j$ pertenezca a $H$ entonces, la solución brindada no es un Hitting Set, en caso de haber llegado al final entonces dicho conjunto si es un Hitting Set

Ahora una implementación de dicho verificador:

```python
    def validar_hitting_set(h: set, lista_subconjuntos: list):
        for sub in lista_subconjuntos:
            alguno = False
            for elemento in sub: 
                if elemento in h: 
                    alguno = True
            if alguno == False: return False
        return True
```

Para verificar finalmente que dicho problema falta con probar que este validador posee tiempo polinomial

Veamos que: 

- Recorrer la lista de subconjuntos es lineal a la cantidad de subconjuntos, dicha cantidad se llamara $m$
- Recorrer los elementos del subconjunto $Bi$ es lineal a la cantidad de elementos del subconjuntos, dicha cantidad se llamara $k$

Ahora si decimos generalizamos $k$ como el maximo cardinal existente de algun conjunto $B_i$ se puede establecer la siguiente cota:

$$
    T(n) = O(m \times k)
$$

Como dicha complejidad es polinomial a $m$ y $k$ entonces se cumple que Hitting Set esta  en $NP$

### Hitting Set es NP-Completo 

Para probar este segmento del informe se debe realizar una reduccion de algun problema NP-Completo conocido a Hitting-Set, en este caso, dicho problema sera Vertex Cover.

En un principio se establecen ambos problemas de decisión: 

    El problema de decisión del vertex cover implica, dado un grafo G y un numero k, determinar si existe un vertex cover de tamaño a lo sumo k 

Por otro lado: 

    El problema de decisión del hitting set implica, sea A un conjunto, B un conjunto de subconjuntos pertenecientes a A, determinar si existe un conjunto H de tamaño al menos k tal que todo subconjunto de B la interseccion entre B_i y H no es vacia 

Entonces veamos la siguiente reducción:

$$
    \text{Vertex Cover} \leq_p \text{Hitting Set} 
$$

Sea $G$ un grafo, $V$ su conjunto de vertices y $E$ su conjunto de aristas, entonces se toma $A$ como el conjunto de vertices. Ahora, que sera $B$, en este caso se podria definir como el conjunto de subconjunto de los pares $(v_i, v_j)$ siempre y cuando exista una arista entre dichos vertices, aunque, esto seria simplemente el conjunto de las aristas de $G$

Habiendo establecido lo anterior, se puede observar que si existe un Hitting Set de tamaño k  para los conjuntos $A = V(G)$ y $B = E(G)$ entonces necesariamente existe un vertex cover de tamaño al menos k, por lo tanto, sabiendo que vertex cover es un problema NP-Completo se puede concluir finalmente que Hitting set también es NP-Completo 

