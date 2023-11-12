# TP3_TDA

## Programa

Para ejecutar el TP bastara con hacer

        make -f entrega.mk back

Una vez hecho eso para llamar a ejecución se tendra que hacer: 

        ./back_tp3

Esto pondra en ejecucion un programa por terminal donde se dispondran de los siguientes comandos para observar el funcionamiento del mismo

## Lista de comandos

        auto "CarpetaPruebas" "CarpetaResultados"

Este comando sirve para ejecutar pruebas automaticas con los archivos contenidos dentro de las carpetas pasadas en el orden mostrando por pantalla el TODO OK si se cumple con lo esperado o mostrara un ERROR, asi como tambien dando información adicional de cual fue el mismo

Este comando contrendra las siguientes flags las cuales se usan para mostrar la solución dadas las diferentes aproximaciones:

        1.  -l Para observar pruebas en volumen usando programación lineal
        2.  -g Para observar pruebas en volumen mediante la aproximación greedy

--- 

        exec "RutaArchivo"

Dicho comando ejecuta la solución mostrando por pantalla el resultado de la ejecución de la solución del programa

El comando tiene las siguientes flags:

        1. -l Ejecuta la versión por programación lineal
        2. -g Ejecuta la versión greedy 