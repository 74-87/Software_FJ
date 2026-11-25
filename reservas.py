"""
Modulo de gestion de reservas de Software FJ.

Permite crear, confirmar, cancelar y procesar reservas,
integrando clientes y servicios especializados.
"""

import math

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio

from excepciones import (
    ErrorValidacion,
    ErrorReserva,
    OperacionNoPermitida
)


class Reserva(Entidad):
    """Representa una reserva de un cliente para un servicio."""

    ESTADOS = (
        "PENDIENTE",
        "CONFIRMADA",
        "CANCELADA",
        "PROCESADA"
    )

    def __init__(
        self,
        codigo,
        cliente,
        servicio,
        duracion,
        cantidad=None
    ):
        # Inicializar la entidad general.
        super().__init__(codigo)

        # Validar el cliente.
        if not isinstance(cliente, Cliente):
            raise ErrorValidacion(
                "La reserva debe estar asociada a un cliente valido."
            )

        # Validar el servicio.
        if not isinstance(servicio, Servicio):
            raise ErrorValidacion(
                "La reserva debe estar asociada a un servicio valido."
            )

        # Validar la duracion.
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ErrorValidacion(
                "La duracion de la reserva debe ser positiva."
            )

        # Validar los parametros del servicio.
        if cantidad is None:
            servicio.validar_parametros(duracion)
        else:
            servicio.validar_parametros(
                duracion,
                cantidad=cantidad
            )

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._cantidad = cantidad
        self._estado = "PENDIENTE"
        self._costo = None

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    def identificador(self):
        """Devuelve el codigo de la reserva."""
        return self.codigo

    def describir(self):
        """Devuelve la informacion general de la reserva."""
        return (
            f"Reserva: {self.codigo} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duracion: {self.duracion} horas | "
            f"Estado: {self.estado}"
        )

    def calcular_costo(self, impuesto=0, descuento=0):
        """Calcula el costo de la reserva."""

        parametros = {
            "impuesto": impuesto,
            "descuento": descuento
        }

        if self._cantidad is not None:
            parametros["cantidad"] = self._cantidad

        return self.servicio.calcular_costo(
            self.duracion,
            **parametros
        )

    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente."""

        if self._estado != "PENDIENTE":
            raise OperacionNoPermitida(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.servicio.validar_parametros(
            self.duracion,
            **(
                {"cantidad": self._cantidad}
                if self._cantidad is not None
                else {}
            )
        )

        self._estado = "CONFIRMADA"

        return f"Reserva {self.codigo} confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self._estado not in ("PENDIENTE", "CONFIRMADA"):
            raise OperacionNoPermitida(
                "La reserva no puede cancelarse en su estado actual."
            )

        self._estado = "CANCELADA"

        return f"Reserva {self.codigo} cancelada correctamente."

    def procesar(self, impuesto=0, descuento=0):
        """Procesa una reserva previamente confirmada."""

        if self._estado != "CONFIRMADA":
            raise OperacionNoPermitida(
                "Solo se pueden procesar reservas confirmadas."
            )

        # Calcular primero para evitar cambiar el estado
        # si se produce un error durante el calculo.
        total = self.calcular_costo(impuesto, descuento)

        self._costo = total
        self._estado = "PROCESADA"

        return total
