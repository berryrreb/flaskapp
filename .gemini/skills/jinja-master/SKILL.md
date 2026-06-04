---
name: jinja-master
description: Directrices expertas para maquetación modular con plantillas Jinja2 y escape seguro de variables en Flask.
---

# Skill: Dominio de Plantillas Jinja2 (jinja-master)

Esta habilidad proporciona pautas de ingeniería para estructurar plantillas Jinja2 de manera segura, reutilizable y eficiente en Flask.

## 📝 Directrices:
1.  **Modularización**: Separa componentes lógicos repetitivos (ej: headers, footers, sidebars) utilizando herencia de plantillas (`{% extends %}`) o inclusiones (`{% include %}`).
2.  **Manejo de Valores Nulos**: Utiliza filtros por defecto (ej. `{{ prompt.category or 'Sin Categoría' }}`) para prevenir renderizados vacíos o con errores visuales.
3.  **Inyección Segura**: Jinja2 escapa variables por defecto. Sin embargo, si necesitas transferir strings que contienen caracteres especiales a variables de JavaScript dentro de tags `<script>`, **nunca las concatenes directamente**. Utiliza atributos de datos HTML (`data-*`) en elementos del DOM ocultos (`display: none`) para leerlos de forma segura con `textContent` en JS.
