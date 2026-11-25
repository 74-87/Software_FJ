"""
Prueba funcional del modulo de reservas de Software FJ.
"""

from clientes import Cliente
from servicios import ServicioSala
from reservas import Reserva

# 1. Crear un cliente.
cliente = Cliente(
    "C001",
    "Carlos Perez",
    "carlos@gmail.com",
    "3001234567"
)

# 2. Crear un servicio.
sala = ServicioSala(
    "S001",
    "Sala principal",
    50000,
    20
)

# 3. Crear una reserva.
reserva = Reserva(
    "R001",
    cliente,
    sala,
    2
)

print("1. RESERVA CREADA:")
print(reserva.describir())

# 4. Confirmar la reserva.
print("\n2. CONFIRMACION:")
print(reserva.confirmar())

# 5. Procesar la reserva.
print("\n3. PROCESAMIENTO:")
costo = reserva.procesar(
    impuesto=19,
    descuento=10
)

print("Costo final:", costo)
print("Estado final:", reserva.estado)

