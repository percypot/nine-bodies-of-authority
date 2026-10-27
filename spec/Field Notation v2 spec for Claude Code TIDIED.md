# Field Notation v2: spec for Claude Code

Prepared 26 October 2026 for Percy. Tidied after the Claude Docs pass. This spec updates the Field Notation design system and rebuilds The Nine Bodies of Authority HTML on it. It adds two view modes, so the system has five.

## Handoff prompt

Read this spec top to bottom. Work in the order in section 9. Edit only the `project/` files of Field Notation, then rebuild the Nine Bodies HTML from the updated system. Do not change the authored words of the document. After each phase, run the checks in section 10 and report the numbers.

## 1. Inputs Claude Code needs from Percy

- A transcript source file of the whole conversation that led to the document, with speaker, time and whether each turn was voice or text. Suggested path: `source/transcript.json`.
- Default mode on open: Network, the first tab.
- Recorded is always public. It ships in every build, Paper and Night. No privacy flag.
- Whether Scripted audio is pre-rendered files or the browser's speech synthesis. Recommended: browser speech as the fallback, with pre-rendered files used when present.

## 2. Token changes in tokens.json

### Colour

| Token | Paper | Night | Why |
|---|---|---|---|
| focal | `#b5452b` (unchanged) | `#ffb4a6` (was `#e0675a`) | Night focal had a 1.0:1 contrast ratio with node-1. New value is about 2:1 against node-1 and 11:1 on ground. Keep the rule that focal is never colour alone. |
| on-node (new) | `#15141a` | `#15141a` | Numerals and text on node fills. Gives 4.3 to 9.5:1 across all eight nodes. Ink on Night fails (1.7 to 3.5:1). |
| control (new) | `#6c6870` | `#9a9c95` | Border for pills, tabs and buttons. 4.75:1 on Paper, 6.96:1 on Night. `rule` was 1.6:1 and 1.8:1. |
| banner | `#0d0e10` | `#000000` | Unchanged, but add a 1px `rule` line under the band on Night (band against ground is 1.09:1). |

Usage text changes:

- `node-1` to `node-8`: every node fill gets a 1.6px ink outline, not only node-3 and node-5. Fills on Paper ground measure 1.7 to 3.5:1, so nodes 1, 2 and 4 also fall under 3:1. Colour identifies the code at a corner, not a sequence. Say so in the legend.
- `focal`: no focal text on `sunk` (4.38:1 on Paper). Draw focal at stroke-route weight.
- `role-act`, `role-decide`, `role-record`: dots, rings and chips only. Never text. The document's `.status.ok` currently sets text in `role-decide`, which is 4.27:1 on ground. Fix it.

### Type

Add these styles. Delete nothing existing.

| Style | Family | Size / line-height / weight | Use |
|---|---|---|---|
| card-title | serif | 18px / 1.25 / 650 | Step, glance and stat card titles |
| caption | serif | 14px / 1.5 / 400, ink-2 | Figure captions, notes, card values |
| annotation | serif | 13px / 1.4 / 400, ink-2 | Sublabels inside SVG. Smallest serif size |
| numeral | mono | 26px / 1 / 700 | Bit digits, large codes |
| chip | mono | 10.5px / 1.3 / 700 / 0.08em tracking | Chips, table heads, status pills, rail headings |

Snap rules for the document:

- Nothing below 10.5px. Raise 9.5 and 10 to 10.5.
- `.sub` 19.5 and `.lede` 18.5 become 19 (the lede style).
- `figcaption` 14.5 becomes 14.
- `.reader dd` 16 becomes 16.5.
- Sans controls 12, 13 become 12.5. Fold and open buttons 11 become 11.5.
- Mobile `section` 26px and `part` 30px are documented responsive steps at 640px and below.

### Fonts

Ship Newsreader as a variable serif with weight axis 200 to 800, so 650 renders truly. Subset to Latin plus the punctuation used (`· → ← − — ’`). Store it in `project/fonts/` and list it in `type.fonts[]`. Add italic.

New serif stack: `"Newsreader", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif`.

Use `font-display: swap`. Embed as base64 in the single-file HTML so the document travels.

### Spacing

Only 29% of spacing values in the document sit on the scale. Add three tokens and snap everything.

Existing tokens stay: `space-1` 4, `space-2` 8, `space-3` 14, `space-4` 24, `space-5` 48, `space-6` 96.

New:

| Token | Value | Use |
|---|---|---|
| space-tight (new) | 6px | Gaps between pills and chips |
| space-ctl (new) | 10px | Grid gaps, control padding |
| space-card (new) | 16px | Figure and card padding |

Snap map: 2, 3 to 4. 5 to 6. 7, 9 to 8. 11, 12, 13 to 14. 15, 18 to 16. 20, 22, 26, 28, 30, 34 to 24. 40, 52, 56, 60 to 48. 84, 90, 120 to 96. So section top padding 56 becomes 48, part top margin 84 becomes 96, and main bottom padding 120 becomes 96.

### Strokes, targets and motion

| Token | Value | Use |
|---|---|---|
| stroke-node (new) | 1.6px | Node outline in ink |
| target-min (new) | 24px | WCAG 2.2 floor for any control |
| target-touch (new) | 44px | Applied under `(pointer: coarse)` |
| motion-dash | 6s linear infinite | Existing dash travel |
| motion-glide (new) | 400ms cubic-bezier(.4,0,.2,1) | Recentring: ring re-forms |
| motion-fade (new) | 200ms ease-out | Step lighting |

All motion stops under `prefers-reduced-motion`. Add no other animation.

## 3. Rule changes in README.md

1. **Voice.** Replace "no may, might, arguably" with: "No epistemic hedges: might, arguably, perhaps, seems. May is allowed only as permission, as in 'May this proceed?'" The Recorded mode is exempt because it is verbatim.
2. **Focal.** Replace "one thing per sheet" with: focal marks the current position, one at a time per view. Written and Scripted: the current part's kicker, and in Scripted the current sentence. Visual: the route being read or the return arrow. Network: the selected node or current step. The keyboard focus ring is exempt.
3. **Line grammar.** Cannot-do items are held powers, so they use dotted lines, not dashed. Dashes are only for computed or contingent. Dividers are never dashed.
4. **Interaction.** Change "Three view modes, always" to "Five view modes, always" and rename Prose to Written (section 5).
5. **Accessibility.** Add: controls have a 3:1 border (`control`); targets are at least `target-min`, and `target-touch` on coarse pointers; tabs follow the full tab pattern.
6. **Audit table.** Mark rows 3, 4, 6 and 7 closed. Add the findings in section 4 of this spec.

## 4. Document fixes (rerun)

| Where | Change |
|---|---|
| `.part .kicker` | colour `ink-3`; only the current part's kicker is focal (the rail already tracks it) |
| `.netinsp summary::before` (the + and − marker) | `ink-3`, not focal |
| `.step .fwd .kicker` | `ink-3` |
| `.step .fwd` top border | `1px solid line`, not dashed |
| `.cando .no` | `1.5px dotted ink-3` border; strike colour `ink-3`, not focal |
| `.status.ok` | text `ink`, border and dot `role-decide` |
| Node numerals | use `on-node` token, not the hard-coded `#15141a` |
| Pills, tabs, tools, fold, travel, links, bits, status | border uses `control` |
| Fold and trail chips | fold padding `8px 11px`; trail chips `7px 9px` (both at least 24px tall) |
| Coarse pointer | `min-height: 44px` on all pills, tabs, tools, fold, travel, links, trail chips |
| Pills | `white-space: nowrap`; under 1100px relabel Way one, two, three to One, Two, Three |
| `.nn:focus{outline:none}` | remove; on `.nn:focus-visible` draw a focal ring of 2px at radius + 6 |
| SVGs | the three without `role="img"` get `role="group"` and an `aria-label`; each figure SVG gets `<title>` and `<desc>` |
| `<html>` | `lang="en-AU"`; move `<title>` into `<head>` |
| Version | one `version` in the data source feeds the band, footer, masthead and PDF. Today they read 2, 3 and 5 |

## 5. Five view modes

Tab order, left to right: **Network, Visual, Written, Scripted, Recorded**. Network is the default tab on open.

Each answers a different question about the same document. Read in the order the material is made, from Recorded to Network, the five words are:

1. **transcription** — what was said (spoken)
2. **transliteration** — what was meant (clean speech for the ear)
3. **translation** — what was claimed (prose for the eye)
4. **transformation** — what was represented, built, conceptualised (graphic)
5. **transposition** — what was associated, synthesised, dynamically architectured (interactive)

The tab bar runs the other way. The table and sections below follow the making order.

| Mode | Answers | Content | Voice rule |
|---|---|---|---|
| Recorded | What was said? | Word-for-word transcript of the voice and text conversation, both speakers | Exempt. Verbatim, not edited |
| Scripted | What was meant? | Clean narration the text-to-speech voiceover reads | Full voice rule |
| Written | What was claimed? | The prose argument (was Prose) | Full voice rule |
| Visual | What was represented? | Images, diagrams, flowcharts, maps and other visual aids, in order | Full voice rule on labels |
| Network | What was associated? | All four joined: toggles, recentring, inspector, tables, matrices, cross-references, links, animations, collapse and expand | Full voice rule |

### Shared behaviour

- Tab bar: five pills with the full tab pattern: `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, and a real `role="tabpanel"` per mode. Left and Right arrows move between tabs, Home and End jump, with roving tabindex. It sits at the top, sticky under the band, and again at the bottom.
- Narrow screens (640px and below): the bar scrolls horizontally, labels stay in full, and the selected tab scrolls into view.
- Bottom bar: Previous and Next step by part in Recorded, Scripted, Written and Visual, and by node in Network.
- Shared reference: one reference (a part or a node) carries across all five modes. Switching mode scrolls straight to that passage. Store it in the URL hash, for example `#m=scripted&r=b3`. The trail of past references persists across modes.
- Collapse: every part folds to its kicker and title in every mode. A Collapse parts tool folds them all.
- Provenance: every Scripted, Written and Visual passage carries `from` ids that point at the Recorded turns it was consolidated from. A mono Source link on each passage jumps to them.

### Recorded

- One column, 42rem. Body type, serif 16.5px.
- Each turn starts with a mono kicker: `PERCY · VOICE · 14:02` or `CLAUDE · TEXT · 14:03`. Claude's turns are set in `ink-2` and indented `space-4` (24px). Colour does not carry the speaker, and role colours are not used.
- Turns are grouped into sessions by date. Each session is a part, collapsed by default.
- Verbatim rule: no edits, fillers kept. Transcription doubt is marked `[?]`, matching the line grammar. Redactions show as `[redacted]` in mono.
- Part boundaries show a hairline and a mono marker such as `→ PART IV · THE LOOP`, which links to Written.
- A Find field sits in the tab bar's tool row, as a pill-shaped input.
- Recorded ships in every build, Paper and Night, with no privacy flag.

### Scripted

- Written for the ear. Short declarative sentences. No parentheses, arrows, tables or symbols. Segments of 60 words or fewer, about 25 seconds each.
- Codes are spelled digit by digit so they are spoken correctly: write "one, zero, one", not "101".
- A Listen pill on each segment, plus a global Listen, Pause and a speed toggle group (1×, 1.25×, 1.5×).
- The current sentence is underlined in focal at 2.5px with a 4px offset. No fill. This is the Scripted mode's one focal.
- Build step: emit `scripted.txt`, one segment per paragraph. This file is what the voice chat reads aloud.
- Each segment links to its Written passage and its Recorded turns.

### Written

The existing prose, renamed. Each paragraph gets a `data-seg` id plus mono Source and Listen links, always visible on touch and on hover or focus elsewhere.

### Visual

The existing figures, plus a numbered figure index (kicker `FIG 1` and so on). Static matrices and tables that are part of the argument stay in Written and Visual.

### Network

- Existing controls stay: span, direction, compass, recentring, trail.
- The inspector gets four collapsible facet sections that mirror the modes: Said (Recorded), Heard (Scripted), Read (Written), Seen (Visual). Each has a mono summary such as `+ SAID · 6 TURNS`, an excerpt of three lines at most, and an Open pill that jumps to that mode at that passage.
- New: a sortable, filterable Table and Matrix component. A row click selects and recentres the node.
- New: inline cross-reference chips (mono code plus label). Click to recentre.
- Animations are limited to the three motion tokens above.

## 6. Data model

One source file builds all five modes. Suggested shape:

```json
{
  "meta": { "id": "nine-bodies", "title": "The Nine Bodies of Authority", "version": "3", "date": "2026-10" },
  "parts": [{ "id": "p4", "kicker": "Part IV", "title": "The loop" }],
  "turns": [{ "id": "t0412", "speaker": "percy", "via": "voice", "at": "2026-10-26T14:02:11+08:00", "text": "...", "flags": [] }],
  "passages": {
    "written":  [{ "id": "w120", "part": "p4", "html": "...", "from": ["t0412"] }],
    "scripted": [{ "id": "s120", "part": "p4", "text": "...", "written": "w120", "from": ["t0412"], "audio": null }],
    "visual":   [{ "id": "v12", "part": "p4", "figure": "loop", "from": ["t0412"] }]
  },
  "nodes": [{ "id": "b3", "code": "111", "refs": { "recorded": ["t0412"], "scripted": ["s120"], "written": ["w120"], "visual": ["v12"] } }]
}
```

## 7. Components to add

Each needs a `README.md` and a `preview.html` under `components/<Name>/`, with line 1 `<!-- @dsCard group="..." height=N -->`.

- Existing, to finish: write `components/bundle.js` as one classic script assigning `window.FieldNotation`, with no imports and no network, covering Compass, NodeRoute, Inspector, Toggle and ViewTabs. Add `bundle.css` from the document CSS. The component previews are blank without it. Raise the Inspector `@dsCard` height until the Close row and fact grid show (about 320).
- ViewTabs: update to five modes with the full tab pattern.
- Transcript: turn, kicker, session fold, Find.
- Script: segment, Listen pill, speed group, current-sentence underline.
- Chip: mono 10.5px, 9px dot, 6px gap.
- Table: surface fill, 1px `line` border, radius 14, header ink fill with ground text in the chip style, cells 10px 14px.
- Spine: 38px numbered circle, 1.5px ink line, card radius 14.
- CanCannot: yes 1.5px solid ink, no 1.5px dotted ink-3 with ink-3 strike.
- Status: pill, mono chip style; ok variant uses a `role-decide` dot and ink text.
- Fold, Trail, Rail.
- Matrix and CrossRef (Network).

## 8. Fix list from the earlier audit that this spec closes

Contrast of controls, focal overuse, node text on Night, spacing and type drift, missing serif, tab semantics, hidden focus, touch targets, wrapping pills, Night banner, version mismatch, blank previews, missing `lang`.

## 9. Order of work

1. `tokens.json`: sections 2 and the new motion and target groups.
2. `README.md`: section 3.
3. Fonts: add Newsreader files and update the stack.
4. Components: bundle, bundle.css, the new components and previews.
5. Data source: build from the transcript and existing document.
6. Rebuild the Nine Bodies HTML with the five modes and the section 4 fixes.
7. Write `lastChange` in `design-system.json` last. Keep every other key and the marker.

## 10. Acceptance checks

- Contrast: every text pair at least 4.5:1 and every control border at least 3:1, on both grounds, computed by script.
- Token adherence in the document: spacing at least 95% on scale, font sizes 100% on token, radii on token, zero hard-coded hex outside `:root`.
- Focal: exactly one focal element per mode view, other than the focus ring. Check with a script.
- Keyboard: walk all five tabs with arrows, open and close the inspector, and see a visible focus ring on every network node.
- Link integrity: every `from`, `refs` and Source link resolves in the other modes. The reference carries across all five.
- The version string appears from a single source and matches in the band, footer, masthead and PDF.
- Reduced motion: all animation and smooth scroll stop.
- Authored words of the Nine Bodies document are unchanged. Diff the prose before and after.
