---
name: openapi-gen
description: Estándares de documentación técnica para mapear endpoints, parámetros y respuestas en formato OpenAPI.
---

# Skill: Documentación de APIs con OpenAPI (openapi-gen)

Esta habilidad estandariza la documentación de endpoints de FlaskPrompt AI en formato amigable de especificación de APIs.

## 📝 Directrices:
1.  **Estructura del Endpoint**: Documenta el método (GET, POST), la ruta exacta (ej. `/prompt/<int:prompt_id>`), y los parámetros de URL.
2.  **Esquemas de Entrada y Salida**: Detalla los campos requeridos en el cuerpo de la solicitud de formulario (`application/x-www-form-urlencoded`) y el tipo de dato de cada uno.
3.  **Códigos de Respuesta HTTP**: Mapea los códigos HTTP esperados ante llamadas exitosas (`200 OK`, `302 Found`) y fallidas (`400 Bad Request`, `404 Not Found`, `500 Internal Error`).
