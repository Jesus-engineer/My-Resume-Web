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
- Cabecera de 72 px y contenedor compartido con el hero de un máximo de 80rem
  (1280 px). Enlaces de al menos 44 × 44 px, con fondo tenue al pasar el cursor
  o recibir foco. Las anclas dejan 16 px bajo la cabecera.
- Menú desplegable con fondo oscuro sólido y separación de 8 px respecto a la
  cabecera. Admite scroll en pantallas bajas; cierra con Escape, al elegir una
  sección, al salir con Tab o al pulsar fuera. La entrada respeta movimiento reducido.
- Un único diseño oscuro, con las ondas y fondos originales de color.

### Hero (`#inicio`) — acento azul

- Antetítulo: `ESTUDIANTE DE INGENIERÍA DE SISTEMAS`.
- Titular: `Jesús David` y `Velásquez Mercado`, en dos líneas en escritorio;
  el apellido se adapta al ancho disponible en móvil. Es el único `h1`.
- Subtítulo: `Me enfoco en desarrollo backend con Python, SQL y APIs. También construyo interfaces con React y sigo aprendiendo con cada proyecto.`
- Badge de disponibilidad: punto verde + `Disponible para prácticas`.
- Botones: `Ver proyectos ↗` (azul sólido, ancla a #proyectos) y `Descargar CV` (contorno, descarga directa de `assets/cv-jesus-velasquez.pdf` en formato ATS de 1 página).
- Tarjeta de perfil a la derecha en escritorio: foto real `assets/foto.webp`
  en formato 4:5, sin filtros y con ancho de hasta 18rem. En móvil y tablet
  ocupa una columna de 5–7rem junto a la presentación, con disponibilidad y
  los dos botones debajo. Los botones comparten fila y admiten texto en dos líneas.
- En escritorio, nombre, foto, acciones, herramientas y pie caben en la primera
  pantalla desde 1024 × 768 y 1280 × 720. El tamaño del título considera el ancho
  y el alto disponibles. En 360 × 800, el hero español mide 850.08 px: una
  reducción del 34.56 % frente a la línea base de E7-01.
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
- Contenedor compartido `--ancho-contenido` (`80rem` / `1280 px`) alineado con cabecera y hero desde `1440 px`.

Tarjeta destacada (ancho completo, texto izquierda ~46 %, maqueta derecha ~54 %):

- Título: `Savio AI` con badge de estado `Investigación en curso` (borde azul, icono de matraz).
- Descripción: `Exploro cómo personalizar contenido académico con inteligencia artificial para el LMS de mi universidad.`
- Chips: `IA`, `Moodle`, `Investigación`.
- Ficha técnica real (`<dl>`): `Entorno` (`Savio (Moodle · UTB)`), `Enfoque` (`Recomendación de recursos académicos`) y `Acceso` (`Investigación académica · sin repositorio público`). Sin botón: no se inventa URL.
- Maqueta decorativa en CSS (no captura real) con leyenda `Vista conceptual`: ventana con puntos macOS, menú lateral (`Savio AI`, `Inicio`, `Recomendaciones`, `Recursos`, `Mi curso`) y panel con `Hola, estudiante`, `Sugerencias de recursos para tu aprendizaje`, `Recursos recomendados` y tres filas (`Resumen: Redes de computadoras`, `Video: Introducción a la IA`, `Ejercicios de práctica`). En `<= 767 px` se simplifica a una sola columna legible (`>= 12 px`).

Fila de tres tarjetas secundarias (3 columnas desde `1024 px`; en tablet `768–1023 px`, SIPIIT ocupa el ancho completo en composición horizontal y las dos tarjetas en progreso comparten la segunda fila; en `<= 767 px`, 1 columna sin las dos maquetas decorativas secundarias):

1. **SIPIIT** (real, `Terminado`): título completo `Intelligent IT Incident Prioritization System (SIPIIT)`, fechas reales febrero-mayo de 2026 y rol `Interfaz Flutter`, descripción real de `content.md`, chips `Flutter`, `Dart`, `Riverpod`, `go_router`, `Git`, portada real `assets/proyectos/sipiit-portada.webp` completa sin recortes y enlace `Ver repositorio ↗` con URL real de GitHub.
2. **GyR Barber** (`En progreso`): metadato `Aplicación web · Reservas y servicios`, descripción `Gestión de reservas, citas y servicios para barbería.`, chips `React`, `Python`, `Supabase`, `PostgreSQL`, `Tailwind CSS`, maqueta decorativa de cabecera compacta (`>= 12 px`) con panel `Citas de hoy` en `>= 768 px` y nota `Sin repositorio público`.
3. **Próximo proyecto** (`En progreso`): metadato `Arquitectura backend · APIs e interfaz`, descripción `Nueva aplicación enfocada en arquitectura backend, diseño de APIs e interfaces modernas.`, chips `Python`, `SQL`, `React`, maqueta decorativa de cabecera compacta (`>= 12 px`) con panel `En construcción` en `>= 768 px` y nota `Sin repositorio público`.

La referencia 02 muestra tres proyectos y no incluye SIPIIT; se conserva SIPIIT
porque es el único proyecto con repositorio real. Las maquetas son ilustraciones
decorativas (`aria-hidden`), nunca capturas presentadas como reales.

### 02 / Sobre mí (`#sobre-mi`) — acento dorado

- Etiqueta: `02 / SOBRE MÍ` con icono monocromo de pingüino Tux (`#icono-tux-marca`) y barra horizontal en acento dorado.
- Titular: `Un poco sobre mí`.
- Columna izquierda:
  - Párrafo 1: `Estudio Ingeniería de Sistemas en la Universidad Tecnológica de Bolívar. Me interesa entender cómo funcionan las aplicaciones y construir soluciones útiles.`
  - Párrafo 2: `Actualmente participo en una investigación sobre recomendaciones académicas con IA para Savio. También soy mentor TEPAYA y acompaño a estudiantes de primer año.`
  - Chips: `Python`, `SQL`, `</> APIs`, `React`.
  - Filas de `Mi camino`, con icono, etiqueta y valor:
    1. `Formación` — `Ingeniería de Sistemas · UTB`.
    2. `Investigación` — `Personalización de contenido en Savio`.
    3. `Comunidad` — `Mentor TEPAYA`.
- Columna derecha: pingüino Ubuntu vectorial, decorativo (`aria-hidden`), con líneas doradas (ancho máximo `25rem` en escritorio; en `<= 1023 px` aparece después de la historia y `Mi camino`, escalado a `14rem` en tablet y `11.5rem` en móvil).
- Contenedor compartido `--ancho-contenido` (`80rem` / `1280 px`) alineado con cabecera, hero y proyectos.
- Subsección inferior: titular `Entornos que estoy explorando` y tres tarjetas: `Linux — Terminal y herramientas`, `Windows — Entorno de trabajo`, `macOS — Exploración del ecosistema`.
- Fondo: facetas vino, coral y violeta inspiradas en el wallpaper de Ubuntu.

Los entornos se presentan como aprendizaje, no como experiencia verificada: así
los diseñó el dueño.

### 03 / Formación (`#certificaciones`) — acento coral

- Etiqueta: `03 / FORMACIÓN` con icono monocromo de Apple (`#icono-apple`) y barra horizontal en acento coral, unificada con `01 / PROYECTOS` y `02 / SOBRE MÍ`.
- Titular: `Certificaciones`.
- Subtítulo: `Cursos y programas que complementan mi formación.`
- Ventana tipo Finder alineada al contenedor compartido de `80rem`, con filtros `Todos`, `Programación` y `Datos e IA`.
- Grilla de tres columnas desde `1024 px`, dos en tablet y una en móvil. En escritorio y tablet, las filas tienen la misma altura y los enlaces se alinean al pie de cada tarjeta.
- En móvil se muestran hasta tres certificados por página. Las flechas y el contador del Finder permiten cambiar de página dentro del filtro activo.
- El visor recorre todos los resultados del filtro activo con `Anterior`, `Siguiente` y las flechas del teclado. Muestra la posición, enlaza al original y devuelve el foco a la tarjeta de origen al cerrar.
- Al abrir el sitio sin JavaScript se muestran las cinco tarjetas con sus enlaces directos a las imágenes. La versión impresa también muestra las cinco.
- Fondo: paisaje costero de la guia HTML optimizado a WebP, con velo de contraste.

La referencia 04 usa la marca de Apple y un certificado de "Habilidades de
Investigación" que no existe en `content.md`. Se toma el emblema decorativo
de la guia para respetar el diseno, pero no se inventa el certificado: se
mantienen los cinco documentos del sitio.

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
- Fondo: ondas azul, violeta y coral con orbitas naranjas, extraidas del HTML de guia y optimizadas a WebP, con encuadre adaptativo y degradado inferior hacia `#0b1525` para enlazar limpiamente con el pie.
- Contenedor compartido `--ancho-contenido` (`80rem` / `1280 px`) en `#contacto` y `.pie`; altura proporcionada en escritorio (`clamp(35rem, 68dvh, 43rem)`) y compacta en móvil (`649.45 px` en `360 × 800`).

### Pie de página

- Línea divisoria superior tenue.
- `JV` a la izquierda (alineado a la izquierda también en móvil, manteniendo objetivo `>= 44 × 44 px`).
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

- **Layout full-bleed:** los fondos llegan a los bordes. El contenido se alinea con `--ancho-contenido` (`80rem`) y un padding lateral de `clamp(1.25rem, 4.5vw, 4.5rem)`.
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
- El nombre del hero se muestra en la primera pintura y la foto aparece cuando carga. Los demás bloques entran con desplazamiento corto y opacidad (máximo 0.7 s).
- Las ondas de luz conservan la deriva lenta. Con JavaScript, los fondos se animan cuando están a menos de 128 px del viewport.
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
