"""Consulta concurrente de fuentes simuladas (semana 9)."""
import asyncio
import random
import time

# nombre de la fuente -> (probabilidad de fallar, retraso máximo en segundos)
FUENTES = {
    "servidor_archivos": (0.2, 1.0),
    "router": (0.1, 0.5),
    "equipo_practica": (0.3, 1.5),
    "impresora": (0.4, 2.5),
}

TIMEOUT = 2.0  # segundos que espero a cada fuente


async def consultar_fuente(nombre, prob_falla, retraso_max):
    """Simula un ping. Puede fallar o tardar demasiado."""
    await asyncio.sleep(random.uniform(0.1, retraso_max))
    if random.random() < prob_falla:
        raise ConnectionError(f"{nombre} no responde")
    return {"fuente": nombre, "estado": "ok"}


async def consultar_con_timeout(nombre, prob_falla, retraso_max):
    """Devuelve siempre un resultado, aunque la fuente falle o se demore."""
    try:
        return await asyncio.wait_for(
            consultar_fuente(nombre, prob_falla, retraso_max), timeout=TIMEOUT
        )
    except asyncio.TimeoutError:
        return {"fuente": nombre, "estado": "timeout"}
    except ConnectionError:
        return {"fuente": nombre, "estado": "caido"}


async def consultar_todas():
    tareas = [
        consultar_con_timeout(nombre, p, r) for nombre, (p, r) in FUENTES.items()
    ]
    return await asyncio.gather(*tareas)


def consultar_secuencial():
    """Misma consulta pero una por una, para comparar tiempos."""
    async def _uno_por_uno():
        resultados = []
        for nombre, (p, r) in FUENTES.items():
            resultados.append(await consultar_con_timeout(nombre, p, r))
        return resultados
    return asyncio.run(_uno_por_uno())


if __name__ == "__main__":
    inicio = time.perf_counter()
    resultados = asyncio.run(consultar_todas())
    t_conc = time.perf_counter() - inicio

    inicio = time.perf_counter()
    consultar_secuencial()
    t_sec = time.perf_counter() - inicio

    for r in resultados:
        print(f"{r['fuente']:<20} {r['estado']}")
    print(f"\nConcurrente: {t_conc:.2f} s | Secuencial: {t_sec:.2f} s")
