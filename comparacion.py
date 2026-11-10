"""Semana 10: comparar secuencial, hilos, procesos y asyncio.

Se hacen dos pruebas distintas:
  1. Tarea de ESPERA (consultar dispositivos): casi todo el tiempo se va
     esperando una respuesta, no calculando.
  2. Tarea de CÁLCULO (contar números primos): el procesador trabaja todo el rato.
"""
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# fuente -> segundos que tarda en responder (fijos, para comparar de forma justa)
FUENTES_FIJAS = {
    "servidor_archivos": 0.4,
    "router": 0.2,
    "equipo_practica": 0.6,
    "impresora": 0.8,
}

LIMITES_CPU = [120_000, 120_000, 120_000, 120_000]


# ---------- 1. tarea de espera ----------

def consultar_bloqueante(nombre, segundos):
    """Versión normal: mientras espera, el programa no hace nada más."""
    time.sleep(segundos)
    return {"fuente": nombre, "estado": "ok"}


async def consultar_async(nombre, segundos):
    """Versión asyncio: mientras espera, deja trabajar a las demás."""
    await asyncio.sleep(segundos)
    return {"fuente": nombre, "estado": "ok"}


def espera_secuencial(fuentes):
    return [consultar_bloqueante(n, s) for n, s in fuentes.items()]


def espera_hilos(fuentes):
    with ThreadPoolExecutor(max_workers=len(fuentes) or 1) as ex:
        return list(ex.map(consultar_bloqueante, fuentes.keys(), fuentes.values()))


def espera_procesos(fuentes):
    with ProcessPoolExecutor(max_workers=len(fuentes) or 1) as ex:
        return list(ex.map(consultar_bloqueante, fuentes.keys(), fuentes.values()))


def espera_asyncio(fuentes):
    async def _todas():
        return await asyncio.gather(
            *(consultar_async(n, s) for n, s in fuentes.items())
        )
    return asyncio.run(_todas())


# ---------- 2. tarea de cálculo ----------

def contar_primos(limite):
    """Cuenta cuántos números primos hay menores que 'limite'."""
    cuenta = 0
    for n in range(2, limite):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            cuenta += 1
    return cuenta


def calculo_secuencial(limites):
    return [contar_primos(l) for l in limites]


def calculo_hilos(limites):
    with ThreadPoolExecutor(max_workers=len(limites) or 1) as ex:
        return list(ex.map(contar_primos, limites))


def calculo_procesos(limites):
    with ProcessPoolExecutor(max_workers=len(limites) or 1) as ex:
        return list(ex.map(contar_primos, limites))


# ---------- medición ----------

def medir(funcion, argumento):
    """Ejecuta la función y devuelve (resultado, segundos que tardó)."""
    inicio = time.perf_counter()
    resultado = funcion(argumento)
    return resultado, time.perf_counter() - inicio


def imprimir_tabla(titulo, filas):
    print(f"\n{titulo}")
    print("-" * 40)
    base = filas[0][1]
    for nombre, segundos in filas:
        print(f"{nombre:<12} {segundos:6.2f} s   (x{base / segundos:.1f} vs secuencial)")


if __name__ == "__main__":
    espera = [
        ("secuencial", espera_secuencial),
        ("hilos", espera_hilos),
        ("procesos", espera_procesos),
        ("asyncio", espera_asyncio),
    ]
    filas = [(n, medir(f, FUENTES_FIJAS)[1]) for n, f in espera]
    imprimir_tabla("Tarea de ESPERA: consultar 4 dispositivos", filas)

    calculo = [
        ("secuencial", calculo_secuencial),
        ("hilos", calculo_hilos),
        ("procesos", calculo_procesos),
    ]
    filas = [(n, medir(f, LIMITES_CPU)[1]) for n, f in calculo]
    imprimir_tabla("Tarea de CÁLCULO: contar primos (4 tareas)", filas)
