const controls = [...document.querySelectorAll('.track-controls input')];
const list = document.querySelector('#lab-list');
const status = document.querySelector('#selection-status');
let labs = [];

const escapeText = value => String(value ?? '').replace(/[&<>"']/g, character => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' })[character]);
const titleCase = value => String(value).replaceAll('-', ' ').replace(/\b\w/g, letter => letter.toUpperCase());

function activeLevels() {
  return new Set(controls.filter(control => control.checked).map(control => control.value));
}

function render() {
  const selected = activeLevels();
  const visible = labs.filter(lab => selected.has(lab.level));
  status.textContent = selected.size ? `${visible.length} project${visible.length === 1 ? '' : 's'} shown across ${selected.size} selected track${selected.size === 1 ? '' : 's'}.` : 'No track is selected. Turn on at least one track to see projects.';
  list.innerHTML = visible.map(lab => `
    <article class="lab">
      <header>
        <p class="eyebrow">${escapeText(lab.level).toUpperCase()}</p>
        <h3>${escapeText(lab.title)}</h3>
        <p class="status-${escapeText(lab.status)}"><strong>${titleCase(escapeText(lab.status))}</strong></p>
      </header>
      <div class="meta"><span>${escapeText(lab.minutes)} minutes</span><span>${escapeText(lab.language)}</span></div>
      <p><strong>You will make:</strong> ${escapeText(lab.result)}</p>
      <p><strong>For:</strong> ${escapeText(lab.audience)}</p>
      <p><strong>Used in:</strong> ${lab.applications.map(escapeText).join(', ')}</p>
      <details><summary>What should I know first?</summary><ul>${lab.prerequisites.map(item => `<li>${escapeText(item)}</li>`).join('')}</ul></details>
      ${lab.status === 'verified' ? `<p><a href="https://github.com/G-B-Industry-LLC/build-everything/tree/main/${escapeText(lab.path)}">Start this project</a></p>` : '<p>Guide planned. It will not be labeled Verified until the explanation and automatic proof both pass.</p>'}
    </article>`).join('');
}

for (const control of controls) control.addEventListener('change', render);

fetch('catalog.json')
  .then(response => {
    if (!response.ok) throw new Error('Catalog could not be loaded.');
    return response.json();
  })
  .then(data => { labs = data.labs || []; render(); })
  .catch(() => { status.textContent = 'The project catalog could not be loaded. Open the GitHub README for the complete list.'; });
