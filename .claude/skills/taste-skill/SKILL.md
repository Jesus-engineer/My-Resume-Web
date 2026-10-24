# taste-skill / design-taste-frontend

> Adaptación del repositorio oficial: https://github.com/Leonxlnx/taste-skill (MIT)

## Propósito
Evitar que el agente genere frontends genéricos ("AI slop"). Para una hoja de vida personal, se busca un diseño limpio, profesional y con buena jerarquía visual.

## Reglas de diseño
1. **Tipografía:** usa una sola familia tipográfica o dos como máximo; si usas dos, que sean claramente distintas (una para títulos, otra para cuerpo).
2. **Espaciado:** aplica un sistema de espaciado consistente (múltiplos de 0.5rem o 1rem). No dejes espacios al azar.
3. **Color:** paleta reducida (fondo, texto, suave, acento). Máximo 1 color de acento para botones o destacados.
4. **Layout:** usa CSS Grid o Flexbox. Contenedor central con `max-width` razonable (~720px) y padding móvil.
5. **Jerarquía visual:** títulos más grandes y con color de acento; texto de cuerpo legible (mínimo 1rem); contraste suficiente.
6. **Sin efectos innecesarios:** no uses sombras pesadas, gradientes llamativos ni animaciones excesivas en un currículum.

## Checklist antes de finalizar
- [ ] La página se lee bien en móvil (ancho ≤ 640px).
- [ ] Hay suficiente contraste entre texto y fondo.
- [ ] Los enlaces de contacto son claros y funcionales.
- [ ] No hay dependencias de framework; solo HTML/CSS/JS puro.
