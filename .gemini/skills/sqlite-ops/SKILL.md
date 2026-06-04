---
name: sqlite-ops
description: Directrices de optimización, persistencia, conexiones eficientes y parametrización en SQLite3.
---

# Skill: Operaciones de SQLite3 Eficientes y Seguras (sqlite-ops)

Esta habilidad proporciona las mejores prácticas de interacción con bases de datos relacionales locales SQLite3 en entornos de Flask.

## 📝 Directrices:
1.  **Conexión Segura**: Utiliza la función `get_db_connection()` para crear una conexión limpia por solicitud de Flask, y recuerda cerrar la conexión con `conn.close()` en bloques `finally` o después de cada consulta para evitar fugas de recursos.
2.  **Row Factory**: Configura siempre `conn.row_factory = sqlite3.Row` para poder interactuar con los registros obtenidos tanto por índice numérico como por nombre de columna.
3.  **Placeholders obligatorios**: **Nunca concatenes variables** de entrada del usuario directamente dentro de sentencias SQL. Usa placeholders de interrogación `?` y pasa los parámetros como tupla (ej: `conn.execute('SELECT * FROM prompts WHERE id = ?', (prompt_id,))`).
