// Placeholder submit: composes an email until a form backend is connected.
document.getElementById('enquiryForm').addEventListener('submit', function(e){
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
  window.location.href = "mailto:studio@fadp.com?subject=" +
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
        const next = parseInt(stepEl.dataset.step, 10) + 1;
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
  document.getElementById('quoteForm').addEventListener('submit', function(e){
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
    window.location.href = "mailto:studio@fadp.com?subject=" +
      encodeURIComponent("Fee proposal request: " + (answers['Project'] || 'project')) + "&body=" + body;
    show('done');
  });
})();
