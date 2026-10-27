# Version 6 implementation strategy

Prepared 27 October 2026, revised the same day against the two rubrics. Version 6 is a plan. No Version 6 HTML exists yet.

Order of authority: `v6-claude-prompt.md` is the spec. Where this file and the prompt differ, the prompt wins. `v6-rubric-design-system.md` and `v6-rubric-document.md` are the instruments the build is aimed at. Every change below names the rubric line it serves. This file records no score for Version 5 or Version 6.

The sum stays `8 codes + 27 ledger names + 27 bodies = 62`.

## Files

The follow-up creates one file and no other:

`<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v6.html`

These stay byte-for-byte as they are, checked by SHA-256 before and after the build:

- `document\The_Nine_Bodies_of_Authority_v4.html` (`4087df66cbd92af4…`)
- `document\The_Nine_Bodies_of_Authority_v5.html` (`5fbaa8853b001f9a…`)
- `document\v5-parts\` (all four fragments) and both Version 5 plans
- `spec\Field_Notation_v4_spec.md`, `project\tokens.json`, `project\design-system.json`, `project\README.md`
- every file under `project\components\` and `project\fonts\`
- `source\transcript.json`, `v6-claude-prompt.md`, both rubric files

No PDF is printed in this build, because the prompt allows one new file. The PDF restamp is on *Next*.

## Review of Version 5

Reviewed 27 October 2026. The whole file was rendered headless at 1280px on Paper and Night, every tab opened, the ledger clicked through all three roles, and every visible text element scanned for contrast. Defect 1 stops the page script, so every behaviour check below ran on a scratch copy with that one escape fixed. The shipped file was not edited.

### What holds

- With no mode in the hash, Interactive opens. With the defect 1 escape fixed, a fresh load of `#m=descriptive&r=b5` opens Descriptive.
- Five modes in the locked order, the full tab pattern, arrow, Home and End keys.
- The 22 Version 4 Comprehensive sections are identical to Version 4, word for word.
- The public ledger: three role pills, authoritative body pressed at load, 8 centre events, 16 dashed branches, a branch closes on a second click, neither click changes the pressed role, no placement control.
- The window *One path of eight* starts on Eight.
- Bodies-by-ways: body 1 blank, the eight codes on bodies 2 to 9, ways two and three empty.
- Liken on the categorical domain eight. Analogy on the ledger categorical eight, at Juxtaposition.
- Transcriptive: 459 turns, `Session 1 · 459 turns · time not recorded`, 225 `VOICE`, 230 `TEXT`, 4 `CLAUDE · TEXT`, the session collapsed at load.
- The sum line is the same sentence in the name frame and the name key.
- `lang="en-AU"`. Claude turns are indented 24px in `ink-2`. Inspector facet markers are `ink-3`. The Night band has its 1px `rule`.

### Defects

Measured, not estimated.

1. **The page script stops on load.** `#turnsData` holds `\Great work` at character 106,535. `\G` is an illegal JSON escape, so `JSON.parse` throws. Shipped, Descriptive renders 0 passages, a stored mode does not open, and every binding after that line is missing. Version 4 carries the same fault.
2. **The ledger mislabels roles once another role is pressed.** The three line labels, the status kicker and the inspection kicker are fixed strings. With embodied agent pressed, the centre line still reads *Authoritative body*, the inspection kicker reads `Authoritative body · Categorical · The Night Paramedic`, and the top branch reads `Embodied agent · The Public Librarian`. The Public Librarian is the authoritative body's archive.
3. **Focal is used more than once per view.**
   - Interactive has three marks: the map's selected node and route, the window's current station, and the ledger's centre label.
   - Comprehensive has 31 marks, because `.kicker` and `.part .kicker` are set in focal and the *How each body is drawn* number sits on a focal fill.
   - Illustrative has 88: every part and figure kicker, plus every cube loop route drawn in focal.
4. **The spec's document fixes (section 4) are absent.**
   - `.status.ok` text is `role-decide`.
   - The Status label is 9.5px.
   - `.cando .no` is dashed `rule`, and its strike is focal.
   - The `.fwd` top rule is dashed, and its kicker is focal.
   - `<title>` sits inside `<body>`.
5. **Source links do not resolve.** The 95 Source buttons carry `from` ids from the 127-turn log (`t0001`–`t0127`). The 459 record turns carry no ids. A Source click opens Transcriptive and marks no turn. Matching words shows the log sits inside the record: 124 of 127 ids are found, on record turns 1 to 233. `t0092`, `t0113` and `t0119` are not found.
6. **The window does not show its whole path.** The station row scrolls inside a 499px box beside the window inspector. At scale Eight, stations 100, 000 and 001 are out of view at 1280px.
7. **The window's facets are wrong.** Read shows the sum line for every station. Said prints `+ SAID` with no count.
8. **Labels outside the window fail contrast.** At scale One, station names sit at 1.84:1 and body numbers at 1.46:1.
9. **Targets under 24px.** 64 Source buttons are 18px tall, 9 `Open in Interactive` buttons are under 24px, and 4 facet summaries in Interactive are 15px.
10. **Figure Source buttons are unstyled.** In Illustrative they take the browser's default grey fill. On Night their label is 2.9:1.
11. **Off-token values.**
    - 14 font sizes are below the 10.5px floor (one 9.5px, thirteen 10px).
    - Further off-token sizes: 11px ×17, 14.5, 16, 21, 22, 34.
    - Spacing is 72.2% on the scale (203 of 281 values).
    - Radii include 3px and 50%.
    - 55 hex values sit outside `:root`, and 8 more in script fallbacks.
    - One transition, `background .15s,border-color .15s`, is outside the three motion tokens.
12. **Figures lack accessible names.** 8 of 9 figure SVGs have no `<title>` or `<desc>`. Figures carry no `FIG` number.
13. **Newsreader is not embedded.** The file has no `@font-face`. The serif falls back on any machine without the face installed.
14. **A water passage kicker reads `Body NaN · Step NaN`.** The passage is *Before the loop*.
15. **Builder language is printed.** The name frame and the name key each print "The name under each lens follows the column order Version 4 already gives."
16. **The version string has two sources.** The band is markup. The footer is a CSS `content` string.
17. **The grammar disagrees with itself on colour.** `project\tokens.json` (version 2) holds the earlier role and way pairs. Spec sections 11.5 and 12 hold the palette ratified on 26 October: one hue per position, Paper `#c8741e #3c9447 #4479c9`, Night `#e8a36a #9ad84a #5ccfe6`, ways aliasing roles. Version 5 uses the section 12 palette.

## How Version 6 is produced

1. Copy Version 5 to `The_Nine_Bodies_of_Authority_v6.html`. The band, masthead and footer keep reading Version 5.
2. Apply changes C1 to C24 below, in the copy only.
3. Run the content check:
   - **Interactive** has content when these are in the file: the travelling map (`#networkView`), the window (`#sequence`), the public ledger (`.fn-stage` with 8 `.fn-event` and 16 `.fn-branch`), and the matrixes (`#matrixes`, bodies-by-ways and the domain eights).
   - **Transcriptive** has content when `#tList` holds 459 `.turn` elements and the session line contains `459 turns · time not recorded`.
4. When both pass, set the one version field to `6`. The band, masthead and footer read it from that field. An empty shell is never stamped. `design-system.json` is not touched.
5. Run every check in the last section.

## Changes, by tab

Each change states where, now, after, why, and the rubric line it answers. DS is the design-system rubric. Doc is the document rubric.

### Whole file

- **C1 · Script runs (defect 1).**
  - Where: the `#turnsData` block.
  - Now: it holds the illegal escape `\Great`.
  - After: the backslash is escaped as `\\Great`, so the stored text keeps its backslash and parses.
  - Why: no view renders past a thrown parse. `source\transcript.json` is not edited.
  - Rubric: DS interaction, "a page script throws before the modes bind".
- **C2 · Fonts (defect 13).**
  - Where: `<head>`.
  - Now: no `@font-face`.
  - After: Newsreader roman and italic embedded as base64, weight `200 800`, `font-display: swap`, read from `project\fonts\`.
  - Why: the serif travels with the file.
  - Rubric: DS visual clarity, "A single-file document embeds the face".
- **C3 · Title (defect 4).**
  - Where: the document start.
  - Now: `<title>` follows `<body>`.
  - After: `<title>` sits inside `<head>`.
  - Rubric: DS accessibility.
- **C4 · One version field (defect 16).**
  - Where: the band, masthead and footer.
  - Now: markup in two places and a CSS `content` string in the footer.
  - After: one `data-version` value on `<html>`, written into all three by script at load.
  - Rubric: DS comprehensibility, "one source".
- **C5 · Token adherence (defect 11).**
  - Where: every style block, inline style and script colour.
  - Now: hex outside `:root`, fallbacks such as `var(--n1, #ef5a52)`, and token blocks redeclared on the `.fn-matrices` wrapper.
  - After: every colour is a `var(--name)` with no fallback, and the wrapper blocks are removed so the fragments read the document `:root`.
  - Rubric: DS token usage, "Hex outside `:root` is zero".
- **C6 · Type sizes on token (defect 11).**
  - 9.5, 10 and 11px go to 10.5 (`kicker`, `chip`, `legend`).
  - 14.5 goes to 14 (`caption`). 16 goes to 16.5 (`body`).
  - 21 and 22 go to 20 (`subsection`). 34 goes to 36 (`part`).
  - Rubric: DS token usage, "Font sizes are 100% on a named style", and visual clarity, "Nothing on the page is below 10.5px".
- **C7 · Spacing on scale (defect 11).**
  - The spec's snap map applies to every padding, margin and gap: 2 and 3 → 4, 5 → 6, 7 and 9 → 8, 11 to 13 → 14, 15 and 18 → 16, 20 to 34 → 24, 40 to 60 → 48, 84 to 120 → 96.
  - Target: at least 95% on scale, measured.
  - Rubric: DS token usage.
- **C8 · Radii and motion (defect 11).**
  - The 3px radius goes to `radius-chip` 12. The 50% radius goes to `radius-pill` 999px.
  - The `.15s` transition is replaced with `motion-fade` (200ms ease-out).
  - Rubric: DS token usage and interaction, "No other animation".
- **C9 · Palette (defect 17).**
  - Version 6 keeps Version 5's colours, which match spec sections 11.5 and 12. They are declared once, in `:root`, and referenced by name everywhere else.
  - No grammar file is retokened, because the prompt forbids it.
  - The design-system rubric gives its top token score to one palette in `tokens.json`. That needs `tokens.json` to take the section 12 values first, in a system pass of its own. That pass is on *Next*.

### Interactive

**Keep:** Version 4's travelling map, the one window *One path of eight* with Eight pressed at load, the public ledger, Version 4's own matrixes, the domain eights, bodies-by-ways, the inspector, the trail and the hash behaviour.

**Keep the ledger interaction exactly:**

- three role pills: embodied agent, authoritative body, authoritative agent
- authoritative body pressed at load
- the pressed role is the centre line
- eight centre events, the categorical imposition: a click inspects position, categorical name and release, and leaves the pressed role as it is
- sixteen dashed branches, two per position: a click previews position, contingent name and that branch's role archive line; a second click closes it; the pressed role is unchanged
- the role pills are the only control that changes the pressed role
- no placement control
- the release text and archive lines Version 5 stores, unchanged

**Changes:**

- **C10 · Ledger labels follow the pressed role (defect 2).**
  - The role-to-archive pairing is fixed as Version 5 prints it at load:
    - embodied agent: The Night Paramedic
    - authoritative body: The Public Librarian
    - authoritative agent: The Climate Modeler
  - Now: the three line labels, the status kicker and the inspection kicker are fixed strings.
  - After:
    - the centre line label names the pressed role
    - the top and bottom labels name the other two roles in column order
    - each branch's meta line names its own role and that role's archive
    - the status kicker reads `<pressed role> · consolidated`
    - the inspection kicker reads `<pressed role> · Categorical · <archive>`
  - Why: the prompt makes the pressed role the centre line, and a branch shows the archive line of the role it belongs to.
  - Rubric: Doc idea coherence, "An Interactive inspection shows the categorical name or the contingent name the name key prints for that position and that role".
- **C11 · One focal in Interactive (defect 3).**
  - Focal marks the shared reference (`r=bN`) only: the selected node on the travelling map and its current connector.
  - The window's current station takes an ink ring at `stroke-route`.
  - The ledger's centre label takes `ink`. An inspected event or an open branch takes an ink ring at `stroke-route`. `aria-pressed` and `aria-expanded` carry those states.
  - Rubric: DS visual clarity, "One focal mark per view … Interactive: the selected node".
- **C12 · Window shows the whole path (defect 6).**
  - Now: the station row scrolls in a 499px box beside the window inspector.
  - After: the inspector sits below the line, and the line takes the card's full width, so all eight stations show at scale Eight at 1280px. At 640px and below the row scrolls, with the current station scrolled into view.
  - Why: scale 8 is the whole path.
- **C13 · Window facets (defect 7).**
  - Read shows the opening of the station's body passage in Comprehensive (`#body-n`) and opens it.
  - Said reads `+ SAID · n TURNS`, counting the record turns that C18 resolves for that body's passage. It reads `+ SAID · NO LINKED TURNS` when none resolve.
  - Rubric: DS component grammar (Inspector facets) and interaction, "a facet summary that should carry a count is blank".
- **C14 · Dimmed labels (defect 8).**
  - Stations outside the window keep their dotted ring and reduced fill.
  - Their name and body number draw in `ink-3` at full opacity: 4.75:1 on Paper, 6.96:1 on Night.
  - Rubric: DS accessibility, "Dimmed labels fall under 4.5:1".
- **C15 · Matrix and Table behaviour.**
  - Bodies-by-ways rows select and recentre. Each row header's existing text sits in a button. Click or Enter calls the same `setFocus` the map uses and updates the hash. The cells stay as they are: body 1 blank, ways two and three empty.
  - The domain eights table sorts by column header (`aria-sort`). The `#` header restores seat order. A filter field narrows rows. Its rows are seats, not bodies, so a row click does not recentre.
  - Rubric: DS component grammar, Matrix "Row click selects and recentres" and Table "In Interactive it sorts and filters".
- **C16 · Ledger inspector anatomy.**
  - Now: `.fn-insp` fills with `ground`.
  - After: `surface`, matching the Inspector component. Shadow stays `lift`.
- **C17 · Targets (defect 9).**
  - Facet summaries, `Open in Interactive` and Source take `min-height: 24px`, and 44px under `(pointer: coarse)`.

### Illustrative

**Keep:** Version 4's eight figures including the cube, and the added ledger figure (eight plus sixteen, the eight codes, the nine triads) with lanes Disposition, Imposition, Superposition on its three lines. 24-plus-3 and the set of sets stay proposed and undrawn.

**Changes:**

- **C18 · Source resolves (defect 5).** This change serves every tab.
  - Each of the 459 record turns gets an id, `r001` to `r459`, as an attribute. The visible text does not change.
  - A `#turnMap` JSON block maps each 127-log id to the record span that holds its words, built by text match at build time. It holds 124 spans. `t0092`, `t0113` and `t0119` are listed as not located.
  - A Source click opens Transcriptive, opens the session, scrolls to the first mapped turn, and marks the span with `aria-current="true"` and a 2.5px `ink` rule on its left edge.
  - A Source whose ids are all unlocated opens Transcriptive at the top.
  - Rubric: DS comprehensibility, "a mono Source link on each passage resolves to those turns".
- **C19 · Figure index and names (defect 12).**
  - A mono kicker `FIG 1` to `FIG 9` sits above each caption, in document order.
  - Each figure SVG gets `role="img"`, a `<title>` from its caption and a `<desc>` from its first caption sentence. Decorative marks get `aria-hidden`.
  - Rubric: DS visual clarity and accessibility.
- **C20 · One focal in Illustrative (defect 3).**
  - Figure kickers take `ink-3`.
  - Focal marks the route of the current figure only. The current figure is tracked the way the rail tracks the current part. Other figures draw their routes in `ink` at `stroke-route`.
  - The cube's loop draws in the active way's colour, and focal marks only its current corner, as spec section 11.5 states.
- **C21 · Figure Source buttons (defect 10).**
  - They take the `.src` style: `control` border, transparent fill, `ink-2` label, 10.5px.

### Comprehensive

**Keep:** Version 4's prose (22 sections, identical today), *The collective names* under that heading, the corrected 62 key beside it, and the domain eights in their own block after the sum.

**Changes:**

- **C22 · Kickers and section 4 fixes (defects 3, 4).**
  - Kickers:
    - `.kicker` and `.part .kicker` take `ink-3`.
    - The current part's kicker takes focal, tracked by the rail.
    - The *How each body is drawn* number takes an `ink` fill.
  - Status pills:
    - `.status.ok` gets `ink` text and a `role-decide` dot.
    - The status label goes to 10.5px.
  - Cannot-do items:
    - `.cando .no` gets a 1.5px dotted `ink-3` border.
    - Its strike becomes `ink-3`.
  - Forward edge:
    - The `.fwd` top rule becomes 1px solid `line`.
    - Its kicker becomes `ink-3`.
  - Rubric: DS visual clarity, component grammar and accessibility.
- **C23 · Builder language (defect 15).** Two sentences are replaced; the wording is in the editorial plan.

### Descriptive

**Keep:** the nine water passages and *Before the loop*. Nothing further is required.

**Changes:**

- C1 restores the view.
- **C24 · Kicker and reference (defect 14).**
  - The *Before the loop* kicker reads `Before the loop`.
  - Opening or switching to Descriptive with `r=bN` scrolls to body N's passage.
  - Opening or switching to Transcriptive with `r=bN` scrolls to the first turn C18 resolves for body N's passage, or to the top when none resolve.
  - Rubric: DS interaction, "Switching mode scrolls to that passage".

### Transcriptive

**Carried forward unchanged:**

- 459 turns, verbatim
- `VOICE` and `TEXT` kickers, with `CLAUDE · TEXT` on the four turns that print it now
- no speaker name added, no clock time added
- the session line `Session 1 · 459 turns · time not recorded`
- Find
- the session collapsed at load
- Previous and Next disabled, because the record is one part

C18 adds invisible ids and the span mark. It changes no word.

## Where the rubrics and the prompt meet

| Rubric line | Status in this plan |
|---|---|
| DS visual clarity: one focal, 10.5px floor, embedded face, `FIG` index | C2, C6, C11, C19, C20, C22 |
| DS comprehensibility: one version source, Source resolves, no hedges | C4, C18; new strings in the editorial plan |
| DS component grammar: Inspector, Matrix, Table, Status, CanCannot anatomy | C13, C15, C16, C21, C22 |
| DS token usage: zero hex outside `:root`, 100% type, 95% spacing, radii | C5 to C8. One palette in `tokens.json` waits for the system pass on *Next* |
| DS interaction: script runs, facets count, reference scrolls, three motions | C1, C8, C13, C24 |
| DS accessibility: contrast both grounds, targets, figure names, title | C3, C14, C17, C19, C21 |
| Doc structural integrity: each tab's job, stored reference opens its mode | C1, C12, C24 |
| Doc idea coherence: inspection matches the name key for position and role | C10 |
| Doc fidelity: every locked item | carried forward; checked below |
| Doc prose: declarative new strings, transcript untouched | editorial plan |

## Stamp rule

Band, masthead and footer read Version 6 only after the content check passes for Interactive and Transcriptive. One field feeds all three. `design-system.json` never takes Version 6.

## Checks the follow-up runs

Byte checks:

- SHA-256 unchanged for: Version 4, Version 5, the four `v5-parts`, both Version 5 plans, the four grammar files, `project\components\`, `project\fonts\`, `source\transcript.json`, the prompt and both rubrics.

Load:

- Zero script errors on load.
- A fresh load of each `#m=<mode>&r=b5` opens that mode at body 5's passage.

Interactive:

- The travelling map, the window (Eight pressed), the public ledger (8 centre events, 16 branches) and both matrixes are present.
- Ledger, by click, with each of the three roles pressed:
  - the centre label names the pressed role
  - each branch meta names its own role and that role's archive
  - a centre click inspects and leaves the pressed role
  - a branch opens, and closes on a second click, with the pressed role unchanged
  - only the pills change the pressed role
  - no placement control
- All eight stations are visible at scale Eight at 1280px.
- A bodies-by-ways row click recentres and writes the hash.

Transcriptive:

- 459 `.turn` elements, ids `r001` to `r459`.
- The session line contains `459 turns · time not recorded`.
- Exactly four `CLAUDE · TEXT` kickers.
- The turn text is identical to Version 5's, compared turn by turn.

Source links:

- Every Source id resolves to a record span or is listed as not located. Exactly three are listed: `t0092`, `t0113`, `t0119`.

Descriptive:

- Nine body passages in body order plus *Before the loop*.
- No `NaN` anywhere in the rendered text.

Comprehensive and locked names:

- The 22 Version 4 sections are identical to Version 4.
- The sum line `8 codes + 27 ledger names + 27 bodies = 62` is the same sentence in the name frame and the name key.
- Body 1 is blank on the codes and on bodies-by-ways, and ways two and three are empty there.
- Liken is on the categorical domain eight, and Analogy is on the ledger categorical eight.
- The words *public ledger* are present.
- *The collective names* is present.
- No rendered text contains "Version 4 already gives".

Figures, focal and type:

- `FIG 1` to `FIG 9` are present, and every figure SVG has a `<title>` and `<desc>`.
- Exactly one focal element per mode view, the focus ring aside, counted by script on Paper and Night.
- The computed body font is Newsreader, with the embedded face loaded.

Tokens, contrast and targets:

- Zero hex outside `:root` and the base64 font data.
- Font sizes 100% on a named style.
- Spacing at least 95% on scale.
- Only the three motion tokens.
- Text 4.5:1 and control borders 3:1, scanned element by element on Paper and Night, all five tabs.
- Every control at least 24px, and 44px under a coarse pointer.

Stamp:

- Band, masthead and footer read Version 6 from one field.

## Next

- A system pass that brings `project\tokens.json` and `project\README.md` onto spec section 12 (role, way and bit hues; `sub` and `lede` 19px; `pill` 12.5px), so one palette has one source.
- Restamp a PDF from the Version 6 HTML.
- Fill further `from` ids only where a passage comes from a turn.
