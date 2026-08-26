/* ==========================================================================
   SPEKTRIC — site behaviour (no dependencies)
   ========================================================================== */
(function () {
  'use strict';
  document.documentElement.classList.add('js');

  var CFG = window.SPEKTRIC_CONFIG || {};
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header: border on scroll ---------- */
  var header = $('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = $('.nav-toggle');
  var panel = $('.nav-panel');
  if (toggle && panel) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      panel.classList.toggle('is-open', open);
      panel.setAttribute('aria-hidden', String(!open));
      document.body.classList.toggle('nav-open', open);
      toggle.querySelector('.label').textContent = open ? 'Close' : 'Menu';
      if (open) { var first = panel.querySelector('a'); if (first) first.focus(); }
    };
    setOpen(false);
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('is-open')) { setOpen(false); toggle.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 900 && panel.classList.contains('is-open')) setOpen(false); });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealables = $$('.reveal, .reveal-stagger, .pathway');
  if (revealables.length) {
    if (reducedMotion || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- Lightweight analytics hook ---------- */
  window.spektricTrack = function (name, data) {
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, data || {});
      if (typeof window.plausible === 'function') window.plausible(name, { props: data || {} });
    } catch (e) { /* analytics is optional */ }
  };
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (el) window.spektricTrack(el.getAttribute('data-track'));
  });

  /* ---------- Resources filter ---------- */
  var filters = $$('.filter[data-filter]');
  if (filters.length) {
    var cards = $$('.article-card[data-cats]');
    filters.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.getAttribute('data-filter');
        filters.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        var shown = 0;
        cards.forEach(function (c) {
          var show = f === 'all' || (' ' + c.getAttribute('data-cats') + ' ').indexOf(' ' + f + ' ') !== -1;
          c.hidden = !show; if (show) shown++;
        });
        var empty = $('[data-filter-empty]'); if (empty) empty.hidden = shown > 0;
        var live = $('[data-filter-live]'); if (live) live.textContent = shown + (shown === 1 ? ' resource shown' : ' resources shown');
      });
    });
  }

  /* ---------- Contact path tabs ---------- */
  var tabs = $$('.path-tab');
  if (tabs.length) {
    var syncTabs = function () {
      var h = location.hash || '#schedule';
      tabs.forEach(function (t) { t.setAttribute('aria-selected', String(t.getAttribute('href') === h)); });
    };
    syncTabs();
    window.addEventListener('hashchange', syncTabs);
    tabs.forEach(function (t) { t.addEventListener('click', function () { setTimeout(syncTabs, 0); }); });
  }

  /* ---------- Submission helper (endpoint / Netlify / email fallback) ---------- */
  function toLines(data) {
    return Object.keys(data).filter(function (k) { return data[k] !== '' && data[k] != null; })
      .map(function (k) { return k + ': ' + data[k]; }).join('\n');
  }
  function submitPayload(formName, data) {
    var provider = CFG.formProvider || 'auto';
    var endpoint = (CFG.formEndpoint || '').trim();
    var useEndpoint = provider === 'endpoint' || (provider === 'auto' && endpoint);
    var useNetlify = provider === 'netlify' || (provider === 'auto' && /\.netlify\.app$/.test(location.hostname));

    if (useEndpoint) {
      return fetch(endpoint, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.assign({ form: formName }, data))
      }).then(function (r) { if (!r.ok) throw new Error('Request failed (' + r.status + ')'); return { mode: 'sent' }; });
    }
    if (useNetlify) {
      var body = new URLSearchParams(Object.assign({ 'form-name': formName }, data)).toString();
      return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: body })
        .then(function (r) { if (!r.ok) throw new Error('Request failed (' + r.status + ')'); return { mode: 'sent' }; });
    }
    // Email fallback: open the visitor's mail app with the request pre-written.
    var subject = (formName === 'consultation-request' ? 'Consultation request' : 'Information request') + ' — spektric.com';
    var href = 'mailto:' + (CFG.contactEmail || 'info@spektric.com') + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(toLines(data) + '\n\n(Sent from the spektric.com website)');
    window.location.href = href;
    return Promise.resolve({ mode: 'email' });
  }

  function successPanel(mode, title, body) {
    var email = CFG.contactEmail || 'info@spektric.com';
    var msg = mode === 'email'
      ? 'Your email app should have opened with your request pre-written — just press send. If it didn\u2019t open, email us directly at <a href="mailto:' + email + '">' + email + '</a>.'
      : body;
    return '<div class="form-success" role="status" tabindex="-1"><div class="tick" aria-hidden="true">&#10003;</div><h3>' + title + '</h3><p>' + msg + '</p><p class="small">Please don\u2019t send medical details by email. We\u2019ll gather anything clinical through secure channels once we connect.</p></div>';
  }

  function setError(field, msg) {
    var input = field.querySelector('input, select, textarea');
    var err = field.querySelector('.error');
    if (input) input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (err) err.textContent = msg || '';
  }
  function validEmail(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }

  /* ---------- Request-information form ---------- */
  var reqForm = $('#request-form');
  if (reqForm) {
    reqForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      var fields = $$('.field[data-required]', reqForm);
      fields.forEach(function (f) {
        var input = f.querySelector('input, select, textarea');
        var v = input ? (input.type === 'checkbox' ? input.checked : input.value.trim()) : '';
        if (!v) { setError(f, f.getAttribute('data-required')); ok = false; }
        else if (input.type === 'email' && !validEmail(v)) { setError(f, 'Enter an email address like name@example.com.'); ok = false; }
        else setError(f, '');
      });
      var hp = reqForm.querySelector('input[name="company"]');
      if (hp && hp.value) return; // honeypot filled — silently ignore bots
      if (!ok) { var firstBad = reqForm.querySelector('[aria-invalid="true"]'); if (firstBad) firstBad.focus(); return; }

      var fd = new FormData(reqForm);
      var data = {};
      fd.forEach(function (v, k) { if (k !== 'company') data[k] = (typeof v === 'string' ? v : ''); });
      data['Submitted from'] = location.href;

      var btn = reqForm.querySelector('button[type="submit"]');
      var status = $('[data-form-status]', reqForm);
      btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending\u2026';
      if (status) status.textContent = '';
      window.spektricTrack('form_submit', { form: 'request' });

      submitPayload('information-request', data).then(function (res) {
        var wrap = reqForm.parentNode;
        wrap.innerHTML = successPanel(res.mode, res.mode === 'email' ? 'One more step' : 'Request received', 'Thank you. A member of our team will follow up using the contact method you chose.');
        wrap.querySelector('.form-success').focus();
      }).catch(function () {
        btn.disabled = false; btn.textContent = btn.dataset.label;
        if (status) status.innerHTML = 'The request didn\u2019t go through. Please try again, or email us at <a href="mailto:' + (CFG.contactEmail || 'info@spektric.com') + '">' + (CFG.contactEmail || 'info@spektric.com') + '</a>.';
      });
    });
  }

  /* ---------- Built-in consultation scheduler ---------- */
  var sched = $('#scheduler');
  if (sched) initScheduler(sched);

  function initScheduler(root) {
    if (CFG.calendlyUrl) {
      root.innerHTML = '<div class="sched-embed"><iframe title="Schedule a consultation" src="' + CFG.calendlyUrl + '" loading="lazy"></iframe></div>';
      return;
    }
    var S = Object.assign({ daysAhead: 28, minLeadDays: 1, weekdays: [1, 2, 3, 4, 5], startTime: '09:00', endTime: '17:00', stepMinutes: 30, timeZoneLabel: '', blockedDates: [] }, CFG.scheduler || {});
    var types = CFG.consultationTypes || [{ id: 'intro', label: 'Introductory call', note: '' }];

    var typesWrap = $('[data-sched-types]', root);
    var calTitle = $('[data-cal-title]', root);
    var calGrid = $('[data-cal-grid]', root);
    var prevBtn = $('[data-cal-prev]', root);
    var nextBtn = $('[data-cal-next]', root);
    var slotsWrap = $('[data-slots]', root);
    var details = $('[data-sched-details]', root);
    var summary = $('[data-sched-summary]', root);
    var form = $('#consult-form', root);
    var live = $('[data-sched-live]', root);
    var stepsEl = $$('.sched-steps li', root);

    var today = new Date(); today.setHours(0, 0, 0, 0);
    var minDate = addDays(today, S.minLeadDays);
    var maxDate = addDays(today, S.daysAhead);
    var state = { type: types[0].id, date: null, time: null, y: minDate.getFullYear(), m: minDate.getMonth() };

    var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    function addDays(d, n) { var r = new Date(d); r.setDate(r.getDate() + n); return r; }
    function key(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function longDate(d) { return DAYS[d.getDay()] + ', ' + MONTHS[d.getMonth()] + ' ' + d.getDate(); }
    function shortDate(d) { return DAYS[d.getDay()].slice(0, 3) + ', ' + MONTHS[d.getMonth()].slice(0, 3) + ' ' + d.getDate(); }
    function available(d) {
      return d >= minDate && d <= maxDate && S.weekdays.indexOf(d.getDay()) !== -1 && (S.blockedDates || []).indexOf(key(d)) === -1;
    }
    function fmtTime(h, m) { var ap = h >= 12 ? 'PM' : 'AM'; var hh = h % 12; if (hh === 0) hh = 12; return hh + ':' + pad(m) + ' ' + ap; }
    function slots() {
      var out = [];
      var s = S.startTime.split(':').map(Number), e = S.endTime.split(':').map(Number);
      var cur = s[0] * 60 + s[1], end = e[0] * 60 + e[1];
      while (cur < end) { out.push(fmtTime(Math.floor(cur / 60), cur % 60)); cur += S.stepMinutes; }
      return out;
    }
    function setStep(n) {
      stepsEl.forEach(function (li, i) {
        li.classList.toggle('is-active', i === n);
        li.classList.toggle('is-done', i < n);
        li.setAttribute('aria-current', i === n ? 'step' : 'false');
      });
    }
    function announce(msg) { if (live) live.textContent = msg; }

    /* Types */
    if (typesWrap) {
      typesWrap.innerHTML = types.map(function (t, i) {
        return '<label class="choice"><input type="radio" name="consultation_type" value="' + t.label + '" data-id="' + t.id + '"' + (i === 0 ? ' checked' : '') + '><span>' + t.label + '</span></label>';
      }).join('');
      typesWrap.addEventListener('change', function (e) {
        if (e.target.name === 'consultation_type') {
          state.type = e.target.getAttribute('data-id');
          var t = types.filter(function (x) { return x.id === state.type; })[0];
          var note = $('[data-type-note]', root); if (note) note.textContent = t && t.note ? t.note : '';
        }
      });
      var note0 = $('[data-type-note]', root); if (note0) note0.textContent = types[0].note || '';
    }

    /* Calendar */
    function renderCal() {
      calTitle.textContent = MONTHS[state.m] + ' ' + state.y;
      var first = new Date(state.y, state.m, 1);
      var daysInMonth = new Date(state.y, state.m + 1, 0).getDate();
      var html = DAYS.map(function (d) { return '<div class="cal-dow" aria-hidden="true">' + d.slice(0, 2) + '</div>'; }).join('');
      for (var b = 0; b < first.getDay(); b++) html += '<div></div>';
      for (var d = 1; d <= daysInMonth; d++) {
        var date = new Date(state.y, state.m, d);
        var k = key(date), avail = available(date);
        html += '<button type="button" class="cal-day' + (avail ? ' is-avail' : '') + (k === key(today) ? ' is-today' : '') + '" data-date="' + k + '"' +
          (avail ? '' : ' disabled') + ' aria-pressed="' + String(state.date === k) + '" aria-label="' + longDate(date) + (avail ? '' : ' (unavailable)') + '">' + d + '</button>';
      }
      calGrid.innerHTML = html;
      prevBtn.disabled = (state.y < minDate.getFullYear()) || (state.y === minDate.getFullYear() && state.m <= minDate.getMonth());
      nextBtn.disabled = (state.y > maxDate.getFullYear()) || (state.y === maxDate.getFullYear() && state.m >= maxDate.getMonth());
    }
    function moveMonth(n) {
      var d = new Date(state.y, state.m + n, 1); state.y = d.getFullYear(); state.m = d.getMonth(); renderCal();
      announce('Showing ' + MONTHS[state.m] + ' ' + state.y);
    }
    prevBtn.addEventListener('click', function () { moveMonth(-1); });
    nextBtn.addEventListener('click', function () { moveMonth(1); });
    calGrid.addEventListener('click', function (e) {
      var btn = e.target.closest('.cal-day'); if (!btn || btn.disabled) return;
      state.date = btn.getAttribute('data-date'); state.time = null;
      renderCal(); renderSlots(); setStep(2);
      details.hidden = true;
      announce('Selected ' + longDate(parse(state.date)) + '. Choose a time.');
      var firstSlot = slotsWrap.querySelector('.slot'); if (firstSlot) firstSlot.focus();
    });
    function parse(k) { var p = k.split('-').map(Number); return new Date(p[0], p[1] - 1, p[2]); }

    /* Slots */
    function renderSlots() {
      if (!state.date) {
        slotsWrap.innerHTML = '<div class="sched-empty">Pick a day on the calendar to see available times.</div>';
        return;
      }
      var d = parse(state.date);
      slotsWrap.innerHTML = '<div class="slots"><h4>Times on ' + shortDate(d) + (S.timeZoneLabel ? ' <span class="muted">(' + S.timeZoneLabel + ')</span>' : '') + '</h4><div class="slot-grid" role="group" aria-label="Available times">' +
        slots().map(function (t) { return '<button type="button" class="slot" data-time="' + t + '" aria-pressed="' + String(state.time === t) + '">' + t + '</button>'; }).join('') + '</div></div>';
    }
    slotsWrap.addEventListener('click', function (e) {
      var btn = e.target.closest('.slot'); if (!btn) return;
      state.time = btn.getAttribute('data-time');
      $$('.slot', slotsWrap).forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      var d = parse(state.date);
      summary.innerHTML = '<span class="when">' + longDate(d) + ' &middot; ' + state.time + (S.timeZoneLabel ? ' ' + S.timeZoneLabel : '') + '</span><button type="button" data-sched-change>Change</button>';
      details.hidden = false; setStep(3);
      announce('Time selected: ' + longDate(d) + ' at ' + state.time + '. Add your details to send the request.');
      var firstInput = details.querySelector('input[type="text"]'); if (firstInput) firstInput.focus();
    });
    root.addEventListener('click', function (e) {
      if (e.target.matches('[data-sched-change]')) { details.hidden = true; state.time = null; renderSlots(); setStep(2); var s = slotsWrap.querySelector('.slot'); if (s) s.focus(); }
    });

    /* Details form */
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      $$('.field[data-required]', form).forEach(function (f) {
        var input = f.querySelector('input, select');
        var v = input.type === 'checkbox' ? input.checked : input.value.trim();
        if (!v) { setError(f, f.getAttribute('data-required')); ok = false; }
        else if (input.type === 'email' && !validEmail(v)) { setError(f, 'Enter an email address like name@example.com.'); ok = false; }
        else setError(f, '');
      });
      if (form.querySelector('input[name="company"]').value) return;
      if (!ok) { var bad = form.querySelector('[aria-invalid="true"]'); if (bad) bad.focus(); return; }

      var t = types.filter(function (x) { return x.id === state.type; })[0];
      var d = parse(state.date);
      var data = {
        'Consultation type': t ? t.label : state.type,
        'Requested date': longDate(d) + ', ' + d.getFullYear(),
        'Requested time': state.time + (S.timeZoneLabel ? ' ' + S.timeZoneLabel : '')
      };
      new FormData(form).forEach(function (v, k) { if (k !== 'company' && typeof v === 'string') data[k] = v; });
      data['Submitted from'] = location.href;

      var btn = form.querySelector('button[type="submit"]');
      var status = $('[data-form-status]', form);
      btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending\u2026';
      window.spektricTrack('form_submit', { form: 'consultation' });

      submitPayload('consultation-request', data).then(function (res) {
        root.innerHTML = successPanel(res.mode, res.mode === 'email' ? 'One more step' : 'Request received',
          'We\u2019ve received your request for <strong>' + longDate(d) + ' at ' + state.time + '</strong>. This time is held as a request, not a confirmed appointment — we\u2019ll confirm by email, or suggest an alternative if that window isn\u2019t available.');
        root.querySelector('.form-success').focus();
      }).catch(function () {
        btn.disabled = false; btn.textContent = btn.dataset.label;
        if (status) status.innerHTML = 'The request didn\u2019t go through. Please try again, or email us at <a href="mailto:' + (CFG.contactEmail || 'info@spektric.com') + '">' + (CFG.contactEmail || 'info@spektric.com') + '</a>.';
      });
    });

    renderCal(); renderSlots(); setStep(1); details.hidden = true;
  }

  /* ---------- Footer year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
