# Brief de diseño: Portfolio nocturno con ondas de luz

Estado: **aprobado por el dueño el 2026-11-10** (issues D1 #42 y D3 #44).
Producto final definido por las **cuatro imágenes de referencia del dueño**, organizadas en `docs/referencias/` como documentación visual del proyecto:

1. `docs/referencias/01-hero-ondas.png` — hero con ondas de luz.
2. `docs/referencias/02-proyectos.png` — sección 01 / Proyectos.
3. `docs/referencias/03-sobre-mi.png` — sección 02 / Sobre mí.
4. `docs/referencias/04-certificaciones-contacto.png` — secciones 03 y 04 + footer.

El contenido de este brief se extrajo de esas imágenes con el modelo de visión
`opencode-go/gemini-4-argon` (ruta 4) el 2026-11-10, porque el modelo de
implementación no procesa imágenes. Los textos literales provienen de esa
extracción y de `content.md`. Nada se inventa: lo que no tiene respaldo real
queda marcado.

## 1. Sujeto y trabajo del sitio

- **Sujeto:** Jesús David Velásquez Mercado, estudiante de Ingeniería de Sistemas. Backend con Python, SQL y APIs. Investigación en recomendaciones con IA para Savio. Interfaz Flutter de SIPIIT.
- **Audiencia:** reclutadores técnicos y líderes de ingeniería que revisan el perfil en menos de un minuto.
- **Trabajo principal:** que en 30 segundos entiendan qué hace, con qué tecnologías trabaja y cómo contactarlo.
- **Estructura:** una sola página con **scroll vertical hacia abajo**, navegación superior fija y cinco anclas: Inicio, Proyectos, Sobre mí, Certificaciones, Contacto.

## 2. Concepto

Una frase: *un portfolio nocturno atravesado por ondas de luz: azul para actuar, dorado para aprender, coral para respaldar.*

Tres adjetivos: nocturno, luminoso, directo.

El fondo es casi negro azulado y cada sección se distingue por una onda de luz de
color propio. La página se lee de arriba abajo como una sola historia: quién soy,
qué construyo, qué me respalda y cómo hablar conmigo.

## 3. Estructura y textos literales

### Navegación superior (todas las secciones)

- Marca: `JV` a la izquierda, en blanco.
- Enlaces a la derecha: `Inicio`, `Proyectos`, `Sobre mí`, `Certificaciones`, `Contacto`.
- Estado activo: texto blanco en negrita y subrayado corto en el color de acento de la sección visible.
- Barra fija con fondo oscuro translúcido y línea divisoria inferior tenue.

### Hero (`#inicio`) — acento azul

- Antetítulo: `JESÚS DAVID VELÁSQUEZ MERCADO`.
- Titular: `Desarrollo software.` y `Sigo explorando.` (segunda línea con leve tinte celeste).
- Subtítulo: `Backend con Python, SQL y APIs. Interfaces con React.`
- Badge de disponibilidad: punto verde + `Disponible para prácticas`.
- Botones: `Ver proyectos ↗` (azul sólido, ancla a #proyectos) y `Descargar CV` (contorno, abre el diálogo de impresión para guardar PDF; no existe un PDF público, no se inventa archivo).
- Bloque `Mis entornos de aprendizaje` con chips: `Linux`, `macOS`, `Windows`.
- Tarjeta de perfil a la derecha: foto original sin filtros (~70 % de la altura), pie con `Jesús David` y `Estudiante de Ingeniería de Sistemas`; debajo y fuera de la tarjeta: `GitHub` y `LinkedIn` separados por línea vertical.
- Indicador centrado al pie del hero: `Desliza para explorar ↓`.
- Ondas: cian/azul descendente desde el borde superior derecho, ámbar desde la izquierda inferior, magenta/violeta desde la derecha inferior.

### 01 / Proyectos (`#proyectos`) — acento azul

- Etiqueta: `01 / PROYECTOS` con línea corta azul.
- Titular: `Ideas que llevo al código.`
- Subtítulo: `Proyectos académicos y personales en desarrollo de software e inteligencia artificial.`

Tarjeta destacada (ancho completo, texto izquierda ~40 %, maqueta derecha ~60 %):

- Badge sólido azul: `PROYECTO DESTACADO`.
- Título: `Savio AI` con badge de estado `Investigación en curso` (borde azul, icono de destello).
- Descripción: `Exploro cómo personalizar contenido académico con inteligencia artificial para el LMS de mi universidad.`
- Chips: `IA`, `Moodle`, `Investigación`.
- Sin botón: la investigación no tiene repositorio ni demo públicos. No se inventa el enlace.
- Maqueta decorativa en CSS (no captura real): ventana con puntos macOS, menú lateral (`Savio AI`, `Inicio`, `Recomendaciones`, `Recursos`, `Mi curso`) y panel con banner `Hola, estudiante`, tres tarjetas de acción (`Revisar tema`, `Ver recurso`, `Practicar`) y chips de `Tipos de recursos` (`Lecturas`, `Videos`, `</> Ejercicios`, `Material adicional`).

Fila de tres tarjetas secundarias:

1. **SIPIIT** (real, `Terminado`): título completo `Intelligent IT Incident Prioritization System (SIPIIT)`, fechas reales febrero-mayo de 2026, descripción real de `content.md`, chips `Flutter`, `Dart`, `Git`, portada real `assets/proyectos/sipiit-portada.webp` y botón `Ver repositorio ↗` con URL real de GitHub.
2. **Finanzas personales** (`En progreso`): `Registro de ingresos y gastos.`, chips `Flutter`, `Dart`. Sin botón: no hay repositorio. Maqueta decorativa con panel `Mis finanzas`, tarjetas `Ingresos` (verde) y `Gastos` (rojo) y gráfico de barras.
3. **StudyPlanner** (`En progreso`): `Organización de tareas y seguimiento de estudio.`, chip `Java`. Sin botón: no hay repositorio. Maqueta decorativa con panel `Mis tareas` y tres tareas con píldoras de color.

Los badges `En progreso` aplican por pedido del dueño a los proyectos que solo
existen en sus imágenes de referencia. Las maquetas son ilustraciones decorativas
(`aria-hidden`), nunca capturas presentadas como reales.

### 02 / Sobre mí (`#sobre-mi`) — acento dorado

- Etiqueta: `02 / SOBRE MÍ`.
- Titular: `Curiosidad para aprender.` (blanco) y `Iniciativa para construir.` (dorado).
- Subtítulo: `Jesús David Velásquez Mercado · Estudiante de Ingeniería de Sistemas`.
- Columna izquierda: dos párrafos reales (universidad, backend, investigación Savio, mentoría TEPAYA) y chips grandes: `Python`, `SQL`, `</> APIs`, `React`.
- Columna derecha: tarjeta `Mi camino`, línea vertical con tres nodos dorados e iconos (birrete, matraz, personas):
  1. `Formación` — `Ingeniería de Sistemas · UTB`.
  2. `Investigación` — `Personalización de contenido para Savio`.
  3. `Comunidad` — `Mentor estudiantil · TEPAYA`.
- Subsección inferior: titular `Aprender también es explorar nuevos entornos.` con badge `En aprendizaje`, subtítulo `Actualmente profundizo en mis herramientas de desarrollo.` y tres tarjetas: `Linux — Terminal y herramientas`, `Windows — Entorno de trabajo`, `macOS — Exploración del ecosistema`.

TEPYA y la educación se integran aquí como hitos del camino; ya no existe una
sección de Experiencia aparte. Los entornos se presentan como aprendizaje, no
como experiencia verificada: así los diseñó el dueño.

### 03 / Certificaciones (`#certificaciones`) — acento coral

- Etiqueta: `03 / CERTIFICACIONES` con línea corta coral.
- Titular: `Formación que impulsa mi camino.`
- Subtítulo: `Aprendizajes en programación, datos e inteligencia artificial.`
- Seis tarjetas reales (la referencia muestra tres; se muestran las seis de `content.md` en grilla de tres columnas): título real completo, emisor real y enlace `Ver certificado ↗` que abre el visor accesible existente.
- Ilustración de documento en CSS con barra y sello que rotan en azul, verde y violeta (no sustituye la imagen real: el visor muestra el certificado verdadero).

### 04 / Contacto (`#contacto`) — acento azul, centrado

- Etiqueta: `04 / CONTACTO` con línea corta azul.
- Titular: `La próxima idea empieza con una conversación.`
- Subtítulo: `Estoy abierto a prácticas y oportunidades para seguir aprendiendo y aportar.`
- Botones: `Escríbeme` (azul sólido, `mailto:` real), `LinkedIn ↗` y `GitHub ↗` (contorno, URLs reales).

### Pie de página

- Línea divisoria superior.
- `Jesús David Velásquez Mercado` a la izquierda.
- `Volver arriba ↑` a la derecha (ancla a `#inicio`).

## 4. Paleta

### Oscuro (tema canónico)

| Token | Valor | Uso |
|---|---|---|
| noche | `#070b14` | fondo |
| superficie | `#111a2e` | tarjetas, chips y paneles |
| superficie-2 | `#0e1729` | tarjetas de proyecto |
| blanco | `#f5f6f8` | texto principal |
| plata | `#c8ccd4` | párrafos |
| gris | `#94a3b8` | subtítulos y metadatos |
| azul | `#2b72fb` | acción principal: botones, enlaces, subrayados |
| azul-claro | `#3b82f6` | etiquetas de sección azules |
| oro | `#f2c94c` | acento de Sobre mí |
| coral | `#f06464` | acento de Certificaciones |
| verde | `#22c55e` | punto de disponibilidad |
| borde | `#26314a` | bordes de tarjetas y chips |

### Claro (alternativa accesible)

| Token | Valor | Uso |
|---|---|---|
| papel | `#f5f7fc` | fondo |
| superficie | `#ffffff` | tarjetas |
| tinta | `#0b1220` | texto principal |
| gris | `#475569` | subtítulos |
| azul | `#1d4ed8` | acción principal |
| oro | `#a16207` | acento de Sobre mí |
| coral | `#be123c` | acento de Certificaciones |
| verde | `#15803d` | disponibilidad |
| borde | `#d8deea` | bordes |

### Contraste medido (WCAG)

Se verifica en la implementación con script sobre los pares texto/fondo y
texto/superficie de ambos temas, incluido el texto que cruza las ondas. La regla:
ningún par por debajo de 4.5:1. Las ondas se mantienen detrás del texto con baja
opacidad y los resplandores evitan las crestas más luminosas, como en la referencia.

### Ondas de luz

- Hero: onda cian/azul (`#1d4ed8` → `#38bdf8`) desde arriba a la derecha; ámbar (`#f59e0b`) abajo a la izquierda; magenta/violeta (`#ec4899` → `#6d28d9`) abajo a la derecha.
- Proyectos: listones azules 3D en la esquina superior derecha.
- Sobre mí: onda dorada que nace arriba a la izquierda y cresta arriba a la derecha.
- Certificaciones: cinta multicolor azul → violeta → coral de izquierda a derecha.
- Contacto: resplandores ámbar, zafiro y púrpura.
- Implementación: SVG con degradados y desenfoque, `aria-hidden`, `pointer-events: none`, estático (sin animación) y con opacidad reducida en tema claro.

## 5. Tipografía

Dos familias, sin cambios:

- **Inter:** titulares, párrafos y navegación.
- **JetBrains Mono:** etiquetas de sección, chips, botones y datos.

Ambas autohospedadas en WOFF2 con `font-display: swap`, `unicode-range` latin y
licencias OFL-1.1 verificadas. La referencia tipográfica de las imágenes es una
sans geométrica; Inter ya cubre ese registro.

## 6. Componentes

- **Layout full-bleed:** sin `max-width` de 75 rem. Todas las secciones usan `padding-inline: clamp(1rem, 4.5vw, 4.5rem)`. A 1440 px el contenido ocupa 1295 px (90.9 % del ancho visible); a 1920 px ronda el 91 %.
- **Hero:** dos columnas por encima de 1023 px (texto flexible + tarjeta de perfil de 384 px); una columna desde 1023 px, con la tarjeta centrada y un máximo de 22 rem.
- **Grillas:** proyectos 3 columnas en escritorio, 2 en tablet y 1 en móvil; certificaciones 3/2/1; entornos 3/2/1. Los párrafos conservan su ancho de lectura.
- **Botón primario:** relleno azul sólido, radio ~10 px, texto blanco, flecha `↗`.
- **Botón secundario:** contorno fino claro, fondo translúcido, texto blanco.
- **Chip:** píldora `9999px`, fondo oscuro, borde fino, icono + etiqueta mono.
- **Tarjeta:** radio ~16 px, fondo translúcido, borde fino, sin sombras pesadas.
- **Badge de estado:** píldora con icono; `Investigación en curso` (borde azul), `En progreso`, `Terminado`, `En aprendizaje` (dorados).
- **Badge destacado:** píldora azul sólida en mayúsculas.
- **Etiqueta de sección:** mono en mayúsculas con número `01 /`, línea corta del acento, titular grande y subtítulo.
- **Foco:** contorno de 2 px, nunca se elimina.
- **Maquetas:** ventanas con puntos macOS, menú lateral y panel; decorativas, `aria-hidden`, ocultas en impresión.

## 7. Movimiento

- Sin parallax ni scroll-jacking. El scroll sigue siendo vertical y predecible.
- Entrada del hero con desplazamiento corto y opacidad, escalonada por bloques (máximo 0.7 s).
- Ondas de luz con deriva lenta y continua (`translate` + `scale`, 18-24 s, alterna).
- Punto de disponibilidad con pulso suave y flecha de "Desliza para explorar" con rebote corto.
- Tarjetas y botones con elevación de 2-4 px y borde iluminado al pasar el puntero.
- Los revelados por scroll se documentan como pendiente D11; no se inventan aquí.
- Hover y foco con transiciones de 150 ms.
- `prefers-reduced-motion`: sin animaciones, transiciones ni scroll suave.
- El scroll es suave con `scroll-behavior: smooth` y `scroll-padding-top` para la barra fija.

## 8. Decisiones de integridad

- **Sin botón en Savio AI:** no existe repositorio ni demo públicos de la investigación.
- **Sin botones en Finanzas personales y StudyPlanner:** son ideas en desarrollo del dueño; se muestran con badge `En progreso` y maqueta decorativa.
- **SIPIIT con datos y URL reales:** es el único proyecto con repositorio público; conserva su portada real.
- **`Descargar CV` abre el diálogo de impresión:** no existe PDF público que descargar.
- **Entornos como aprendizaje:** Linux, macOS y Windows se presentan como exploración, no como experiencia verificada.
- **Certificaciones con nombres completos reales** de `content.md`, no los abreviados de la referencia.
- **h1 = titular del hero** (`Desarrollo software. Sigo explorando.`), como en la referencia; el nombre completo vive en el antetítulo, la tarjeta de perfil, el `title`, el pie y el JSON-LD.

## 9. Verificación de la dirección

- [ ] Scroll vertical único con navegación superior fija.
- [ ] Cinco anclas: inicio, proyectos, sobre-mi, certificaciones, contacto.
- [ ] Ondas de luz por sección, detrás del texto.
- [ ] Un solo `h1`; jerarquía h2/h3 correcta.
- [ ] Contraste AA en claro y oscuro, incluido el texto sobre ondas.
- [ ] Teclado completo: menú móvil, visor de certificados, volver arriba.
- [ ] Impresión A4 sin ondas, navegación, maquetas ni botones.
- [ ] Sin contenido inventado: todo texto sale de `content.md` o de las imágenes del dueño.
- [ ] Tema claro alternativo funcional.

## 10. Referencias

- Cuatro imágenes del dueño (2026-11-10): producto final, versionadas en `docs/referencias/` con nombres ASCII.
- `bchiang7/v4` (MIT): superada por estas imágenes; su crédito se retira del pie y queda en el historial del repositorio.
- Inter: OFL-1.1 (`github.com/rsms/inter`).
- JetBrains Mono: OFL-1.1 (`github.com/JetBrains/JetBrainsMono`).
- Skills: `frontend-design` (Apache 2.0), `ui-ux-pro-max` (MIT), `taste-skill`, `web-design`, `web-interface-guidelines` en `.claude/skills/`.

## 11. Alternativas descartadas

- **Portfolio técnico nocturno (Brittany Chiang)**: implementada en `bcc373a`; el dueño definió un nuevo producto final con sus propias imágenes. El crédito visible se retira.
- **Cianotipo**: revertida en `2847675`.
- **Signal dossier** y **Editorial cobalto**: descartadas antes de implementarse.

## 12. Pendientes

- Aprobación visual del dueño sobre la implementación.
- Regenerar OG y favicon en la nueva paleta (hecho en esta iteración; ver sección 13).
- D8: revalidar Lighthouse, axe y navegadores con el diseño nuevo.
- D11: paridad visual fina y revelados por scroll; ver issue correspondiente.
- Las cuatro imágenes de referencia viven en `docs/referencias/` y se versionan con el proyecto.
