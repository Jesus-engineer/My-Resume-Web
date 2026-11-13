---
name: ats-resume-engineer
description: >-
  Audits, optimizes, tailors, and builds ATS-friendly 1-page software engineering
  resumes (PDF) grounded in Tech Interview Handbook, r/EngineeringResumes,
  Harvard CS, and The Pragmatic Engineer standards. Use when the user asks to
  improve their CV, pass ATS/company filters, tailor their resume to a job
  posting, or regenerate the downloadable PDF resume.
---

# ATS Resume Engineer

Skill para auditar, redactar y generar hojas de vida técnicas capaces de superar
filtros automáticos (**ATS** como Workday, Greenhouse, Lever) y la revisión
rápida de reclutadores y *engineering managers*.

## Reglas innegociables

1. **Cero invención:** todos los hechos, fechas, tecnologías, cargos y métricas
   deben provenir de `content.md` o de confirmación explícita del usuario. Si
   falta una métrica de impacto, señalarla como `[AGREGAR MÉTRICA SI EXISTE]`
   y nunca inventar números.
2. **Privacidad:** nunca incluir en el PDF público datos marcados `publico: no`
   o sensibles (teléfono personal, número de documento/cédula, enlaces de
   verificación que expongan cédula como Xertify).
3. **Formato ATS estricto (1 página):**
   - Una sola columna con orden de lectura lineal de arriba hacia abajo.
   - Sin tablas de maquetación, sin cajas flotantes, sin fotos, sin iconos
     gráficos ni barras de nivel.
   - Encabezados estándar: Resumen, Educación, Experiencia, Proyectos,
     Habilidades técnicas, Certificaciones.
   - Texto 100 % seleccionable en PDF (nunca texto rasterizado).

## Flujo de trabajo

### 1. Auditar contenido (`content.md`) y vacante objetivo
- Leer [ats-playbook.md](./references/ats-playbook.md) para aplicar la fórmula
  **X-Y-Z** / `[Verbo de acción] + [Tecnología/Contexto] + [Resultado/Alcance]`
  y el orden de secciones según experiencia (estudiante/practicante vs.
  profesional con 2+ años).
- Si el usuario aporta una oferta laboral:
  1. Extraer las palabras clave técnicas reales de la vacante (lenguajes,
     bases de datos, frameworks, prácticas).
  2. Compararlas contra `content.md` y reportar **coincidencias reales** vs.
     **brechas**.
  3. Reordenar viñetas y categorías de habilidades para priorizar lo más
     relevante al rol sin inventar experiencia.

### 2. Generar el PDF ATS de 1 página
Ejecutar desde la raíz del repositorio:

```bash
python .agents/skills/ats-resume-engineer/scripts/build_ats_cv.py
```

Esto genera `assets/cv-jesus-velasquez.pdf` (formato Letter/A4 de 1 página,
una sola columna, enlaces clicables y texto lineal).

### 3. Validar el PDF generado
Ejecutar el auditor automático después de cada generación:

```bash
python .agents/skills/ats-resume-engineer/scripts/audit_ats_pdf.py assets/cv-jesus-velasquez.pdf
```

Criterios de aprobación:
- Exactamente **1 página** (falla si pasa a 2 páginas).
- Texto extraíble completo en orden lógico de lectura.
- Presencia de secciones obligatorias y enlaces de contacto públicos.
- Cero cadenas sensibles filtradas (`telefono`, `730E7489`, `xertify`).

