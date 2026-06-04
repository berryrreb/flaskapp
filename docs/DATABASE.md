# Directrices de Base de Datos - FlaskPrompt AI

La aplicación utiliza SQLite3 como motor de base de datos debido a su ligereza, velocidad y facilidad de configuración sin dependencias pesadas de infraestructura.

## 🗄️ Esquema de la Base de Datos (`schema.sql`)

El esquema consta de una única tabla llamada `prompts` que almacena los prompts de IA creados por el usuario:

```sql
DROP TABLE IF EXISTS prompts;

CREATE TABLE prompts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category TEXT
);
```

### Columnas:
1.  `id`: Entero autoincremental que actúa como Clave Primaria.
2.  `title`: Cadena de texto obligatoria (`NOT NULL`) para el título identificativo del prompt.
3.  `content`: Cadena de texto obligatoria (`NOT NULL`) que contiene el prompt con sus marcadores y variables.
4.  `category`: Cadena de texto opcional para fines de clasificación y filtrado.

---

## 🔌 Patrón de Conexión y Persistencia

Para interactuar de manera segura y eficiente con SQLite3 en Flask, se utiliza el patrón de conexión por solicitud mediante una función helper:

```python
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas como si fuera un diccionario
    return conn
```

### Inicialización de la Base de Datos:
El comando de terminal `flask init-db` está registrado en la interfaz de comandos (CLI) de Flask usando Click. Ejecuta la función `init_db()` la cual lee y aplica recursivamente el script `schema.sql` para borrar y recrear la tabla.

---

## 🔒 Buenas Prácticas de Consultas SQL

Toda consulta SQL que involucre parámetros proporcionados por el usuario **debe utilizar placeholders (`?`)** para realizar consultas preparadas y parametrizadas de SQLite3. Esto garantiza inmunidad total frente a ataques de **SQL Injection**.

*Ejemplo de Consulta Parametrizada Segura:*
```python
# SEGURO - Uso de placeholders
query = 'SELECT * FROM prompts WHERE title LIKE ? OR category LIKE ?'
prompts = conn.execute(query, (f'%{search_query}%', f'%{search_query}%')).fetchall()
```

*Práctica Prohibida (Insegura):*
```python
# INSEGURO - ¡Nunca concatenar strings o usar f-strings directamente en la consulta SQL!
query = f"SELECT * FROM prompts WHERE title LIKE '%{search_query}%'"
```
