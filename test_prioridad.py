from datetime import date
import pytest
from src.core.prioridad import (
    prioridad_dispositivo, prioridad_factura, subir_nivel,
)

HOY = date(2026, 11, 9)


def test_servidor_caido_es_alta():
    assert prioridad_dispositivo("servidor_archivos", 1) == "alta"


def test_impresora_es_baja():
    assert prioridad_dispositivo("impresora", 1) == "baja"


def test_varios_caidos_sube_un_nivel():
    assert prioridad_dispositivo("impresora", 2) == "media"


def test_no_pasa_de_alta():
    assert subir_nivel("alta") == "alta"


def test_dispositivo_desconocido():
    with pytest.raises(ValueError):
        prioridad_dispositivo("tostadora", 1)


def test_factura_vencida_monto_alto():
    assert prioridad_factura(date(2026, 11, 1), 5000, False, HOY) == "maxima"


def test_factura_vence_pronto():
    assert prioridad_factura(date(2026, 11, 11), 200, False, HOY) == "alta"


def test_factura_pagada_sale_de_la_cola():
    assert prioridad_factura(date(2026, 11, 1), 5000, True, HOY) is None


def test_monto_negativo():
    with pytest.raises(ValueError):
        prioridad_factura(date(2026, 11, 20), -50, False, HOY)
