# My-Resume-Web

Esta es mi hoja de vida web. Me llamo **Jesús David Velásquez Mercado**, soy
estudiante de Ingeniería de Sistemas en la Universidad Tecnológica de Bolívar y
me enfoco en desarrollo backend con Python, SQL y APIs, además de construir
interfaces con React.

En este sitio presento mi perfil técnico, los proyectos en los que trabajo, mis
certificaciones y mis canales de contacto. Lo diseñé para que reclutadores
técnicos y líderes de ingeniería puedan revisar mi trayectoria en menos de un
minuto.

## Stack

- HTML, CSS y JavaScript puro.
- Sin framework, sin paso de build y sin imports de Node.
- Fuentes autohospedadas: Inter y JetBrains Mono (OFL-1.1).
- Gestor de paquetes: **pnpm**.
- Despliegue previsto: GitHub Pages desde `main` en la raíz del repositorio.

## Cómo abrirlo

Puedes abrir `index.html` directamente en el navegador o levantar un servidor
local para probar rutas y fuentes con el mismo origen:

```bash
pnpm install
pnpm dev
```

`pnpm dev` solo recuerda abrir `index.html`; no hay servidor propio. Para una
revisión con servidor local:

```bash
python -m http.server 8765
```

Luego visita `http://127.0.0.1:8765/`.

### Español e inglés

El selector **ES / EN** está en la cabecera de escritorio y dentro del menú
móvil. Cada idioma tiene su propio HTML: `index.html` y
[`en/index.html`](en/index.html). También puedes abrir cualquiera directamente
desde archivo. Ambas versiones comparten los fondos oscuros, los estilos y las
interacciones; los enlaces de idioma conservan el ancla de la sección actual.

Cada página declara su idioma, metadatos sociales, URL canónica y enlaces
`hreflang`. Los textos, las etiquetas accesibles y los estados de las
interacciones están traducidos. Los certificados conservan sus imágenes
originales y cada idioma descarga su propio CV ATS de una página.

Para regenerar y auditar el PDF en inglés:

```bash
python .agents/skills/ats-resume-engineer/scripts/build_ats_cv.py --lang en
python .agents/skills/ats-resume-engineer/scripts/audit_ats_pdf.py assets/cv-jesus-velasquez-en.pdf --lang en
```

El generador conserva `--lang es` como opción por defecto. Los dos PDF se
guardan en rutas independientes. La validación HTML revisa las versiones
española e inglesa y el deck con el mismo comando `pnpm run validate:html`.

### Deck de presentación (independiente)

El repositorio también incluye una presentación independiente construida con
**Reveal.js** (MIT, vendorizado en `vendor/reveal/`) sin enlace desde
`index.html`:

- Abrir directamente: `deck/index.html` (o `/deck/` en GitHub Pages).
- Exportar a PDF: añadir `?print-pdf` (`deck/index.html?print-pdf`) y usar la
  opción de imprimir/guardar como PDF del navegador.

## Estructura

```text
index.html                 Página única con las cinco secciones
en/index.html              Versión en inglés con sus metadatos y enlaces de idioma
styles.css                 Sistema visual oscuro, responsive e impresión A4
app.js                     Navegación, filtros, revelado y visor de certificados
deck/                      Presentación independiente con Reveal.js (?print-pdf)
vendor/reveal/             Reveal.js 6.0.2 vendorizado localmente (licencia MIT)
assets/fonts/              Inter y JetBrains Mono en WOFF2 + licencias OFL
assets/certificados/       Seis certificados reales en WebP
assets/proyectos/          Portada real de SIPIIT
assets/fondos/             Fondos WebP derivados de mis guías HTML
assets/cv-jesus-velasquez.pdf  Hoja de vida ATS de 1 página en PDF para descarga directa
assets/cv-jesus-velasquez-en.pdf  CV ATS en inglés de 1 página
docs/diseno.md             Brief, decisiones finales y pendientes para merge a main
docs/auditorias/           Evidencia y métricas de revisiones visuales
scripts/audit_ui.py        Auditoría visual opcional con capturas de escritorio y móvil
docs/referencias/          Mis imágenes de referencia (locales, ignoradas por Git)
docs/codigoshtml/          Código de apoyo local (ignorado por Git)
```

Las rutas son relativas y los nombres de archivo van en minúsculas, con la grafía
exacta en el HTML, para que funcionen igual en Windows, Linux y GitHub Pages.

## Accesibilidad y verificación

- Un solo `h1`; jerarquía `h2`/`h3`/`h4` consistente.
- Skip link, foco visible, navegación por teclado, menú móvil con `Escape` y
  visor de certificados con retorno de foco.
- `prefers-reduced-motion` respetado; fallback sin JavaScript.
- Diseño oscuro con contraste de texto y foco visible sobre los fondos de color.
- Impresión A4 sin ondas, navegación, maquetas ni botones.
- Verificación manual: abrir `index.html`, revisar la consola y recorrer las cinco
  anclas.
- Validación HTML en local (y en CI vía `.github/workflows/validate.yml` en
  `push` a `main` y `pull_request`, usando reglas de `.htmlvalidate.json` para
  detectar errores reales de HTML sin paso de build):

```bash
pnpm install
pnpm run validate:html
```

Evidencia de la última revisión y handoff (2026-11-12):

- Paridad visual validada en las cinco secciones (incluidos los fondos WebP de Certificaciones y Contacto en `assets/fondos/`).
- Sin errores de consola ni respuestas HTTP `>= 400` en `index.html` y `deck/index.html`.
- Sin desborde horizontal en `360`, `390`, `768`, `1023`, `1024`, `1440` y `1920` px.
- Filtros de certificaciones (`Todos`: 6, `Programación`: 2, `Datos e IA`: 4) y enlaces externos verificados.
- Deck Reveal.js (7 diapositivas) verificado en HTTP, `file://` y exportación `?print-pdf`.
- Revisión previa (2026-11-11): Lighthouse 98/100/100/100, axe 0 violaciones e impresión A4 en 3 páginas.

El detalle de decisiones y pendientes previos al merge a `main` está en `docs/diseno.md`.

### Auditoría visual de E7

La [línea base de E7-01 (#61)](docs/auditorias/e7-01/README.md), realizada el
2026-11-21, registra ocho tamaños de pantalla en los dos temas, 152 capturas,
métricas de las cinco secciones y el orden de ajustes para #63 a #67.

El sitio conserva únicamente el diseño oscuro por decisión del dueño. La línea
base anterior se mantiene como evidencia histórica. Para auditar el estado
actual, instala una vez las dependencias opcionales de Python y Chromium:

```bash
python -m pip install -r scripts/requirements-ui.txt
python -m playwright install chromium
python scripts/audit_ui.py
```

El script inicia y cierra su servidor local y guarda la galería en
`artifacts/ui/actual/index.html`, con ocho pantallas del diseño oscuro. Las
capturas están ignoradas por Git. Estas
herramientas son opcionales para revisar el sitio; abrir `index.html` sigue sin
requerir instalación ni build. En PowerShell, si la política bloquea
`pnpm.ps1`, la validación HTML se puede ejecutar con `pnpm.cmd run validate:html`.

La [verificación de E7-02 (#62)](docs/auditorias/e7-02/README.md) documenta la
versión inglesa, las pruebas de navegación ES/EN y el CV ATS. Para generar sus
capturas con las dependencias anteriores:

```bash
python scripts/audit_ui.py --lang en --output artifacts/ui/e7-02-en
```

La [revisión de E7-03 (#63)](docs/auditorias/e7-03/README.md) recoge los ajustes
de hero y cabecera en ES/EN, las medidas frente a la línea base y las pruebas
de menú, teclado y navegación. Cabecera y hero comparten un ancho máximo de
1280 px; el hero completo cabe en las pantallas de escritorio revisadas y en
360 × 800 ocupa un 34.56 % menos de alto en español.

## Contenido y privacidad

`content.md` es mi fuente local de datos reales y no se publica. Las imágenes de
`docs/referencias/`, el código de `docs/codigoshtml/`, `AGENTS.md`, `content.md`,
`foto_950kb.jpg` y `Profile*.pdf` están ignorados por Git. No incluyo enlaces,
certificados, capturas ni métricas inventadas.

## Enlaces y backlog

- Sitio previsto: https://jesus-engineer.github.io/My-Resume-Web/
- Backlog (issues y milestones): https://github.com/Jesus-engineer/My-Resume-Web/issues y https://github.com/Jesus-engineer/My-Resume-Web/milestones
- Backlog (issues y milestones): https://github.com/Jesus-engineer/My-Resume-Web/issues y https://github.com/Jesus-engineer/My-Resume-Web/milestones
- GitHub: https://github.com/Jesus-engineer
- LinkedIn: https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev

El push y el merge a `main` los gestiono directamente como dueño del repositorio.
