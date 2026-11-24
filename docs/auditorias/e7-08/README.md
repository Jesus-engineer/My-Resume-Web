# E7-08 · QA integral del portafolio

Auditoría del 23 de noviembre de 2026. Se probó la revisión publicada
`39225158210a048e0128b94d9b2b3c876674e478` y se verificaron los ajustes de
impresión y accesibilidad en `desarrollador`, sobre `3715b71`. [Tarea #68](https://github.com/Jesus-engineer/My-Resume-Web/issues/68)

## Interfaz y navegación

Se completaron 32 verificaciones de composición en Chrome 157 a escala 1 y
con movimiento reducido. Las dos rutas pasaron en los ocho tamaños con
ambas preferencias de color del sistema. Se mantuvo el ancho común de
los bloques del hero, las secciones de contenido y el pie. No hubo desborde
horizontal, errores de consola ni solapamiento del nombre con la foto. El
hero completo cupo en las cuatro pantallas de escritorio.

| Pantalla CSS | Ancho común |
| --- | ---: |
| 1024 × 768 | 916,84 px |
| 1280 × 720 | 1149,81 px |
| 1440 × 900 | 1280 px |
| 1920 × 1080 | 1280 px |
| 320 × 568 | 280 px |
| 360 × 800 | 320 px |
| 390 × 844 | 350 px |
| 430 × 932 | 390 px |

El sitio aplica el tema oscuro aprobado con cualquiera de las dos
preferencias del sistema. El criterio de verificar un tema claro
independiente requiere revisar esa decisión de diseño. [Decisión de tema](../../diseno.md#decisión-de-tema-2026-11-21)

En HTTP local y en GitHub Pages pasaron las pruebas de anclas, menú móvil,
selector ES/EN con conservación de la sección, filtros del Finder y visor.
Se recorrieron los certificados con los botones y las flechas del teclado.
`Tab`, `Shift+Tab` y `Escape` verificaron el foco y su retorno al enlace de
origen. También se comprobaron los destinos de contacto y la descarga de
los dos CV ATS de una página. Las pruebas interactivas usaron escritorio de
1440 × 900 y móvil emulado de 360 × 800 con entrada táctil.
Las dos rutas abrieron directamente con `file://`, con JavaScript activado
y desactivado.

Para el cierre de E7-08 se acordó usar la evidencia de móvil emulado en
Chrome.

## Rendimiento y accesibilidad

Lighthouse 13.6.0 con Chrome 157 ejecutó una corrida por ruta y perfil sobre
GitHub Pages. Las cuatro superaron el objetivo de 98 en rendimiento.

| Ruta | Perfil | Rendimiento | Accesibilidad | Buenas prácticas | SEO |
| --- | --- | ---: | ---: | ---: | ---: |
| ES | Escritorio | 100 | 100 | 100 | 100 |
| ES | Móvil | 99 | 100 | 100 | 100 |
| EN | Escritorio | 100 | 100 | 100 | 100 |
| EN | Móvil | 100 | 100 | 100 | 100 |

En producción, axe-core 4.14.0 detectó una regla de impacto grave,
`label-content-name-mismatch`, en los dos selectores de idioma. Se reprodujo
con la navegación de escritorio y con el menú móvil abierto. Los nombres
accesibles locales ahora comienzan con las etiquetas visibles ES y EN.
La repetición local obtuvo cero violaciones en los diez estados de página,
menú o visor. Queda pendiente repetir axe sobre la corrección publicada.
[WCAG 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)

La revisión manual comprobó que las referencias ARIA apuntan a elementos
existentes. El contraste mínimo muestreado en Contacto fue 14,02:1 en las
cuatro combinaciones de ruta y perfil. El informe de axe conserva los
elementos con fondos complejos que el análisis automático dejó por revisar.

## Impresión y CI

- El portafolio imprime tres páginas A4 por idioma. El pie usa fondo blanco y
  el encabezado de Certificaciones acompaña a las tarjetas. Las cinco
  certificaciones aparecen en el PDF incluso después de filtrar el Finder.
- `/deck/` funciona en HTTP y `file://`. Se recorrió con teclado y controles
  en escritorio y con desplazamiento en móvil emulado. La exportación
  `?print-pdf` usa la altura de diapositiva de Reveal.js dentro de la página
  PDF. Se renderizaron y revisaron las siete diapositivas con sus tarjetas.
- `Validate HTML` pasó en `main` para `3922515`. Se comprobó también la
  validación local de `index.html`, `en/index.html` y `deck/index.html`.
  [Ejecución de GitHub Actions](https://github.com/Jesus-engineer/My-Resume-Web/actions/runs/45301491188)

Los informes completos de Lighthouse y axe, las capturas y los PDF de
verificación se guardan en `artifacts/ui/e7-08/`. Las correcciones de esta
auditoría están listas para su comprobación tras publicar en GitHub Pages.
