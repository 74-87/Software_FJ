"""
Modulo de pruebas integrales de Software FJ.

Ejecuta operaciones validas e invalidas para verificar
el funcionamiento de clientes, servicios y reservas.

Demuestra:
- try/except
- try/except/else/finally
- Excepciones personalizadas
- Encadenamiento de excepciones
- Registro de eventos y errores
"""

from gestor import GestorSoftwareFJ

from clientes import Cliente

from servicios import (
    ServicioSala,
    AlquilerEquipo
)

from excepciones import (
    ErrorValidacion,
    ErrorCliente,
    ServicioNoDisponible
)

from registro import registrar_evento, registrar_error


# Crear el gestor central.
gestor = GestorSoftwareFJ()

total_pruebas = 11
pruebas_aprobadas = 0


def resultado(numero, descripcion, correcto):
    """Muestra el resultado de cada operacion."""

    global pruebas_aprobadas

    if correcto:
        pruebas_aprobadas += 1
        estado = "APROBADA"
    else:
        estado = "FALLIDA"

    print(f"{numero}. {descripcion}: {estado}")


print("=" * 60)
print("INICIO DE PRUEBAS INTEGRALES - SOFTWARE FJ")
print("=" * 60)


registrar_evento("Inicio de pruebas integrales.")


# --------------------------------------------------
# PRUEBA 1. REGISTRO VALIDO DE CLIENTE
# --------------------------------------------------

try:
    cliente1 = Cliente(
        "C001",
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )

    gestor.registrar_cliente(cliente1)

except Exception as error:
    registrar_error("Prueba 1: error al registrar cliente", error)
    resultado(1, "Registro valido de cliente", False)

else:
    resultado(1, "Registro valido de cliente", True)

finally:
    print("   Finalizacion de la operacion 1.")


# --------------------------------------------------
# PRUEBA 2. REGISTRO INVALIDO DE CLIENTE
# --------------------------------------------------

try:
    cliente_invalido = Cliente(
        "C002",
        "Maria Rodriguez",
        "correo_invalido",
        "3001234567"
    )

    gestor.registrar_cliente(cliente_invalido)

    resultado(2, "Rechazo de datos invalidos", False)

except ErrorValidacion as error:
    registrar_error("Prueba 2: cliente con correo invalido", error)
    resultado(2, "Rechazo de datos invalidos", True)


# --------------------------------------------------
# PRUEBA 3. REGISTRO DE UN SEGUNDO CLIENTE VALIDO
# --------------------------------------------------

try:
    cliente2 = Cliente(
        "C003",
        "Ana Martinez",
        "ana@gmail.com",
        "3101234567"
    )

    gestor.registrar_cliente(cliente2)

    resultado(3, "Registro de segundo cliente", True)

except Exception as error:
    registrar_error("Prueba 3: error de registro", error)
    resultado(3, "Registro de segundo cliente", False)


# --------------------------------------------------
# PRUEBA 4. CREACION DE SERVICIO DE SALA
# --------------------------------------------------

try:
    sala = ServicioSala(
        "S001",
        "Sala principal",
        50000,
        20
    )

    gestor.registrar_servicio(sala)

    resultado(4, "Creacion de servicio de sala", True)

except Exception as error:
    registrar_error("Prueba 4: error de servicio de sala", error)
    resultado(4, "Creacion de servicio de sala", False)


# --------------------------------------------------
# PRUEBA 5. CREACION DE SERVICIO DE EQUIPOS
# --------------------------------------------------

try:
    equipo = AlquilerEquipo(
        "E001",
        "Proyector",
        20000,
        5
    )

    gestor.registrar_servicio(equipo)

    resultado(5, "Creacion de servicio de equipos", True)

except Exception as error:
    registrar_error("Prueba 5: error de servicio de equipos", error)
    resultado(5, "Creacion de servicio de equipos", False)


# --------------------------------------------------
# PRUEBA 6. CREACION INCORRECTA DE SERVICIO
# --------------------------------------------------

try:
    servicio_invalido = ServicioSala(
        "S002",
        "Sala incorrecta",
        40000,
        0
    )

    resultado(6, "Rechazo de servicio con capacidad invalida", False)

except ErrorValidacion as error:
    registrar_error("Prueba 6: capacidad de sala invalida", error)
    resultado(6, "Rechazo de servicio con capacidad invalida", True)


# --------------------------------------------------
# PRUEBA 7. CREACION Y PROCESAMIENTO DE RESERVA
# --------------------------------------------------

try:
    reserva = gestor.crear_reserva(
        "R001",
        "C001",
        "S001",
        2
    )

    reserva.confirmar()

    costo = reserva.procesar(
        impuesto=19,
        descuento=10
    )

    correcto = (
        costo == 107100.0
        and reserva.estado == "PROCESADA"
    )

    resultado(7, "Reserva exitosa y calculo de costo", correcto)

except Exception as error:
    registrar_error("Prueba 7: error en reserva exitosa", error)
    resultado(7, "Reserva exitosa y calculo de costo", False)


# --------------------------------------------------
# PRUEBA 8. RESERVA DE SERVICIO NO DISPONIBLE
# --------------------------------------------------

try:
    sala_cerrada = ServicioSala(
        "S003",
        "Sala no disponible",
        40000,
        10,
        False
    )

    gestor.registrar_servicio(sala_cerrada)

    gestor.crear_reserva(
        "R002",
        "C001",
        "S003",
        2
    )

    resultado(8, "Rechazo de reserva no disponible", False)

except ServicioNoDisponible as error:
    registrar_error("Prueba 8: servicio no disponible", error)
    resultado(8, "Rechazo de reserva no disponible", True)


# --------------------------------------------------
# PRUEBA 9. RESERVA CON CLIENTE INEXISTENTE
# --------------------------------------------------

try:
    gestor.crear_reserva(
        "R003",
        "C999",
        "S001",
        2
    )

    resultado(9, "Rechazo de cliente inexistente", False)

except ErrorCliente as error:
    registrar_error("Prueba 9: cliente inexistente", error)
    resultado(9, "Rechazo de cliente inexistente", True)


# --------------------------------------------------
# PRUEBA 10. REGISTRO DUPLICADO DE CLIENTE
# --------------------------------------------------

try:
    gestor.registrar_cliente(cliente1)

    resultado(10, "Rechazo de cliente duplicado", False)

except ErrorCliente as error:
    registrar_error("Prueba 10: cliente duplicado", error)
    resultado(10, "Rechazo de cliente duplicado", True)


# --------------------------------------------------
# PRUEBA 11. ENCADENAMIENTO DE EXCEPCIONES
# --------------------------------------------------

def crear_cliente_con_encadenamiento():
    """Transforma un error de validacion en otro error."""

    try:
        return Cliente(
            "C011",
            "Cliente de prueba",
            "correo_incorrecto",
            "3001234567"
        )

    except ErrorValidacion as error:
        raise ErrorCliente(
            "No se pudo crear el cliente por datos invalidos."
        ) from error


try:
    crear_cliente_con_encadenamiento()

    resultado(11, "Encadenamiento de excepciones", False)

except ErrorCliente as error:
    registrar_error("Prueba 11: excepcion encadenada", error)

    correcto = isinstance(error.__cause__, ErrorValidacion)

    resultado(11, "Encadenamiento de excepciones", correcto)


# --------------------------------------------------
# RESUMEN FINAL
# --------------------------------------------------

print("\n" + "=" * 60)
print("RESULTADO FINAL DE LAS PRUEBAS")
print("=" * 60)

print("Total de operaciones:", total_pruebas)
print("Operaciones aprobadas:", pruebas_aprobadas)
print("Operaciones fallidas:", total_pruebas - pruebas_aprobadas)

print("Clientes registrados:", len(gestor.clientes))
print("Servicios registrados:", len(gestor.servicios))
print("Reservas registradas:", len(gestor.reservas))

if pruebas_aprobadas == total_pruebas:
    print("\nSISTEMA SOFTWARE FJ: TODAS LAS PRUEBAS APROBADAS")
    registrar_evento("Todas las pruebas integrales fueron aprobadas.")
else:
    print("\nATENCION: EXISTEN PRUEBAS FALLIDAS")
    registrar_evento("Las pruebas integrales finalizaron con fallos.")

print("=" * 60)
