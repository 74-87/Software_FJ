from servicios import ServicioSala
from excepciones import ServicioNoDisponible

sala = ServicioSala(
    "S002",
    "Sala secundaria",
    40000,
    10,
    False
)

try:
    sala.calcular_costo(2)

except ServicioNoDisponible as error:
    print("ERROR CONTROLADO:", error)

print("El programa continúa funcionando.")