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


// ================================================================
// Motion: scroll reveal + header solidify. Progressive: without JS
// nothing is ever hidden; classes are only added when JS runs.
// ================================================================
(function(){
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // Elements that rise in as they enter the viewport
  var targets = document.querySelectorAll(
    'section .wrap > *, .assurance-line .wrap, .case, .post-lg, .svc-block, .cta-band .wrap'
  );
  targets.forEach(function(el, i){ el.classList.add('will-reveal'); });

  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

  targets.forEach(function(el){ io.observe(el); });

  // Stagger children of grids slightly
  document.querySelectorAll('.work-grid, .svc-panels, .quotes, .post-grid, .directors-strip').forEach(function(grid){
    Array.prototype.forEach.call(grid.children, function(child, i){
      child.classList.add('will-reveal');
      child.style.transitionDelay = (i * 90) + 'ms';
      io.observe(child);
    });
  });
})();

// Header: transparent over the hero, solid after scrolling past it
(function(){
  if (!document.body.classList.contains('overlay-hero')) return;
  var header = document.querySelector('header');
  if (!header) return;
  function onScroll(){
    if (window.scrollY > 60) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();


// ================================================================
// SIGNATURE: draw the Magnetic Blue rule under section labels
// as they scroll into view (left-to-right). Reduced-motion users
// get them pre-drawn via CSS.
// ================================================================
(function(){
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var labels = document.querySelectorAll('.sec-label');
  if (!labels.length || !('IntersectionObserver' in window)) {
    labels.forEach(function(l){ l.classList.add('drawn'); });
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting){
        e.target.classList.add('drawn');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.2 });
  labels.forEach(function(l){ io.observe(l); });
})();


// ================================================================
// News/blog category filter (Foster+Partners style pill bar)
// ================================================================
(function(){
  var pills = document.querySelectorAll('.filter-pill');
  var rows  = document.querySelectorAll('.news-row');
  var count = document.getElementById('artCount');
  var empty = document.querySelector('.news-empty');
  if (!pills.length || !rows.length) return;

  pills.forEach(function(pill){
    pill.addEventListener('click', function(){
      var f = pill.getAttribute('data-filter');
      pills.forEach(function(p){ p.classList.remove('active'); });
      pill.classList.add('active');
      var shown = 0;
      rows.forEach(function(row){
        var match = (f === 'All') || (row.getAttribute('data-cat') === f);
        row.hidden = !match;
        if (match) shown++;
      });
      if (count) count.textContent = shown;
      if (empty) empty.hidden = shown !== 0;
    });
  });
})();


// ================================================================
// Mobile navigation panel (the Menu button was previously inert)
// ================================================================
(function(){
  var btn   = document.querySelector('.menu-btn');
  var panel = document.getElementById('mobileNav');
  if (!btn || !panel) return;

  function open(){
    panel.hidden = false;
    // next frame so the transition runs
    requestAnimationFrame(function(){ panel.classList.add('open'); });
    btn.setAttribute('aria-expanded','true');
    btn.setAttribute('aria-label','Close menu');
    document.body.classList.add('nav-open');
  }
  function close(){
    panel.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    btn.setAttribute('aria-label','Open menu');
    document.body.classList.remove('nav-open');
    setTimeout(function(){
      if (!panel.classList.contains('open')) panel.hidden = true;
    }, 300);
  }

  btn.addEventListener('click', function(){
    if (btn.getAttribute('aria-expanded') === 'true') close(); else open();
  });

  // close on link tap
  panel.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', close);
  });

  // close on Escape
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') close();
  });

  // close if resized up to desktop
  window.addEventListener('resize', function(){
    if (window.innerWidth > 900 && btn.getAttribute('aria-expanded') === 'true') close();
  });
})();


// ================================================================
// Hero video: pause for reduced-motion users (the poster still
// remains visible), and fall back to the poster if the file is
// missing or cannot play.
// ================================================================
(function(){
  var v = document.querySelector('video.hero-bg');
  if (!v) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    v.removeAttribute('autoplay');
    v.pause();
    return;
  }

  // If the source is missing or unplayable the poster stays put.
  v.addEventListener('error', function(){ v.pause(); }, true);

  // Some browsers block autoplay until interaction; retry quietly.
  var attempt = v.play();
  if (attempt && typeof attempt.catch === 'function'){
    attempt.catch(function(){ /* poster remains visible */ });
  }
})();


// ================================================================
// Project-journey tool: accessible tabbed stage explorer
// ================================================================
(function(){
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.jn-tab'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.jn-panel'));
  if (!tabs.length) return;

  function select(tab){
    var key = tab.getAttribute('data-stage');
    tabs.forEach(function(t){
      var on = t === tab;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
    });
    panels.forEach(function(p){
      var on = p.id === 'panel-' + key;
      p.classList.toggle('active', on);
      p.hidden = !on;
    });
  }

  tabs.forEach(function(tab, i){
    tab.addEventListener('click', function(){ select(tab); });
    tab.addEventListener('keydown', function(e){
      var idx = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') idx = (i + 1) % tabs.length;
      if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   idx = (i - 1 + tabs.length) % tabs.length;
      if (e.key === 'Home') idx = 0;
      if (e.key === 'End')  idx = tabs.length - 1;
      if (idx !== null){
        e.preventDefault();
        tabs[idx].focus();
        select(tabs[idx]);
      }
    });
  });
})();
