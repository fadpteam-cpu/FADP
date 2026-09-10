// Set this to a live Formspree id when you have one. Until then, forms
// open mail to design@fadp.co.uk — they must not post to a dummy URL.
const FORMSPREE_ENDPOINT = ""; // e.g. "https://formspree.io/f/xxxxxxxx"

function clip(v, n){
  return String(v == null ? "" : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "").slice(0, n);
}

function isHoneypotFilled(form){
  var hp = form.querySelector('[name="company"], [name="website_url"]');
  return hp && String(hp.value || "").trim() !== "";
}

function validAttachment(input){
  if (!input || !input.files || !input.files[0]) return true;
  var f = input.files[0];
  var okType = /^(image\/(jpeg|pjpeg|png|webp|gif)|application\/pdf)$/i.test(f.type);
  return okType && f.size <= 8 * 1024 * 1024;
}

function mailtoEnquiry(form, extra){
  var data = new FormData(form);
  if (extra) Object.keys(extra).forEach(function(k){ data.set(k, extra[k]); });
  var lines = [];
  data.forEach(function(val, key){
    if (key.charAt(0) === "_" || key === "company" || key === "website_url") return;
    if (typeof val === "string" && val.trim()) lines.push(key + ": " + clip(val, 2000));
  });
  var sub = encodeURIComponent("FADP enquiry");
  var body = encodeURIComponent(lines.join("\n").slice(0, 1800));
  window.location.href = "mailto:design@fadp.co.uk?subject=" + sub + "&body=" + body;
  return Promise.resolve();
}

function postEnquiry(form, extra){
  if (isHoneypotFilled(form)) return Promise.resolve();
  var file = form.querySelector('input[type="file"]');
  if (file && !validAttachment(file)) {
    return Promise.reject(new Error("file"));
  }
  var live = FORMSPREE_ENDPOINT && FORMSPREE_ENDPOINT.indexOf("YOUR_FORM_ID") === -1;
  if (!live) return mailtoEnquiry(form, extra);

  var data = new FormData(form);
  if (extra) Object.keys(extra).forEach(function(k){ data.set(k, clip(extra[k], 200)); });
  data.set("page", clip(window.location.pathname, 180));
  data.delete("company");
  data.delete("website_url");
  return fetch(FORMSPREE_ENDPOINT, {
    method: "POST",
    body: data,
    headers: { "Accept": "application/json" }
  }).then(function(res){
    if (!res.ok) throw new Error("submit failed");
    return res;
  });
}

function showFormOk(el, msg){
  if (!el) return;
  el.hidden = false;
  el.textContent = msg || "A director will reply within one working day.";
}

const enquiryForm = document.getElementById("enquiryForm");
if (enquiryForm) enquiryForm.addEventListener("submit", function(e){
  e.preventDefault();
  const status = document.getElementById("enquiryStatus");
  const btn = enquiryForm.querySelector('button[type="submit"]');
  if (btn) btn.disabled = true;
  postEnquiry(enquiryForm)
    .then(function(){
      if (isHoneypotFilled(enquiryForm)) {
        showFormOk(status);
        return;
      }
      enquiryForm.reset();
      showFormOk(status);
      enquiryForm.querySelectorAll("input,textarea,button").forEach(function(n){ if (n.type !== "hidden") n.disabled = true; });
    })
    .catch(function(err){
      if (btn) btn.disabled = false;
      if (status){
        status.hidden = false;
        status.textContent = err && err.message === "file"
          ? "Attach a JPG, PNG or PDF under 8 MB, or email the file to design@fadp.co.uk."
          : "The form could not send. Email design@fadp.co.uk with the address.";
      }
    });
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

  const urlProject = new URLSearchParams(window.location.search).get('project');
  if (urlProject) answers['Project'] = clip(urlProject, 80);

  document.querySelectorAll('[data-project]').forEach(el => {
    el.addEventListener('click', () => { answers['Project'] = clip(el.dataset.project, 80); });
  });

  function show(step){
    current = step;
    steps.forEach(s => s.classList.toggle('active', s.dataset.step == String(step)));
    if(typeof step === 'number'){
      qNum.textContent = step;
      qBar.style.width = (step / 5 * 100) + '%';
      panel.closest('.quote-wrap').scrollIntoView({behavior:'auto', block:'nearest'});
    }
  }

  steps.forEach(stepEl => {
    const key = stepEl.dataset.key;
    stepEl.querySelectorAll('.q-option').forEach(card => {
      card.addEventListener('click', () => {
        stepEl.querySelectorAll('.q-option').forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        answers[key] = clip(card.dataset.value, 80);
        let next = parseInt(stepEl.dataset.step, 10) + 1;
        if (next === 2 && answers['Project'] && key !== 'Project') next = 3;
        setTimeout(() => show(next), 220);
      });
    });
  });

  panel.querySelectorAll('.q-back').forEach(btn => {
    btn.addEventListener('click', () => {
      const step = parseInt(btn.closest('.q-step').dataset.step, 10);
      if(step > 1) show(step - 1);
    });
  });

  const quoteForm = document.getElementById('quoteForm');
  if (quoteForm) quoteForm.addEventListener('submit', function(e){
    e.preventDefault();
    const btn = quoteForm.querySelector('button[type="submit"]');
    if (btn) btn.disabled = true;
    postEnquiry(quoteForm, {
      "Property type": answers['Property type'] || "not answered",
      "Project": answers['Project'] || "not answered",
      "Timescale": answers['Timescale'] || "not answered",
      "Budget": answers['Budget'] || "not answered"
    }).then(function(){
      show('done');
    }).catch(function(){
      if (btn) btn.disabled = false;
      var fb = quoteForm.querySelector('.q-fallback');
      if (fb) fb.textContent = "The form could not send. Email design@fadp.co.uk with the address.";
    });
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

// ================================================================
// SCROLL REVEAL ANIMATIONS — DISABLED
// Removed per request: no fade/rise-in effects as elements enter view.
// All content is visible immediately for a stable, non-juttery scroll.
// ================================================================
(function(){
  // No-op. Left intentionally empty.
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
// Section-label underline — DISABLED animation.
// Rules are pre-drawn immediately, no scroll-triggered draw effect.
// ================================================================
(function(){
  var labels = document.querySelectorAll('.sec-label');
  labels.forEach(function(l){ l.classList.add('drawn'); });
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

// ---- Cookie notice ----
(function(){
  try{
    if(localStorage.getItem('fadp_cookies_ok')) return;
  }catch(e){}
  var bar = document.createElement('div');
  bar.className = 'cookie-notice';
  bar.setAttribute('role','region');
  bar.setAttribute('aria-label','Cookie notice');
  var p = document.createElement('p');
  p.appendChild(document.createTextNode('This site uses only essential cookies for the page to work and to load fonts. It does not track you. '));
  var a = document.createElement('a');
  var base = document.body.getAttribute('data-base') || '';
  if (!/^(\.\.\/)*$/.test(base)) base = '';
  a.href = base + 'privacy/';
  a.textContent = 'Read our privacy notice';
  p.appendChild(a);
  p.appendChild(document.createTextNode('.'));
  var btnOk = document.createElement('button');
  btnOk.type = 'button';
  btnOk.className = 'cookie-ok';
  btnOk.textContent = 'OK';
  bar.appendChild(p);
  bar.appendChild(btnOk);
  document.body.appendChild(bar);
  btnOk.addEventListener('click', function(){
    try{ localStorage.setItem('fadp_cookies_ok','1'); }catch(e){}
    bar.remove();
  });
})();

/* ---------------------------------------------------------------
   GA4 event tracking (FADP)
   Fires standard + custom events. No-ops safely until a real
   Measurement ID is live in the gtag config on each page.
---------------------------------------------------------------- */
(function () {
  function track(name, params) {
    if (typeof window.gtag === 'function') { window.gtag('event', name, params || {}); }
  }
  // Phone clicks
  document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
    a.addEventListener('click', function () {
      track('phone_click', { link_url: a.getAttribute('href') });
    });
  });
  // Email clicks
  document.querySelectorAll('a[href^="mailto:"]').forEach(function (a) {
    a.addEventListener('click', function () {
      track('email_click', { link_url: a.getAttribute('href') });
    });
  });
  // Enquiry form submit (contact page)
  var ef = document.getElementById('enquiry-form') || document.querySelector('form.enquiry, form[data-form="enquiry"]');
  if (ef) ef.addEventListener('submit', function () {
    track('generate_lead', { form: 'enquiry', value: 1, currency: 'GBP' });
  });
  // Quote wizard final submit
  var qf = document.getElementById('quote-form') || document.querySelector('form[data-form="quote"]');
  if (qf) qf.addEventListener('submit', function () {
    track('generate_lead', { form: 'quote_wizard', value: 1, currency: 'GBP' });
  });
  // Quote wizard step progression (any element with data-quote-step)
  document.querySelectorAll('[data-quote-next], .wizard-next').forEach(function (btn) {
    btn.addEventListener('click', function () { track('quote_step', {}); });
  });
})();
