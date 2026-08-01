---
layout: default
title: Home
---

<section class="hero">
  <p class="kicker">Broadcasting live · 100,000 channels</p>
  <h1>The 23rd Cohort</h1>
  <p class="lede">
    Four worlds. One planet. A conquered Faerûn, a world drowning in aether,
    an Earth with no magic and thousands of warheads, and one the Administration
    has not yet named.
  </p>
  <p><a class="button" href="{{ '/world/session-zero-primer.html' | relative_url }}">Read the opening broadcast →</a></p>
</section>

<section>
  <h2>Start here</h2>
  <div class="tiles">
    <a class="tile" href="{{ '/world/' | relative_url }}">
      <h3>The World</h3>
      <p>The Session 0 primer, plus everyone and everywhere you've encountered.</p>
    </a>
    <a class="tile" href="{{ '/sessions/' | relative_url }}">
      <h3>Sessions</h3>
      <p>What happened, in the order it happened to you.</p>
    </a>
    <a class="tile" href="{{ '/items/' | relative_url }}">
      <h3>Items</h3>
      <p>What you've found, and what it turned out to do.</p>
    </a>
  </div>
</section>

<section>
  <h2>Latest session</h2>
  {%- assign sessions = site.pages | where_exp: "p", "p.type == 'session' and p.player_known == true" | sort: "session_number" | reverse -%}
  {%- assign latest = sessions | slice: 0, 1 -%}
  {% include entry-list.html pages=latest empty="No sessions have aired yet." %}
</section>

<p class="fineprint">
  Records appear here only after the Administration clears them. If something you
  remember isn't listed, it hasn't been cleared — not that it didn't happen.
</p>
