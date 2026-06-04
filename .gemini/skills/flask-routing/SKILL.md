---
name: flask-routing
description: Prácticas recomendadas para la creación de endpoints, rutas de Flask, validación de formularios y respuestas semánticas.
---

# Skill: Desarrollo de Rutas de Flask (flask-routing)

Esta habilidad guía al desarrollador en la especificación correcta de endpoints de servidor en Flask, verbos HTTP y lógica de control.

## 📝 Directrices:
1.  **Métodos HTTP Explícitos**: Declara siempre los métodos que la ruta acepta (ej. `@app.route('/add', methods=('GET', 'POST'))`).
2.  **Validación de Entradas**: Antes de procesar datos en peticiones `POST`, valida que los campos requeridos estén presentes en `request.form` (ej. `title = request.form['title']`) y que no sean strings vacíos.
3.  **Redirecciones Seguras**: Tras un POST exitoso que muta el estado (creación, edición, eliminación), realiza siempre un redirect usando `redirect(url_for('index'))` para cumplir con el patrón Post/Redirect/Get (PRG) y evitar reenvíos accidentales de formularios.
4.  **Respuestas de Error Semánticas**: Si un recurso consultado por ID no existe, retorna explícitamente un código de estado de error (ej. `"Not Found", 404`).
