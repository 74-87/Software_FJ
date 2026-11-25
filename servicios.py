
"""
Modulo de servicios especializados de Software FJ.

Implementa una clase abstracta Servicio y tres servicios derivados:
1. ServicioSala
2. AlquilerEquipo
3. AsesoriaEspecializada

Aplica abstraccion, herencia y polimorfismo.
"""

import math
from abc import abstractmethod

from entidades import Entidad
from excepciones import (
    ErrorValidacion,
    ErrorCalculo,
    ServicioNoDisponible
)


class Servicio(Entidad):
    """Clase abstracta que representa un servicio general."""

    def __init__(self, codigo, nombre, tarifa_base, disponible=True):
        super().__init__(codigo)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre del servicio es obligatorio.")

        if (
            isinstance(tarifa_base, bool)
            or not isinstance(tarifa_base, (int, float))
            or not math.isfinite(tarifa_base)
            or tarifa_base <= 0
        ):
            raise ErrorValidacion("La tarifa debe ser un numero positivo.")

        if not isinstance(disponible, bool):
            raise ErrorValidacion("La disponibilidad debe ser verdadera o falsa.")

        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        """Cambia la disponibilidad del servicio."""
        if not isinstance(estado, bool):
            raise ErrorValidacion("El estado debe ser verdadero o falso.")

        self._disponible = estado

    def validar_disponibilidad(self):
        """Comprueba si el servicio esta disponible."""
        if not self._disponible:
            raise ServicioNoDisponible(
                f"El servicio {self._nombre} no esta disponible."
            )

    def _validar_duracion(self, duracion):
        """Valida la duracion del servicio."""
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ErrorValidacion("La duracion debe ser un numero positivo.")

    def _calcular_total(self, subtotal, impuesto=0, descuento=0):
        """Calcula el total aplicando impuesto y descuento."""

        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
            or not math.isfinite(impuesto)
            or not 0 <= impuesto <= 100
        ):
            raise ErrorCalculo("El impuesto debe estar entre 0 y 100.")

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not math.isfinite(descuento)
            or not 0 <= descuento <= 100
        ):
            raise ErrorCalculo("El descuento debe estar entre 0 y 100.")

        total = subtotal * (1 - descuento / 100)
        total = total * (1 + impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def validar_parametros(self, duracion, **kwargs):
        pass

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        pass

    @abstractmethod
    def identificador(self):
        pass

    @abstractmethod
    def describir(self):
        pass


class ServicioSala(Servicio):
    """Servicio de alquiler de salas por horas."""

    def __init__(self, codigo, nombre, tarifa_base, capacidad, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)

        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise ErrorValidacion("La capacidad debe ser un entero positivo.")

        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def validar_parametros(self, duracion, **kwargs):
        self._validar_duracion(duracion)
        self.validar_disponibilidad()

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        self.validar_parametros(duracion)
        subtotal = self.tarifa_base * duracion
        return self._calcular_total(subtotal, impuesto, descuento)

    def identificador(self):
        return self.codigo

    def describir(self):
        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnologicos."""

    def __init__(self, codigo, nombre, tarifa_base, cantidad, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise ErrorValidacion("La cantidad debe ser un entero positivo.")

        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad

    def validar_parametros(self, duracion, **kwargs):
        self._validar_duracion(duracion)
        self.validar_disponibilidad()

        cantidad = kwargs.get("cantidad", self.cantidad)

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise ErrorValidacion("La cantidad debe ser un entero positivo.")

        if cantidad > self.cantidad:
            raise ErrorValidacion(
                "La cantidad solicitada supera los equipos disponibles."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        self.validar_parametros(duracion, **kwargs)

        cantidad = kwargs.get("cantidad", self.cantidad)
        subtotal = self.tarifa_base * duracion * cantidad

        return self._calcular_total(subtotal, impuesto, descuento)

    def identificador(self):
        return self.codigo

    def describir(self):
        return (
            f"Alquiler de equipo: {self.nombre} | "
            f"Unidades disponibles: {self.cantidad} | "
            f"Tarifa por hora y unidad: ${self.tarifa_base:,.2f}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria profesional especializada."""

    def __init__(self, codigo, nombre, tarifa_base, especialidad, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorValidacion("La especialidad es obligatoria.")

        self._especialidad = especialidad.strip()

    @property
    def especialidad(self):
        return self._especialidad

    def validar_parametros(self, duracion, **kwargs):
        self._validar_duracion(duracion)
        self.validar_disponibilidad()

    def calcular_costo(self, duracion, impuesto=0, descuento=0, **kwargs):
        self.validar_parametros(duracion)

        subtotal = self.tarifa_base * duracion

        return self._calcular_total(subtotal, impuesto, descuento)

    def identificador(self):
        return self.codigo

    def describir(self):
        return (
            f"Asesoria: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )
