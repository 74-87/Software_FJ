
"""
Módulo de gestión de clientes de Software FJ.

Implementa la clase Cliente mediante herencia,
encapsulación y validaciones de datos personales.
"""

import re

from entidades import Entidad
from excepciones import ErrorValidacion


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    def __init__(self, codigo, nombre, correo, telefono):

        # Inicializar la entidad general.
        super().__init__(codigo)

        # Validar el nombre.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorValidacion("El nombre del cliente es obligatorio.")

        if len(nombre.strip()) < 3:
            raise ErrorValidacion("El nombre debe tener al menos 3 caracteres.")

        # Validar el correo electrónico.
        if not isinstance(correo, str):
            raise ErrorValidacion("El correo debe ser texto.")

        patron_correo = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.fullmatch(patron_correo, correo.strip()):
            raise ErrorValidacion("El correo electrónico no es válido.")

        # Validar el teléfono.
        if not isinstance(telefono, str):
            raise ErrorValidacion("El teléfono debe ser texto.")

        telefono_limpio = telefono.strip()

        if not telefono_limpio.isdigit():
            raise ErrorValidacion("El teléfono solo debe contener números.")

        if not 7 <= len(telefono_limpio) <= 15:
            raise ErrorValidacion("El teléfono debe tener entre 7 y 15 dígitos.")

        # Encapsulación de los datos personales.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono_limpio

    @property
    def nombre(self):
        """Consultar el nombre del cliente."""
        return self.__nombre

    @property
    def correo(self):
        """Consultar el correo del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Consultar el teléfono del cliente."""
        return self.__telefono

    def identificador(self):
        """Devuelve el código único del cliente."""
        return self.codigo

    def describir(self):
        """Devuelve una descripción general del cliente."""
        return (
            f"Cliente: {self.__nombre} | "
            f"Código: {self.codigo} | "
            f"Correo: {self.__correo}"
        )

    def __str__(self):
        """Representación textual del cliente."""
        return self.describir()