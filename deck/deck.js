/* Inicialización del deck Reveal.js con soporte para ?print-pdf y prefers-reduced-motion */

const movimientoReducido = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (typeof Reveal !== 'undefined') {
  Reveal.initialize({
    width: 1280,
    height: 720,
    margin: 0.04,
    minScale: 0.2,
    maxScale: 1.5,
    hash: true,
    controls: true,
    progress: true,
    slideNumber: 'c/t',
    center: false,
    transition: movimientoReducido ? 'none' : 'fade',
    transitionSpeed: 'default',
    backgroundTransition: movimientoReducido ? 'none' : 'fade',
    pdfSeparateFragments: false,
    pdfMaxPagesPerSlide: 1
  });
}
