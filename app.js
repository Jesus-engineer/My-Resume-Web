// Interacciones del sitio: cabecera, menu movil, navegacion activa,
// filtros de certificaciones, revelado por scroll y visor accesible de
// certificados. Sin dependencias.

const raiz = document.documentElement;
const cabecera = document.querySelector('#cabecera');
const botonMenu = document.querySelector('.cabecera__menu');
const navegacion = document.querySelector('#navegacion');
const enlacesNav = [...document.querySelectorAll('.cabecera__enlace')];

/* ---------- Idioma de la pagina e interacciones compartidas ---------- */

const idiomaIngles = raiz.lang.toLowerCase().startsWith('en');
const textos = idiomaIngles
  ? { certificado: 'Certificate', certificacion: 'certification', certificaciones: 'certifications', de: 'of' }
  : { certificado: 'Certificado', certificacion: 'certificación', certificaciones: 'certificaciones', de: 'de' };

// Las anclas compartidas conservan la seccion al cambiar entre rutas ES / EN.
const enlacesIdioma = [...document.querySelectorAll('[data-idioma]')]
  .map(enlace => ({ enlace, ruta: enlace.getAttribute('href') }));

function actualizarEnlacesIdioma() {
  for (const { enlace, ruta } of enlacesIdioma) enlace.setAttribute('href', ruta + window.location.hash);
}

window.addEventListener('hashchange', actualizarEnlacesIdioma);
actualizarEnlacesIdioma();

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

  document.addEventListener('focusin', evento => {
    if (menuAbierto && cabecera && !cabecera.contains(evento.target)) cerrarMenu();
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

/* ---------- Cabecera y enlace activo durante el desplazamiento ---------- */

const seccionesNavegables = enlacesNav
  .map(enlace => ({
    enlace,
    seccion: document.querySelector(enlace.getAttribute('href')),
  }))
  .filter(({ seccion }) => seccion);

let frameDesplazamiento = null;
let geometriaNavegacion = null;
let altoVentana = 0;
let enlaceActual = enlacesNav.find(enlace => enlace.getAttribute('aria-current') === 'location');

function medirNavegacion(desplazamiento) {
  const limite = (cabecera?.getBoundingClientRect().height ?? 0) + 24;
  geometriaNavegacion = {
    inicios: seccionesNavegables.map(({ seccion }) => seccion.getBoundingClientRect().top + desplazamiento - limite),
    altoDocumento: raiz.scrollHeight,
  };
  altoVentana = window.innerHeight;
}

function actualizarDesplazamiento() {
  frameDesplazamiento = null;
  if (observadorGeometria && !geometriaNavegacion) return;

  const desplazamiento = window.scrollY;
  if (!observadorGeometria && seccionesNavegables.length) medirNavegacion(desplazamiento);

  cabecera?.classList.toggle('cabecera--compacta', desplazamiento > 8);
  if (!geometriaNavegacion) return;

  const { inicios, altoDocumento } = geometriaNavegacion;
  const alFinal = desplazamiento > 0 && desplazamiento + altoVentana >= altoDocumento - 2;
  let indice = 0;
  for (let i = 1; i < inicios.length; i++) {
    if (alFinal || desplazamiento >= inicios[i]) indice = i;
  }

  const actual = seccionesNavegables[indice].enlace;
  if (actual === enlaceActual) return;
  enlaceActual?.removeAttribute('aria-current');
  actual.setAttribute('aria-current', 'location');
  enlaceActual = actual;
}

function programarDesplazamiento() {
  if (frameDesplazamiento === null) frameDesplazamiento = requestAnimationFrame(actualizarDesplazamiento);
}

// ResizeObserver notifica después del layout. El scroll reutiliza estas medidas.
const observadorGeometria = window.ResizeObserver && seccionesNavegables.length
  ? new ResizeObserver(() => {
    medirNavegacion(window.scrollY);
    programarDesplazamiento();
  }) : null;

if (observadorGeometria) {
  for (const elemento of [cabecera, document.body, ...seccionesNavegables.map(({ seccion }) => seccion)]) {
    if (elemento) observadorGeometria.observe(elemento, { box: 'border-box' });
  }
} else {
  document.fonts?.ready.then(programarDesplazamiento);
  programarDesplazamiento();
}

window.addEventListener('scroll', programarDesplazamiento, { passive: true });
window.addEventListener('resize', () => {
  if (geometriaNavegacion) altoVentana = window.innerHeight;
  programarDesplazamiento();
});
window.addEventListener('hashchange', programarDesplazamiento);
window.addEventListener('pageshow', programarDesplazamiento);

/* ---------- Filtros y páginas de certificaciones ---------- */

const filtros = [...document.querySelectorAll('[data-filtro]')];
const certificaciones = [...document.querySelectorAll('.certificacion')];
const estadoFiltro = document.querySelector('#filtro-estado');
const paginacionCertificaciones = document.querySelector('.finder__paginacion');
const rangoCertificaciones = document.querySelector('.finder__rango');
const pasosCertificaciones = document.querySelectorAll('[data-finder-paso]');
const vistaCertificacionesMovil = window.matchMedia('(max-width: 767px)');
const certificadosPorPagina = 3;
let certificacionesFiltradas = certificaciones;
let paginaActual = 0;

function mostrarPaginaCertificaciones(pagina) {
  const total = certificacionesFiltradas.length;
  const paginas = vistaCertificacionesMovil.matches
    ? Math.max(1, Math.ceil(total / certificadosPorPagina)) : 1;
  if (pagina < 0 || pagina >= paginas) return;

  paginaActual = pagina;
  const paginar = paginas > 1;
  const inicio = pagina * certificadosPorPagina;
  const fin = paginar ? Math.min(inicio + certificadosPorPagina, total) : total;
  const visibles = certificacionesFiltradas.slice(inicio, fin);
  for (const tarjeta of certificaciones) tarjeta.hidden = !visibles.includes(tarjeta);

  if (!paginar && paginacionCertificaciones.contains(document.activeElement)) {
    filtros.find(boton => boton.getAttribute('aria-pressed') === 'true')?.focus({ preventScroll: true });
  }
  paginacionCertificaciones.hidden = !paginar;
  for (const boton of pasosCertificaciones) {
    const limite = boton.dataset.finderPaso === '-1' ? 0 : paginas - 1;
    boton.setAttribute('aria-disabled', String(pagina === limite));
  }
  const rango = inicio + 1 === fin ? String(fin) : `${inicio + 1}–${fin}`;
  const conteo = paginar ? `${rango} ${textos.de} ${total}` : total;
  rangoCertificaciones.textContent = paginar ? conteo : '';
  estadoFiltro.textContent = `${conteo} ${total === 1 ? textos.certificacion : textos.certificaciones}`;
  if (!observadorGeometria) programarDesplazamiento();
}

function mostrarPaginaDelCertificado(tarjeta) {
  const indice = certificacionesFiltradas.indexOf(tarjeta);
  const pagina = vistaCertificacionesMovil.matches
    ? Math.floor(Math.max(0, indice) / certificadosPorPagina) : 0;
  mostrarPaginaCertificaciones(pagina);
}

function aplicarFiltro(categoria) {
  for (const boton of filtros) {
    boton.setAttribute('aria-pressed', String(boton.dataset.filtro === categoria));
  }

  certificacionesFiltradas = certificaciones.filter(
    tarjeta => categoria === 'todos' || tarjeta.dataset.categoria === categoria
  );
  mostrarPaginaCertificaciones(0);
}

for (const boton of filtros) {
  boton.addEventListener('click', () => aplicarFiltro(boton.dataset.filtro));
}

for (const boton of pasosCertificaciones) {
  boton.addEventListener('click', () => mostrarPaginaCertificaciones(paginaActual + Number(boton.dataset.finderPaso)));
}

vistaCertificacionesMovil.addEventListener('change', () => {
  mostrarPaginaDelCertificado(document.activeElement?.closest('.certificacion'));
});
mostrarPaginaCertificaciones(0);

/* ---------- Movimiento al entrar en el área visible ---------- */

if ('IntersectionObserver' in window) {
  const observadorFondos = new IntersectionObserver(entradas => {
    for (const { target, isIntersecting } of entradas) {
      target.classList.toggle('fondo--fuera', !isIntersecting);
    }
  }, { rootMargin: '128px 0px' });

  for (const fondo of document.querySelectorAll('.hero__fondo, .seccion__fondo')) {
    fondo.classList.add('fondo--fuera');
    observadorFondos.observe(fondo);
  }
}

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
  const anterior = visorCertificado.querySelector('[data-visor-paso="-1"]');
  const siguiente = visorCertificado.querySelector('[data-visor-paso="1"]');
  const posicion = visorCertificado.querySelector('.visor-certificado__posicion');
  const estado = visorCertificado.querySelector('.visor-certificado__estado');
  const enlaces = [...document.querySelectorAll('[data-certificado]')];
  let enlaceOrigen = null;
  let recorrido = [];
  let indiceActual = 0;

  function mostrarCertificado(indice) {
    const enlace = recorrido[indice];
    if (!enlace) return;

    indiceActual = indice;
    const encabezado = enlace.closest('.certificacion')?.querySelector('h3');
    const nombre = encabezado?.textContent.trim() || textos.certificado;
    const conteo = `${indice + 1} ${textos.de} ${recorrido.length}`;
    titulo.textContent = nombre;
    posicion.textContent = conteo;
    estado.textContent = `${nombre}, ${conteo}`;
    anterior.setAttribute('aria-disabled', String(indice === 0));
    siguiente.setAttribute('aria-disabled', String(indice === recorrido.length - 1));
    original.href = enlace.href;
    imagen.alt = nombre;
    imagen.hidden = true;
    error.hidden = true;
    imagen.src = enlace.href;
  }

  for (const enlace of enlaces) {
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
      enlaceOrigen = enlace;
      recorrido = enlaces.filter(item => certificacionesFiltradas.includes(item.closest('.certificacion')));
      mostrarCertificado(recorrido.indexOf(enlace));
      visorCertificado.showModal();
      raiz.classList.add('visor-abierto');
    });
  }

  function actualizarImagen() {
    if (!visorCertificado.open || !imagen.hasAttribute('src') || !imagen.complete) return;
    const cargada = imagen.naturalWidth > 0;
    imagen.hidden = !cargada;
    error.hidden = cargada;
  }

  imagen.addEventListener('load', actualizarImagen);
  imagen.addEventListener('error', actualizarImagen);
  cerrar.addEventListener('click', () => visorCertificado.close());

  for (const boton of [anterior, siguiente]) {
    boton.addEventListener('click', () => mostrarCertificado(indiceActual + Number(boton.dataset.visorPaso)));
  }

  visorCertificado.addEventListener('keydown', evento => {
    if (evento.defaultPrevented || evento.ctrlKey || evento.metaKey || evento.altKey) return;
    if (evento.key === 'ArrowLeft' || evento.key === 'ArrowRight') {
      evento.preventDefault();
      mostrarCertificado(indiceActual + (evento.key === 'ArrowLeft' ? -1 : 1));
    }
    if (evento.key !== 'Tab') return;
    if (evento.shiftKey && document.activeElement === cerrar) {
      evento.preventDefault();
      original.focus();
    } else if (!evento.shiftKey && document.activeElement === original) {
      evento.preventDefault();
      cerrar.focus();
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
    imagen.removeAttribute('src');
    imagen.hidden = true;
    if (enlaceOrigen && enlaceOrigen.isConnected) {
      const tarjeta = enlaceOrigen.closest('.certificacion');
      if (tarjeta?.hidden) mostrarPaginaDelCertificado(tarjeta);
      enlaceOrigen.focus({ preventScroll: true });
    }
    enlaceOrigen = null;
    recorrido = [];
  });
}
