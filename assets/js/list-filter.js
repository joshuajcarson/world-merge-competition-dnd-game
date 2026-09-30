/* Search and filter for index pages built from _includes/type-group.html.
   Markup contract: a [data-filterable] container holding details.type-group
   sections of li.card elements (data-text, data-origin, data-stub), plus the
   #filter-bar form. Without this script the page is a plain list. */
(function () {
  var root = document.querySelector('[data-filterable]');
  var form = document.getElementById('filter-bar');
  if (!root || !form) return;
  form.hidden = false;

  var input = document.getElementById('filter-q');
  var stubBox = document.getElementById('filter-hide-stubs');
  var toggleAll = document.getElementById('filter-toggle-all');
  var clearBtn = document.getElementById('filter-clear');
  var status = document.getElementById('filter-status');
  var emptyMsg = document.getElementById('filter-empty');
  var groups = Array.prototype.slice.call(root.querySelectorAll('details.type-group'));
  var dm = document.documentElement.getAttribute('data-dm') === 'on';

  function playerVisible(card) { return dm || !card.classList.contains('dm-only'); }

  var model = groups.map(function (g) {
    var cards = Array.prototype.slice.call(g.querySelectorAll('li.card'));
    return { el: g, cards: cards, count: g.querySelector('.count'),
             wasOpen: g.open, type: g.getAttribute('data-type'), label: g.getAttribute('data-label') };
  });

  var state = { q: '', types: {}, origins: {}, hideStubs: false };

  // Long groups start collapsed; the counts in the headings say what is inside.
  model.forEach(function (m) {
    m.total = m.cards.filter(playerVisible).length;
    if (m.total > 12) { m.el.open = false; m.wasOpen = false; }
  });

  function label(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

  function buildChips(kind, items) {
    var row = form.querySelector('[data-chips="' + kind + '"]');
    items.forEach(function (it) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'chip';
      b.textContent = it.label;
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () {
        var map = kind === 'type' ? state.types : state.origins;
        if (map[it.key]) { delete map[it.key]; } else { map[it.key] = true; }
        b.setAttribute('aria-pressed', map[it.key] ? 'true' : 'false');
        apply();
      });
      row.appendChild(b);
    });
    if (!items.length) row.hidden = true;
  }

  buildChips('type', model.filter(function (m) { return m.total > 0; })
    .map(function (m) { return { key: m.type, label: m.label }; }));

  var origins = {};
  model.forEach(function (m) {
    m.cards.filter(playerVisible).forEach(function (c) {
      var o = c.getAttribute('data-origin');
      if (o && o !== 'unknown') origins[o] = true;
    });
  });
  buildChips('origin', Object.keys(origins).sort().map(function (o) { return { key: o, label: label(o) }; }));

  function any(map) { return Object.keys(map).length > 0; }

  function apply() {
    state.q = input.value.trim().toLowerCase();
    state.hideStubs = stubBox.checked;
    var words = state.q ? state.q.split(/\s+/) : [];
    var active = words.length > 0 || any(state.types) || any(state.origins) || state.hideStubs;
    var shownTotal = 0, allTotal = 0;

    model.forEach(function (m) {
      var typeOk = !any(state.types) || state.types[m.type];
      var shown = 0;
      m.cards.forEach(function (c) {
        var ok = typeOk && playerVisible(c);
        if (ok && any(state.origins)) ok = !!state.origins[c.getAttribute('data-origin')];
        if (ok && state.hideStubs) ok = !c.hasAttribute('data-stub');
        if (ok && words.length) {
          var hay = c.getAttribute('data-text') || '';
          ok = words.every(function (w) { return hay.indexOf(w) !== -1; });
        }
        c.classList.toggle('filtered-out', !ok);
        if (ok) shown++;
      });
      m.shown = shown;
      allTotal += m.total;
      shownTotal += shown;
      m.count.textContent = active ? shown + ' of ' + m.total : String(m.total);
      m.el.classList.toggle('filtered-out', active && shown === 0);
      if (active) { m.el.open = shown > 0; } else { m.el.open = m.wasOpen; }
    });

    clearBtn.hidden = !active;
    emptyMsg.hidden = !(active && shownTotal === 0);
    status.textContent = active ? shownTotal + ' of ' + allTotal + ' entries' : '';
  }

  // Remember how the viewer left each section while no filter is active.
  model.forEach(function (m) {
    m.el.addEventListener('toggle', function () {
      if (!clearBtn.hidden) return;
      m.wasOpen = m.el.open;
    });
  });

  input.addEventListener('input', apply);
  stubBox.addEventListener('change', apply);
  form.addEventListener('submit', function (e) { e.preventDefault(); });

  clearBtn.addEventListener('click', function () {
    input.value = '';
    stubBox.checked = false;
    state.types = {};
    state.origins = {};
    Array.prototype.forEach.call(form.querySelectorAll('.chip'), function (b) { b.setAttribute('aria-pressed', 'false'); });
    apply();
    input.focus();
  });

  toggleAll.addEventListener('click', function () {
    var collapse = toggleAll.textContent === 'Collapse all';
    model.forEach(function (m) {
      if (!m.el.classList.contains('filtered-out')) { m.el.open = !collapse; m.wasOpen = !collapse; }
    });
    toggleAll.textContent = collapse ? 'Expand all' : 'Collapse all';
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target && e.target.tagName;
    if (t === 'INPUT' || t === 'TEXTAREA' || t === 'SELECT') return;
    e.preventDefault();
    input.focus();
  });

  apply();
})();
