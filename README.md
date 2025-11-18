# Aplicación de Gestión de Prompts

Esta es una aplicación web simple construida con Flask para gestionar una colección de prompts. Permite a los usuarios agregar, ver, editar y eliminar prompts.

## Prerrequisitos

- Python 3.8+
- pip

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/berryrreb/flaskapp.git
    cd flaskapp
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *(En Windows, usa `venv\Scripts\activate`)*

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos

La aplicación utiliza SQLite para la base de datos. Para crear la base de datos y la tabla inicial, ejecuta el siguiente comando en tu terminal:

```bash
flask init-db
```

Esto creará un archivo `prompts.db` en el directorio del proyecto.

## Ejecución de la Aplicación

Una vez que la base de datos esté inicializada, puedes ejecutar la aplicación de dos maneras:

1.  **Usando el comando `flask`:**

    ```bash
    flask run
    ```

2.  **Ejecutando el script de Python directamente:**

    ```bash
    python3 app.py
    ```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## Uso

-   **Página principal (`/`):** Muestra todos los prompts guardados.
-   **Añadir Prompt (`/add`):** Permite crear un nuevo prompt.
-   **Ver Prompt (`/prompt/<id>`):** Muestra un prompt específico.
-   **Editar Prompt (`/edit/<id>`):** Permite modificar un prompt existente.
-   **Eliminar Prompt (`/delete/<id>`):** Elimina un prompt (se accede a través de un botón en la página principal).
