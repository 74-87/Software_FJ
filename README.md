SOFTWARE FJ

Sistema Integral de Gestión de Clientes, Servicios y Reservas

1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite administrar clientes, servicios y reservas mediante programación orientada a objetos.

El sistema está diseñado para gestionar tres tipos de servicios:

Reservas de salas.

Alquiler de equipos.

Asesorías especializadas.

La aplicación permite registrar clientes, administrar servicios, crear reservas, confirmar, cancelar y procesar operaciones, incorporando validaciones y manejo de excepciones.

El proyecto no utiliza bases de datos. La información se administra mediante objetos y listas internas, mientras que los archivos se utilizan para registrar eventos y errores.

2. Objetivo general

Desarrollar un sistema modular y funcional que permita gestionar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos, validaciones y manejo avanzado de excepciones.

3. Tecnologías utilizadas

Lenguaje de programación: Python.

Entorno de desarrollo: Visual Studio Code.

Sistema operativo de desarrollo: Windows 11.

Registro de eventos: biblioteca logging de Python.

Organización del código: módulos independientes.

Almacenamiento de información: listas y objetos en memoria.

4. Arquitectura del proyecto

El sistema está organizado en los siguientes módulos:

Archivo

Descripción

entidades.py

Define la entidad abstracta general.

clientes.py

Implementa la clase Cliente y sus validaciones.

servicios.py

Implementa los servicios especializados.

reservas.py

Gestiona la creación y los estados de las reservas.

excepciones.py

Contiene las excepciones personalizadas.

gestor.py

Administra las listas de clientes, servicios y reservas.

registro.py

Configura el registro de eventos y errores.

pruebas.py

Ejecuta las pruebas integrales del sistema.

main.py

Contiene el menú y el punto de entrada principal.

README.md

Documentación técnica del proyecto.

5. Principios de programación orientada a objetos

El desarrollo aplica los siguientes principios:

Abstracción: se utiliza una clase abstracta Entidad para establecer una estructura general.

Herencia: las clases especializadas reutilizan características de sus clases base.

Encapsulación: se utilizan atributos internos y propiedades para controlar el acceso a los datos.

Polimorfismo: los servicios especializados implementan comportamientos propios para describir, validar y calcular sus costos.

Validación: se comprueban los datos ingresados y los parámetros necesarios para las operaciones.

6. Gestión de servicios

El sistema contempla tres tipos de servicios:

ServicioSala: administración de reservas de salas.

AlquilerEquipo: administración del alquiler de equipos.

AsesoriaEspecializada: gestión de servicios de asesoría.

Cada servicio cuenta con parámetros y validaciones según sus características.

Los cálculos de costos permiten utilizar parámetros opcionales para impuestos y descuentos.

7. Gestión de reservas

La clase Reserva integra:

Código de reserva.

Cliente asociado.

Servicio solicitado.

Duración.

Estado.

Costo calculado.

Los estados implementados son:

PENDIENTE.

CONFIRMADA.

CANCELADA.

PROCESADA.

El sistema controla las operaciones permitidas y evita transiciones incorrectas mediante excepciones.

8. Manejo de excepciones

El proyecto incorpora excepciones personalizadas para controlar situaciones como:

Datos inválidos.

Clientes inexistentes.

Servicios no disponibles.

Reservas incorrectas.

Operaciones no permitidas.

Errores durante los cálculos.

También utiliza estructuras try/except, try/except/else, try/except/finally y encadenamiento de excepciones en las pruebas correspondientes.

9. Registro de eventos y errores

Se utiliza la biblioteca logging de Python para registrar acontecimientos importantes y errores.

El archivo de registro se encuentra en:

logs/software_fj.log

Los registros incluyen fecha, hora, nivel del mensaje y descripción del acontecimiento.

10. Instalación y ejecución

Requisitos:

Tener Python instalado.

Tener Visual Studio Code o una terminal compatible.

Disponer de los archivos del proyecto.

Ejecución del sistema:

Abrir la terminal en la carpeta Software_FJ y ejecutar:

python main.py

Ejecución de las pruebas integrales:

python pruebas.py

Comprobación de sintaxis:

python -m py_compile main.py

11. Pruebas realizadas

Se implementaron 11 operaciones de prueba para comprobar el comportamiento del sistema.

Las pruebas contemplan:

Registro válido de clientes.

Rechazo de datos inválidos.

Registro de clientes adicionales.

Creación de servicios de sala.

Creación de servicios de alquiler de equipos.

Rechazo de servicios con parámetros incorrectos.

Creación, confirmación y procesamiento de reservas.

Rechazo de reservas de servicios no disponibles.

Control de clientes inexistentes.

Rechazo de registros duplicados.

Encadenamiento de excepciones.

Resultado de la ejecución documentada:

Operaciones ejecutadas: 11.

Operaciones aprobadas: 11.

Operaciones fallidas: 0.

12. Consideraciones y limitaciones

La información de clientes, servicios y reservas permanece en memoria durante la ejecución del programa.

Al cerrar la aplicación, las listas se reinician, ya que el proyecto no utiliza bases de datos ni persistencia de registros comerciales.

Los archivos de registro conservan los eventos y errores generados durante las ejecuciones.

13. Conclusión

El proyecto Software FJ integra módulos de clientes, servicios y reservas mediante programación orientada a objetos.

Las pruebas realizadas permitieron verificar operaciones válidas e inválidas, el control de excepciones, los cálculos de costos y la continuidad de la aplicación ante situaciones de error.

El sistema constituye una solución modular de gestión desarrollada en Python, sin utilización de motores de bases de datos.