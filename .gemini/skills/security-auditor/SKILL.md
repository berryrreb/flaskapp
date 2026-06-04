---
name: security-auditor
description: Skill experta en análisis de seguridad, mitigación de inyección SQL, prevención de XSS y protección de secretos.
---

# Skill: Auditoría y Saneamiento de Seguridad (security-auditor)

Esta habilidad recopila directrices de ciberseguridad defensiva críticas para blindar la aplicación FlaskPrompt AI.

## 📝 Directrices:
1.  **Inyección SQL**: Cualquier código de persistencia debe evaluarse bajo la regla estricta de consultas parametrizadas. El uso de f-strings en SQL es considerado un hallazgo crítico de seguridad.
2.  **Cross-Site Scripting (XSS)**: Neutraliza la ejecución de scripts. En la vista detallada de prompts, sanea cualquier previsualización HTML mediante funciones nativas de escape (`escapeHtml`) antes de inyectar contenido con `.innerHTML`.
3.  **Exposición de Secretos**: El linter o el agente debe alertar inmediatamente si detecta contraseñas crudas, claves secretas o variables sensibles escritas directamente en el código. Exige la extracción a un archivo `.env` externo y verifica su registro en `.gitignore`.
