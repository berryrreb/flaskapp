---
name: mermaid-diagrammer
description: Guía experta de sintaxis Mermaid.js para crear diagramas de flujo, secuencia y ERDs legibles en Markdown.
---

# Skill: Diagramación Técnica con Mermaid.js (mermaid-diagrammer)

Esta habilidad dota de conocimiento técnico exhaustivo sobre la sintaxis de **Mermaid.js** para diagramar flujos de sistema y presentarlos de forma interactiva en archivos Markdown.

## 📝 Directrices:

1.  **Diagramas de Flujo (`graph` / `flowchart`)**:
    - Dirección preferida: De arriba a abajo (`TD` o `TB`) o de izquierda a derecha (`LR`).
    - Nodos con formas semánticas: Rectángulos `[Texto]` para procesos, rombos `{"Decisión?"}` para condiciones, bordes redondeados `(Inicio/Fin)`.
    - Conectores con texto: `-->|"Texto descriptivo"|` para flujos claros.

2.  **Diagramas de Secuencia (`sequenceDiagram`)**:
    - Define claramente los participantes (`participant`) y actores (`actor`).
    - Usa mensajes síncronos `->>` y respuestas asíncronas o de retorno `-->>`.
    - Incorpora bloques de activación (`activate` / `deactivate`) para mostrar el tiempo de vida de la ejecución de solicitudes en el servidor.

3.  **Diagramas de Entidad-Relación (`erDiagram`)**:
    - Estructura las tablas con sus tipos de datos y restricciones (ej: `id INTEGER PK`).
    - Mapea cardinalidades claras (ej: `one-to-many` usando `||--o{`).

4.  **Ejemplo Práctico de Sintaxis de Flujo**:
    ```mermaid
    flowchart LR
        Usuario((Usuario)) -->|Hace clic en Copy| Boton[Botón de Tarjeta]
        Boton -->|Acción optimista| UI[Texto cambia a Copied!]
        Boton -->|Async Clip| Clip[Copia al portapapeles]
    ```
