# Field Notation

A quiet, typographic system for thinking on paper: flowcharts, concept maps, master blueprints and interactive documents. Two grounds (Paper, Night), three type voices (serif for meaning, mono for structure, sans for controls), one `focal` colour, and a line grammar where the style of each line carries meaning: solid is settled, dashed is computed or contingent, dotted is held.

Use it for any original framework, argument or model that needs structure you can see: claim chains, triads, loops, category systems and routes through a set of nodes.

Reference document: *The Nine Bodies of Authority* (Version 4). Canonical words: the 30-page Expanded edition. The README line that once said “version 5 draft” was an audit label, not an edition.

## Voice

- **Declarative.** State what holds. No epistemic hedges: might, arguably, perhaps, seems. May is allowed only as permission, as in “May this proceed?” If something is unfinished, it goes on a list headed *Next*, not into a qualifier.
- **Specific.** Name things in the author’s own terms, exactly as written. Coined words are never “corrected”.
- **Short.** Node labels are four words at most. Every connector carries a verb (“authorises”, “returns”, “accounts for”), or it is cut.
- **Transcriptive is exempt.** Transcriptive is verbatim. Fillers, misspellings and hedges stay.

## Mode inflections

Five modes, tab order left to right. Interactive opens first. It is the live space, not an output. The four outputs are illustrative, comprehensive, descriptive, and transcriptive.

Seven forms only. No `-al` forms. Agent nouns take `-er`. Descriptive's adverb is `descriptively`. Transcriptive's adverb is `transcriptively`.

| Mode | -ive | Verb | -able | Agent -er | -ion | -ing | -ly |
|---|---|---|---|---|---|---|---|
| Interactive | interactive | interact | interactable | interacter | interaction | interacting | interactively |
| Illustrative | illustrative | illustrate | illustratable | illustrater | illustration | illustrating | illustratively |
| Comprehensive | comprehensive | comprehend | comprehendable | comprehender | comprehension | comprehending | comprehensively |
| Descriptive | descriptive | describe | describable | describer | description | describing | descriptively |
| Transcriptive | transcriptive | transcribe | transcribable | transcriber | transcription | transcribing | transcriptively |

Comprehensive splits its stem. `comprehensive`, `comprehension`, and `comprehensively` use comprehens-. `comprehend`, `comprehendable`, `comprehender`, and `comprehending` use comprehend-. That split stays.

Retired as labels: haptic, visual, written, spoken, scripted, recorded, network, scriptive, narrative, documentative.

## Foundations

**Two grounds.** *Paper* (`ground` #f3efe4) is the default for drafting and reading. *Night* (`ground` #0d0e10) is the same system inverted, for presenting and for public-facing sheets. Type, spacing, radii and line grammar never change between them. Only the tokens swap. On Night, draw a 1px `rule` under the banner.

**Three type voices.**

- **Serif** (`--font-serif`) carries meaning: titles at weight 650, prose at 400, and node text. Stack: `"Newsreader", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif`. Newsreader files are listed in `type.fonts[]` and ship in `project/fonts/` at the font step.
- **Mono** (`--font-mono`) carries structure: kickers, codes, routes, legends and step counters. It is set in uppercase with wide tracking. Nothing below 10.5px.
- **Sans** (`--font-sans`) carries controls: pills, buttons and connector verbs.

**One focal colour.** `focal` marks the current position, one at a time per view. Comprehensive and Descriptive: the current part’s kicker. Illustrative: the route being read or the return arrow. Interactive: the selected node or current step. The keyboard focus ring is exempt. If two things are focal, neither is. Draw focal at `stroke-route`. No focal text on `sunk`.

**Lines over boxes.** Hierarchy comes from type and hairlines. Nodes, control groups and content panels (figures, tables, cards) get a border and a radius. Only the inspector gets a shadow.

## Line grammar

| Line | Meaning |
| --- | --- |
| Solid | Settled, selected, travelled |
| Dashed | Computed, contingent, needs work, or uncertain (mark the label [?]) |
| Dotted | Held, unexplored, a possible path not taken, or a cannot-do (held power, unexercised) |

Colour never carries one of these meanings on its own. Dividers are never dashed. Cannot-do items use dotted `ink-3`, not dashed.

## Colour sets

- **Neutrals:** `ink`, `ink-2` and `ink-3` for text, `line` and `rule` for structure, `control` for pill, tab and button borders, `surface` and `sunk` for panels and wells.
- **Three roles** (`role-act`, `role-decide`, `role-record`): for any triad of distinct positions. They appear as dots, rings and chips, never as text.
- **Eight nodes** (`node-1` … `node-8`, red through pink): for any set of eight. They always appear in this order as fills. Colour identifies the **code at a corner**, not a sequence. Every fill gets a 1.6px ink outline (`stroke-node`). Numerals and labels on fills use `on-node`, not `ink`.

## Forms

Choose the form by what matters most in the source:

| What matters | Form | Shape |
| --- | --- | --- |
| Order | **Flowchart** | Nodes on one axis, verb-labelled connectors, focal path through it |
| Relationships | **Concept map** | Nodes placed by affinity, connectors labelled, clusters in bands |
| The whole architecture | **Master blueprint** | Numbered bands (3–5), each a titled section of triads, grids or loops |

Every sheet is landscape, grid-aligned and generous with whitespace. Each one has a footer reading *title · version · date · legend*. A sheet holds at most about 12 nodes per section; beyond that, start a second sheet.

## Interaction

Interactive versions add these behaviours and nothing else:

1. **Toggle groups.** A kicker over a row of pills, with one pressed. The pressed pill fills with `ink` (and with `ground` text on Night). Pills are `white-space: nowrap`.
2. **Node travel.** Step through a route of up to eight nodes. Each step lights the next node and connector in `focal`, and a mono counter reads `STEP 3 OF 8`. The route’s code sequence sits under the diagram.
3. **Inspector.** Clicking a node opens a `surface` panel. It shows a kicker, a serif title, a short definition and a grid of facts in label-and-value pairs, with a Close pill.
4. **Five view modes, always.** Every document has five tabs, left to right: **Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive**. Interactive is the default tab on open. The tab bar sits at the top, sticky under the notice band, and again at the bottom. The bottom bar also has Previous and Next page buttons, which step by part in Transcriptive, Descriptive, Comprehensive and Illustrative and by node in Interactive. Tabs use the full tab pattern: `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, and a `role="tabpanel"` per mode.
5. **Span and direction.** Interactive controls choose the span (all eight nodes, the selected node with the one before and after, or the selected node alone) and the direction. Horizontal travels along a route; vertical travels across parallel routes at the same position.
6. **Compass and recentring.** The core node sits at the centre and defines the eight around it, with dotted spokes to each. Selecting a node previews it, and recentring makes it the new reference, so the ring re-forms around it. The reference carries across modes: switching mode scrolls straight to that node’s passage. A trail of past references sits under the map. Store the reference in the URL hash.
7. **Collapse and expand.** Every part folds to its kicker and title, and a Collapse parts tool folds them all. Inspector sections are collapsible, each with a mono summary prefixed + or −.

Making order, the other way from the tab bar: Transcriptive (what was said), Descriptive (what the case enacts), Comprehensive (what was written), Illustrative (what was drawn), Interactive (where the four meet). Transcriptive is public in every build, Paper and Night. No privacy flag. There is no narrative mode and no voiceover file.

Motion is only `motion-dash` (6s), `motion-glide` (400ms), `motion-fade` (200ms). Everything stops under `prefers-reduced-motion`.

## Components

- **Masthead:** kicker, display title, lede and a notice band.
- **Toggle:** a labelled pill group.
- **NodeRoute:** eight nodes with step-through travel.
- **Inspector:** the node detail panel.
- **ViewTabs:** the Interactive, Illustrative, Comprehensive, Descriptive and Transcriptive tabs, with page navigation.
- **Compass:** a core node with eight around it, which you can recentre.

`components/bundle.js` and `bundle.css` cover Compass, NodeRoute, Inspector, Toggle and ViewTabs. Previews also exist for Chip, Table, Spine, CanCannot, Status, Fold, Trail, Rail, Transcript, Script, Matrix and CrossRef.

## Accessibility

- Text meets 4.5:1 on its ground in both themes. `ink-3` is the floor. Keep `ink-3` off `sunk`.
- Role and node colours are never the only signal. Every node carries its label or code in `on-node`.
- Control borders use `control` and meet 3:1.
- Targets are at least `target-min` (24px), and `target-touch` (44px) on coarse pointers.
- Tabs follow the full tab pattern. Interactive nodes show a visible `:focus-visible` ring.

## Audit · 2026-10-26

Reviewed against *The Nine Bodies of Authority* (Version 4, Expanded edition). The system fits the model closely: nine bodies are the Compass (a core and eight), act, authorise and account are the three roles, and the three positionings are a three-pill Toggle. The line grammar gives held, unexercised powers their own mark.

| # | Finding | Status |
| --- | --- | --- |
| 1 | Component previews were blank: `components/bundle.js` was missing. | Closed: `components/bundle.js` and `bundle.css` assign `window.FieldNotation` |
| 2 | Serif specimens rendered as a sans on Windows. | Closed: Newsreader variable files are in `project/fonts/` and embedded in the Version 4 HTML |
| 3 | `focal` (Night) was close to `node-1`, so a focal route over coloured segments could lose its focus. | Closed: Night focal is `#ffb4a6`; draw at `stroke-route`; never colour alone |
| 4 | The document borders figures, tables and cards; the old rule allowed borders only on nodes and controls. | Closed: rule widened to panels |
| 5 | The document uses patterns that were not listed: role chip, table, spine, can/cannot grid, status pill, trail, contents rail, fold. | Closed: Chip, Table, Spine, CanCannot, Status, Fold, Trail, Rail, Transcript, Script, Matrix and CrossRef each have a preview |
| 6 | Values in the document were missing as tokens: strokes 1.2 and 1.6, radius 14, part title 36. | Closed: added, plus `stroke-node`, spacing 6/10/16, type card-title/caption/annotation/numeral/chip |
| 7 | `ink-3` on `sunk` and pale node fills fall under contrast floors on Paper. | Closed: `ink-3` off `sunk`; every node fill has an ink outline; numerals use `on-node` |
| 8 | Night `banner` barely separates from `ground`. Toggle pill “Way three” wraps. | Closed in the Version 4 HTML: 1px `rule` under the Night band; pills use `nowrap`; under 1100px the way pills read One, Two, Three |

## Next

- Newsreader has no arrow glyphs. `→` and `←` fall through to the next face in a stack that includes them. Mono already draws the arrows in the UI.

## Done this pass (recorded links · flagged dispositions · V4 restamp)

- Sentence/passage-level `from` ids filled in `data/nine-bodies.json` for Comprehensive (77), Descriptive (water), and Illustrative (v09). Source controls jump only to ids present in the 127-turn Untitled 15 log.
- Flagged-turn dispositions are explicit in `source/FLAGGED_DISPOSITION.md` and on each turn (`disposition` / `disposition_note`). Overlaps without timed audio stay marked; separable chrome was trimmed; one noise-only turn held.
- Band, masthead, footer, and `@media print` (PDF Version 4) all read Version 4 with Expanded as the words source. Do not stamp 5.
