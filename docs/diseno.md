# Brief de diseño: Portfolio técnico nocturno

Estado: **aprobado por el dueño el 2026-11-10** (issue D1, #42).
Referencia elegida por el dueño: **`bchiang7/v4`** (Brittany Chiang).

## 1. Sujeto y trabajo del sitio

- **Sujeto:** Jesús David Velásquez Mercado, estudiante de Ingeniería de Sistemas. Backend con Python, SQL y APIs. Proyecto de interfaces Flutter (SIPIIT). Investigación en recomendaciones con IA para Savio.
- **Audiencia:** reclutadores técnicos y líderes de ingeniería que revisan el perfil en menos de un minuto.
- **Trabajo principal:** que en 30 segundos entiendan qué hace, con qué tecnologías trabaja y cómo contactarlo.
- **Vernáculo del sujeto:** terminal, editor de código, documentación técnica y tableros de proyecto. La referencia traduce ese mundo a una pieza editorial: fondo navy, acento teal y etiquetas monoespaciadas.

## 2. Concepto

Una frase: *un portfolio de desarrollador que se lee como una consola bien cuidada: oscuro, ordenado y con un acento que guía la lectura.*

Tres adjetivos: preciso, nocturno, directo.

La dirección toma la estructura y el lenguaje visual de `bchiang7/v4` porque el dueño la eligió de forma explícita. No es una copia: se reescribe el contenido, se adapta a un CV con educación, certificaciones y habilidades, y se agregan tema claro, impresión A4 y accesibilidad AA.

## 3. Qué se toma y qué no

Se toma de la referencia:

- Rail izquierdo fijo en escritorio con identidad, navegación y contacto.
- Fondo navy, superficies un escalón más claras y un único acento teal.
- Etiquetas de sección en monoespaciada con numeración `01.`, `02.`.
- Enlaces con subrayado fino y botones de contorno.
- Etiquetas tipo píldora para tecnologías.
- Spotlight radial muy tenue que sigue al puntero.

No se toma:

- El texto de la referencia ("Hello, my name is", "I build things for the web") ni sus datos.
- Su paleta exacta en el tema claro: la referencia no tiene tema claro; aquí se construye uno con el mismo matiz y contraste AA.
- Animaciones de entrada por sección, parallax ni carruseles.
- Iconos de redes dibujados a mano: se usan SVG propios con etiqueta accesible.

### Nota sobre los rasgos genéricos

La skill `frontend-design` marca como cliché el fondo navy con acento teal, las etiquetas monoespaciadas y la numeración de secciones. Esta dirección los usa porque el dueño eligió la referencia de forma consciente. La decisión queda documentada y se mitiga así:

- No se copia el copy ni la composición exacta.
- El tema claro es propio y no un invertido automático.
- El movimiento se limita a una entrada y al spotlight; sin animaciones por sección.
- El elemento memorable es el retrato y la portada real de SIPIIT, no un efecto.

## 4. Paleta

### Oscuro (tema canónico)

| Token | Valor | Uso |
|---|---|---|
| noche | `#0a192f` | fondo |
| capa | `#112240` | superficies, tarjetas y etiquetas |
| tinta | `#ccd6f6` | texto principal y títulos |
| pizarra | `#8892b0` | texto secundario |
| teal | `#64ffda` | acento: enlaces, foco, números y botones |
| borde | `#233554` | líneas y bordes |
| sobre-acento | `#0a192f` | texto sobre botón teal |

### Claro

| Token | Valor | Uso |
|---|---|---|
| papel | `#f7fafc` | fondo |
| capa | `#e8eef6` | superficies, tarjetas y etiquetas |
| tinta | `#0a192f` | texto principal y títulos |
| pizarra | `#475569` | texto secundario |
| teal oscuro | `#0b7263` | acento: enlaces, foco, números y botones |
| borde | `#cbd5e1` | líneas y bordes |
| sobre-acento | `#ffffff` | texto sobre botón teal |

### Contraste medido (WCAG)

| Par | Ratio | Requisito | Uso |
|---|---|---|---|
| tinta / noche | 12.17:1 | 4.5:1 | texto principal en oscuro |
| pizarra / noche | 5.69:1 | 4.5:1 | secundario en oscuro |
| teal / noche | 14.13:1 | 4.5:1 | enlaces y foco en oscuro |
| tinta / capa oscura | 10.94:1 | 4.5:1 | texto en tarjetas |
| pizarra / capa oscura | 5.11:1 | 4.5:1 | secundario en tarjetas |
| teal / capa oscura | 12.71:1 | 4.5:1 | enlaces en tarjetas |
| tinta / papel | 16.79:1 | 4.5:1 | texto principal en claro |
| pizarra / papel | 7.23:1 | 4.5:1 | secundario en claro |
| teal oscuro / papel | 5.56:1 | 4.5:1 | enlaces y foco en claro |
| tinta / capa clara | 15.08:1 | 4.5:1 | texto en tarjetas |
| pizarra / capa clara | 6.49:1 | 4.5:1 | secundario en tarjetas |
| teal oscuro / capa clara | 5.00:1 | 4.5:1 | enlaces en tarjetas |
| blanco / teal oscuro | 5.83:1 | 4.5:1 | texto sobre botón claro |
| noche / teal | 14.13:1 | 4.5:1 | texto sobre botón oscuro |

Un solo acento en cada tema. Sin colores secundarios ni degradados de marca.

## 5. Tipografía

Dos familias:

- **Texto e interfaz: Inter.** Cuerpo, títulos y navegación. Pesos 400, 500, 600 y 700.
- **Etiquetas y datos: JetBrains Mono.** Números de sección, fechas, tecnologías y botones. Pesos 400 y 500.

Ambas se autohospedan en `assets/fonts/` en WOFF2 variable, con `font-display: swap` y `unicode-range` latin.

Licencias verificadas el 2026-11-10:

- Inter: OFL-1.1 (`github.com/rsms/inter`).
- JetBrains Mono: OFL-1.1 (`github.com/JetBrains/JetBrainsMono`).

Escala:

| Token | Tamaño | Uso |
|---|---|---|
| `--text-xs` | 12 px | etiquetas mono y numeración |
| `--text-sm` | 14 px | metadatos, fechas y notas |
| `--text-base` | 16 px | cuerpo |
| `--text-lg` | 18 px | entradilla |
| `--text-xl` | 20 px | títulos de tarjeta |
| `--text-2xl` | 24 px | subtítulos |
| `--text-3xl` | 32 px | títulos de sección |
| `--text-4xl` | 40-64 px | nombre en el hero, con `clamp()` |

Interlineado 1.6 en cuerpo y 1.1 en títulos. Medida máxima de línea: 68 caracteres.

## 6. Layout

**Escritorio (desde 1024 px):** rail izquierdo fijo de 40 % y columna de contenido de 60 %, con scroll en la columna derecha. El rail se centra verticalmente.

```
+---------------------------------------------------------------+
| Jesús David              |  01. Sobre mí                      |
| Velásquez Mercado        |  ...                               |
| Desarrollador Full Stack |                                    |
|                          |  02. Experiencia                   |
| [01] Sobre mí            |  2026-01  Mentor estudiantil       |
| [02] Experiencia         |           Universidad ...          |
| [03] Proyectos           |                                    |
| [04] Educación           |  03. Proyectos                     |
| [05] Habilidades         |  SIPIIT                            |
| [06] Contacto            |                                    |
|                          |  04. Educación y certificaciones   |
| GitHub · LinkedIn · Mail |  05. Habilidades                   |
| Tema      Imprimir       |  06. Contacto                      |
+---------------------------------------------------------------+
```

**Tablet (640-1023 px):** una columna. Cabecera con nombre, cargo y navegación en una fila; contenido debajo.

**Móvil (menos de 640 px):** una columna. Cabecera compacta sin fijación, navegación en dos filas, retrato de 96 px y botones a ancho completo.

## 7. Elemento memorable

Dos piezas, en este orden:

1. El **retrato** en el hero, con marco teal desplazado y tratamiento duotono en navy y teal.
2. La **portada real de SIPIIT** en la tarjeta del proyecto, sin marco ni sombra.

Todo lo demás se mantiene sobrio. El spotlight es un detalle ambiental, no el elemento principal.

## 8. Movimiento

- Entrada inicial: nombre, cargo y retrato aparecen con un desplazamiento de 12 px y opacidad, en 500 ms, con 80 ms de separación.
- Spotlight: radial de 600 px que sigue al puntero en el hero, con opacidad máxima de 0.08. Solo en puntero fino.
- Hover: subrayado teal en enlaces y borde teal en botones, 150 ms.
- Sin animación por sección, sin parallax y sin carruseles.
- Con `prefers-reduced-motion: reduce`, no hay entrada, spotlight ni transiciones.

## 9. Componentes

- **Rail:** nombre, cargo, navegación numerada con estado activo, enlaces sociales, botón de tema y botón de imprimir. En móvil pasa a cabecera.
- **Etiqueta de sección:** número mono en teal, título en Inter 32 px y línea horizontal de 1 px que ocupa el resto.
- **Hero:** nombre, cargo, propuesta de valor de dos líneas, dos acciones (correo y LinkedIn) y retrato.
- **Botón:** contorno teal de 1 px, radio 4 px, texto mono de 14 px, relleno teal al 10 % en hover.
- **Enlace:** teal con subrayado de 1 px y `text-underline-offset: 4px`.
- **Etiqueta de tecnología:** píldora de 999 px, fondo `--color-capa`, texto mono de 12 px.
- **Experiencia:** lista vertical con fecha en `<time>` a la izquierda; puesto, empresa y tres logros. Sin tabs.
- **Proyecto SIPIIT:** portada, título, fechas, descripción, tecnologías y enlace al repositorio.
- **Educación y certificaciones:** lista con institución, fechas y actividades; certificados con enlace al emisor.
- **Habilidades:** grupos con etiquetas de tecnología.
- **Contacto:** correo, LinkedIn, GitHub y ubicación.
- **Foco:** contorno de 2 px en `--color-acento` con `offset` de 2 px; nunca se elimina.

## 10. Texto de la interfaz

- Verbos simples y frases cortas. Sin "proactivo" ni adjetivos sin prueba.
- Botones con la acción real: "Escribir por correo", "Ver repositorio en GitHub", "Imprimir o guardar PDF".
- Las etiquetas de sección usan sustantivos: "Sobre mí", "Experiencia", "Proyectos", "Educación", "Habilidades", "Contacto".
- Sin signos de admiración ni emojis.

## 11. Verificación de la dirección

- [ ] Dos familias: Inter e JetBrains Mono, ambas autohospedadas.
- [ ] Un solo acento por tema.
- [ ] Contraste AA en claro y oscuro (sección 4).
- [ ] Rail fijo en escritorio y cabecera en móvil.
- [ ] Etiquetas de sección numeradas y en mono.
- [ ] Un solo elemento memorable principal (retrato) y la portada de SIPIIT.
- [ ] Sin copy de la referencia.
- [ ] Tema claro y oscuro con el mismo contenido.
- [ ] Impresión A4 legible sin rail ni botones.

## 12. Referencias

Verificadas el 2026-11-10:

- `bchiang7/v4` (Brittany Chiang): licencia MIT. Referencia de estructura, paleta oscura y lenguaje visual. Se da crédito en el README del proyecto y en el pie del sitio si se publica.
- `every-layout.dev` (Heydon Pickering y Andy Bell): fundamentos de layout en CSS gratuitos; el libro y los componentes son de pago. Solo referencia; no se copian ejemplos.
- `utopia.fyi` (James Gilyead y Trys Mudford): escalas fluidas de tipo y espacio. Solo referencia de método.
- Inter: OFL-1.1 (`github.com/rsms/inter`).
- JetBrains Mono: OFL-1.1 (`github.com/JetBrains/JetBrainsMono`).
- `anthropics/skills`, skill `frontend-design`: Apache 2.0. Copiada en `.claude/skills/frontend-design/` con su `LICENSE.txt`.
- `nextlevelbuilder/ui-ux-pro-max-skill`, skill `ui-ux-pro-max`: MIT. Copiada en `.claude/skills/ui-ux-pro-max/` con su `LICENSE.txt`.

## 13. Alternativas descartadas

- **Cianotipo** (implementada en `bfff558` y revertida en `2847675`): papel azul, serif Literata y Bricolage Grotesque. Rechazada por el dueño por fría y técnica. No se recupera.
- **Signal dossier**: fondo casi negro con lima y etiquetas mono. Rasgos genéricos de la skill y contraste insuficiente del lima sobre papel.
- **Editorial cobalto**: papel crema con serif. Rasgo genérico de la skill.
- **shadcn/ui clean**: sistema neutral y corporativo; el dueño prefirió un portfolio con identidad propia.
- **al-folio académico**: sesgo académico que no refleja el perfil de desarrollo.
- **Carbon / Primer / USWDS**: sistemas enterprise, correctos pero impersonales para un CV.

## 14. Pendientes

- Crédito visible a `bchiang7/v4` en el README y en el pie del sitio.
- D6: usar `assets/proyectos/sipiit-portada.webp` (imagen real provista por el dueño).
- D8: revalidar Lighthouse y axe con el diseño nuevo.
