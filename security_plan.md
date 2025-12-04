# Plan de Seguridad para la Aplicación de Gestión de Prompts

Este documento detalla el análisis de seguridad actual de la aplicación y propone un plan de acción para mitigar vulnerabilidades y fortalecer la postura de seguridad.

## 1. Análisis de Vulnerabilidades

Tras revisar el código fuente (`app.py`, `templates/`, `requirements.txt`), se han identificado los siguientes riesgos:

*   **Falta de Protección CSRF (Cross-Site Request Forgery):** Los formularios (agregar, editar, eliminar) no utilizan tokens CSRF. Esto permite que atacantes forjen solicitudes en nombre de usuarios auténticos sin su consentimiento.
*   **Gestión de Secretos Inexistente:** La aplicación no define una `SECRET_KEY`. Flask requiere una clave secreta para firmar cookies de sesión y para el funcionamiento correcto de extensiones de seguridad.
*   **Modo Debug Activado:** El bloque `if __name__ == '__main__':` ejecuta `app.run(debug=True)`. En un entorno de producción, esto expone información sensible (trazas de pila) y permite la ejecución de código arbitrario mediante el depurador interactivo.
*   **Ausencia de Cabeceras de Seguridad:** No se están configurando cabeceras HTTP de seguridad (como HSTS, X-Content-Type-Options, Content-Security-Policy), dejando la aplicación expuesta a diversos ataques.
*   **Validación de Entrada Limitada:** La validación depende principalmente del frontend o de restricciones básicas de base de datos. Se requiere una validación más robusta en el servidor.
*   **Falta de Autenticación:** Actualmente, cualquiera con acceso a la red puede modificar la base de datos.

## 2. Plan de Acción Inmediata (Prioridad Alta)

Estos pasos deben implementarse lo antes posible para cerrar las brechas de seguridad más críticas.

### 2.1. Configuración de `SECRET_KEY`
**Acción:** Configurar una clave secreta robusta y cargarla desde variables de entorno.
**Implementación:**
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-para-local')
```

### 2.2. Implementar Protección CSRF
**Acción:** Integrar `Flask-WTF` para manejar formularios de manera segura con protección CSRF automática.
**Pasos:**
1.  Agregar `Flask-WTF` a `requirements.txt`.
2.  Inicializar `CSRFProtect` en `app.py`.
3.  Incluir el token CSRF en todos los formularios HTML:
    ```html
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    ```

### 2.3. Desactivar Modo Debug en Producción
**Acción:** Asegurar que `debug=True` no se use fuera del desarrollo local.
**Recomendación:** Eliminar `debug=True` de la llamada `app.run()` y controlar el modo de depuración mediante la variable de entorno `FLASK_DEBUG`.

## 3. Mejoras Recomendadas (Prioridad Media)

### 3.1. Validaciones Robustas con WTForms
**Acción:** Reemplazar el manejo manual de `request.form` con clases de formulario de `WTForms`. Esto centraliza la validación y mejora la seguridad de los datos.

### 3.2. Cabeceras de Seguridad (Security Headers)
**Acción:** Implementar cabeceras HTTP para mejorar la seguridad del navegador.
**Herramienta:** Usar la librería `flask-talisman` o configurar cabeceras manualmente (`Strict-Transport-Security`, `X-Content-Type-Options`, etc.).

## 4. Consideraciones a Largo Plazo

*   **Autenticación y Autorización:** Implementar un sistema de usuarios (p.ej., `Flask-Login`) para restringir el acceso a las funciones de edición y borrado.
*   **Servidor de Producción WSGI:** Utilizar un servidor como **Gunicorn** o **uWSGI** para el despliegue en producción, en lugar del servidor de desarrollo de Flask.
*   **Rate Limiting:** Implementar `Flask-Limiter` para proteger contra ataques de fuerza bruta o denegación de servicio.
