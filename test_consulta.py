import asyncio
from src.core.consulta import consultar_todas, FUENTES


def test_devuelve_un_resultado_por_fuente():
    resultados = asyncio.run(consultar_todas())
    assert len(resultados) == len(FUENTES)


def test_estados_validos():
    resultados = asyncio.run(consultar_todas())
    for r in resultados:
        assert r["estado"] in {"ok", "caido", "timeout"}
