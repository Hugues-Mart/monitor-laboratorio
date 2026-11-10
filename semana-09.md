# Semana 9: consulta concurrente

## Qué hice
- Simulé 4 fuentes (servidor, router, equipo de práctica e impresora) con retrasos y fallos aleatorios.
- Las consulté todas a la vez con asyncio.gather.
- Agregué un timeout de 2 segundos para que una fuente lenta no bloquee a las demás.
- Comparé el tiempo concurrente contra el secuencial.

## Qué problemas tuve
- (escribe aquí algo real que te pasó, por ejemplo un error con asyncio.run o una fuente que se quedaba colgada)

## Resultado
- (pega aquí lo que imprimió al ejecutar, por ejemplo los tiempos)

## Qué sigue
- Semana 10: comparar con hilos y procesos.
