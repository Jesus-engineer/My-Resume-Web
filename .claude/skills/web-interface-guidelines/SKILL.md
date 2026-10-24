# web-interface-guidelines

> Basado en https://github.com/vercel-labs/web-interface-guidelines (MIT)

## Propósito
Revisar que la interfaz cumpla con accesibilidad, teclado, ARIA y buenas prácticas de UX antes de publicar.

## Reglas clave para este sitio
1. **Teclado funciona en todas partes:** todos los elementos interactivos son alcanzables y operables con teclado.
2. **Focus visible:** cada elemento enfocable muestra un anillo de foco claro (`:focus-visible`).
3. **Iconos sin texto:** si un botón solo tiene ícono, necesita `aria-label`.
4. **Labels:** las etiquetas de formularios son clicables y están asociadas a su control (`htmlFor` o envolviendo el control).
5. **Motion reducido:** respeta `prefers-reduced-motion`; no hay animaciones automáticas > 5 segundos sin controles de pausa.
6. **Idioma:** `<html lang="es">` declarado correctamente.
7. **Viewport:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

## Checklist de auditoría
- [ ] Se puede navegar solo con Tab y Enter.
- [ ] El foco de teclado es visible en todos los elementos interactivos.
- [ ] La página anuncia su idioma como español.
- [ ] No hay movimiento automático molesto.
