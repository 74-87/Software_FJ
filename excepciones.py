
"""
Módulo de excepciones personalizadas del sistema Software FJ.

Este módulo define los errores específicos que pueden presentarse
durante la gestión de clientes, servicios y reservas.
"""


class ErrorSoftwareFJ(Exception):
    """Excepción base para los errores propios del sistema."""
    pass


class ErrorValidacion(ErrorSoftwareFJ):
    """Se presenta cuando los datos ingresados no son válidos."""
    pass


class ErrorCliente(ErrorSoftwareFJ):
    """Se presenta cuando ocurre un problema con un cliente."""
    pass


class ErrorServicio(ErrorSoftwareFJ):
    """Se presenta cuando ocurre un problema con un servicio."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Se presenta cuando un servicio no está disponible."""
    pass


class ErrorReserva(ErrorSoftwareFJ):
    """Se presenta cuando ocurre un problema con una reserva."""
    pass


class ReservaNoEncontrada(ErrorReserva):
    """Se presenta cuando no existe la reserva solicitada."""
    pass


class OperacionNoPermitida(ErrorSoftwareFJ):
    """Se presenta cuando se intenta realizar una operación no permitida."""
    pass


class ErrorCalculo(ErrorSoftwareFJ):
    """Se presenta cuando ocurre un error en un cálculo de costos."""
    pass