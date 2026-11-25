"""
Modulo de registro de eventos y errores de Software FJ.

Utiliza la biblioteca logging de Python para registrar
la actividad del sistema en un archivo externo.
"""

import logging
from pathlib import Path


# Obtener la ubicacion de la carpeta del proyecto.
RUTA_PROYECTO = Path(__file__).resolve().parent

# Crear la carpeta logs si no existe.
RUTA_LOGS = RUTA_PROYECTO / "logs"
RUTA_LOGS.mkdir(parents=True, exist_ok=True)

# Definir el archivo de registro.
ARCHIVO_LOG = RUTA_LOGS / "software_fj.log"


# Configurar el registrador principal.
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)
logger.propagate = False


# Evitar duplicar los manejadores al importar el modulo.
if not logger.handlers:

    manejador = logging.FileHandler(
        ARCHIVO_LOG,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    """Registra un evento importante del sistema."""

    logger.info(mensaje)


def registrar_error(mensaje, error=None):
    """Registra un error y, cuando existe, su informacion tecnica."""

    if error is None:
        logger.error(mensaje)
    else:
        logger.error(
            "%s: %s",
            mensaje,
            error,
            exc_info=(
                type(error),
                error,
                error.__traceback__
            )
        )


def registrar_advertencia(mensaje):
    """Registra una advertencia del sistema."""

    logger.warning(mensaje)


def obtener_ruta_log():
    """Devuelve la ubicacion del archivo de registro."""

    return str(ARCHIVO_LOG)
