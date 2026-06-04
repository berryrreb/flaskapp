# Directrices de Seguridad - FlaskPrompt AI

Este documento recopila las políticas y lineamientos de seguridad obligatorios aplicados en FlaskPrompt AI para salvaguardar la integridad de la base de datos, evitar la inyección de código malicioso y proteger los datos en entornos locales y de producción.

## 🛡️ 1. Prevención de Inyección SQL

La inyección SQL (SQLi) es mitigada por completo forzando el uso de consultas parametrizadas en todas las interacciones con SQLite3.
- **Placeholder**: SQLite3 utiliza el carácter de interrogación `?` como placeholder para los parámetros.
- **Regla**: Queda estrictamente prohibido el uso de concatenación de cadenas (`+`), formateo de cadenas tradicional (`%s`) o `f-strings` para inyectar variables del usuario de manera directa en consultas SQL.

---

## 🌐 2. Saneamiento contra Cross-Site Scripting (XSS)

El Cross-Site Scripting (XSS) ocurre cuando un atacante inyecta scripts de JS en el contenido que se renderiza dinámicamente en las páginas del cliente.

### Medidas de Mitigación en FlaskPrompt AI:
1.  **Escape Automático de Jinja2**: Por defecto, Jinja2 escapa de forma segura todo el texto inyectado en las plantillas (convirtiendo `<` en `&lt;`, `>` en `&gt;`, etc.). Esto evita que etiquetas `<script>` se ejecuten en las tarjetas del dashboard.
2.  **Escape Seguro en Bloques de Script (Javascript)**: Al transferir texto del prompt desde Jinja2 a variables de JavaScript en las plantillas (como en `view_prompt.html`), el texto nunca debe concatenarse directamente en el script. En su lugar, se lee desde el DOM desde un contenedor seguro oculto con `display: none` (`.prompt-content-raw`), o se procesa con una función sanitizadora de JS como `escapeHtml()` para neutralizar caracteres HTML peligrosos antes de renderizar la previsualización en vivo en el terminal `#terminal-preview`.

---

## 🔑 3. Gestión de Secretos y Configuración

- **Credenciales y Tokens**: No se deben guardar, imprimir en consola o subir a sistemas de control de versiones (Git) credenciales como contraseñas, claves secretas (`SECRET_KEY`) o tokens de API de LLMs.
- **Variables de Entorno**: Se deben almacenar en un archivo `.env` local que **debe estar listado obligatoriamente en `.gitignore`** para evitar su subida accidental al repositorio.
- **Clave Secreta de Flask**: Si se introduce protección contra ataques de falsificación de solicitudes en sitios cruzados (CSRF) mediante formularios seguros, se debe configurar una variable de entorno `FLASK_SECRET_KEY` para firmar de forma segura las cookies de sesión de Flask.
