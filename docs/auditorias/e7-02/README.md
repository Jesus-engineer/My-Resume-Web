# E7-02: versión inglesa del sitio y CV ATS

Implementación local de [#62](https://github.com/Jesus-engineer/My-Resume-Web/issues/62),
verificada el 2026-11-21 en la rama `desarrollador`.

## Resultado

- [x] Página inglesa estática en [`en/index.html`](../../../en/index.html),
  enlazada con la española mediante controles ES / EN accesibles en escritorio
  y en el menú móvil. Cada enlace ofrece un objetivo de al menos 44 × 44 px.
- [x] Traducción de las cinco secciones, maquetas decorativas, fechas, textos
  alternativos, etiquetas accesibles, estados de filtros, pie y visor.
- [x] `lang="en"`, título, descripción, Open Graph, Twitter, canonical y JSON-LD
  Person en inglés; enlaces alternativos `es`, `en` y `x-default` en las dos páginas.
- [x] [CV ATS inglés de una página](../../../assets/cv-jesus-velasquez-en.pdf),
  con texto extraíble, idioma declarado y enlaces clicables. La descarga
  española conserva su PDF original.
- [x] `pnpm.cmd run validate:html` pasa para ES, EN y el deck. El workflow
  existente de GitHub Actions ejecuta ese mismo comando.

Las dos páginas se sirven directamente, comparten `styles.css` y `app.js` y
conservan el diseño oscuro. Los IDs de las secciones son iguales para que al
cambiar de idioma se mantenga el ancla, por ejemplo `#certificaciones`.
Los enlaces funcionan sin JavaScript; el contenido inglés y sus metadatos no
dependen de una traducción en tiempo de ejecución ni de un build.

## Verificación de navegador

Se probaron ES y EN en `1024 × 768`, `1280 × 720`, `1440 × 900`, `1920 × 1080`,
`320 × 568`, `360 × 800`, `390 × 844` y `430 × 932`.

| Comprobación | Evidencia local |
| --- | --- |
| 16 casos HTTP bajo `/My-Resume-Web/` | Sin desborde horizontal ni errores de consola o HTTP en uso normal. |
| 16 viajes ES → EN → ES o EN → ES → EN | Se conserva la sección y el prefijo del proyecto, tanto con el menú móvil como en escritorio. |
| Descarga de CV en los 16 casos | Los bytes coinciden con el PDF del idioma correspondiente y el nombre inglés termina en `-EN.pdf`. |
| Filtros y visor | Recuentos 6 / 2 / 4 y mensajes en el idioma correcto; título y alt de la imagen coinciden con la tarjeta. Se conserva Escape, Tab, Shift+Tab y retorno de foco. |
| Error de imagen simulado, ES y EN | Mensaje localizado, alternativa para abrir el original y cierre por teclado. |
| Cuatro casos sin JavaScript | Idiomas accesibles en 320 y 1440 px, seis certificados visibles y cambio de ruta funcional. La cabecera se adapta sin depender del botón del menú. |
| Dos casos `file://` | Se abren ES y EN desde archivo, funcionan los filtros y los enlaces cambian al otro HTML. |

La auditoría visual inglesa adicional registra ocho pantallas y 76 capturas
originales en `artifacts/ui/e7-02-en/`. La comprobación funcional y sus
resultados están en `artifacts/ui/i18n-en/verificacion.json`. Son archivos
locales ignorados por Git; los resúmenes de `imagenes/` acompañan este informe.

[Portada en inglés](imagenes/escritorio-en.webp) ·
[Selector dentro del menú móvil](imagenes/menu-movil-en.webp).

## Verificación del PDF

El PDF inglés tiene una página Letter, 4043 caracteres extraíbles y 198027
bytes. Se comprobó el orden de los seis encabezados, el idioma `en`, los enlaces
de contacto y la ausencia de los identificadores y URLs privados que revisa el
auditor. Los cinco destinos únicos son correo, LinkedIn, GitHub, portafolio
inglés y repositorio SIPIIT.

Se revisó visualmente su renderizado completo a escala 2. Mantiene una sola
columna, texto seleccionable, márgenes legibles y el contenido del CV español
existente, con las mismas fechas, cifras y tecnologías. Los títulos de cursos
se traducen para su lectura en inglés; las imágenes originales de las
credenciales y sus emisores se conservan.

```bash
python .agents/skills/ats-resume-engineer/scripts/build_ats_cv.py --lang en
python .agents/skills/ats-resume-engineer/scripts/audit_ats_pdf.py assets/cv-jesus-velasquez-en.pdf --lang en
python scripts/audit_ui.py --lang en --output artifacts/ui/e7-02-en
pnpm run validate:html
```

La revisión se realizó en Chromium y emulación táctil, con movimiento reducido
para las capturas. La publicación de las rutas y la comprobación en teléfonos
físicos corresponden al despliegue y QA posterior.
