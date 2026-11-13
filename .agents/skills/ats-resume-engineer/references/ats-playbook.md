# Playbook ATS para Ingeniería de Software

Síntesis operativa basada en **Tech Interview Handbook**, **`r/EngineeringResumes` Wiki**,
**Harvard Mignone Center for Career Success (CS/Tech)**, **The Pragmatic Engineer
(*The Tech Resume Inside Out*)** y las plantillas **Jake's Resume** / **RenderCV**.

---

## 1. Reglas de oro para pasar filtros ATS

- **Una sola columna:** los parsers antiguos (Workday, Taleo, iCIMS) leen de
  izquierda a derecha cruzando columnas; dos columnas mezclan fechas, empresas
  y habilidades.
- **Cero gráficos ni barras de habilidades:** los porcentajes ("Python 85 %")
  no significan nada para un ingeniero y los iconos SVG pueden romper la
  extracción de texto.
- **Una sola página:** obligatorio para estudiantes, recién egresados y
  perfiles con menos de 5–7 años de experiencia.
- **Tercio superior ("6-second scan zone"):** nombre, enlace directo a GitHub /
  LinkedIn / correo y perfil objetivo deben responder en 6 segundos qué rol
  buscas y cuál es tu stack principal.
- **Fuentes y PDF limpio:** tipografía estándar sans/serif legible (9.5–11 pt en
  cuerpo), márgenes equilibrados (0.45–0.6 in) y exportación vectorial con texto
  seleccionable.

## 2. Orden de secciones recomendado

### Estudiante / Practicante / Junior (perfil actual)
1. **Encabezado:** Nombre, título breve orientado al rol, ciudad/país,
   correo, LinkedIn, GitHub y web CV.
2. **Resumen (2–3 líneas máx.):** especialidad técnica + qué construyes + qué
   buscas (prácticas / rol junior).
3. **Educación:** carrera, universidad, fecha prevista, énfasis técnico o
   comunidades (IEEE).
4. **Proyectos técnicos:** 2–4 proyectos reales con stack explícito, enlace al
   repositorio cuando exista y viñetas de impacto/arquitectura.
5. **Experiencia:** liderazgo, mentoría o prácticas con viñetas de acción.
6. **Habilidades técnicas:** agrupadas por categoría (*Lenguajes, Desarrollo,
   Datos e IA, Herramientas, Idiomas*).
7. **Certificaciones:** solo las relevantes al rol técnico, con emisor y fecha.

### Profesional (2+ años de experiencia)
Mover **Experiencia** inmediatamente debajo del resumen/encabezado y pasar
**Educación** al final.

## 3. Cómo redactar viñetas (Fórmula X-Y-Z / Impact-First)

Estructura base:
> **[Verbo de acción en pasado o presente]** + **[Qué construiste / arquitectura / herramienta]** + **[Resultado, escala o propósito verificable]**

Evitar siempre:
- *"Responsable de..."*, *"Encargado de..."*, *"Ayudé con..."*, *"Apasionado por..."*.
- Adjetivos sin respaldo (*"proactivo"*, *"líder nato"*, *"excelente comunicador"*).

Ejemplos aplicados al contexto de estudiante backend:
- **Débil:** *"Hice la interfaz de una app en Flutter."*
- **Fuerte (verificable):** *"Diseñé y desarrollé la interfaz móvil en Flutter (Dart, Riverpod, go_router, Material Design 3) estructurada por rol bajo principios de Clean Code."*
- **Con métrica (cuando se confirme):** *"Acompañé a [N] estudiantes de primer semestre en el programa TEPAYA resolviendo dudas académicas y reduciendo incidencias de matrícula."* (Solo usar `[N]` cuando el candidato confirme el número real).

## 4. Checklist previo a enviar una postulación

- [ ] Archivo en PDF con nombre profesional (`CV-Nombre-Apellido.pdf`), nunca `cv_final_v3.pdf`.
- [ ] Exactamente 1 página sin líneas huérfanas.
- [ ] Palabras clave exactas de la vacante presentes (p. ej. `Python`, `SQL`, `PostgreSQL`, `APIs REST`, `Git`) solo donde haya respaldo real.
- [ ] Todos los enlaces (`mailto:`, LinkedIn, GitHub, repositorios) son clicables y funcionan.
- [ ] Cero datos sensibles innecesarios (cédula, dirección exacta, foto en mercados internacionales/ATS).

