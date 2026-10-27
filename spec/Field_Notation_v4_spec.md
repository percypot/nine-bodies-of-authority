# Field Notation v2: spec for Claude Code

Prepared 26 October 2026 for Percy. Tidied after the Claude Docs pass. This spec is the Version 4 rebuild of the Expanded edition (30 pages, 26 October 2026), the canonical authored source. It updates the Field Notation design system and rebuilds The Nine Bodies of Authority HTML on it. The system has five view modes.

Mode names, 26 October 2026. Pipeline and tab order:

1. **Interactive** — the live mode where all the forms meet.
2. **Illustrative** — the visual mode in graphic form.
3. **Comprehensive** — the written mode in full depth form within the scope.
4. **Descriptive** — the explanatory mode in narrative enactment form.
5. **Transcriptive** — the recorded mode in text form.

Retired as mode labels: haptic, visual, written, spoken, scripted, recorded, network, scriptive, narrative, documentative. Do not use them.

## Mode inflections

Seven forms only, in this order. No `-al` forms (not interactional, illustrational, descriptional, or any other). No other inflections. Agent nouns take `-er`, including where the usual spelling is `-or`. The adverb is `-ly` on every row: the `-ive` adjective plus `ly`. Descriptive's adverb is `descriptively`, not `descriptionally`. Transcriptive's adverb is `transcriptively`.

| Mode | -ive | Verb | -able | Agent -er | -ion | -ing | -ly |
|---|---|---|---|---|---|---|---|
| Interactive | interactive | interact | interactable | interacter | interaction | interacting | interactively |
| Illustrative | illustrative | illustrate | illustratable | illustrater | illustration | illustrating | illustratively |
| Comprehensive | comprehensive | comprehend | comprehendable | comprehender | comprehension | comprehending | comprehensively |
| Descriptive | descriptive | describe | describable | describer | description | describing | descriptively |
| Transcriptive | transcriptive | transcribe | transcribable | transcriber | transcription | transcribing | transcriptively |

Suffix check. The `-ly` column matches on all five: each adverb is the `-ive` adjective plus `ly`. Interactive is one stem throughout. Illustrative is one stem throughout, which is why the locked spellings are `illustratable` and `illustrater`. Describe and transcribe mirror each other: `-able`, `-er`, and `-ing` use describ- and transcrib-; `-ive`, `-ion`, and `-ly` use descript- and transcript-. Comprehensive does not. Its `-ive`, `-ion`, and `-ly` use comprehens- (`comprehensive`, `comprehension`, `comprehensively`), while the verb, `-able`, `-er`, and `-ing` use comprehend- (`comprehend`, `comprehendable`, `comprehender`, `comprehending`). That stem split stays. It is not a typo, and it is not rewritten here.

Interactive is the live space, not an output. The four outputs are illustrative, comprehensive, descriptive, and transcriptive.

## Handoff prompt

Read this spec top to bottom. Work in the order in section 9. Edit only the `project/` files of Field Notation, then rebuild the Nine Bodies HTML from the updated system. Do not change the authored words of the document. After each phase, run the checks in section 10 and report the numbers.

## 1. Inputs Claude Code needs from Percy

- A transcript source file of the whole conversation that led to the document, with speaker, time and whether each turn was voice or text. Suggested path: `source/transcript.json`.
- Default mode on open: Interactive, the first tab.
- Transcriptive is always public. It ships in every build, Paper and Night. No privacy flag.
- There is no narrative mode and no voiceover file. Narrative was the output side of voice. Transcriptive is the input side.

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

1. **Voice.** Replace "no may, might, arguably" with: "No epistemic hedges: might, arguably, perhaps, seems. May is allowed only as permission, as in 'May this proceed?'" Transcriptive is exempt because it is verbatim. It is spoken audio turned into text, the input side of voice. Descriptive explains the material. Narrative, the output side of voice, is not a mode.
2. **Focal.** Replace "one thing per sheet" with: focal marks the current position, one at a time per view. Comprehensive and Descriptive: the current part's kicker. Illustrative: the route being read or the return arrow. Interactive: the selected node or current step. The keyboard focus ring is exempt.
3. **Line grammar.** Cannot-do items are held powers, so they use dotted lines, not dashed. Dashes are only for computed or contingent. Dividers are never dashed.
4. **Interaction.** Change "Three view modes, always" to "Five view modes, always" and rename Prose to Comprehensive (section 5).
5. **Accessibility.** Add: controls have a 3:1 border (`control`); targets are at least `target-min`, and `target-touch` on coarse pointers; tabs follow the full tab pattern.
6. **Audit table.** Mark rows 3, 4, 6 and 7 closed. Add the findings in section 4 of this spec.
7. **Mode inflections.** Copy the seven-form table from the top of this spec into the design guide. Those spellings are locked, including `interacter`, `illustrater`, `interactable`, `illustratable`, and `comprehendable`. Adverbs: `interactively`, `illustratively`, `comprehensively`, `descriptively`, `transcriptively`. Not `descriptionally`. Do not add `-al` forms.

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

Pipeline order, and tab order left to right: **Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive**. Interactive is the default tab on open.

1. **Interactive** — the live mode where all the forms meet.
2. **Illustrative** — the visual mode in graphic form.
3. **Comprehensive** — the written mode in full depth form within the scope.
4. **Descriptive** — the explanatory mode in narrative enactment form.
5. **Transcriptive** — the recorded mode in text form.

Interactive holds the toggles, recentring, inspector, tables, matrices, cross-references, links, animations, and collapse and expand. It is not an output.

| Mode | Kind | Answers | Voice rule |
|---|---|---|---|
| Interactive | Combined space | What connects? | Full voice rule |
| Illustrative | Output | What is seen? | Full voice rule on labels |
| Comprehensive | Output | What is read? | Full voice rule |
| Descriptive | Output | What is explained? | Full voice rule |
| Transcriptive | Output | What was said? | Exempt. Verbatim, not edited |

### Shared behaviour

- Tab bar: five pills with the full tab pattern: `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, and a real `role="tabpanel"` per mode. Left and Right arrows move between tabs, Home and End jump, with roving tabindex. It sits at the top, sticky under the band, and again at the bottom.
- Narrow screens (640px and below): the bar scrolls horizontally, labels stay in full, and the selected tab scrolls into view.
- Bottom bar: Previous and Next step by part in Transcriptive, Descriptive, Comprehensive and Illustrative, and by node in Interactive.
- Shared reference: one reference (a part or a node) carries across all five modes. Switching mode scrolls straight to that passage. Store it in the URL hash, for example `#m=transcriptive&r=b3`. The trail of past references persists across modes.
- Collapse: every part folds to its kicker and title in every mode. A Collapse parts tool folds them all.
- Provenance: every Descriptive, Comprehensive and Illustrative passage carries `from` ids that point at the Transcriptive turns it was consolidated from. A mono Source link on each passage jumps to them. Interactive opens those same passages in place.

### Transcriptive

- One column, 42rem. Body type, serif 16.5px.
- Each turn starts with a mono kicker: `PERCY · VOICE · 14:02` or `CLAUDE · TEXT · 14:03`. Claude's turns are set in `ink-2` and indented `space-4` (24px). Colour does not carry the speaker, and role colours are not used.
- Turns are grouped into sessions by date. Each session is a part, collapsed by default.
- Verbatim rule: no edits, fillers kept. Transcription doubt is marked `[?]`, matching the line grammar. Redactions show as `[redacted]` in mono.
- Part boundaries show a hairline and a mono marker such as `→ PART IV · THE LOOP`, which links to Comprehensive.
- A Find field sits in the tab bar's tool row, as a pill-shaped input.
- This mode ships in every build, Paper and Night, with no privacy flag.

### Descriptive

The explanatory mode in narrative enactment form.

- One column, 42rem. Serif, the body size. Short passages, each tied to one Comprehensive passage.
- Each passage links to its Comprehensive passage and to its Transcriptive turns.
- No `narrative.txt`. Narrative is not a mode.

### Comprehensive

The existing prose, renamed from Prose. Each paragraph gets a `data-seg` id plus a mono Source link, always visible on touch and on hover or focus elsewhere.

### Illustrative

The existing figures, plus a numbered figure index (kicker `FIG 1` and so on). Static matrices and tables that are part of the argument stay in Comprehensive and Illustrative.

### Interactive

The combined space, not an output. Existing controls stay: span, direction, compass, recentring, trail.

- The inspector gets four collapsible facet sections, one per output: Said (Transcriptive), Explained (Descriptive), Read (Comprehensive), Seen (Illustrative). Each has a mono summary such as `+ SAID · 6 TURNS`, an excerpt of three lines at most, and an Open pill that jumps to that output at that passage.
- New: a sortable, filterable Table and Matrix component. A row click selects and recentres the node.
- New: inline cross-reference chips (mono code plus label). Click to recentre.
- Animations are limited to the three motion tokens above.

## 6. Data model

One source file builds all five modes. Suggested shape:

```json
{
  "meta": { "id": "nine-bodies", "title": "The Nine Bodies of Authority", "version": "4", "date": "2026-10", "source": "expanded-30" },
  "parts": [{ "id": "p4", "kicker": "Part IV", "title": "The loop" }],
  "turns": [{ "id": "t0412", "speaker": "percy", "via": "voice", "at": "2026-10-26T14:02:11+08:00", "text": "...", "flags": [] }],
  "passages": {
    "comprehensive":  [{ "id": "w120", "part": "p4", "html": "...", "from": ["t0412"] }],
    "descriptive": [{ "id": "d120", "part": "p4", "text": "...", "comprehensive": "w120", "from": ["t0412"] }],
    "illustrative":   [{ "id": "v12", "part": "p4", "figure": "loop", "from": ["t0412"] }],
    "transcriptive": [{ "id": "t0412" }]
  },
  "nodes": [{ "id": "b3", "code": "111", "refs": { "transcriptive": ["t0412"], "descriptive": ["d120"], "comprehensive": ["w120"], "illustrative": ["v12"] } }]
}
```

## 7. Components to add

Each needs a `README.md` and a `preview.html` under `components/<Name>/`, with line 1 `<!-- @dsCard group="..." height=N -->`.

- Existing, to finish: write `components/bundle.js` as one classic script assigning `window.FieldNotation`, with no imports and no network, covering Compass, NodeRoute, Inspector, Toggle and ViewTabs. Add `bundle.css` from the document CSS. The component previews are blank without it. Raise the Inspector `@dsCard` height until the Close row and fact grid show (about 320).
- ViewTabs: five modes in pipeline order, with the full tab pattern. Labels: Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive.
- Transcriptive: turn, kicker, session fold, Find.
- Descriptive: explanation passage, linked to Comprehensive and Transcriptive.
- Chip: mono 10.5px, 9px dot, 6px gap.
- Table: surface fill, 1px `line` border, radius 14, header ink fill with ground text in the chip style, cells 10px 14px.
- Spine: 38px numbered circle, 1.5px ink line, card radius 14.
- CanCannot: yes 1.5px solid ink, no 1.5px dotted ink-3 with ink-3 strike.
- Status: pill, mono chip style; ok variant uses a `role-decide` dot and ink text.
- Fold, Trail, Rail.
- Matrix and CrossRef (Interactive).

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
- Keyboard: walk all five tabs with arrows, open and close the inspector, and see a visible focus ring on every node in Interactive.
- Link integrity: every `from`, `refs` and Source link resolves in the other modes. The reference carries across all five.
- The version string appears from a single source and matches in the band, footer, masthead and PDF.
- Reduced motion: all animation and smooth scroll stop.
- Authored words of the Nine Bodies document are unchanged. Diff the prose before and after.

## 11. Expansion: how to use what is already locked

This section adds depth. It does not replace sections 1 to 10. Where a sentence above and a sentence here could be read two ways, the earlier sentence stays in force and this section says how to apply it.

Version stamp. This file is the Version 4 specification. The canonical authored source is the Expanded edition, 30 pages, 26 October 2026. The Nine Bodies HTML in Downloads is the Version 3 interaction prototype and is behind that edition. Do not promote the HTML's "Version 3" footer, the 22-page Version 2, or a README "version 5 draft" label over Version 4. One version string, `4`, feeds the band, the footer, the masthead and any PDF.

### 11.1 Why five modes, and how they cite each other

A reader meets the same reference in five places. Interactive is where that meeting is live. The other four are outputs. Switching mode does not invent a new reference. It shows the same reference in another form.

| From | To | What the cross-reference does |
|---|---|---|
| Interactive | any output | An inspector facet opens that output at the current node. Said opens Transcriptive, Explained opens Descriptive, Read opens Comprehensive, Seen opens Illustrative. |
| Illustrative | Comprehensive | A figure's Source link opens the prose the figure is drawn from. |
| Illustrative | Transcriptive | The same Source link can open the turns the figure was consolidated from. |
| Comprehensive | Descriptive | Each full passage has a short enactment that says what the passage is doing. |
| Descriptive | Comprehensive | Each enactment names the passage it enacts. |
| Descriptive | Transcriptive | Each enactment names the turns it was consolidated from. |
| Transcriptive | Comprehensive | A part-boundary marker such as `→ PART IV · THE LOOP` opens the written passage. |
| Any output | Interactive | The shared hash (`#m=interactive&r=b3`) recentres the live compass on that node. |

Usage. Do not duplicate a long argument in Interactive. Interactive shows the connection and the four facets. Comprehensive holds the argument. Descriptive holds the enactment. Illustrative holds the graphic. Transcriptive holds the words that were said.

Example. Body 3, the enforcement triad, is reference `b3`. In Interactive the inspector lists Said, Explained, Read and Seen. In Illustrative the compass node and the cube corner for that body are current. In Comprehensive the section "Enforcement, intelligence, surveillance" is the passage. In Descriptive the water-case step for that body is the enactment. In Transcriptive the turns whose `from` ids point at that passage are the record.

### 11.2 Mode by mode: rationale, example, rule

**Interactive** — the live mode where all the forms meet.

Rationale. The other four can be read alone. Interactive is the only mode in which a choice in one form moves the others. It is not a fifth essay and not a fifth picture.

Example. Selecting the sanitation position inside body 5 recentres the compass, opens the Seen facet on the cube corner, and keeps the Read facet on the Preservational account so the reader can see that a permit and an account are different questions.

Usage. Put toggles, recentring, the inspector, tables, matrices, cross-references, links, animation, and collapse and expand here. Do not put a second copy of the full prose here. Voice rule applies in full. One focal mark: the selected node or the current step.

**Illustrative** — the visual mode in graphic form.

Rationale. A graphic has to be checkable against the words. The figure index (`FIG 1` onward) is how a picture stays inside the argument instead of floating beside it.

Example. Figure 8 is the cube. Its caption states which way is active. The route stroke is the way colour from section 11.5, not a new focal colour for each way. Focal still marks only the current corner.

Usage. Figures, the compass, the cube, and static matrices that are part of the argument. Labels take the voice rule. Every figure carries `from` ids. Role colour is a dot, never the label text.

**Comprehensive** — the written mode in full depth form within the scope.

Rationale. "Within the scope" means the passage covers the whole of its part and does not wander into another part's argument. Full depth is not a longer Descriptive enactment. Descriptive stays short. Comprehensive carries the literary form.

Example. The part "How each body is drawn" is Comprehensive. The one-paragraph water step for the same body is Descriptive. Both cite the same Transcriptive turns.

Usage. The existing prose, renamed from Prose. Each paragraph has `data-seg` and a Source link. Voice rule applies in full. The current part's kicker is the one focal mark.

**Descriptive** — the explanatory mode in narrative enactment form.

Rationale. Enactment is how a function is shown in a case, not a separate Listen mode and not a voiceover file. The water case is the worked enactment. Narrative is not a mode. There is no `narrative.txt`.

Example. "Energy resources supplies power for the pumps. Sanitation approves or denies the operation against containment. Preservational records whether the contamination persists." That is one body's enactment. It does not replace the Comprehensive drawing of body 5.

Usage. One column, 42rem, serif at body size. Each passage links to one Comprehensive passage and to its Transcriptive turns. Voice rule applies. Do not write `descriptionally`. The adverb is `descriptively`.

**Transcriptive** — the recorded mode in text form.

Rationale. This is the input side of voice: spoken audio recorded and converted into text. It is always public, in Paper and in Night, with no privacy flag. It is exempt from the voice rule because it is verbatim.

Example. A kicker reads `PERCY · VOICE` or `CLAUDE · TEXT`. The source transcript has no wall-clock times, so a missing time is shown as absent, not invented. Doubt is `[?]`. A redaction is `[redacted]` in mono.

Usage. One column, 42rem, serif 16.5px. Claude's turns are ink-2 and indented 24px. Sessions are parts, collapsed by default. Find sits in the tool row.

### 11.3 Inflections in use

The seven-form table in "Mode inflections" is closed. Examples of allowed sentences:

- An interacter interacts interactively with the compass. The interaction is interactable.
- An illustrater illustrates the cube illustratively. The illustration is illustratable.
- A comprehender comprehends the passage comprehensively. The comprehension is comprehendable.
- A describer describes the case descriptively. The description is describable.
- A transcriber transcribes the turn transcriptively. The transcription is transcribable.

Forbidden. Any `-al` form, including interactional, illustrational, descriptional. `descriptionally`. An agent noun in `-or` (illustrator, interactor). A fifth adverb spelled `transcriptive` without `-ly`.

The comprehensive stem split stays. Write `comprehensive`, `comprehension`, `comprehensively` with comprehens-. Write `comprehend`, `comprehendable`, `comprehender`, `comprehending` with comprehend-. Do not "correct" one stem into the other.

Illustrative stays one stem, which is why the locked spellings are `illustratable` and `illustrater`, keeping `-at-` and `-er`.

### 11.4 The nine bodies

The Expanded edition is the source for names. Each body is a triad: embodied agent (enacts and submits, or responds and requests), authoritative body (approves or denies), authoritative agent (records and reviews). Classification follows the activity, not the organisation.

| # | Embodied agent | Authoritative body | Authoritative agent | Loop 1 code | Collective name |
|---|---|---|---|---|---|
| 1 | Governmental | Constitutional | Diplomatic | none | none. Body 1 is the bridge, not a corner |
| 2 | Legal | Judicial | Auditorial | 101 | Consequential |
| 3 | Enforcement | Intelligence | Surveillance | 111 | Deterministic |
| 4 | Development logistics | Civic welfare | Property stewardship | 011 | Propositional |
| 5 | Energy resources | Sanitation | Preservational | 010 | Environmental |
| 6 | Medical | Scientific | Nutritional provision | 110 | Reproducible |
| 7 | Manufacturing | Commercial | Financial | 100 | Contractual |
| 8 | Content creation | Media distribution | News journalism | 000 | Transmissible |
| 9 | Cultural | Educational | Religious | 001 | Transformational |

Body 5's account is Preservational so that Environmental can name code 010. Body 9's acting position is Cultural. Collective names belong to codes. On ways two and three a body inherits the name of the code it sits on. Reproducible is the strained cross-loop name. Ways two and three are not fully scored. Loop 1 is the baseline.

Node colour names the code at a corner, not the body number and not the order around the compass. The eight node fills keep their existing tokens. Every node has a 1.6px ink outline. Numerals use `on-node`.

Compass labels do not use the short names Governmental, Legal, Enforcement, or Development. Those four were applied by mistake. Body 1's compass label is Bridge. Bodies 2 to 9 take the collective name of the code they hold on the active way. On way one those names are Consequential, Deterministic, Propositional, Environmental, Reproducible, Contractual, Transmissible, Transformational.

Fourth name. The Expanded edition and `nine-bodies-transcript.json` were searched for a fourth name that the short label Development had displaced. The name in the Expanded edition for that corner, Loop 1 code 011, is Propositional, and the body's acting name there is Development logistics. Both are present. An earlier transcript wording, "built environment" and "housing and built environment", is not carried in the Expanded edition, so it is not the compass label. The edition's fourth overview panel is "Collective overview" / "Eight code names". That panel does not add a permanent name for a separate governmental traversal, and this spec does not invent one.

### 11.5 The cube, its three roots, and the way colours

The cube has 8 corners, 12 edges, and 6 routes that visit every corner once and change one bit per step. Bodies 2 to 9 sit on the corners. Body 1 does not. Bits are read E-B-A: embodied agent, authoritative body, authoritative agent. A 1 is in focus and equal. A 0 is out of focus. The code measures standing, not presence.

Three roots are the three ways. Their geometry on the governmental stage is the geometry already in the Version 3 HTML, and it stays:

| Root | Lead | Route |
|---|---|---|
| Way one | E | 101 → 111 → 011 → 010 → 110 → 100 → 000 → 001 → 101 |
| Way two | B | 101 → 111 → 110 → 100 → 000 → 010 → 011 → 001 → 101 |
| Way three | A | 101 → 111 → 110 → 010 → 011 → 001 → 000 → 100 → 101 |

Way colour is constant across stages. It marks the root, not the stage and not the body.

| Root | Lead | Paper | Night | Where it is used |
|---|---|---|---|---|
| Way one | E, orange | `#c8741e` | cedar `#e8a36a` | The way control, the options that root drives, the compass stroke while that way is active |
| Way two | B, green | `#3c9447` | lime `#9ad84a` | The same, for way two |
| Way three | A, blue | `#4479c9` | cyan `#5ccfe6` | The same, for way three |

One hue per position (ratified 26 October 2026). Each way takes the colour of the position that leads it, so `way-1`, `way-2` and `way-3` alias `role-act`, `role-decide` and `role-record`. The cube's bit strokes use the same three. Paper uses the standard set; Night uses the bright set. This replaces the earlier yellow, green and blue hexes and the rule that role colours are not reused as way colours.

Way colour is a border, a 9px dot, or a stroke. It is not text colour and never focal.

**Way one is kept as it is.** Its label on the governmental stage remains `Way one · E leads`. Its route, its pulse readout, and its cube drawing stay the drawing already in the HTML. Yellow is added to the control. No new options list is built for way one.

**Ways two and three are rebuilt per stage.** The stage control sits on the cube figure. Governmental is the default, so the file opens as it does now, plus the way colours.

| Stage | Way one | Way two | Way three |
|---|---|---|---|
| Governmental | unchanged: `Way one · E leads` | unchanged: `Way two · B leads` | unchanged: `Way three · A leads` |
| Legal | unchanged: `Way one · E leads` | rebuilt: Judicial | rebuilt: Auditorial |
| Enforcement | unchanged: `Way one · E leads` | rebuilt: Intelligence | rebuilt: Surveillance |

On Legal and Enforcement, choosing way two or way three shows that position's options, taken from the authored sentences already in the HTML, and the list is bordered and dotted in that way's colour. Choosing way one hides that rebuilt list and shows the original way-one cube. On Governmental, ways two and three keep their routes and do not gain a replacement options list. Their controls are still green and blue. Way one's is orange.

Legal options, way two (Judicial). "Approves or denies applications through authoritative rulings." "The judicial body rules on them, and its rulings set the precedent later cases rely on." "Rules on them within its remit."

Legal options, way three (Auditorial). "Independently records and reviews authorised material, procedures and outcomes." "Auditorial records the evidence, procedure, reasoning and outcome, and returns that account to everyone with standing to question it." "Records the evidence presented, the procedure followed, the reasoning given and the decision reached, and checks that the findings and principles were represented faithfully."

Enforcement options, way two (Intelligence). "Assesses information and approves or denies proposed operations." "Intelligence assesses information and decides whether each operation proceeds." "Assesses the information and approves or denies each operation within the permissions already granted."

Enforcement options, way three (Surveillance). "Records and reviews observations through separately controlled monitoring infrastructure." "Surveillance holds the observational record on infrastructure controlled separately from both." "Records what was found and what was done, and checks whether conditions afterwards match the account given."

The bug this closes: on the enforcement triad, ways two and three used to leave the same options on screen, because legal stays at 101 and enforcement stays at 111 on every geometric way. The rebuilt labels and option lists are the visible difference. The geometric routes remain available on the governmental stage.

### 11.6 The illustrative compass

The compass is Illustrative figure work and Interactive's live map. Both read the same way state.

Each node carries way one, way two, and way three. The three roots are controls on the compass, coloured orange, green, and blue. Clicking a root sets the active way and repaints the compass stroke, the cube, and the option list in that colour. Clicking a body node selects that body and keeps the way that was clicked with it, so the active way changes when the click is on a way root and the reference changes when the click is on a body.

The centre of the compass reads the active way's name and which position leads (`E LEADS`, `B LEADS`, or `A LEADS`). The loop stroke uses the active way colour. Focal still marks only the current body or the current corner. Way colour and focal are different marks.

Under 1100px the way labels may shorten to One, Two, Three, as section 4 already requires. The colours do not change when the labels shorten.

### 11.7 What this expansion does not do

It does not rebuild the HTML, `tokens.json`, the design guide, or the Nine Bodies document. It does not add a narrative mode, a `-al` form, or a fourth way. It does not rename way one on any stage. It does not treat Governmental, Legal, Enforcement, or Development as compass node labels.

## 12. Decisions logged, 26 October 2026

- One hue per position for roles, ways and bits: Paper `#c8741e` `#3c9447` `#4479c9`; Night `#e8a36a` `#9ad84a` `#5ccfe6`.
- Fifteen flagged turns: `t0028` and `t0032` join the thirteen.
- Kickers print what happened: `CLAUDE · VOICE` and `PERCY · TEXT` where true.
- Transcriptive is a working record for the author's own reference, not evidence.
- The Matrix crosses bodies (rows) with ways (columns); a code-to-name list is a key, not a matrix.
- Where an earlier line here differs from the five locked mode definitions at the top, the definitions win.
