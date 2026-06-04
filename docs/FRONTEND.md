# Directrices de Frontend - FlaskPrompt AI

Este documento contiene las especificaciones y lineamientos de diseño, maquetado e interactividad de la interfaz de usuario de FlaskPrompt AI.

## 🎨 Paleta de Colores y Modo Claro/Oscuro

La aplicación implementa un sistema dinámico de temas (Light/Dark) basado en variables CSS (`:root` y `body.light-mode`).

### Modo Oscuro (Premium Slate - Predeterminado)
- **Fondo General (`--bg-main`)**: `#0f172a` (Slate 900)
- **Barra Lateral (`--sidebar-bg`)**: `#1e293b` (Slate 800)
- **Tarjetas (`--card-bg`)**: `rgba(30, 41, 59, 0.7)` (Slate 800 translúcido con desenfoque de fondo de 12px)
- **Acento Primario (`--accent-primary`)**: `#22d3ee` (Cyan 400)
- **Acento Secundario (`--accent-secondary`)**: `#c084fc` (Purple 400)

### Modo Claro (Minimalist Professional)
- **Fondo General (`--bg-main`)**: `#f8fafc` (Slate 50)
- **Barra Lateral / Tarjetas**: `#ffffff`
- **Acento Primario (`--accent-primary`)**: `#0891b2` (Cyan 600)
- **Acento Secundario (`--accent-secondary`)**: `#9333ea` (Purple 600)

---

## 🏷️ Sistema de Filtrado de Categorías

Las pestañas de categoría se generan de forma 100% dinámica en el lado del cliente (JS) al cargar la página principal:
1. El script lee el atributo `data-category` de cada elemento `.prompt-card` renderizado.
2. Crea un conjunto (`Set`) de categorías únicas.
3. Genera botones `.tab-pill` dinámicos en el contenedor `#category-tabs`.
4. El filtrado oculta/muestra tarjetas usando la propiedad `display: none !important;` (asignada mediante la clase `.hidden`) para asegurar que la reordenación visual sea instantánea y que los lectores de pantalla actualicen correctamente el árbol de accesibilidad.

---

## 📋 Botones de Copiado con Optimistic UI

Para garantizar una experiencia fluida, el copiado de prompts utiliza un patrón de **UI Optimista**:
1. Al hacer clic en un botón de copiado (`.copy-btn`), la interfaz cambia **inmediatamente** a un estado de éxito (`✓ Copied!`) para evitar latencias.
2. Por detrás, se intenta escribir en el portapapeles usando la API asíncrona `navigator.clipboard.writeText`.
3. Si la API es bloqueada por seguridad del navegador (ej. en navegadores headless, automatizaciones o sandboxes), se ejecuta automáticamente un fallback silencioso con un elemento `<textarea>` temporal y `document.execCommand('copy')`.

---

## 🪄 Panel de Variables y Previsualizador de Terminal

En la vista de detalles (`templates/view_prompt.html`), la aplicación detecta marcadores de variables:
- **Formatos soportados**: Doble llave `{{variable}}` y corchetes `[variable]`.
- **Panel de Relleno**: Si se detectan variables, se muestra el panel `#variables-panel` y se generan campos de entrada de texto (`<input type="text">`) en tiempo real para cada marcador único.
- **Terminal de Previsualización (`#terminal-preview`)**: Emula una terminal retro oscura. Utiliza etiquetas `<mark>` para resaltar con color cian las variables pendientes y con color morado las variables que el usuario va rellenando.
