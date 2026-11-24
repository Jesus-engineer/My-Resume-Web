# assets/certificados/

Única carpeta de imágenes de certificados. Todo lo que está aquí se publica con
GitHub Pages, así que revisa cada archivo antes de subirlo.

## Reglas

- **Solo imágenes WebP.** No se suben PDF. Si un certificado llega en PDF, se
  convierte a imagen y el PDF se guarda fuera del repositorio.
- **Sin datos sensibles.** No subir cédulas, documentos de identidad ni datos
  médicos. Si un certificado los trae, se tapan en la imagen antes de subirla.
- **Nombres:** minúsculas, sin tildes, sin espacios, con guiones.
- **Medidas:** 1200 px de ancho, menos de 200 KB por imagen.
- **Originales:** los PDF y PNG de trabajo se guardan fuera del repositorio, en
  `C:\Users\jesus\Documents\certificados-originales\`.

## Archivos publicados

| Archivo | Certificación | Datos visibles |
|---|---|---|
| `gci-world-2026.webp` | GCI World April 2026 (Matsuo-Iwasawa Lab, UTokyo) | nombre y fecha de emisión |
| `supabase-baas.webp` | Curso de Supabase. Backend as a Service (BaaS) desde cero (Udemy) | número y URL de verificación |
| `ibm-ai-literacy.webp` | AI Literacy (IBM SkillsBuild) | número y URL de verificación |
| `certificado-analisis-de-datos.webp` | Análisis de Datos Nivel Intermedio (Ministerio TIC y UTB) | cédula y QR tapados |
| `certificado-programacion.webp` | Programación Nivel Intermedio (Ministerio TIC y UTB) | cédula y QR tapados |

## Después de agregar una imagen

Avisar para conectar la imagen en `index.html`, en la sección de certificaciones,
y actualizar `content.md`, sección 12.
