# Brief de diseño: Cianotipo

Estado: **aprobado por el dueño el 2026-11-10** (issue D1, #42).

## 1. Sujeto y trabajo del sitio

- **Sujeto:** Jesús David Velásquez Mercado, estudiante de Ingeniería de Sistemas. Backend con Python, SQL y APIs. Proyecto de interfaces Flutter (SIPIIT). Investigación en recomendaciones con IA para Savio.
- **Audiencia:** reclutadores técnicos y líderes de ingeniería que revisan el perfil en menos de un minuto.
- **Trabajo principal:** que en 30 segundos entiendan qué hace, con qué tecnologías trabaja y cómo contactarlo.
- **Vernáculo del sujeto:** planos técnicos, diagramas de sistemas, trazas de ejecución y esquemas de base de datos. De ahí sale la dirección: el cianotipo era el papel azul con el que se copiaban los planos técnicos.

## 2. Concepto

Una frase: *un plano técnico de alguien que construye sistemas: claro, medido, sin decoración.*

Tres adjetivos: preciso, sobrio, con un solo punto memorable.

## 3. Rasgos genéricos que se evitan

Basado en la skill `frontend-design` (anthropics/skills):

- Fondo crema con serif y acento terracota.
- Fondo casi negro con acento lima o ácido. **Retira la propuesta anterior "Signal dossier"**, que lo usaba.
- Tarjetas idénticas con sombra suave y gradientes decorativos.
- Etiquetas en mayúsculas encima de cada título.
- Fuente monoespaciada en etiquetas pequeñas. **También retirada de "Signal dossier".**
- Punto medio entre datos (`A · B · C`). Se usan saltos de línea o separación.
- Flecha `→` en enlaces y botones.
- Numeración `01 / 02 / 03` en secciones. Solo sería válida en una secuencia real; la línea de tiempo se marca con fechas.
- Resaltar una sola palabra del titular.

## 4. Paleta

### Claro

| Token | Valor | Uso |
|---|---|---|
| papel | `#f3f5f7` | fondo |
| tinta | `#1b2330` | texto principal |
| cianotipo | `#1f4e8c` | acento: enlaces, foco y botón |
| niebla | `#5b6573` | texto secundario |
| superficie | `#e6ebf1` | bloques y fondo del retrato |
| trazo | `#d5dce4` | líneas y bordes |

### Oscuro

| Token | Valor | Uso |
|---|---|---|
| noche | `#0c2238` | fondo |
| luz | `#e6eef7` | texto principal |
| azul claro | `#8ec5ff` | acento: enlaces, foco y botón |
| bruma | `#a9b8c9` | texto secundario |
| capa | `#132d48` | superficies |
| trazo | `#24415e` | líneas y bordes |

### Contraste medido (WCAG)

| Par | Ratio | Requisito | Uso |
|---|---|---|---|
| tinta / papel | 14.45:1 | 4.5:1 | texto principal |
| niebla / papel | 5.41:1 | 4.5:1 | texto secundario |
| cianotipo / papel | 7.60:1 | 4.5:1 | enlaces y foco |
| tinta / superficie | 13.17:1 | 4.5:1 | texto en bloques |
| niebla / superficie | 4.93:1 | 4.5:1 | secundario en bloques |
| luz / noche | 13.78:1 | 4.5:1 | texto principal |
| bruma / noche | 7.98:1 | 4.5:1 | texto secundario |
| azul claro / noche | 8.90:1 | 4.5:1 | enlaces y foco |
| luz / capa | 11.99:1 | 4.5:1 | texto en bloques |
| bruma / capa | 6.94:1 | 4.5:1 | secundario en bloques |

Un solo acento en cada tema. Sin lima ni colores secundarios.

## 5. Tipografía

Dos familias, claramente distintas:

- **Display: Bricolage Grotesque.** Nombre, títulos y cifras. Peso 600 a 700.
- **Texto: Literata.** Serif de lectura para el cuerpo. Interlineado 1.6 por ser serif.

Ninguna otra familia. Sin monoespaciada. Ambas se autohospedan en `assets/fonts/` en WOFF2 con `font-display: swap`.

Licencias verificadas el 2026-11-10:
- Bricolage Grotesque: OFL-1.1 (`github.com/ateliertriay/bricolage`).
- Literata: OFL-1.1 (`github.com/googlefonts/literata`).

Escala (escritorio): 14, 16, 18, 22, 28, 40 y 64 px. En móvil, el display baja con `clamp()`. Medida de línea máxima: 68 caracteres.

## 6. Layout

Alineación a la izquierda en todo el sitio, incluido el hero. Sin texto centrado.

**Escritorio (desde 900 px):** rail izquierdo fijo con identidad y contacto, y columna principal con el contenido.

```
+-------------------------------------------------------------+
| RAIL                  | Jesús David                         |
| Cargo                 | Velásquez Mercado        [retrato]  |
| Contacto              | Propuesta de valor                  |
| Anclas                |                                     |
| Tema / imprimir       | Experiencia                         |
|                       | 2026-01  Mentor estudiantil         |
|                       |          Universidad ...            |
|                       | Proyecto                            |
|                       | Educación                           |
|                       | Certificaciones                     |
|                       | Habilidades y contacto              |
+-------------------------------------------------------------+
```

**Móvil (menos de 640 px):** una columna. El rail pasa a cabecera compacta, sin fijación. Retrato de 96 px.

## 7. Elemento memorable

Un solo elemento: el retrato en **duotono cianotipo** (tinta y papel del proyecto), de unos 480 px en escritorio. Es la única pieza con color intenso. Todo lo demás se mantiene sobrio.

## 8. Movimiento

- Una sola secuencia al cargar: el retrato se revela en unos 600 ms.
- Sin animación por sección ni hover en tarjetas.
- Hover solo en enlaces (subrayado).
- Con `prefers-reduced-motion`, no hay animación.

## 9. Componentes

- **Rail:** nombre, cargo, contacto, anclas con estado activo (subrayado, sin fondo de color), tema y botón de imprimir.
- **Hero:** nombre, cargo, propuesta de valor, dos acciones (correo y LinkedIn) y retrato.
- **Experiencia:** cronología con fecha en `<time>` a la izquierda; puesto, empresa y tres logros. Sin numeración.
- **Proyecto SIPIIT:** título, fechas en línea propia, descripción, tecnologías como texto y enlace "Repositorio en GitHub".
- **Educación:** título, institución, fechas y actividades.
- **Certificaciones:** imágenes en dos columnas en escritorio y una en móvil. El emisor y la fecha van en línea propia.
- **Habilidades:** grupos como lista de texto, sin etiquetas tipo chip.
- **Contacto:** correo, LinkedIn y GitHub.

## 10. Texto de la interfaz

- Verbos simples y frases cortas. Sin "proactivo" ni adjetivos sin prueba.
- Botones con la acción real: "Escribir por correo", "Ver repositorio en GitHub", "Imprimir o guardar PDF".
- Sin flechas ni puntos medios.

## 11. Verificación de la dirección

- [ ] Dos familias, una de ellas de lectura.
- [ ] Un solo acento por tema.
- [ ] Contraste AA en claro y oscuro (sección 4).
- [ ] Un solo elemento memorable (retrato).
- [ ] Ningún rasgo de la sección 3.
- [ ] Alineación a la izquierda en todo el sitio.

## 12. Referencias (candidatas; verificar enlace y licencia antes de usar)

Verificadas el 2026-11-10:

- `bchiang7/v4` (Brittany Chiang): licencia MIT. Referencia de estructura de rail fijo y biografía. No se copian paleta ni código; si se toma algo, se da crédito.
- `every-layout.dev` (Heydon Pickering y Andy Bell): fundamentos de layout en CSS gratuitos; el libro y los componentes son de pago. Solo referencia; no se copian ejemplos.
- `utopia.fyi` (James Gilyead y Trys Mudford): escalas fluidas de tipo y espacio. Solo referencia de método.
- Bricolage Grotesque y Literata: OFL-1.1 (sección 5).
- `anthropics/skills`, skill `frontend-design`: Apache 2.0. Copiada en `.claude/skills/frontend-design/` con su `LICENSE.txt`.

## 13. Alternativas descartadas

- **Signal dossier** (propuesta anterior): fondo casi negro con lima y etiquetas en monoespaciada. Rasgos 2 y 5 de la skill. Además, el lima como texto sobre papel claro daba **1.13:1**.
- **Editorial cobalto**: papel crema con serif. Rasgo 1 de la skill.

## 14. Pendientes

- Captura o mockup de SIPIIT para D6. Sin esto, D6 usa un mockup CSS marcado como `PENDIENTE`.
