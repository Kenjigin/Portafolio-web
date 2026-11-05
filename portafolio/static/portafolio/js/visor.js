// Visor: al hacer clic en una foto se abre en grande; flechas del teclado para navegar, Esc para cerrar.
(function () {
  const visor = document.getElementById('visor');
  if (!visor) return;
  const img = visor.querySelector('img');
  const pie = visor.querySelector('figcaption');
  const fotos = Array.from(document.querySelectorAll('img[data-visor]'));
  let actual = 0;

  function mostrar(i) {
    actual = (i + fotos.length) % fotos.length;
    const f = fotos[actual];
    img.src = f.src;
    img.alt = f.alt;
    pie.textContent = f.alt + (f.dataset.descripcion ? ' — ' + f.dataset.descripcion : '');
    visor.hidden = false;
    document.body.style.overflow = 'hidden';
  }
  function cerrar() {
    visor.hidden = true;
    document.body.style.overflow = '';
  }

  fotos.forEach((f, i) => f.addEventListener('click', () => mostrar(i)));
  visor.querySelector('.visor__cerrar').addEventListener('click', cerrar);
  visor.querySelector('.visor__ant').addEventListener('click', () => mostrar(actual - 1));
  visor.querySelector('.visor__sig').addEventListener('click', () => mostrar(actual + 1));
  visor.addEventListener('click', (e) => { if (e.target === visor) cerrar(); });
  document.addEventListener('keydown', (e) => {
    if (visor.hidden) return;
    if (e.key === 'Escape') cerrar();
    if (e.key === 'ArrowLeft') mostrar(actual - 1);
    if (e.key === 'ArrowRight') mostrar(actual + 1);
  });
})();
