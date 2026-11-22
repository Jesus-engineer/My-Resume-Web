# Brief de diseño: Portfolio nocturno con ondas de luz

Estado: **aprobado por el dueño el 2026-11-10** (issues D1 #42 y D3 #44).
Actualizado el 2026-11-11 para alinear el documento con las cinco imágenes de
referencia y con la implementación de D11.
Actualizado el 2026-11-21: el dueño decidió conservar únicamente el diseño
oscuro original y retirar el modo claro y los paneles blancos.

Producto final: las **cinco imágenes de referencia del dueño**, guardadas en
`docs/referencias/` como material local (ignoradas por Git, no se publican):

1. `01-hero-ondas.png` — hero con nombre, ondas de luz y tarjeta de perfil.
2. `02-proyectos.png` — sección 01 / Proyectos.
3. `03-sobre-mi.png` — sección 02 / Sobre mí, con pingüino Ubuntu.
4. `04-certificaciones-contacto.png` — sección 03 / Formación y avance de contacto.
5. `05-ultimapagina.png` — sección 04 / Contacto en dos columnas y pie.

Las imágenes mandan sobre este documento en lo visual y estructural. `content.md`
manda en los datos reales, enlaces y privacidad. El código de `docs/codigoshtml/`
es una ayuda local de implementación (SVG, medidas, composiciones e iconos); no
es el producto, no se publica y no se copia literalmente porque usa otra
tipografía, cinco páginas separadas y algunos textos que no existen en el CV.

## 1. Sujeto y trabajo del sitio

- **Sujeto:** Jesús David Velásquez Mercado, estudiante de Ingeniería de Sistemas. Backend con Python, SQL y APIs. Investigación en recomendaciones con IA para Savio. Interfaz Flutter de SIPIIT.
- **Audiencia:** reclutadores técnicos y líderes de ingeniería que revisan el perfil en menos de un minuto.
- **Trabajo principal:** que en 30 segundos entiendan qué hace, con qué tecnologías trabaja y cómo contactarlo.
- **Estructura:** una sola página con **scroll vertical hacia abajo**, navegación superior fija y cinco anclas: Inicio, Proyectos, Sobre mí, Certificaciones, Contacto.

## 2. Concepto

Una frase: *un portfolio nocturno atravesado por ondas de luz: azul para actuar, dorado para aprender, coral para respaldar.*

Tres adjetivos: nocturno, luminoso, directo.

El fondo es casi negro azulado y cada sección se distingue por una onda o un
wallpaper de luz con color propio. La página se lee de arriba abajo como una sola
historia: quién soy, qué construyo, qué me respalda y cómo hablar conmigo.

## 3. Estructura y textos literales

### Navegación superior (todas las secciones)

- Marca: `JV` a la izquierda, en blanco.
- Enlaces a la derecha: `Inicio`, `Proyectos`, `Sobre mí`, `Certificaciones`, `Contacto`.
- Estado activo: texto blanco en negrita y subrayado corto en el color de acento de la sección visible.
- Barra fija con fondo oscuro translúcido al hacer scroll y línea divisoria inferior tenue.
- Un único diseño oscuro, con las ondas y fondos originales de color.

### Hero (`#inicio`) — acento azul

- Antetítulo: `ESTUDIANTE DE INGENIERÍA DE SISTEMAS`.
- Titular: `Jesús David` y `Velásquez Mercado`, en dos líneas. Es el único `h1`.
- Subtítulo: `Me enfoco en desarrollo backend con Python, SQL y APIs. También construyo interfaces con React y sigo aprendiendo con cada proyecto.`
- Badge de disponibilidad: punto verde + `Disponible para prácticas`.
- Botones: `Ver proyectos ↗` (azul sólido, ancla a #proyectos) y `Descargar CV` (contorno, descarga directa de `assets/cv-jesus-velasquez.pdf` en formato ATS de 1 página).
- Tarjeta de perfil a la derecha: foto real `assets/foto.webp` en formato 4:5, sin filtros, con retrato limpio y encuadre compacto (máximo 15.5rem en escritorio, 14rem en tablet y 12rem en móvil) para que no compita con el nombre.
- Bloque inferior `Herramientas y entornos`:
  - Tecnologías: `Python`, `SQL`, `React`.
  - Sistemas operativos: `Linux`, `Windows`, `macOS`.
- Pie del hero: `GitHub` y `LinkedIn` a la izquierda; `Continúa hacia mis proyectos ↓` a la derecha.
- Ondas: wallpaper vectorial con cintas azules (Windows), órbitas naranjas y ladera violeta (Ubuntu), y ondas coral (macOS). El texto vive sobre un velo oscuro para conservar contraste.

### 01 / Proyectos (`#proyectos`) — acento azul

- Etiqueta: `01 / PROYECTOS` con icono de cuadrícula.
- Titular: `Proyectos seleccionados`.
- Subtítulo: `Una selección de lo que estoy construyendo y aprendiendo.`
- Fondo: cintas azules 3D en la esquina superior derecha.

Tarjeta destacada (ancho completo, texto izquierda ~45 %, maqueta derecha ~55 %):

- Título: `Savio AI` con badge de estado `Investigación en curso` (borde azul, icono de matraz).
- Descripción: `Exploro cómo personalizar contenido académico con inteligencia artificial para el LMS de mi universidad.`
- Chips: `IA`, `Moodle`, `Investigación`.
- Sin botón: la investigación no tiene repositorio ni demo públicos. No se inventa el enlace.
- Maqueta decorativa en CSS (no captura real): ventana con puntos macOS, menú lateral (`Savio AI`, `Inicio`, `Recomendaciones`, `Recursos`, `Mi curso`) y panel con `Hola, estudiante`, `Sugerencias de recursos para tu aprendizaje`, `Recursos recomendados` y tres filas (`Resumen: Redes de computadoras`, `Video: Introducción a la IA`, `Ejercicios de práctica`).

Fila de tres tarjetas secundarias, separadas por líneas verticales como en la referencia:

1. **SIPIIT** (real, `Terminado`): título completo `Intelligent IT Incident Prioritization System (SIPIIT)`, fechas reales febrero-mayo de 2026, descripción real de `content.md`, chips `Flutter`, `Dart`, `Git`, portada real `assets/proyectos/sipiit-portada.webp` completa sin recortes y enlace `Ver repositorio ↗` con URL real de GitHub.
2. **GyR Barber** (`En progreso`): `Gestión de reservas, citas y servicios para barbería.`, chips `React`, `Python`, `Supabase`, `PostgreSQL`, `Tailwind CSS`. Sin botón: proyecto en desarrollo. Maqueta decorativa con panel `Citas de hoy` y horarios de atención.
3. **Próximo proyecto** (`En progreso`): `Desarrollando una nueva aplicación en progreso para seguir practicando arquitectura backend, APIs e interfaces modernas.`, chips `Python`, `SQL`, `React`. Maqueta decorativa con panel `En construcción` y etapas de avance.

La referencia 02 muestra tres proyectos y no incluye SIPIIT; se conserva SIPIIT
porque es el único proyecto con repositorio real. Las maquetas son ilustraciones
decorativas (`aria-hidden`), nunca capturas presentadas como reales.

### 02 / Sobre mí (`#sobre-mi`) — acento dorado

- Etiqueta: `02 / SOBRE MÍ` con icono de personas.
- Titular: `Un poco sobre mí`.
- Columna izquierda:
  - Párrafo 1: `Estudio Ingeniería de Sistemas en la Universidad Tecnológica de Bolívar. Me interesa entender cómo funcionan las aplicaciones y construir soluciones útiles.`
  - Párrafo 2: `Actualmente participo en una investigación sobre recomendaciones académicas con IA para Savio. También soy mentor TEPAYA y acompaño a estudiantes de primer año.`
  - Chips: `Python`, `SQL`, `</> APIs`, `React`.
  - Filas de `Mi camino`, con icono, etiqueta y valor:
    1. `Formación` — `Ingeniería de Sistemas · UTB`.
    2. `Investigación` — `Personalización de contenido en Savio`.
    3. `Comunidad` — `Mentor TEPAYA`.
- Columna derecha: pingüino Ubuntu vectorial, decorativo (`aria-hidden`), con líneas doradas.
- Subsección inferior: titular `Entornos que estoy explorando` y tres tarjetas: `Linux — Terminal y herramientas`, `Windows — Entorno de trabajo`, `macOS — Exploración del ecosistema`.
- Fondo: facetas vino, coral y violeta inspiradas en el wallpaper de Ubuntu.

Los entornos se presentan como aprendizaje, no como experiencia verificada: así
los diseñó el dueño.

### 03 / Formación (`#certificaciones`) — acento coral

- Etiqueta: `03 / FORMACIÓN` con acento coral; emblema plateado decorativo junto al titulo.
- Titular: `Certificaciones`.
- Subtítulo: `Cursos y programas que complementan mi formación.`
- Ventana tipo Finder con barra de tres puntos, título `Mi formación` y filtros `Todos`, `Programación`, `Datos e IA`.
- Seis certificaciones reales en grilla de tres columnas (dos filas), con icono de documento, título completo, emisor y enlace `Ver certificado ↗` que abre el visor accesible existente.
- Los filtros son una mejora progresiva: sin JavaScript se muestran las seis.
- Fondo: paisaje costero de la guia HTML optimizado a WebP, con velo de contraste.

La referencia 04 usa la marca de Apple y un certificado de "Habilidades de
Investigación" que no existe en `content.md`. Se toma el emblema decorativo
de la guia para respetar el diseno, pero no se inventa el certificado: se
mantienen los seis documentos reales.

### 04 / Contacto (`#contacto`) — acento azul, dos columnas

- Etiqueta: `04 / CONTACTO`.
- Titular: `¿Hablamos?`.
- Subtítulo: `Busco prácticas y oportunidades para aportar, aprender y seguir desarrollando software.`
- Disponibilidad: punto verde y texto plano `Disponible para prácticas`.
- Cierre: `Gracias por conocer mi trabajo.`
- Columna derecha, tres filas con icono y flecha:
  1. `Correo` — `Escríbeme directamente` — `mailto:` real.
  2. `LinkedIn` — `Conoce mi perfil profesional` — URL real.
  3. `GitHub` — `Explora mis repositorios` — URL real.
- Fondo: ondas azul, violeta y coral con orbitas naranjas, extraidas del HTML de guia y optimizadas a WebP.

### Pie de página

- Línea divisoria superior.
- `JV` a la izquierda.
- `Jesús David Velásquez Mercado` y `Desarrollo de software` separados por líneas verticales.
- `Volver al inicio ↑` a la derecha (ancla a `#inicio`).

## 4. Paleta

### Oscuro (tema canónico y por defecto)

| Token | Valor | Uso |
|---|---|---|
| noche | `#070b14` | fondo |
| superficie | `rgb(17 26 46 / 78%)` | tarjetas, chips y paneles |
| superficie-2 | `rgb(14 23 41 / 90%)` | cabecera compacta y tarjetas de proyecto |
| blanco | `#f5f6f8` | texto principal |
| plata | `#c8ccd4` | párrafos |
| gris | `#94a3b8` | subtítulos y metadatos |
| azul | `#2b72fb` | acción principal: botones, enlaces, subrayados |
| azul-claro | `#60a5fa` | etiquetas de sección azules |
| oro | `#f2c94c` | acento de Sobre mí |
| coral | `#f06464` | acento de Certificaciones y resplandores |
| verde | `#22c55e` | punto de disponibilidad |
| borde | `#26314a` | bordes de tarjetas y chips |

### Decisión de tema (2026-11-21)

Se conserva únicamente el tema oscuro. El control de cambio de tema, la
preferencia guardada y las reglas del modo claro se retiran. Los fondos,
colores, ilustraciones y composición del diseño oscuro original se mantienen.

### Contraste medido (WCAG)

Se verifica en la implementación con script sobre los pares texto/fondo y
texto/superficie del diseño oscuro, incluido el texto que cruza las ondas. La regla:
ningún par por debajo de 4.5:1. Las ondas se mantienen detrás del texto con un
velo de contraste y los resplandores evitan las crestas más luminosas.

### Ondas y wallpapers

- Hero: SVG de 1536 × 1024 con cintas azules, órbitas naranjas, ladera violeta y ondas coral; velo oscuro de izquierda a derecha.
- Proyectos: cintas azules 3D en la esquina superior derecha.
- Sobre mí: facetas vino/coral/violeta y pingüino Ubuntu.
- Formación: costa al atardecer en `assets/fondos/certificaciones.webp`.
- Contacto: ondas azul, violeta y coral en `assets/fondos/contacto.webp`.
- Implementación: Hero, Proyectos y Sobre mi conservan sus SVG; Formación y Contacto usan los fondos de las guias HTML convertidos a WebP, con velo para proteger la lectura. Ninguna imagen privada de `docs/referencias/` se publica.

## 5. Tipografía

Dos familias, sin cambios:

- **Inter:** titulares, párrafos y navegación.
- **JetBrains Mono:** etiquetas de sección, chips, botones y datos.

Ambas autohospedadas en WOFF2 con `font-display: swap`, `unicode-range` latin y
licencias OFL-1.1 verificadas. Las referencias usan una sans geométrica; Inter
cubre ese registro sin añadir una tercera familia ni fuentes base64.

## 6. Componentes

- **Layout full-bleed:** sin `max-width` de 75 rem. El padding general es `clamp(1.25rem, 4.5vw, 4.5rem)`; Formación y Contacto usan un margen lateral mayor en escritorio para coincidir con las referencias.
- **Hero:** dos columnas por encima de 1023 px (texto flexible + tarjeta de perfil de 20.5 rem); una columna desde 1023 px, con la tarjeta alineada a la izquierda y un máximo de 18 rem.
- **Grillas:** proyectos 3 columnas en escritorio, 2 en tablet y 1 en móvil; certificaciones 3/2/1; entornos 3/2/1. Los párrafos conservan su ancho de lectura.
- **Botón primario:** relleno azul con degradado, radio ~10 px, texto blanco, flecha `↗`.
- **Botón secundario:** contorno fino claro, fondo translúcido, texto blanco.
- **Chip:** píldora `9999px`, fondo oscuro, borde fino, icono + etiqueta mono.
- **Tarjeta:** radio ~14-18 px, fondo translúcido, borde fino, sin sombras pesadas.
- **Badge de estado:** píldora con icono; `Investigación en curso` (azul), `En progreso` (dorado), `Terminado` (verde).
- **Ventana de formación:** contenedor tipo Finder con barra de puntos, título, filtros y grilla de certificados.
- **Maquetas:** ventanas con puntos macOS, menú lateral y panel; decorativas, `aria-hidden`, ocultas en impresión.
- **Foco:** contorno de 2 px, nunca se elimina.

## 7. Movimiento

- Sin parallax ni scroll-jacking. El scroll sigue siendo vertical y predecible.
- Entrada del hero con desplazamiento corto y opacidad, escalonada por bloques (máximo 0.7 s).
- Ondas de luz con deriva lenta y continua (`translate` + `scale`, 24-28 s, alterna).
- Punto de disponibilidad con pulso suave y flecha de continuar con rebote corto.
- Tarjetas y botones con elevación de 2-4 px y borde iluminado al pasar el puntero.
- Revelado por scroll con `IntersectionObserver`, una sola vez, solo en cabeceras, tarjetas y bloques; sin parallax y sin cambiar dimensiones.
- Fallback sin JavaScript: todo visible.
- `prefers-reduced-motion`: sin animaciones, transiciones ni scroll suave.
- El scroll es suave con `scroll-behavior: smooth` y `scroll-padding-top` para la barra fija.

## 8. Decisiones de integridad

- **Sin botón en Savio AI:** no existe repositorio ni demo públicos de la investigación.
- **Sin botones en GyR Barber y Próximo proyecto:** son desarrollos en progreso del dueño; se muestran con badge `En progreso` y maqueta decorativa.
- **SIPIIT con datos y URL reales:** es el único proyecto con repositorio público; conserva su portada real.
- **`Descargar CV` descarga `assets/cv-jesus-velasquez.pdf`:** PDF ATS de 1 página generado solo con los datos públicos aprobados.
- **Entornos como aprendizaje:** Linux, macOS y Windows se presentan como exploración, no como experiencia verificada.
- **Certificaciones con nombres completos reales** de `content.md`, no los abreviados de la referencia.
- **h1 = nombre completo en el hero**, como en la referencia 01; el `title`, el JSON-LD, la tarjeta de perfil y el pie conservan el nombre.
- **Foto real:** la referencia 01 muestra un marco vacío; el sitio usa `assets/foto.webp`, que es la foto aprobada en `content.md`.
- **Emblema plateado:** se usa la silueta decorativa junto a Certificaciones para seguir la referencia 04; los certificados y sus enlaces siguen siendo reales.
- **Sin enlaces inventados:** los botones y filas de contacto usan las URLs reales de `content.md`.

## 9. Verificación de la dirección

- [x] Scroll vertical único con navegación superior fija.
- [x] Cinco anclas: inicio, proyectos, sobre-mi, certificaciones, contacto.
- [x] Ondas de luz por sección, detrás del texto.
- [x] Un solo `h1`; jerarquía h2/h3 correcta.
- [x] Contraste AA en el diseño oscuro, incluido el texto sobre ondas.
- [x] Teclado completo: menú móvil, filtros, visor de certificados, volver arriba.
- [x] Impresión A4 sin ondas, navegación, maquetas ni botones.
- [x] Sin contenido inventado: todo texto sale de `content.md` o de las imágenes del dueño.
- [x] Diseño oscuro único, por decisión del dueño el 2026-11-21.
- [x] Aprobación visual del dueño contra las cinco referencias (validado en D11 `#53` y revalidado en D9 `#50`).

## 10. Referencias

- Cinco imágenes del dueño (2026-11-10): producto final; solo locales en `docs/referencias/`, ignoradas por Git y no publicadas.
- `docs/codigoshtml/` (2026-11-11): ayuda local de implementación; no se publica, no se commitea y no sustituye las referencias.
- `bchiang7/v4` (MIT): superada por estas imágenes; su crédito se retira del pie y queda en el historial del repositorio.
- Inter: OFL-1.1 (`github.com/rsms/inter`).
- JetBrains Mono: OFL-1.1 (`github.com/JetBrains/JetBrainsMono`).
- Reveal.js 6.0.2 (MIT): vendorizado localmente en `vendor/reveal/` para el deck independiente en `deck/` (`D10 #52`).
- Skills: `frontend-design` (Apache 2.0), `ui-ux-pro-max` (MIT), `taste-skill`, `web-design`, `web-interface-guidelines` en `.claude/skills/`.

## 11. Alternativas descartadas

- **Portfolio técnico nocturno (Brittany Chiang)**: implementada en `bcc373a`; el dueño definió un nuevo producto final con sus propias imágenes. El crédito visible se retira.
- **Cianotipo**: revertida en `2847675`.
- **Signal dossier** y **Editorial cobalto**: descartadas antes de implementarse.
- **Copiar literalmente `docs/codigoshtml/`:** descartado por usar Lato, cinco páginas, fuentes base64 y textos que no existen en el CV.

## 12. Estado de las tareas

- D0 #41: cerrado (ideas del 2026-11-10 absorbidas en `8d9251e`, `7d75607`, `5c3b020` y `e34cce0` / `#53`).
- D1 #42: cerrado.
- D2 #43 a D8 #49: cerrados con evidencia.
- D11 #53: cerrado tras aprobación visual del dueño (`e34cce0`).
- D10 #52: cerrado (deck independiente con Reveal.js en `deck/`, vendorizado en `vendor/reveal/`, con `?print-pdf`).
- D9 #50: aprobación y handoff completados (restauración de `assets/fondos/*.webp`, verificación visual y documental).

## 13. Pendientes previos al merge a `main` y publicación

- Revisión final local del dueño sobre `index.html` y `deck/index.html`, `git push` de `desarrollador` y merge a `main`.
- Épica E5 / E6: activar GitHub Pages en `main` / raíz (`#32`), verificación post-despliegue (`#33`) y cierre de tareas administrativas de repo (`#27`, `#30`, `#31`, opcionales `#34`, `#35`).
- E7-02: versión inglesa implementada en `en/index.html`, con selector ES/EN,
  metadatos propios y CV ATS en inglés. Verificación local en
  `docs/auditorias/e7-02/README.md`.
- Las cinco imágenes de referencia viven en `docs/referencias/`, están ignoradas por Git y no se publican.
- `docs/codigoshtml/` está ignorado por Git y no se publica.
