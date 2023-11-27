# TP3_TDA

## Programa

Tenes dos formas de ejecutar este hermoso trabajo:

1. Ejecuntando el main usando directamente python de esta manera:
        
        python main.py 

Esta forma es windows friendly y te permite correrlo en cualquier maquina con python

2. Usando makefile, la versión pro-player (faker para los loleros) y consta de dos pasos 

"Compilado" mediante el uso de makefile 

        make -f entrega.mk back

Una vez hecho eso le mandas:  

        ./back_tp3

Esto pondra en ejecución el hermoso programa

## Lista de comandos

        exec <Ruta Archivo>

Con este comando llamaras a ejecución el algoritmo que mas te guste para resolver el problema, ya sea de manera aproximada o exacta, ojo que para llamar las distintas versiones debes especificar:

        exec -> Busca la solución con Backtracking
        exec_lineal -> Busca la solución por programación lineal entera
        exec_greedy -> Ejecuta el algoritmo de aproximación greedy
        exec_linealc -> Ejecuta la aproximación por programación lineal

Recorda que tenes que pasar el archivo pillin 

--- 

### NO TE BASTA CON ESO PARA QUERER ROMPER MI PROGRAMA ????? (VERSION BETA)

Evidentemente no, te conozco pillin, tambien tenes el siguiente comando 

        auto <Nombre de la carpeta con archivos de prueba> <Archivo con optimos>

Este comando tiene dos versiones:

        auto -> Solución por backtracking
        auto_lineal -> Solución por programción lineal entera 

Este comando lo que realiza es una serie de test en volumen con todos los archivos contenidos en la carpeta pasada por parametro y verifica que el resultado (Longitud del optimo) coincida con lo esperado (Lo contenido en el archivo de resultados)

---
        close 

Porque no puedo ser tan trucho y pedirte un ctrl + c, hasta se despide de ti de manera elegante 

### Formato archivo de prueba:

El archivo que contenga los resultados debe ser de la siguiente manera:

        <Nombre del archivo>:<Optimo>

Un ejemplito pa que no se te rompa:

        5.txt: 2
        7.txt: 3

ESOOOO es tood por ahora amiguitos, nos vemos, más adelante