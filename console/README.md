# Módulo Console

El módulo `console` está diseñado para gestionar y renderizar una interfaz de consola interactiva en entornos Windows. Proporciona funcionalidades avanzadas para la manipulación de bases de datos y documentos, así como herramientas para mejorar la experiencia del usuario a través de mensajes coloridos y animaciones.

## Tabla de Contenidos

- [Características](#características)
- [Estructura del Módulo](#estructura-del-módulo)
  - [`__init__.py`](#__init__.py)
  - [`databases.py`](#databasespy)
  - [`documents.py`](#documentspy)


- **Renderizado Dinámico**: Actualiza la consola en tiempo real con datos dinámicos.
- **Gestión de Bases de Datos**: Interactúa con múltiples bases de datos utilizando operaciones de conjuntos.
- **Gestión de Documentos**: Crea, lista, elimina y edita documentos dentro de una base de datos.
- **Mensajes Animados y Coloreados**: Mejora la experiencia del usuario con mensajes animados y en colores.
- **Interfaz Interactiva**: Menús interactivos para facilitar la navegación y operación dentro de la consola.

## Estructura del Módulo

### `__init__.py`

Este archivo configura el entorno de la consola para entornos Windows, habilitando secuencias ANSI para colores y configuraciones avanzadas. Además, proporciona funciones utilitarias para imprimir mensajes con animaciones y colores.

#### Funciones Principales

- **Configuración Inicial**: Habilita el modo ANSI en la consola de Windows.

- **Funciones de Log**:
  - `log(*args)`: Imprime mensajes normales.
  - `error(*args)`: Imprime mensajes de error en rojo.
  - `warning(*args)`: Imprime advertencias en amarillo.

+ **Cambio de Colores**: Las funciones de log utilizan secuencias ANSI para cambiar el color del texto en la consola. Por ejemplo, `\033[91m` para rojo en errores y `\033[93m` para amarillo en advertencias. Estas secuencias permiten resaltar mensajes específicos, mejorando la legibilidad y proporcionando una mejor experiencia al usuario.

+ **Implementación de Animaciones**: La función `ellipsis()` implementa una animación de puntos suspensivos utilizando un bucle que imprime puntos incrementales con retrasos de tiempo gracias a `time.sleep()`. Esto brinda retroalimentación visual al usuario durante operaciones en curso, haciendo la interfaz más dinámica.

+ **Uso de `flush`**: En las funciones de impresión, se utiliza el parámetro `flush=True` en las llamadas a `print` para asegurar que el texto se muestre inmediatamente en la consola sin esperar a llenar el buffer. Esto es esencial para que las animaciones y mensajes aparezcan en tiempo real, manteniendo la sincronización con las acciones del programa.

+ **Módulos Utilizados**:
  - `msvcrt`: Biblioteca específica de Windows utilizada para operaciones de consola de bajo nivel, como la lectura de caracteres sin bloquear la ejecución. Es fundamental para la implementación de menús interactivos y la detección de entradas de teclado.
  
  - `ctypes` y `kernel32`: Se emplean para interactuar con la API de Windows, permitiendo configurar el modo de la consola para soportar secuencias ANSI y habilitar características avanzadas como el procesamiento de salida virtual de terminal. `kernel32` en particular facilita la configuración del entorno de la consola para mejoras visuales y funcionales.

- **Menús Interactivos**:
  - `show_options_menu(options: list[str], title: str) -> str`: Muestra un menú interactivo para que el usuario seleccione opciones.

### `databases.py`

Gestiona las operaciones relacionadas con las bases de datos dentro de la consola.

#### Funciones Principales

- **`list_databases(directory: dict) -> None`**: Lista las bases de datos disponibles en un directorio específico.
- **`show_menu() -> str`**: Muestra un menú con las operaciones disponibles para gestionar bases de datos, como listar, acceder, crear, unir, intersecar, y diferenciar bases de datos.
- **`show_set_operation(dataset: dict) -> None`**: Muestra el resultado de una operación de conjunto aplicada a las bases de datos.

### `documents.py`

Encargado de gestionar las operaciones relacionadas con documentos dentro de una base de datos.

#### Funciones Principales

- **`show_menu(database_name: str) -> None`**: Muestra un menú con las operaciones disponibles para gestionar documentos dentro de una base de datos específica.
- **`list_documents(database: dict) -> None`**: Lista los documentos almacenados en una base de datos, permitiendo al usuario verlos en segmentos según su preferencia.