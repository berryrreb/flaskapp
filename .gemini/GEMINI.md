# Índice de Directrices y Contexto - FlaskPrompt AI

Este archivo actúa como el núcleo de contexto del proyecto para Gemini CLI y el equipo de desarrollo. Utiliza directrices modulares integradas para estructurar de manera óptima las instrucciones del sistema.

---

## 📂 Directrices de Ingeniería Especializadas

@docs/FRONTEND.md
@docs/BACKEND.md
@docs/DATABASE.md
@docs/SECURITY.md

---

## ⚙️ Configuración de Gemini CLI y Browser Agent (Para el Equipo)

Este repositorio incluye una configuración preestablecida en `.gemini/settings.json` para facilitar las pruebas locales y el uso de los agentes autónomos de automatización.

### Requisitos Previos para el Equipo:

1.  **Configuración en Google Cloud (Administrador)**:
    Asegúrate de que en la consola de Google Cloud, bajo **Admin for Gemini > Settings**, la opción de **Release channels for Gemini Code Assist in local IDEs** esté configurada en **Preview**.

2.  **Variable de Entorno Local**:
    Antes de utilizar el CLI en el proyecto, exporta el ID de tu proyecto de Google Cloud con licencia de Gemini Code Assist Standard:
    ```bash
    export GOOGLE_CLOUD_PROJECT="tu-id-de-proyecto-gcp"
    ```

3.  **Uso del Browser Agent**:
    Con esta configuración local, el `browser_agent` tiene permiso para navegar en `localhost`, lo que te permitirá realizar pruebas automatizadas directamente sobre tu servidor de desarrollo Flask en ejecución.
