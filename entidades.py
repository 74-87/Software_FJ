"""
Módulo de entidades generales del sistema Software FJ.

Contiene la clase abstracta Entidad, que establece
la estructura básica de las entidades del sistema.
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general.

    Las clases derivadas deben implementar los métodos
    identificador() y describir().
    """

    def __init__(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de la entidad es obligatorio.")

        self._codigo = codigo.strip()

    @property
    def codigo(self):
        """Permite consultar el código de la entidad."""
        return self._codigo

    @abstractmethod
    def identificador(self):
        """Devuelve la identificación de la entidad."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la entidad."""
        pass