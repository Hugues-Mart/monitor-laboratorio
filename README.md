# Monitor de servicios del laboratorio

Proyecto del curso de Python. Es una herramienta que revisa el estado de varios equipos y pasarelas de pago al mismo tiempo, ordena las fallas según su urgencia y guarda el historial para consultarlo después en una página web.

## Problema que resuelve

En el laboratorio hay equipos, impresoras y servidores que fallan sin que nadie lo note a tiempo, y los cobros se pierden de vista entre distintos canales. Este proyecto reúne todo en un solo lugar para saber qué está fallando y qué hay que atender primero.

## Qué hace

- Consulta varias fuentes en paralelo con `asyncio`, aunque alguna falle o se demore.
- Registra cada falla como un caso con descripción, categoría, estado y prioridad.
- Calcula la prioridad con reglas definidas en funciones puras.
- Guarda el historial en una base de datos SQLite.
- Muestra y permite registrar casos desde una página web.
- Resume los datos con `pandas`: qué falla más, en qué horarios y por estado, canal o semana.

## Módulos

**Dispositivos**

| Fuente (simulada) | Criticidad |
|---|---|
| Servidor de archivos | Alta |
| Router / switch | Media |
| Equipo de práctica | Media |
| Impresora | Baja |

**Pagos y facturas**

| Fuente (simulada) | Descripción |
|---|---|
| Pasarela A | Cobros en línea |
| Pasarela B | Cobros alternativos |
| Banco simulado | Pagos por transferencia |

Los dos módulos comparten el mismo motor de consulta, las mismas reglas de prioridad y la misma base de datos.

## Reglas de prioridad

**Dispositivos**
- Servidor caído: prioridad alta.
- Impresora sin respuesta: prioridad baja.
- Si hay más de un dispositivo caído a la vez, la prioridad sube un nivel.

**Facturas**
- Vencida y con monto alto: prioridad máxima.
- Vence en menos de 3 días: prioridad alta.
- Pagada: sale de la cola.

## Avance del proyecto

- [X] Semana 9: consulta concurrente de fuentes simuladas con `asyncio`
- [ ] Semana 10: comparación entre hilos, procesos y `asyncio`
- [X] Semana 11: funciones para clasificar y priorizar
- [ ] Semana 12: pruebas con entradas inesperadas y fallos de red
- [ ] Semana 13: base de datos con SQLite
- [ ] Semana 14: página web para registrar y consultar casos
- [ ] Semana 15: resúmenes con `pandas`
- [ ] Semana 16: integración y presentación final





TU NOMBRE · Curso de Python · TU UNIVERSIDAD
