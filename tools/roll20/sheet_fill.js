// Paste into the Roll20 editor page console (Claude in Chrome: javascript_tool), GM only.
// Fills "D&D 5E & 5.5E" NPC sheets by writing the sheet's `store` attribute. Worked 2026-11-19.
// Prereqs: the target sheet's attribs must be loaded (open its sheet once, then close it), and the
// sheet must be CLOSED while you run this (an open edit form can overwrite the write).
// Workflow per new creature:
//   1. Fully build one NPC (e.g. __TEMPLATE below) through the sheet's NPC setup so it has integrants.
//   2. __clone(target, {...core numbers}) copies the template and swaps abilities/AC/HP/speed/CR/etc.
//   3. __f(target, {...traits, actions, attacks, languages, resist, darkvision}) adds the content.
//   4. __p(target, [[category, name, level]], {attackName: reachFt}) adds save/skill proficiencies + reach.
// Reopen the sheet and check it renders; a bad key silently does nothing.
// NEVER press Tab in the sheet's form: focus lands on an "add" button and typed spaces spam empty rows.
const __TEMPLATE = 'Gemified Thrall'; // any finished NPC whose Attack/Action/Features you want stripped

window.__clone = (target, sp) => {
  const get = n => Campaign.characters.models.find(c => c.get('name') === n);
  const T = get(__TEMPLATE), C = get(target);
  const S = JSON.parse(JSON.stringify(T.attribs.models.find(x => x.get('name') === 'store').get('current')));
  const I = S.integrants.integrants, vs = Object.values(I);
  const atk = new Set(vs.filter(i => i.type === 'Attack' && i._id !== 'unarmed-strike').map(i => i._id));
  vs.forEach(i => { if (['Features', 'Action', 'Language'].includes(i.type) || atk.has(i._id) || atk.has(i.parentID) || (i.type === 'Defense' && !i.parentID)) delete I[i._id]; });
  S.features.speciesTraitsDisplayOrder = '[]';
  const ab = { Strength: sp.ab[0], Dexterity: sp.ab[1], Constitution: sp.ab[2], Intelligence: sp.ab[3], Wisdom: sp.ab[4], Charisma: sp.ab[5] };
  const have = {};
  Object.values(I).filter(i => i.type === 'Ability Score' && i.source === 'Custom').forEach(i => { have[i.ability] = i; i.valueFormula.flatValue = ab[i.ability]; });
  Object.keys(ab).forEach(k => { if (!have[k]) { const o = JSON.parse(JSON.stringify(have.Strength)); o._id = crypto.randomUUID(); o.ability = k; o.valueFormula.flatValue = ab[k]; I[o._id] = o; } });
  const walk = Object.values(I).find(i => i.type === 'Speed' && i.source === 'Custom'); walk.valueFormula.flatValue = sp.speed;
  Object.entries(sp.extraSpeeds || {}).forEach(([k, v]) => { const o = JSON.parse(JSON.stringify(walk)); o._id = crypto.randomUUID(); o.speed = k; o.valueFormula.flatValue = v; I[o._id] = o; });
  Object.values(I).find(i => i.type === 'Armor Class' && i.source === 'Custom').valueFormula.flatValue = sp.ac;
  Object.values(I).find(i => i.type === 'Hit Points' && i.source === 'Custom').valueFormula.flatValue = sp.hp;
  Object.assign(S.npc, { acNotes: sp.acNotes, challengeRating: sp.cr, customXP: sp.xp, rollHP: sp.rollHP });
  Object.assign(S.about.characteristics, { size: sp.size, alignment: sp.align }); S.character.creatureType = sp.type;
  C.attribs.models.find(x => x.get('name') === 'store').save({ current: S });
  C.attribs.models.find(x => x.get('name') === 'appState').save({ current: 'npc' });
  return Object.keys(I).length;
};

window.__f = (charName, spec) => {
  const c = Campaign.characters.models.find(c => c.get('name') === charName);
  const m = c.attribs.models.find(x => x.get('name') === 'store');
  const s = JSON.parse(JSON.stringify(m.get('current'))), I = s.integrants.integrants;
  const rid = n => { const a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'; let o = ''; for (let i = 0; i < n; i++) o += a[Math.floor(Math.random() * a.length)]; return o; };
  const base = () => ({ _enabled: true, _id: crypto.randomUUID(), builderDisplayName: '', childIDs: '[]', createdTime: Date.now(), label: '', name: '', parentID: '', shortID: rid(9), source: '' });
  const add = o => { I[o._id] = o; return o; };
  if (spec.darkvision != null) Object.values(I).find(i => i.type === 'Sense' && i.name === 'Darkvision').valueFormula.flatValue = spec.darkvision;
  if (spec.languages) { Object.values(I).filter(i => i.type === 'Language').forEach(i => delete I[i._id]); spec.languages.forEach(n => add(Object.assign(base(), { name: n, type: 'Language' }))); }
  (spec.resist || []).forEach(d => add(Object.assign(base(), { damage: d, defense: 'Resistance', name: 'Resistance to ' + d, type: 'Defense' })));
  const ord = JSON.parse(s.features.speciesTraitsDisplayOrder || '[]');
  (spec.traits || []).forEach(([n, d]) => { const o = add(Object.assign(base(), { description: d, name: n, source: 'Species', type: 'Features' })); ord.push(o._id); });
  s.features.speciesTraitsDisplayOrder = JSON.stringify(ord);
  // actions: [name, description, actionType] with actionType 'Action' (default) | 'Bonus Action' | 'Reaction'
  (spec.actions || []).forEach(([n, d, t]) => add(Object.assign(base(), { actionType: t || 'Action', description: d, excludeFamilialResources: false, name: n, type: 'Action' })));
  // attacks: for a saving-throw action use {n, save:{ability:'Dexterity', dc:15}, dmg:[...]} (Attack Save, auto-rolls the save); else {n, k:'Melee'|'Ranged', hit (flat to-hit), r (range text), d (extra text), dmg:[{c dice count, die 'd8', b bonus, ty type}]}
  (spec.attacks || []).forEach(a => {
    const at = add(Object.assign(base(), { actionType: a.t || 'Action', attack: a.save ? { type: 'Attack Save' } : { bonusFlat: a.hit, type: a.k }, description: a.d || '', name: a.n, range: a.r || '', source: '', type: 'Attack' }, a.save ? { autoHit: false, save: { bonus: a.save.bonus || 0, saveAbility: a.save.ability, saveFlat: a.save.dc } } : {}));
    at.childIDs = JSON.stringify(a.dmg.map(g => add(Object.assign(base(), { _bonus: g.b, _diceCount: g.c, ability: 'none', critDiceSize: '', damageType: g.ty, diceSize: g.die, name: a.n + ' Damage', overrideCrit: false, parentID: at._id, type: 'Damage' }))._id));
  });
  m.save({ current: s });
  return Object.keys(I).length;
};

// profs: [['Saving Throw','Constitution'], ['Skill','Stealth','Expertise']]; reach: {'Long Reach': 20} (melee reach shown on the sheet)
window.__p = (charName, profs, reach) => {
  const c = Campaign.characters.models.find(c => c.get('name') === charName);
  const m = c.attribs.models.find(x => x.get('name') === 'store');
  const s = JSON.parse(JSON.stringify(m.get('current'))), I = s.integrants.integrants;
  const have = Object.values(I).filter(i => i.type === 'Proficiency');
  profs.forEach(([cat, name, lvl]) => {
    if (have.find(i => i.category === cat && i.proficiency === name)) return;
    const o = { _enabled: true, _id: crypto.randomUUID(), builderDisplayName: '', category: cat, childIDs: '[]', createdTime: Date.now(), increaseIfAlreadyAt: false, label: '', name: '', notes: '', parentID: '', proficiency: name, proficiencyLevel: lvl || 'Proficient', rollAbility: 'Query Attribute', shortID: Math.random().toString(36).slice(2, 11), source: 'Custom', type: 'Proficiency' };
    I[o._id] = o;
  });
  Object.entries(reach || {}).forEach(([n, r]) => { const a = Object.values(I).find(i => i.type === 'Attack' && i.name === n); if (a) { a._reach = true; a._reachText = String(r); a.range = String(r); } });
  m.save({ current: s });
};
