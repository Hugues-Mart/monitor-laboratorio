"""Semana 10: pruebas de la comparación hilos / procesos / asyncio."""
from src.core.comparacion import (
    contar_primos, medir,
    espera_secuencial, espera_hilos, espera_procesos, espera_asyncio,
    calculo_secuencial, calculo_hilos, calculo_procesos,
)

FUENTES = {"a": 0.2, "b": 0.2, "c": 0.2}  # 0.6 s en secuencial


def nombres(resultados):
    return sorted(r["fuente"] for r in resultados)


def test_todos_los_metodos_devuelven_las_mismas_fuentes():
    for metodo in (espera_secuencial, espera_hilos, espera_procesos, espera_asyncio):
        assert nombres(metodo(FUENTES)) == ["a", "b", "c"]


def test_sin_fuentes_devuelve_lista_vacia():
    for metodo in (espera_secuencial, espera_hilos, espera_procesos, espera_asyncio):
        assert metodo({}) == []


def test_hilos_son_mas_rapidos_que_secuencial():
    _, t_sec = medir(espera_secuencial, FUENTES)
    _, t_hilos = medir(espera_hilos, FUENTES)
    assert t_hilos < t_sec * 0.7


def test_asyncio_es_mas_rapido_que_secuencial():
    _, t_sec = medir(espera_secuencial, FUENTES)
    _, t_async = medir(espera_asyncio, FUENTES)
    assert t_async < t_sec * 0.7


def test_contar_primos_valores_conocidos():
    assert contar_primos(2) == 0
    assert contar_primos(10) == 4      # 2, 3, 5, 7
    assert contar_primos(100) == 25


def test_calculo_da_lo_mismo_con_los_tres_metodos():
    limites = [1000, 2000, 3000]
    esperado = calculo_secuencial(limites)
    assert calculo_hilos(limites) == esperado
    assert calculo_procesos(limites) == esperado
