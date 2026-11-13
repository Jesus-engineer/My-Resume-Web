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
styles.css                 Sistema visual, responsive, temas e impresión A4
app.js                     Tema, navegación, filtros, revelado y visor de certificados
deck/                      Presentación independiente con Reveal.js (?print-pdf)
vendor/reveal/             Reveal.js 6.0.2 vendorizado localmente (licencia MIT)
assets/fonts/              Inter y JetBrains Mono en WOFF2 + licencias OFL
assets/certificados/       Seis certificados reales en WebP
assets/proyectos/          Portada real de SIPIIT
assets/fondos/             Fondos WebP derivados de mis guías HTML
docs/diseno.md             Brief, decisiones finales y pendientes para merge a main
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
- Contraste AA en tema oscuro y claro.
- Impresión A4 sin ondas, navegación, maquetas ni botones.
- Verificación manual: abrir `index.html`, revisar la consola y recorrer las cinco
  anclas.

Evidencia de la última revisión y handoff (2026-11-12):

- Paridad visual validada en las cinco secciones (incluidos los fondos WebP de Certificaciones y Contacto en `assets/fondos/`).
- Sin errores de consola ni respuestas HTTP `>= 400` en `index.html` y `deck/index.html`.
- Sin desborde horizontal en `360`, `390`, `768`, `1023`, `1024`, `1440` y `1920` px.
- Filtros de certificaciones (`Todos`: 6, `Programación`: 2, `Datos e IA`: 4) y enlaces externos verificados.
- Deck Reveal.js (7 diapositivas) verificado en HTTP, `file://` y exportación `?print-pdf`.
- Revisión previa (2026-11-11): Lighthouse 98/100/100/100, axe 0 violaciones e impresión A4 en 3 páginas.

El detalle de decisiones y pendientes previos al merge a `main` está en `docs/diseno.md`.

## Contenido y privacidad

`content.md` es mi fuente local de datos reales y no se publica. Las imágenes de
`docs/referencias/`, el código de `docs/codigoshtml/`, `AGENTS.md`, `content.md`,
`foto_950kb.jpg` y `Profile*.pdf` están ignorados por Git. No incluyo enlaces,
certificados, capturas ni métricas inventadas.

## Enlaces y backlog

- Sitio previsto: https://jesus-engineer.github.io/My-Resume-Web/
- Backlog (issues y milestones): https://github.com/Jesus-engineer/My-Resume-Web/issues y https://github.com/Jesus-engineer/My-Resume-Web/milestones
- GitHub: https://github.com/Jesus-engineer
- LinkedIn: https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev

El push y el merge a `main` los gestiono directamente como dueño del repositorio.
