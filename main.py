"""
Programa principal de Software FJ.

Permite administrar clientes, servicios y reservas
mediante un menu interactivo.
"""

from gestor import GestorSoftwareFJ

from clientes import Cliente

from servicios import (
    ServicioSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from registro import registrar_evento, registrar_error


def mostrar_menu():
    """Muestra las opciones principales del sistema."""

    print("\n" + "=" * 50)
    print("          SISTEMA SOFTWARE FJ")
    print("=" * 50)
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Consultar clientes")
    print("4. Consultar servicios")
    print("5. Crear reserva")
    print("6. Consultar reservas")
    print("7. Confirmar reserva")
    print("8. Cancelar reserva")
    print("9. Procesar reserva")
    print("0. Salir")
    print("=" * 50)


def registrar_nuevo_cliente(gestor):
    """Solicita los datos y registra un cliente."""

    print("\n--- REGISTRO DE CLIENTE ---")

    codigo = input("Codigo: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electronico: ").strip()
    telefono = input("Telefono: ").strip()

    cliente = Cliente(codigo, nombre, correo, telefono)

    gestor.registrar_cliente(cliente)

    print("Cliente registrado correctamente.")


def registrar_nuevo_servicio(gestor):
    """Permite registrar diferentes tipos de servicios."""

    print("\n--- REGISTRO DE SERVICIO ---")
    print("1. Sala")
    print("2. Alquiler de equipos")
    print("3. Asesoria especializada")

    tipo = input("Seleccione el tipo de servicio: ").strip()

    codigo = input("Codigo del servicio: ").strip()
    nombre = input("Nombre del servicio: ").strip()
    tarifa = float(input("Tarifa base: "))

    if tipo == "1":

        capacidad = int(input("Capacidad de la sala: "))

        servicio = ServicioSala(
            codigo, nombre, tarifa, capacidad
        )

    elif tipo == "2":

        cantidad = int(input("Cantidad de equipos: "))

        servicio = AlquilerEquipo(
            codigo, nombre, tarifa, cantidad
        )

    elif tipo == "3":

        especialidad = input("Especialidad: ").strip()

        servicio = AsesoriaEspecializada(
            codigo, nombre, tarifa, especialidad
        )

    else:
        print("Tipo de servicio no valido.")
        return

    gestor.registrar_servicio(servicio)

    print("Servicio registrado correctamente.")


def consultar_clientes(gestor):
    """Muestra todos los clientes registrados."""

    print("\n--- CLIENTES REGISTRADOS ---")

    clientes = gestor.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(
            f"{cliente.codigo} | "
            f"{cliente.nombre}"
        )


def consultar_servicios(gestor):
    """Muestra todos los servicios registrados."""

    print("\n--- SERVICIOS REGISTRADOS ---")

    servicios = gestor.listar_servicios()

    if not servicios:
        print("No hay servicios registrados.")
        return

    for servicio in servicios:
        print(servicio.describir())


def crear_nueva_reserva(gestor):
    """Crea una reserva a partir de un cliente y servicio."""

    print("\n--- CREAR RESERVA ---")

    codigo = input("Codigo de reserva: ").strip()
    codigo_cliente = input("Codigo del cliente: ").strip()
    codigo_servicio = input("Codigo del servicio: ").strip()

    duracion = float(input("Duracion en horas: "))

    servicio = gestor.buscar_servicio(codigo_servicio)

    cantidad = None

    if isinstance(servicio, AlquilerEquipo):
        cantidad = int(input("Cantidad de equipos solicitados: "))

    reserva = gestor.crear_reserva(
        codigo,
        codigo_cliente,
        codigo_servicio,
        duracion,
        cantidad
    )

    print("Reserva creada correctamente.")
    print(reserva.describir())


def consultar_reservas(gestor):
    """Muestra todas las reservas registradas."""

    print("\n--- RESERVAS REGISTRADAS ---")

    reservas = gestor.listar_reservas()

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.describir())


def confirmar_reserva(gestor):
    """Confirma una reserva pendiente."""

    codigo = input("Codigo de reserva: ").strip()

    reserva = gestor.buscar_reserva(codigo)

    print(reserva.confirmar())


def cancelar_reserva(gestor):
    """Cancela una reserva permitida."""

    codigo = input("Codigo de reserva: ").strip()

    reserva = gestor.buscar_reserva(codigo)

    print(reserva.cancelar())


def procesar_reserva(gestor):
    """Procesa una reserva confirmada."""

    codigo = input("Codigo de reserva: ").strip()

    reserva = gestor.buscar_reserva(codigo)

    impuesto = float(input("Impuesto (%): "))
    descuento = float(input("Descuento (%): "))

    costo = reserva.procesar(
        impuesto=impuesto,
        descuento=descuento
    )

    print("Reserva procesada correctamente.")
    print(f"Costo final: ${costo:,.2f}")
    print("Estado:", reserva.estado)


def main():
    """Ejecuta el programa principal."""

    gestor = GestorSoftwareFJ()

    registrar_evento("Aplicacion principal iniciada.")

    print("\nBienvenido al sistema Software FJ.")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        try:

            if opcion == "1":
                registrar_nuevo_cliente(gestor)

            elif opcion == "2":
                registrar_nuevo_servicio(gestor)

            elif opcion == "3":
                consultar_clientes(gestor)

            elif opcion == "4":
                consultar_servicios(gestor)

            elif opcion == "5":
                crear_nueva_reserva(gestor)

            elif opcion == "6":
                consultar_reservas(gestor)

            elif opcion == "7":
                confirmar_reserva(gestor)

            elif opcion == "8":
                cancelar_reserva(gestor)

            elif opcion == "9":
                procesar_reserva(gestor)

            elif opcion == "0":

                registrar_evento(
                    "Aplicacion principal finalizada."
                )

                print("Gracias por utilizar Software FJ.")
                break

            else:
                print("Opcion no valida. Intente nuevamente.")

        except (ValueError, TypeError) as error:

            registrar_error(
                "Error en los datos ingresados",
                error
            )

            print("Error: verifique los datos ingresados.")

        except Exception as error:

            registrar_error(
                "Error durante la operacion del sistema",
                error
            )

            print("Operacion no realizada:", error)


if __name__ == "__main__":
    main()
