# Proyecto: Aplicación Flask de Gestión de Prompts

## Instrucciones Generales:

- Al generar nuevo código Python, por favor, sigue el estilo de codificación existente.
- Asegúrate de que todas las nuevas funciones y clases tengan comentarios claros y concisos.
- Prioriza la claridad y la legibilidad del código.
- Todo el código debe ser compatible con Python 3.8+.

## Estilo de Codificación:

- Usa 4 espacios para la indentación (PEP 8).
- Nombres de variables y funciones en `snake_case`.
- Nombres de clases en `CamelCase`.
- Utiliza f-strings para formatear cadenas cuando sea apropiado.

## Componentes Específicos:

### `app.py`
- Contiene la lógica principal de la aplicación Flask, definición de rutas y manejo de solicitudes.
- Asegúrate de que las rutas incluyan manejo de errores robusto y validación de entrada.

### `templates/`
- Contiene las plantillas Jinja2 para la interfaz de usuario.
- Asegúrate de que las plantillas sean reutilizables y sigan las mejores prácticas de Jinja2.

### `static/style.css`
- Contiene los estilos CSS de la aplicación.
- Sigue una estructura CSS organizada y utiliza selectores eficientes.

### Base de Datos (`prompts.db`, `schema.sql`)
- La aplicación utiliza SQLite para la persistencia de datos.
- `schema.sql` define la estructura de la base de datos.
- Asegúrate de que las interacciones con la base de datos sean seguras y eficientes.

## Respecto a las Dependencias:

- Evita introducir nuevas dependencias externas a menos que sea absolutamente necesario.
- Si se requiere una nueva dependencia, por favor, justifica la razón.