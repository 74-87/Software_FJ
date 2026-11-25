"""
Modulo central de administracion de Software FJ.

Gestiona las listas internas de clientes, servicios y reservas.
No utiliza bases de datos.
"""

from clientes import Cliente
from servicios import Servicio
from reservas import Reserva

from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)

from registro import registrar_evento, registrar_error


class GestorSoftwareFJ:
    """Administra los clientes, servicios y reservas."""

    def __init__(self):
        self._clientes = []
        self._servicios = []
        self._reservas = []

        registrar_evento("Gestor central de Software FJ iniciado.")

    @property
    def clientes(self):
        return tuple(self._clientes)

    @property
    def servicios(self):
        return tuple(self._servicios)

    @property
    def reservas(self):
        return tuple(self._reservas)

    def registrar_cliente(self, cliente):
        """Agrega un cliente a la lista interna."""

        try:
            if not isinstance(cliente, Cliente):
                raise ErrorCliente("El objeto no es un cliente valido.")

            if any(c.codigo == cliente.codigo for c in self._clientes):
                raise ErrorCliente(
                    f"Ya existe el cliente {cliente.codigo}."
                )

            self._clientes.append(cliente)

            registrar_evento(
                f"Cliente registrado: {cliente.codigo}."
            )

            return cliente

        except Exception as error:
            registrar_error("Error al registrar cliente", error)
            raise

    def registrar_servicio(self, servicio):
        """Agrega un servicio a la lista interna."""

        try:
            if not isinstance(servicio, Servicio):
                raise ErrorServicio("El objeto no es un servicio valido.")

            if any(s.codigo == servicio.codigo for s in self._servicios):
                raise ErrorServicio(
                    f"Ya existe el servicio {servicio.codigo}."
                )

            self._servicios.append(servicio)

            registrar_evento(
                f"Servicio registrado: {servicio.codigo}."
            )

            return servicio

        except Exception as error:
            registrar_error("Error al registrar servicio", error)
            raise

    def buscar_cliente(self, codigo):
        """Busca un cliente por su codigo."""

        for cliente in self._clientes:
            if cliente.codigo == codigo:
                return cliente

        raise ErrorCliente(
            f"No se encontro el cliente {codigo}."
        )

    def buscar_servicio(self, codigo):
        """Busca un servicio por su codigo."""

        for servicio in self._servicios:
            if servicio.codigo == codigo:
                return servicio

        raise ErrorServicio(
            f"No se encontro el servicio {codigo}."
        )

    def buscar_reserva(self, codigo):
        """Busca una reserva por su codigo."""

        for reserva in self._reservas:
            if reserva.codigo == codigo:
                return reserva

        raise ErrorReserva(
            f"No se encontro la reserva {codigo}."
        )

    def crear_reserva(
        self,
        codigo,
        codigo_cliente,
        codigo_servicio,
        duracion,
        cantidad=None
    ):
        """Crea una reserva y la almacena en la lista interna."""

        try:
            if any(r.codigo == codigo for r in self._reservas):
                raise ErrorReserva(
                    f"Ya existe la reserva {codigo}."
                )

            cliente = self.buscar_cliente(codigo_cliente)
            servicio = self.buscar_servicio(codigo_servicio)

            reserva = Reserva(
                codigo,
                cliente,
                servicio,
                duracion,
                cantidad
            )

            self._reservas.append(reserva)

            registrar_evento(
                f"Reserva creada: {codigo} para cliente {codigo_cliente}."
            )

            return reserva

        except Exception as error:
            registrar_error("Error al crear reserva", error)
            raise

    def listar_clientes(self):
        """Devuelve la lista de clientes registrados."""
        return list(self._clientes)

    def listar_servicios(self):
        """Devuelve la lista de servicios registrados."""
        return list(self._servicios)

    def listar_reservas(self):
        """Devuelve la lista de reservas registradas."""
        return list(self._reservas)
