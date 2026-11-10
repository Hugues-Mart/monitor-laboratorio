
from datetime import date

NIVELES = ["baja", "media", "alta"]

CRITICIDAD = {
    "servidor_archivos": "alta",
    "router": "media",
    "equipo_practica": "media",
    "impresora": "baja",
}


def subir_nivel(nivel):
 
    i = NIVELES.index(nivel)
    return NIVELES[min(i + 1, len(NIVELES) - 1)]


def prioridad_dispositivo(fuente, total_caidos):
   
    if fuente not in CRITICIDAD:
        raise ValueError(f"Dispositivo desconocido: {fuente}")
    nivel = CRITICIDAD[fuente]
    if total_caidos > 1:
        nivel = subir_nivel(nivel)
    return nivel


def prioridad_factura(vencimiento, monto, pagada, hoy=None, monto_alto=1000):

    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    if pagada:
        return None
    hoy = hoy or date.today()
    dias = (vencimiento - hoy).days
    if dias < 0 and monto >= monto_alto:
        return "maxima"
    if dias < 3:
        return "alta"
    return "media" if monto >= monto_alto else "baja"
