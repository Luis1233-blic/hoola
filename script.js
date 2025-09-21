// JavaScript: controla la apertura de los pétalos
const petals = Array.from(document.querySelectorAll('.petal'));
let opened = false;

function setTransforms(open, immediate) {
  petals.forEach((g, i) => {
    const baseAngle = i * 45; // original rotation
    const offset = open ? ((i % 2 === 0 ? 1 : -1) * 40) : 0; // abrir hacia afuera
    const rotateTo = baseAngle + offset;

    g.style.transition = immediate
      ? 'transform 320ms ease-out'
      : `transform ${420 + i * 30}ms cubic-bezier(.2,.9,.2,1)`;

    g.setAttribute('transform', `rotate(${rotateTo})`);
  });

  const center = document.getElementById('center');
  center.style.transition = immediate
    ? 'transform 220ms'
    : 'transform 380ms cubic-bezier(.2,.9,.2,1)';
  center.style.transform = open ? 'scale(0.92)' : 'scale(1)';

  opened = open;
}

// Botón Toggle
document.getElementById('toggleBtn').addEventListener('click', () => {
  setTransforms(!opened, false);
  updateShareLink();
});

// Botón Bloom
document.getElementById('bloomBtn').addEventListener('click', () => {
  setTransforms(false, true);
  setTimeout(() => setTransforms(true, false), 120);
  updateShareLink();
});

// Actualizar link compartible
function updateShareLink() {
  const url = new URL(window.location.href);
  if (opened) url.searchParams.set('open', '1');
  else url.searchParams.delete('open');
  document.getElementById('shareLink').value = url.toString();
}

// Copiar link
document.getElementById('copyBtn').addEventListener('click', async () => {
  const txt = document.getElementById('shareLink').value;
  try {
    await navigator.clipboard.writeText(txt);
    alert('Link copiado!');
  } catch (e) {
    prompt('Copia este link:', txt);
  }
});

// Revisar si debe abrirse automáticamente
function checkUrlOpen() {
  const qp = new URLSearchParams(window.location.search);
  const openq = qp.get('open');
  if (openq === '1' || location.hash === '#open') {
    setTimeout(() => setTransforms(true, false), 120);
  } else {
    setTransforms(false, true);
  }
  updateShareLink();
}

checkUrlOpen();

// Accesibilidad: tecla espacio abre/cierra
window.addEventListener('keydown', e => {
  if (e.key === ' ' || e.key === 'Spacebar') {
    e.preventDefault();
    setTransforms(!opened, false);
    updateShareLink();
  }
});

window.addEventListener('resize', updateShareLink);
