// Placeholder submit: composes an email until a form backend is connected.
const enquiryForm = document.getElementById('enquiryForm');
if (enquiryForm) enquiryForm.addEventListener('submit', function(e){
  e.preventDefault();
  const f = new FormData(this);
  const body = encodeURIComponent(
    "Name: " + f.get('name') + "\n" +
    "Telephone: " + (f.get('telephone') || "not provided") + "\n" +
    "Email: " + f.get('email') + "\n" +
    "Project type: " + f.get('type') + "\n" +
    "Location: " + (f.get('location') || "not provided") + "\n\n" +
    (f.get('message') || "")
  );
  window.location.href = "mailto:design@fadp.co.uk?subject=" +
    encodeURIComponent("Consultation request: " + f.get('type')) + "&body=" + body;
});

// ---------------- Quote wizard ----------------
(function(){
  const panel = document.querySelector('.quote-panel');
  if(!panel) return;

  const steps = Array.from(panel.querySelectorAll('.q-step'));
  const qNum = document.getElementById('qNum');
  const qBar = document.getElementById('qBar');
  const answers = {};
  let current = 1;

  // Deep-link via URL: ?project=Extension pre-fills the project step
  const urlProject = new URLSearchParams(window.location.search).get('project');
  if (urlProject) answers['Project'] = urlProject;

  // Deep-link: service panels set the project type and skip step 2
  document.querySelectorAll('[data-project]').forEach(el => {
    el.addEventListener('click', () => { answers['Project'] = el.dataset.project; });
  });

  function show(step){
    current = step;
    steps.forEach(s => s.classList.toggle('active', s.dataset.step == String(step)));
    if(typeof step === 'number'){
      qNum.textContent = step;
      qBar.style.width = (step / 5 * 100) + '%';
      panel.closest('.quote-wrap').scrollIntoView({behavior:'smooth', block:'nearest'});
    }
  }

  // Card selection: record answer, advance after a beat
  steps.forEach(stepEl => {
    const key = stepEl.dataset.key;
    stepEl.querySelectorAll('.q-option').forEach(card => {
      card.addEventListener('click', () => {
        stepEl.querySelectorAll('.q-option').forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        answers[key] = card.dataset.value;
        let next = parseInt(stepEl.dataset.step, 10) + 1;
        // If the project was chosen via a service panel, skip the project step
        if (next === 2 && answers['Project'] && key !== 'Project') next = 3;
        setTimeout(() => show(next), 220);
      });
    });
  });

  // Back buttons
  panel.querySelectorAll('.q-back').forEach(btn => {
    btn.addEventListener('click', () => {
      const step = parseInt(btn.closest('.q-step').dataset.step, 10);
      if(step > 1) show(step - 1);
    });
  });

  // Final submit — composes an email until a form backend is connected
  const quoteForm = document.getElementById('quoteForm');
  if (quoteForm) quoteForm.addEventListener('submit', function(e){
    e.preventDefault();
    const f = new FormData(this);
    const body = encodeURIComponent(
      "FEE PROPOSAL REQUEST\n\n" +
      "Property type: " + (answers['Property type'] || "not answered") + "\n" +
      "Project: " + (answers['Project'] || "not answered") + "\n" +
      "Timescale: " + (answers['Timescale'] || "not answered") + "\n" +
      "Budget: " + (answers['Budget'] || "not answered") + "\n\n" +
      "Name: " + f.get('name') + "\n" +
      "Telephone: " + (f.get('telephone') || "not provided") + "\n" +
      "Email: " + f.get('email') + "\n" +
      "Postcode: " + (f.get('postcode') || "not provided")
    );
    window.location.href = "mailto:design@fadp.co.uk?subject=" +
      encodeURIComponent("Fee proposal request: " + (answers['Project'] || 'project')) + "&body=" + body;
    show('done');
  });
})();


// Mega menu: click toggles open/closed; clicking anywhere else, or
// pressing Escape, closes it. Hover behaviour is handled in CSS.
(function(){
  const hm = document.querySelector('.has-mega');
  if (!hm) return;
  const btn = hm.querySelector('.mega-btn');
  btn.addEventListener('click', function(e){
    e.stopPropagation();
    const nowOpen = hm.classList.toggle('open');
    if (!nowOpen) btn.blur();
  });
  document.addEventListener('click', function(e){
    if (!hm.contains(e.target)) hm.classList.remove('open');
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape'){ hm.classList.remove('open'); btn.blur(); }
  });
})();
