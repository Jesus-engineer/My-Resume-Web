// Interacciones del sitio: tema, cabecera, menu movil, navegacion activa,
// filtros de certificaciones, revelado por scroll y visor accesible de
// certificados. Sin dependencias.

const raiz = document.documentElement;
const cabecera = document.querySelector('#cabecera');
const botonMenu = document.querySelector('.cabecera__menu');
const navegacion = document.querySelector('#navegacion');
const enlacesNav = [...document.querySelectorAll('.cabecera__enlace')];

/* ---------- Tema oscuro canonico / claro alternativo ---------- */

const botonTema = document.querySelector('.tema-toggle');

function temaEfectivo() {
  return raiz.dataset.theme === 'light' ? 'light' : 'dark';
}

function actualizarBotonTema() {
  if (!botonTema) return;
  const oscuro = temaEfectivo() === 'dark';
  botonTema.setAttribute('aria-label', oscuro ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro');
  botonTema.textContent = oscuro ? 'Tema claro' : 'Tema oscuro';
}

if (botonTema) {
  botonTema.addEventListener('click', () => {
    const siguiente = temaEfectivo() === 'dark' ? 'light' : 'dark';
    raiz.dataset.theme = siguiente;
    try {
      localStorage.setItem('tema', siguiente);
    } catch (error) {}
    actualizarBotonTema();
  });
}

actualizarBotonTema();

/* ---------- Cabecera compacta al hacer scroll ---------- */

let frameCabecera = null;

function actualizarCabecera() {
  if (!cabecera) return;
  cabecera.classList.toggle('cabecera--compacta', window.scrollY > 8);
}

function programarCabecera() {
  if (frameCabecera !== null) return;
  frameCabecera = requestAnimationFrame(() => {
    frameCabecera = null;
    actualizarCabecera();
  });
}

window.addEventListener('scroll', programarCabecera, { passive: true });
window.addEventListener('load', actualizarCabecera);
actualizarCabecera();

/* ---------- Menu movil ---------- */

let menuAbierto = false;

function abrirMenu() {
  if (!cabecera || !botonMenu) return;
  menuAbierto = true;
  cabecera.classList.add('cabecera--abierta');
  botonMenu.setAttribute('aria-expanded', 'true');
  const primerEnlace = navegacion ? navegacion.querySelector('a, button') : null;
  if (primerEnlace) primerEnlace.focus();
}

function cerrarMenu(devolverFoco = false) {
  if (!cabecera || !botonMenu) return;
  menuAbierto = false;
  cabecera.classList.remove('cabecera--abierta');
  botonMenu.setAttribute('aria-expanded', 'false');
  if (devolverFoco) botonMenu.focus();
}

if (botonMenu) {
  botonMenu.addEventListener('click', () => {
    if (menuAbierto) cerrarMenu();
    else abrirMenu();
  });

  document.addEventListener('keydown', evento => {
    if (evento.key === 'Escape' && menuAbierto) {
      evento.stopPropagation();
      cerrarMenu(true);
    }
  });

  document.addEventListener('click', evento => {
    if (!menuAbierto || !cabecera) return;
    if (!cabecera.contains(evento.target)) cerrarMenu();
  });

  for (const enlace of enlacesNav) {
    enlace.addEventListener('click', () => {
      if (menuAbierto) cerrarMenu();
    });
  }

  const mediaEscritorio = window.matchMedia('(min-width: 1024px)');
  const alCambiarAncho = evento => {
    if (evento.matches && menuAbierto) cerrarMenu();
  };
  if (typeof mediaEscritorio.addEventListener === 'function') {
    mediaEscritorio.addEventListener('change', alCambiarAncho);
  } else {
    mediaEscritorio.addListener(alCambiarAncho);
  }
}

/* ---------- Enlace activo segun la seccion visible ---------- */

const seccionesNavegables = enlacesNav
  .map(enlace => ({
    enlace,
    seccion: document.querySelector(enlace.getAttribute('href')),
  }))
  .filter(({ seccion }) => seccion);

let frameNavegacion = null;

function actualizarSeccionActual() {
  if (!seccionesNavegables.length) return;

  const altoCabecera = cabecera ? cabecera.getBoundingClientRect().height : 0;
  const limite = altoCabecera + 24;
  let actual = seccionesNavegables[0].enlace;

  for (const item of seccionesNavegables) {
    if (item.seccion.getBoundingClientRect().top <= limite) actual = item.enlace;
  }

  const alFinal = window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2;
  if (alFinal && window.scrollY > 0) {
    actual = seccionesNavegables[seccionesNavegables.length - 1].enlace;
  }

  for (const { enlace } of seccionesNavegables) {
    if (enlace === actual) enlace.setAttribute('aria-current', 'location');
    else enlace.removeAttribute('aria-current');
  }
}

function programarSeccionActual() {
  if (frameNavegacion !== null) return;
  frameNavegacion = requestAnimationFrame(() => {
    frameNavegacion = null;
    actualizarSeccionActual();
  });
}

if (seccionesNavegables.length) {
  window.addEventListener('scroll', programarSeccionActual, { passive: true });
  window.addEventListener('resize', programarSeccionActual);
  window.addEventListener('hashchange', programarSeccionActual);
  window.addEventListener('load', programarSeccionActual);
  if (document.fonts) document.fonts.ready.then(programarSeccionActual);
  actualizarSeccionActual();
}

/* ---------- Filtros de certificaciones ---------- */

const filtros = [...document.querySelectorAll('[data-filtro]')];
const certificaciones = [...document.querySelectorAll('.certificacion')];
const grillaCertificaciones = document.querySelector('.certificaciones');
const estadoFiltro = document.querySelector('#filtro-estado');

function actualizarFilasCertificaciones() {
  if (!grillaCertificaciones) return;
  const visibles = certificaciones.filter(certificacion => !certificacion.hidden);
  const columnas = window.matchMedia('(max-width: 767px)').matches
    ? 1
    : window.matchMedia('(max-width: 1100px)').matches ? 2 : 3;

  for (const certificacion of certificaciones) {
    certificacion.classList.remove('certificacion--inicio-fila', 'certificacion--fila-siguiente');
  }
  for (const [indice, certificacion] of visibles.entries()) {
    if (indice % columnas === 0) certificacion.classList.add('certificacion--inicio-fila');
    if (indice >= columnas) certificacion.classList.add('certificacion--fila-siguiente');
  }
}

function aplicarFiltro(categoria) {
  for (const boton of filtros) {
    boton.setAttribute('aria-pressed', String(boton.dataset.filtro === categoria));
  }

  let visibles = 0;
  for (const certificacion of certificaciones) {
    const coincide = categoria === 'todos' || certificacion.dataset.categoria === categoria;
    certificacion.hidden = !coincide;
    if (coincide) visibles += 1;
  }

  if (grillaCertificaciones) {
    grillaCertificaciones.classList.toggle('certificaciones--filtradas', categoria !== 'todos');
    actualizarFilasCertificaciones();
  }

  if (estadoFiltro) {
    estadoFiltro.textContent = visibles === 1 ? '1 certificación' : `${visibles} certificaciones`;
  }
}

for (const boton of filtros) {
  boton.addEventListener('click', () => aplicarFiltro(boton.dataset.filtro));
}

if (grillaCertificaciones) window.addEventListener('resize', actualizarFilasCertificaciones);

/* ---------- Revelado por scroll ---------- */

const elementosRevelar = [...document.querySelectorAll('.revelar')];
const movimientoReducido = window.matchMedia('(prefers-reduced-motion: reduce)');

if (elementosRevelar.length) {
  if (movimientoReducido.matches || !('IntersectionObserver' in window)) {
    for (const elemento of elementosRevelar) elemento.classList.add('visible');
  } else {
    for (const elemento of elementosRevelar) elemento.classList.add('revelar--oculto');

    const observador = new IntersectionObserver(
      entradas => {
        for (const entrada of entradas) {
          if (!entrada.isIntersecting) continue;
          entrada.target.classList.add('visible');
          observador.unobserve(entrada.target);
        }
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }
    );

    for (const elemento of elementosRevelar) observador.observe(elemento);
  }

  movimientoReducido.addEventListener('change', evento => {
    if (!evento.matches) return;
    for (const elemento of elementosRevelar) {
      elemento.classList.add('visible');
      elemento.classList.remove('revelar--oculto');
    }
  });
}

/* ---------- Visor accesible de certificados ---------- */

const visorCertificado = document.querySelector('#visor-certificado');

if (visorCertificado && typeof visorCertificado.showModal === 'function') {
  const imagen = visorCertificado.querySelector('.visor-certificado__imagen');
  const titulo = visorCertificado.querySelector('#visor-certificado-titulo');
  const original = visorCertificado.querySelector('.visor-certificado__original');
  const error = visorCertificado.querySelector('.visor-certificado__error');
  const cerrar = visorCertificado.querySelector('.visor-certificado__cerrar');
  let enlaceOrigen = null;

  function enfocarPrimero() {
    if (cerrar) cerrar.focus();
  }

  for (const enlace of document.querySelectorAll('[data-certificado]')) {
    enlace.setAttribute('aria-haspopup', 'dialog');
    enlace.setAttribute('aria-controls', visorCertificado.id);
    enlace.addEventListener('click', evento => {
      if (
        evento.defaultPrevented ||
        evento.button !== 0 ||
        evento.ctrlKey ||
        evento.metaKey ||
        evento.shiftKey ||
        evento.altKey
      ) {
        return;
      }
      evento.preventDefault();
      const tarjeta = enlace.closest('.certificacion');
      const encabezado = tarjeta ? tarjeta.querySelector('h3') : null;
      const nombre = encabezado ? encabezado.textContent.trim() : 'Certificado';
      enlaceOrigen = enlace;
      if (titulo) titulo.textContent = nombre;
      if (original) original.href = enlace.href;
      if (imagen) {
        imagen.alt = nombre;
        imagen.hidden = false;
        imagen.removeAttribute('src');
        imagen.src = enlace.href;
      }
      if (error) error.hidden = true;
      visorCertificado.showModal();
      raiz.classList.add('visor-abierto');
      enfocarPrimero();
    });
  }

  if (imagen) {
    imagen.addEventListener('error', () => {
      if (!visorCertificado.open) return;
      imagen.hidden = true;
      if (error) error.hidden = false;
    });
  }

  if (cerrar) {
    cerrar.addEventListener('click', () => visorCertificado.close());
  }

  visorCertificado.addEventListener('keydown', evento => {
    if (evento.key !== 'Tab' || evento.ctrlKey || evento.metaKey || evento.altKey) return;
    const enfocables = [cerrar, original].filter(
      elemento => elemento && !elemento.hidden && elemento.offsetParent !== null
    );
    if (!enfocables.length) return;
    const primero = enfocables[0];
    const ultimo = enfocables[enfocables.length - 1];
    if (evento.shiftKey && document.activeElement === primero) {
      evento.preventDefault();
      ultimo.focus();
    } else if (!evento.shiftKey && document.activeElement === ultimo) {
      evento.preventDefault();
      primero.focus();
    }
  });

  visorCertificado.addEventListener('click', evento => {
    if (evento.target !== visorCertificado) return;
    const limites = visorCertificado.getBoundingClientRect();
    const fuera =
      evento.clientX < limites.left ||
      evento.clientX > limites.right ||
      evento.clientY < limites.top ||
      evento.clientY > limites.bottom;
    if (fuera) visorCertificado.close();
  });

  visorCertificado.addEventListener('close', () => {
    raiz.classList.remove('visor-abierto');
    if (imagen) {
      imagen.removeAttribute('src');
      imagen.hidden = true;
    }
    if (enlaceOrigen && enlaceOrigen.isConnected) enlaceOrigen.focus({ preventScroll: true });
    enlaceOrigen = null;
  });
}
