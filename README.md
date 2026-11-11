# My-Resume-Web

Hoja de vida personal de **Jesús David Velásquez Mercado**, estudiante de
Ingeniería de Sistemas en la Universidad Tecnológica de Bolívar. El sitio presenta
su perfil backend, los proyectos en los que trabaja, sus certificaciones y sus
canales de contacto. Está pensado para reclutadores técnicos y líderes de
ingeniería que revisan el perfil en menos de un minuto.

## Stack

- HTML, CSS y JavaScript puro.
- Sin framework, sin paso de build y sin imports de Node.
- Fuentes autohospedadas: Inter y JetBrains Mono (OFL-1.1).
- Gestor de paquetes: **pnpm**.
- Despliegue previsto: GitHub Pages desde `main` en la raíz del repositorio.

## Cómo abrirlo

Abre `index.html` directamente en el navegador. También puedes usar un servidor
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

## Estructura

```text
index.html                 Página única con las cinco secciones
styles.css                 Sistema visual, responsive, temas e impresión A4
app.js                     Tema, navegación, filtros, revelado y visor de certificados
assets/fonts/              Inter y JetBrains Mono en WOFF2 + licencias OFL
assets/certificados/       Seis certificados reales en WebP
assets/proyectos/          Portada real de SIPIIT
docs/diseno.md             Brief y decisiones de diseño
docs/referencias/          Imágenes del dueño (locales, ignoradas por Git)
docs/codigoshtml/          Código de apoyo del dueño (local, ignorado por Git)
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

Evidencia de la última revisión (2026-11-11):

- Lighthouse: performance 98, accessibility 100, best practices 100, SEO 100.
- axe: 0 violaciones en oscuro 1440/390 y claro 1440.
- Sin desborde horizontal entre 360 y 1920 px.
- Impresión A4 en 3 páginas con las seis certificaciones y las URLs de contacto.

## Contenido y privacidad

`content.md` es la fuente local de datos reales y no se publica. Las imágenes de
`docs/referencias/`, el código de `docs/codigoshtml/`, `AGENTS.md`, `content.md`,
`foto_950kb.jpg` y `Profile*.pdf` están ignorados por Git. No se inventan enlaces,
certificados, capturas ni métricas.

## URLs

- Sitio previsto: https://jesus-engineer.github.io/My-Resume-Web/
- GitHub: https://github.com/Jesus-engineer
- LinkedIn: https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev

El push y el merge a `main` los hace el dueño del repositorio.
