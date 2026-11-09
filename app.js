// Tema claro/oscuro: sigue al sistema y permite forzarlo con persistencia.
const botonTema = document.querySelector('.tema-toggle');
const mediaOscuro = window.matchMedia('(prefers-color-scheme: dark)');

function temaEfectivo() {
  const guardado = document.documentElement.dataset.theme;
  if (guardado === 'dark' || guardado === 'light') return guardado;
  return mediaOscuro.matches ? 'dark' : 'light';
}

function actualizarBotonTema() {
  if (!botonTema) return;
  const oscuro = temaEfectivo() === 'dark';
  botonTema.setAttribute('aria-pressed', String(oscuro));
  botonTema.setAttribute('aria-label', oscuro ? 'Activar tema claro' : 'Activar tema oscuro');
  botonTema.textContent = oscuro ? 'Tema claro' : 'Tema oscuro';
}

if (botonTema) {
  botonTema.addEventListener('click', () => {
    const siguiente = temaEfectivo() === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = siguiente;
    try {
      localStorage.setItem('tema', siguiente);
    } catch (error) {}
    actualizarBotonTema();
  });
}

mediaOscuro.addEventListener('change', () => {
  if (!document.documentElement.dataset.theme) actualizarBotonTema();
});

const botonImprimir = document.querySelector('.boton-imprimir');
if (botonImprimir) {
  botonImprimir.addEventListener('click', () => window.print());
}

actualizarBotonTema();
