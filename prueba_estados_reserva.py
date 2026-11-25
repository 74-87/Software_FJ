"""
Pruebas de estados y excepciones de las reservas.
"""

from clientes import Cliente
from servicios import ServicioSala
from reservas import Reserva
from excepciones import OperacionNoPermitida


cliente = Cliente(
    "C002",
    "Maria Rodriguez",
    "maria@gmail.com",
    "3001234567"
)

sala = ServicioSala(
    "S002",
    "Sala secundaria",
    40000,
    10
)

# PRUEBA 1: Cancelar una reserva pendiente.

reserva1 = Reserva("R002", cliente, sala, 2)

print("PRUEBA 1: CANCELACION")

print("Estado inicial:", reserva1.estado)

print(reserva1.cancelar())

print("Estado final:", reserva1.estado)


# PRUEBA 2: Intentar procesar una reserva pendiente.

reserva2 = Reserva("R003", cliente, sala, 2)

print("\nPRUEBA 2: OPERACION NO PERMITIDA")

try:
    reserva2.procesar()

except OperacionNoPermitida as error:
    print("ERROR CONTROLADO:", error)

print("Estado de la reserva:", reserva2.estado)

print("\nTodas las pruebas finalizaron.")
