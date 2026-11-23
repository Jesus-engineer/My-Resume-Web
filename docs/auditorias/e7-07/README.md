# E7-07 · Rendimiento en escritorio y móvil

Implementación verificada el 23 de noviembre de 2026 para las rutas ES y EN de
`desarrollador`. [Tarea #67](https://github.com/Jesus-engineer/My-Resume-Web/issues/67)

- `styles.css` agrupa los ajustes responsivos junto a los cortes de 1100, 1023,
  767 y 460 px. La eliminación de reglas duplicadas y redundantes reduce la
  hoja de 68 026 a 66 009 bytes. El HTML carga la hoja directamente y difiere
  la ejecución de `app.js`.
- La foto usa variantes WebP de 224 y 360 px que pesan 4326 y 7568 bytes. La
  portada de SIPIIT usa variantes de 448 y 800 px que pesan 11 668 y 25 650
  bytes. `srcset` conserva los originales de 480 y 1280 px para pantallas que
  necesitan más resolución. El nombre se pinta con el contenido inicial y la
  foto aparece cuando carga.
- Los fondos de Certificaciones y Contacto usan carga diferida. Sus WebP
  originales pesan 26 764 y 22 454 bytes y mantienen la resolución del encuadre
  `cover`. Contacto sale de la carga inicial en los dos perfiles. La distancia
  al viewport determina cuándo el navegador anticipa Certificaciones.
- Las olas del Finder comparten un `viewBox` de 1200 × 320 y reutilizan un
  tramo SVG por capa. Los fondos se animan cerca del viewport. El pulso de
  disponibilidad anima opacidad y escala, y los nodos del hero se dibujan
  sin un filtro animado. Lighthouse pasó de cuatro animaciones fuera del
  compositor a cero.
- `ResizeObserver` mide la cabecera, las secciones y el alto del documento
  después del layout. Un solo callback por cuadro actualiza el enlace activo
  y la cabecera compacta. En un recorrido de 60 pasos con las imágenes ya
  cargadas, las llamadas a `getBoundingClientRect()` para la cabecera y las
  secciones pasaron de 360 a cero.

## Lighthouse

Lighthouse 13.6.0 y Chrome 157.0.8103.79, con el perfil móvil predeterminado y
`--preset=desktop` para escritorio. La línea base local incluye los cambios
que ya estaban en la rama al iniciar la tarea. [Configuración de los perfiles de Lighthouse](https://github.com/GoogleChrome/lighthouse/blob/main/docs/emulation.md)

| Sitio | Perfil | Rendimiento inicial → final | TBT inicial → final | Transferencia inicial → final |
| --- | --- | ---: | ---: | ---: |
| ES local | Escritorio | 100 → 100 | 0 → 0 ms | 359 961 → 288 590 B |
| ES local | Móvil | 99 → 100 | 90 → 79 ms | 359 961 → 299 330 B |
| EN local | Escritorio | 100 → 100 | 0 → 2,8 ms | 358 706 → 287 347 B |
| EN local | Móvil | 99 → 99 | 98 → 91 ms | 358 706 → 298 087 B |

Accesibilidad, Buenas prácticas y SEO obtuvieron 100 en las cuatro corridas
finales. Lighthouse registró cero recálculos forzados y CLS de cero. En móvil,
el LCP simulado pasó de 1,50 a 1,35 s en ES y de 1,50 a 1,59 s en EN. El
elemento medido pasó del enlace de marca en la cabecera al nombre en el hero.
Las cifras de transferencia de la tabla corresponden a HTTP local sin compresión.

La versión actualmente desplegada obtuvo 100 en escritorio y 98 en móvil,
con 100 en las otras categorías. La verificación de esta revisión en GitHub
Pages queda pendiente de que se publique desde `main`. [Versión publicada](https://jesus-engineer.github.io/My-Resume-Web/)

## Verificación de la interfaz

La auditoría visual cubrió ocho resoluciones por idioma con movimiento
reducido. En ambas rutas se verificaron el menú, la paginación del Finder, los
filtros, la navegación con teclado dentro del visor y el retorno de foco.
También se comprobó la apertura directa de los dos HTML con JavaScript
habilitado y deshabilitado, las anclas después de cambiar el viewport y el
desplazamiento de las olas cuando entran en pantalla.

## Reproducción

```bash
python scripts/audit_ui.py --lang es --output artifacts/ui/e7-07/es
python scripts/audit_ui.py --lang en --output artifacts/ui/e7-07/en
pnpm run validate:html
node --check app.js
```

Para Lighthouse local, sirve el directorio raíz con `python -m http.server
8000 --bind 127.0.0.1` y ejecuta ambas corridas con Chrome estable. Las mismas
opciones aplican a `/en/` y a la URL publicada.

```bash
pnpm dlx lighthouse@13.6.0 http://127.0.0.1:8000/ --chrome-flags=--headless --preset=desktop
pnpm dlx lighthouse@13.6.0 http://127.0.0.1:8000/ --chrome-flags=--headless
```

Los informes de Lighthouse están en `artifacts/ui/e7-07/`. Los archivos
`base-*-estable.json` y `published-*-estable.json` registran la línea base y
la versión publicada. Los archivos `local-*-final.json` guardan las corridas
de los cambios locales. Las capturas de Chromium están en
`artifacts/ui/e7-07/es/` y `artifacts/ui/e7-07/en/`.
