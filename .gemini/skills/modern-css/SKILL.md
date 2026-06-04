---
name: modern-css
description: Guía experta para el diseño de UI moderna, variables CSS, layouts responsivos e interactividad fluida.
---

# Skill: Estilos CSS Modernos y UX (modern-css)

Esta habilidad proporciona reglas deterministas de diseño visual y de experiencia de usuario para garantizar interfaces premium.

## 📝 Directrices:
1.  **Variables en `:root`**: Siempre utiliza variables CSS para definir colores, espaciados y familias tipográficas. Esto facilita la compatibilidad nativa con Modo Oscuro/Claro.
2.  **Transiciones**: Utiliza la función de tiempo cúbica `transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);` para animar hover, foco y transiciones de estados de forma orgánica.
3.  **Layouts Flexibles**: Utiliza CSS Grid para layouts bidimensionales (ej: cuadrículas de tarjetas) y Flexbox para layouts unidimensionales (ej: barras de navegación, botones en fila).
4.  **Optimistic UI**: Implementa estados visuales instantáneos al hacer clic en botones de copia o guardado rápido (ej. clases `.copied` o `.success`) para anular latencias de llamadas asíncronas.
