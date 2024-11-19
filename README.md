# Base de Datos No Relacional - Base Builders

![Coverage](https://raw.githubusercontent.com/pybalt/uade-algo1-tp-integrador/9d72a1a6b6b729a2eca1d8d38a3300fb82fb7a93/coverage.svg)

Una base de datos no relacional implementada en Python que permite almacenar y manipular documentos con tipos de datos personalizados.

## Características Principales

- Almacenamiento de documentos en formato JSON
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Búsqueda por expresiones regulares
- Operaciones de conjuntos entre bases de datos (unión, intersección, diferencia)
- Interfaz de consola interactiva con colores y animaciones
- Validación de tipos de datos
- Análisis de código automatizado

## Estructura del Proyecto
```
├── console/
│ ├── README.md
│ ├── __init__.py
│ ├── databases.py
│ └── documents.py
├── database/
│ ├── __init__.py
│ ├── directory.py
│ ├── functions.py
│ └── test_database.py
├── documents/
│ ├── __init__.py
│ └── functions.py
├── utils/
│ └── __init__.py
├── data/
│ ├── directory.json
│ ├── animales.py
│ └── mascotas.json
├── .github/workflows/
├── app.py
└── __main__.py
```

## Tipos de Datos Soportados

- `str`: Cadenas de texto
- `int`: Números enteros
- `float`: Números decimales
- `tuple`: Tuplas
- `list`: Listas
- `set`: Conjuntos
- `matrix`: Matrices

## Operaciones Disponibles

### Bases de Datos
- Listar bases de datos
- Crear nueva base de datos
- Acceder a una base de datos
- Unión de bases de datos
- Intersección de bases de datos
- Diferencia de bases de datos
- Diferencia simétrica de bases de datos

### Documentos
- Crear documento
- Listar documentos
- Eliminar documento
- Filtrar documentos por ID
- Editar documento
- Buscar documento por patrón
- Mostrar documentos únicos

## Integración Continua

El proyecto incluye flujos de trabajo de GitHub Actions para:
- Análisis estático de código
- Verificación de características por sprint
- Pruebas unitarias
- Cobertura de código

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/uade-algo1-tp-integrador.git
```

## Uso

Para iniciar la aplicación:

```bash
py uade-algo1-tp-integrador
```

## Desarrollo

El proyecto está estructurado en sprints incrementales, cada uno agregando nuevas funcionalidades:

- Sprint 1: Estructuras de datos básicas
- Sprint 2: Funciones de orden superior y operaciones de archivos
- Sprint 3: Expresiones regulares
- Sprint 4: Manejo de excepciones
- Sprint 5: Recursión y pruebas unitarias