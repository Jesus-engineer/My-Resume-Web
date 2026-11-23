# E7-06 · Finder y visor de certificados

Implementación local de [#66](https://github.com/Jesus-engineer/My-Resume-Web/issues/66),
verificada el 2026-11-22 en `desarrollador` para español e inglés.

- El Finder comparte ancho y eje con el resto del contenido. La grilla tiene
  tres columnas desde 1024 px, dos en tablet y una en móvil. Las filas de
  escritorio y tablet tienen la misma altura.
- En móvil, el Finder muestra hasta tres certificados por página, con flechas
  y contador. `Todos` ocupa dos páginas de tres, `Datos e IA` se reparte en
  tres y uno, y `Programación` muestra sus dos resultados en una página.
  Los filtros usan 13 px y los controles tienen objetivos de al menos 44 × 44 px.
- El visor recorre todos los resultados del filtro activo con los botones
  `Anterior` y `Siguiente` o con `ArrowLeft` y `ArrowRight`. Se detiene en
  los extremos e indica la posición. `Tab` y `Shift+Tab` recorren sus
  controles. Cerrar, `Escape` y el clic fuera devuelven el foco al enlace
  original, incluso si se abrió desde otra página del Finder.
- En 360 × 800, la imagen mostrada pasa de 227 a 252 px de alto y el margen
  lateral del diálogo pasa de 16 a 8 px. La imagen completa sigue disponible
  desde su enlace.

| Pantalla | Ancho del Finder | Alto anterior y actual en ES | Alto anterior y actual en EN |
| --- | ---: | ---: | ---: |
| 1024 × 768 | 916.84 px | 818.53 → 818.75 px | 818.53 → 818.75 px |
| 1440 × 900 | 1280 px | 828 → 793 px | 828 → 793 px |
| 1920 × 1080 | 1280 px | 1008 → 886.58 px | 1008 → 886.58 px |
| 360 × 800 | 320 px | 1689.05 → 915.08 px | 1668.75 → 873.48 px |

La auditoría de Chromium cubrió ocho resoluciones por idioma con movimiento
reducido. Las 16 ejecuciones completaron las pruebas de filtros y visor con
cero desbordes horizontales y cero errores de consola o red. También se
comprobó la apertura directa del HTML, la navegación sin JavaScript, la
impresión de los seis certificados y la recuperación tras un error de imagen.
En el tema oscuro vigente, las muestras de texto del Finder alcanzaron un
mínimo de 8.14:1 y los separadores de 3.13:1.

## Reproducción

```bash
python scripts/audit_ui.py --lang es --output artifacts/ui/e7-06-es
python scripts/audit_ui.py --lang en --output artifacts/ui/e7-06-en
pnpm run validate:html
node --check app.js
```

Las capturas y métricas completas están en `artifacts/ui/e7-06-es/` y
`artifacts/ui/e7-06-en/`.
