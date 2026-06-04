# Directrices de Backend - FlaskPrompt AI

Este documento contiene los estándares y especificaciones de desarrollo para el componente de servidor (Python y Flask) de la aplicación.

## 🐍 Cumplimiento de PEP 8 y Estilo

Todo el código de Python desarrollado para el proyecto debe cumplir estrictamente con los estándares de PEP 8 para asegurar la legibilidad y mantenibilidad:
- **Indentación**: Usar exactamente 4 espacios por nivel de indentación (no usar tabuladores).
- **Nomenclatura**:
  - Funciones, métodos y variables: `snake_case` (ej. `get_db_connection`, `prompt_id`).
  - Clases: `CamelCase` (ej. `FlaskAppTestCase`).
  - Constantes: `UPPER_SNAKE_CASE` (ej. `DATABASE`).
- **Líneas de Código**: Limitar el ancho máximo a 79 caracteres cuando sea posible, dividiendo expresiones largas apropiadamente.
- **Cadenas de texto**: Preferir el uso de `f-strings` para el formateo de strings en lugar de concatenaciones o el método `.format()`.

---

## 🎛️ Estructura de app.py y Rutas de Flask

La lógica del backend está centralizada en `app.py`. El flujo de control sigue estas directrices:

### 1. Definición de Rutas y Métodos HTTP
Toda ruta debe definir explícitamente los métodos que soporta:
- `GET /`: Listar y buscar prompts.
- `GET, POST /add`: Agregar un nuevo prompt.
- `GET /prompt/<id>`: Ver los detalles de un prompt individual.
- `GET, POST /edit/<id>`: Modificar un prompt existente.
- `POST /delete/<id>`: Eliminar un prompt de manera segura.

### 2. Manejo de Errores Robustos
- Si un recurso no es encontrado en la base de datos (ej. un `prompt_id` inexistente), la aplicación debe retornar una respuesta HTTP de error apropiada (ej. un mensaje informativo acompañado del código de estado `404 Not Found`).
- Las operaciones que mutan datos (POST en creación, edición y eliminación) deben verificar que la base de datos esté accesible y manejar excepciones apropiadas para evitar caídas del servidor (retornando códigos de error `500` o `400` según corresponda).

---

## 🧪 Estructura de Pruebas Unitarias

La aplicación implementa pruebas unitarias robustas utilizando la librería estándar `unittest`:
- **Base de Datos de Prueba**: En el método `setUp()`, las pruebas crean un archivo SQLite temporal con `tempfile.mkstemp()`, configuran Flask en modo `TESTING = True`, e inicializan el esquema limpio.
- **Limpieza**: El método `tearDown()` se encarga de cerrar la conexión de base de datos de prueba y eliminar el archivo temporal para no dejar basura en el entorno.
- **Ubicación**: Todos los scripts de testing están organizados dentro del directorio de pruebas (ej: `tests/test_app.py` o similar).
