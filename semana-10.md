# Semana 10: hilos, procesos o asyncio

## Qué hice
- Escribí `src/core/comparacion.py`, que ejecuta la misma tarea de cuatro formas: secuencial, con hilos, con procesos y con `asyncio`.
- Hice dos pruebas distintas, porque la mejor opción depende del tipo de tarea:
  1. **Tarea de espera:** consultar 4 dispositivos que tardan en responder. Casi todo el tiempo se va esperando.
  2. **Tarea de cálculo:** contar números primos. El procesador trabaja todo el tiempo.
- Usé tiempos fijos (en vez de aleatorios) para que la comparación sea justa.

## Resultados en mi computadora


## Qué aprendí
- **Hilos y asyncio** sirven cuando el programa pasa el tiempo esperando (red, discos, respuestas de dispositivos). Mientras uno espera, los demás avanzan.
- **Procesos** sirven cuando hay que calcular mucho, porque cada proceso usa un núcleo distinto del procesador. Con hilos no se gana nada en cálculo, porque en Python el GIL deja correr un solo hilo a la vez.
- Los procesos tienen un costo extra: crearlos tarda y consumen más memoria.
- Con 1 solo núcleo, los procesos tampoco aceleran el cálculo. Mis resultados dependen de cuántos núcleos tiene mi computadora. (escribe aquí cuántos tiene la tuya)

## Decisión para el proyecto
Consultar dispositivos y pasarelas es una tarea de espera, así que me quedo con **`asyncio`**:
- Es la más liviana (una sola línea de ejecución, sin crear hilos ni procesos).
- Permite poner timeout a cada fuente fácilmente.
- Escala bien si algún día son cientos de fuentes.



## Qué problemas tuve
- (escribe aquí algo real que te pasó)

## Qué sigue
- Ya tengo todas las semanas del plan hasta la 13. Sigue la semana 14: la página web.
