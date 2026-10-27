# The Nine Bodies of Authority · Version 4 editorial plan

Locked 26 October 2026 from [General chat](8c6d8415-4eda-4658-b176-8c1afb2b5356) (Perth). This file is the change list for the next rebuild. It does not rebuild the HTML.

Each row names the file, the current value, the next value, and why. Authored claims in the Expanded edition do not move. Version 3 HTML interaction stays only where it does not contradict Expanded.

## 1. Edition

| File | Current | Next | Why |
|---|---|---|---|
| Band, footer, masthead, PDF | Mixed: Three Ways print says 2; HTML footer says 3; Field Notation README audit says “version 5 draft” | One field, `version: "4"`, feeds all four | 2 is the print argument. 3 is the interactive prototype. 5 is what you stamp after the remaining tests close. The README’s “version 5 draft” is an audit snapshot of the system, not an edition of the document. Jumping to 5 now skips 4 and mixes those histories. |
| Spec data-model example in [spec/Field Notation v2 spec for Claude Code TIDIED.md](../spec/Field%20Notation%20v2%20spec%20for%20Claude%20Code%20TIDIED.md) §6 | `"version": "3"` | `"version": "4"` | The chat locked Expanded as the words of Version 4. The example in the spec is stale. |
| [project/design-system.json](../project/design-system.json) | `lastChange` is the v1 audit against a “v5 draft” document | Tokens and rules staged; Nine Bodies rebuild has not started | This pass stages the system. It does not ship the document. |

**Version 5 waits for:** cannot-do lists, remits, conflicting approvals, further recourse, blind raters, ways two and three, top-row regime names.

## 2. Words that do not move

Canonical words: `<home>\Downloads\The_Nine_Bodies_of_Authority_Expanded.pdf` (30 pages, 26 Oct). It keeps the 16-page core and adds the cube, six cycles, collective names, and the audit.

| Claim | Current in the stack | Next | Why |
|---|---|---|---|
| Body 5 account | Expanded and HTML: **Preservational**. 16-page visual: Environmental | Preservational | Environmental is freed to name code `010`. The visual is stale on this one name. Do not copy it forward. |
| Body 9 acting | **Cultural** | Cultural | Locked in Expanded. |
| Collective names | Sit on **codes**, not bodies | Codes | A body can move; a code does not. |
| Loop 1 assignment | `101, 111, 011, 010, 110, 100, 000, 001` | Unchanged | Only fully baseline-compatible assignment. The early cube draft both claimed Loop 1 was fully checked and later said rows 4–9 were untested. Expanded follows the full Loop 1 confirmation. |
| Six Hamiltonian cycles | Verified as geometry | Geometry only | Geometry does not prove social fit. Do not write that it does. |
| Pulse | A traversal | Traversal, not a ruler | Not a political office. |
| Governmental dominance vs eight-corner reciprocity | Separated in Expanded | Keep the split | They are different cycles. |
| Open work named in Expanded | Influence reference, equality, uncertainty, cross-loop name strain (especially **Reproducible**), no meta-transition rule yet | Leave open, under **Next** | Unfinished items do not become hedges in the prose. |
| Authored prose | Expanded | Unchanged | The spec’s “do not change the authored words” now means Expanded, not the HTML. HTML prose is not the book. |
| Version 3 HTML interaction | Compass, span, way pills, inspector, trail, three-mode bar | Keep the behaviour where it does not contradict Expanded | The HTML is ahead as a product and behind as an edition. |

The fourteen expansion pages (atlas, transitions, mappings, water-under-cube, audit) go into **Visual** and **Network**, not as a second competing book.

## 3. Token deltas

Source of the old set: Claude scratch Field Notation `tokens.json` (system version 2). Staged next set: [project/tokens.json](../project/tokens.json). Font files are listed, not embedded, until the font step.

| Token | File | Current | Next | Why |
|---|---|---|---|---|
| `focal` Night | tokens.json | `#e0675a` | `#ffb4a6` | Night focal had a 1.0:1 contrast ratio with `node-1`. New value is about 2:1 against node-1 and 11:1 on ground. Focal is never colour alone. |
| `focal` Paper | tokens.json | `#b5452b` | Unchanged | Still distinguishable on Paper. |
| `on-node` (new) | tokens.json | Missing. HTML hard-codes `#15141a` | `#15141a` on Paper and Night | Ink on Night fails on node fills (1.7 to 3.5:1). Near-black numerals give 4.3 to 9.5:1 across all eight. |
| `control` (new) | tokens.json | Missing. Pills use `rule` (1.6:1 Paper, 1.8:1 Night) | `#6c6870` Paper, `#9a9c95` Night | 4.75:1 and 6.96:1. A control border has to reach 3:1. |
| `banner` Night | tokens.json | `#000000` against ground `#0d0e10` (1.09:1) | Value unchanged; draw a 1px `rule` under the band | The token is fine. The band needs a line so it reads as a band. |
| `node-1` … `node-8` usage | tokens.json | Outline only called out for node-3 and node-5 | Every fill gets `stroke-node` 1.6px ink. Colour names a **corner**, not a sequence | Nodes 1, 2 and 4 are also under 3:1 on Paper (2.9, 2.2, 2.3). On ways two and three, colour-as-order is a lie. |
| `focal` usage | tokens.json | “One thing per sheet” | Current position, one at a time per view. No focal text on `sunk` (4.38:1 Paper). Draw at `stroke-route` | The document used focal on every part kicker, plus-markers, rings, and the route. If two things are focal, neither is. |
| `role-*` usage | tokens.json | Dots, rings, chips | Unchanged, and never text. `.status.ok` currently sets text in `role-decide` (4.27:1) | Colour is not the sentence. |
| `rule` usage | tokens.json | “pill and control borders” | Section rules and hairline structure only | Control borders moved to `control`. |
| Serif stack | tokens.json | `"Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif` | `"Newsreader", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif` | Iowan is not on Windows. Palatino Linotype has no true 650. Newsreader variable 200–800 makes 650 a real weight. Files land in `project/fonts/` at the font step. |
| `type.fonts[]` | tokens.json | `[]` | Newsreader roman and italic listed, not embedded | Listing now; shipping files and base64 embed is the next build. |
| card-title | tokens.json | Missing | Serif 18px / 1.25 / 650 | Step, glance and stat card titles already exist in the document. |
| caption | tokens.json | Missing (`note` is 14/1.5/400 ink, not ink-2) | Serif 14px / 1.5 / 400, ink-2 | Figure captions, notes, card values. |
| annotation | tokens.json | Missing | Serif 13px / 1.4 / 400, ink-2 | Smallest serif. SVG sublabels. Floor is 10.5px; this stays above it. |
| numeral | tokens.json | Missing | Mono 26px / 1 / 700 | Bit digits and large codes. |
| chip | tokens.json | Missing | Mono 10.5px / 1.3 / 700 / 0.08em | Chips, table heads, status pills, rail headings. |
| Existing type styles | tokens.json | display 56, part 36, section 30, subsection 20, sub 19.5, lede 18.5, body 16.5, node 15, note 14, kicker 10.5, code 12.5, legend 10.5, pill 12, relation 11.5 | Keep all of them in the token file | Spec: add styles, delete nothing. Document CSS snaps separately (see §5). |
| `space-tight` (new) | tokens.json | Missing; document uses 6 | 6px | Gaps between pills and chips. Only 29% of document spacing sat on the old scale. |
| `space-ctl` (new) | tokens.json | Missing; document uses 10 | 10px | Grid gaps, control padding. |
| `space-card` (new) | tokens.json | Missing; document uses 16 | 16px | Figure and card padding. |
| Existing space | tokens.json | 4 / 8 / 14 / 24 / 48 / 96 | Unchanged | The scale grows; it does not reset. |
| `stroke-node` (new) | tokens.json | Missing; document already outlines nodes | 1.6px ink | Universal node outline. |
| `target-min` (new) | tokens.json | Missing. Fold ~23px, trail chips ~20px | 24px | WCAG 2.2 floor. |
| `target-touch` (new) | tokens.json | Missing. Pills ~28px, tabs ~30px | 44px under `(pointer: coarse)` | Touch screens. |
| `motion-dash` | tokens.json | In prose only, 6s | `6s linear infinite` | Make the existing travel a token. |
| `motion-glide` (new) | tokens.json | Missing | `400ms cubic-bezier(.4,0,.2,1)` | Compass recentring. |
| `motion-fade` (new) | tokens.json | Missing | `200ms ease-out` | Step lighting. No other animation. All three stop under `prefers-reduced-motion`. |

Document CSS snaps at rebuild, not in this token file:

| Current in HTML | Next | Why |
|---|---|---|
| 9.5px, 10px | 10.5px | Nothing below the floor. |
| `.sub` 19.5, `.lede` 18.5 | 19px (lede) | Two near-values, one style. |
| `figcaption` 14.5 | 14px | Caption token. |
| `.reader dd` 16 | 16.5px | Body token. |
| Sans 12 / 13 | 12.5px | One control size. |
| Fold/open 11 | 11.5px | Relation token. |
| Section 26 / part 30 at mobile | Keep as documented steps at 640px and below | Responsive, not drift. |
| Spacing 2, 3 → 4; 5 → 6; 7, 9 → 8; 11, 12, 13 → 14; 15, 18 → 16; 20, 22, 26, 28, 30, 34 → 24; 40, 52, 56, 60 → 48; 84, 90, 120 → 96 | Snap | Section top padding 56 becomes 48. Part top margin 84 becomes 96. Main bottom padding 120 becomes 96. |

## 4. Rule deltas

Staged in [project/README.md](../project/README.md).

| Rule | Current | Next | Why |
|---|---|---|---|
| Voice | “No hedges, no may, might, arguably” | No epistemic hedges: might, arguably, perhaps, seems. **May** is allowed only as permission (“May this proceed?”). Recorded is exempt because it is verbatim | The model’s central question uses may as permission. A blanket ban contradicts the document. |
| Focal | One thing per sheet | Current position, one at a time per view. Written/Scripted: current part kicker; Scripted also the current sentence. Visual: the route or the return arrow. Network: the selected node or current step. Keyboard focus ring is exempt | The document broke “one thing per sheet” on every kicker. The rail already tracks the current part. |
| Line grammar · cannot-do | Dashed (computed) | Dotted (`stroke-held`, `ink-3`) | Cannot-do items are held powers, unexercised. Dashes are computed or contingent only. Dividers are never dashed. |
| View modes | “Three view modes, always”: Prose, Visual, Network | “Five view modes, always”: Network, Visual, Written, Scripted, Recorded. Prose is renamed Written | Chat locked five modes and the five words. |
| Accessibility | Text 4.5:1; colour never the only signal | Plus: control borders 3:1 (`control`); targets `target-min` / `target-touch`; tabs use the full tab pattern | The old README did not cover controls, targets, or tabs. |
| Audit table | Rows 3, 4, 6, 7 “rule added” | Those four **Closed**. Rows 1, 2, 5, 8 stay **Next** | Tokens and rules now carry the closed findings. Previews, webfont, extra components, Night band line, and wrapping pills are not done. |
| Document under audit | “v5 draft” | Version 4 edition, Expanded as words | Same mix of histories as §1. |

Rows still open after this pass:

1. `components/bundle.js` missing — previews blank.
2. No serif webfont file.
5. Chip, Table, Spine, CanCannot, Status, Fold, Trail, Rail, Matrix, CrossRef not in the system.
8. Night banner still needs the 1px rule in CSS; “Way three” still wraps until `nowrap` and the 1100px relabel land in the document.

## 5. Document fixes (HTML, not this pass)

File: `<home>\Downloads\The_Nine_Bodies_of_Authority.html`. Apply at rebuild.

| Where | Current | Next | Why |
|---|---|---|---|
| `.part .kicker` | All kickers `focal` | `ink-3`; only the current part’s kicker is focal | One focal per view. The rail already tracks it. |
| `.netinsp summary::before` | Focal + / − | `ink-3` | Markers are structure, not the current position. |
| `.step .fwd .kicker` | Focal | `ink-3` | Same. |
| `.step .fwd` top border | Dashed | `1px solid line` | Dividers are never dashed. |
| `.cando .no` | Dashed / focal strike | `1.5px dotted ink-3`; strike `ink-3` | Held power, not computed. |
| `.status.ok` | Text in `role-decide` | Text `ink`; border and dot `role-decide` | Roles are never text colour. |
| Node numerals | Hard-coded `#15141a` | `on-node` | One token, both grounds. |
| Pills, tabs, tools, fold, travel, links, bits, status | Border `rule` | Border `control` | 3:1 floor. |
| Fold / trail chips | ~23px / ~20px | Fold padding `8px 11px`; trail `7px 9px` (≥24px) | `target-min`. |
| Coarse pointer | No 44px floor | `min-height: 44px` on those controls | `target-touch`. |
| Pills | “Way three” wraps | `white-space: nowrap`; under 1100px labels One, Two, Three | Audit row 8. |
| `.nn:focus{outline:none}` | Hides keyboard focus | Remove. `.nn:focus-visible` gets a 2px focal ring at radius + 6 | Keyboard is exempt from the one-focal rule, not from a visible ring. |
| SVGs | Three lack `role="img"` | `role="group"` + `aria-label`; each figure SVG gets `<title>` and `<desc>` | Colour is never the only signal. |
| `<html>` | No `lang`; `<title>` outside `<head>` | `lang="en-AU"`; title in head | Australian spelling. Valid document. |
| Version strings | 2 / 3 / 5 | One `version` from the data source: **4** | §1. |
| Fourteen expansion pages | Not in the HTML | Visual and Network | Expanded is the book. HTML is not a second book. |
| 16-page visual name | Body 5 account Environmental | Preservational | §2. |

## 6. Five modes

Tab order left to right: **Network, Visual, Written, Scripted, Recorded**. Network opens first. Recorded is public in Paper and Night. No privacy flag.

Making order, the other way:

| Word | Mode | Answers | Voice |
|---|---|---|---|
| transcription | Recorded | What was said | Exempt. Verbatim. |
| transliteration | Scripted | What was meant | Full rule. Clean speech for the ear. |
| translation | Written | What was claimed | Full rule. Was Prose. |
| transformation | Visual | What was represented | Full rule on labels. |
| transposition | Network | What was associated, synthesised, architected | Full rule. |

Shared, all five:

- Full tab pattern: `tablist` / `tab` / `aria-selected` / `aria-controls` / `tabpanel`. Arrows, Home, End, roving tabindex.
- Sticky bar under the band, and again at the bottom. Below 640px the bar scrolls; labels stay in full.
- Previous / Next by part in Recorded, Scripted, Written, Visual; by node in Network.
- One reference (part or node) in the URL hash, for example `#m=scripted&r=b3`. Trail persists.
- Every part folds. Collapse-parts folds them all.
- Scripted, Written, Visual passages carry `from` ids into Recorded. A mono Source link jumps.

Recorded uses [source/transcript.json](../source/transcript.json). See [source/CONVERSION.md](../source/CONVERSION.md). Kickers are `PERCY · VOICE` / `CLAUDE · TEXT`. `at` is null until a timed log exists; do not invent times. Flagged turns ship visible. The log is not clean until that pass.

Scripted: segments ≤60 words; codes spelled digit by digit; Listen / Pause / 1× 1.25× 1.5×; current sentence underlined in focal at 2.5px with a 4px offset, no fill. Emit `scripted.txt`. Browser speech when no audio file is present.

Network keeps span, direction, compass, recentring, trail. Inspector facets: Said, Heard, Read, Seen. Add Table, Matrix, CrossRef. Motion is only the three tokens.

## 7. Components still missing

Each needs `components/<Name>/README.md` and `preview.html` with line 1 `<!-- @dsCard group="..." height=N -->`. Not this pass.

| Component | Current | Next | Why |
|---|---|---|---|
| `bundle.js` / `bundle.css` | Missing. Previews blank | Classic script, `window.FieldNotation`, no imports, no network. Compass, NodeRoute, Inspector, Toggle, ViewTabs. Inspector `@dsCard` height ~320 | Audit row 1. The system looks broken when it is not. |
| ViewTabs | Three modes | Five modes, full tab pattern | §6. |
| Transcript | Missing | Turn, kicker, session fold, Find | Recorded. |
| Script | Missing | Segment, Listen, speed, current-sentence underline | Scripted. |
| Chip | In the document, not in the system | Mono 10.5px, 9px dot, 6px gap | Roles as dots, never text. |
| Table | In the document | Surface, 1px `line`, radius 14, ink header, cells 10×14 | Network and Visual. |
| Spine | Water-map in the document | 38px numbered circle, 1.5px ink line, card radius 14 | Expansion pages. |
| CanCannot | In the document, dashed “no” | Yes solid ink; no dotted `ink-3` | Held vs computed. |
| Status | Text in `role-decide` | Pill, chip style; ok = `role-decide` dot + ink text | §5. |
| Fold, Trail, Rail | In the document | System components | Audit row 5. |
| Matrix, CrossRef | Missing | Sortable/filterable; row click recentres; chips are code + label | Network. |
| Newsreader files | Missing | `project/fonts/`, then base64 in the single-file HTML | Audit row 2. |

## 8. Acceptance checks (next build)

From spec §10. This pass does not run them. The rebuild fails if any fail.

1. Contrast: every text pair ≥4.5:1, every control border ≥3:1, both grounds, by script.
2. Token adherence: spacing ≥95% on scale, font sizes 100% on token, radii on token, zero hard-coded hex outside `:root`.
3. Focal: exactly one focal element per mode view, other than the focus ring, by script.
4. Keyboard: five tabs by arrow, inspector open/close, visible focus ring on every network node.
5. Link integrity: every `from`, `refs`, and Source link resolves. The reference carries across all five.
6. One version string: **4**, in band, footer, masthead, PDF.
7. Reduced motion: all animation and smooth scroll stop.
8. Authored words of Expanded unchanged. Diff the prose before and after. HTML interaction copy may stay only where it does not contradict.

## 9. Ordered next build

This pass stops after staging. The next build, in this order:

1. Fonts: add Newsreader files under `project/fonts/` and confirm `type.fonts[]`.
2. Components: `bundle.js`, `bundle.css`, the components in §7, previews.
3. One JSON source: Expanded words + [source/transcript.json](../source/transcript.json). `meta.version` is `"4"`. Passages point `from` the Recorded turns. Do not merge `<home>\Downloads\nine-bodies-transcript.json`.
4. Rebuild the Nine Bodies HTML: five modes, §5 fixes, fourteen expansion pages in Visual and Network, interaction from Version 3 HTML where it does not contradict Expanded.
5. Write `lastChange` in [project/design-system.json](../project/design-system.json) last. Keep every other key.

Do not start step 4 before 1–3. Do not stamp 5. Do not rewrite Expanded.
