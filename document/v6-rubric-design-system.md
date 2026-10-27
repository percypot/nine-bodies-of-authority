# Rubric for the Field Notation design system

Instrument for the Field Notation design system and for any Claude Code implementation of it. Version 4 is the grammar baseline. Version 5 (`document/The_Nine_Bodies_of_Authority_v5.html`) is the current draft. This file records no score for Version 5 and no score for Version 6.

Give each dimension one score from 0 to 4. Report the six scores side by side. Leave them uncombined. A strong score on one dimension leaves the others as they are.

The companion instrument `document/v6-rubric-document.md` scores a five-tab document’s ideas and locked names. This file scores the design system those tabs are built in. A build can pass here and fail there, and the reverse. Do not copy a score across.

## Baseline

Version 4 is the grammar baseline. Read these files and score against them:

- `spec/Field_Notation_v4_spec.md`
- `project/tokens.json`
- `project/design-system.json`
- `project/README.md`
- `document/The_Nine_Bodies_of_Authority_v4.html`

`document/The_Nine_Bodies_of_Authority_v4.html` is the reference rendering of that grammar. It is not a second spec, and this rubric does not grade it.

Version 5 is the current draft to name when a review says which file was opened: `document/The_Nine_Bodies_of_Authority_v5.html`, *The Nine Bodies of Authority*. Naming the draft is not a score. Version 6 is outside this file. Leave both rows blank in the score record.

If a sentence in this rubric and a baseline file disagree on a fact of the grammar, the baseline file wins. The instruction to leave Version 5 and Version 6 unscored stays in force either way.

### What owns a rule

| Concern | Owner |
|---|---|
| Mode names, the seven inflections, voice, line grammar, focal, interaction, component jobs, accessibility floors | `spec/Field_Notation_v4_spec.md`, and `project/README.md` where it copies those rules. The five mode definitions at the top of the spec win over a later sentence. |
| Token names and values | `project/tokens.json` |
| System identity | `project/design-system.json` (`title` Field Notation, `namespace` FieldNotation). `"v": 3` is the file format. |
| A travelling document | The Version 4 HTML, as a rendering of the rules above |

Mode names, in tab order, Interactive first: Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive. Retired as mode labels: haptic, visual, written, spoken, scripted, recorded, network, scriptive, narrative, documentative.

### Two artifact classes

Name the artifact before scoring.

1. **System.** Token file, design guide, `design-system.json`, component previews, and the bundle. A preview that does not run cannot support a 4 on interaction.
2. **Document build.** A Claude Code rebuild of the Nine Bodies HTML, or a later document built in this system. It includes every surface sections 5 and 7 of the spec require.

Score the controls the artifact ships. A cube, a compass, or a transcript Find field that is present follows the rules below. A control a later document plan removes is absent from this score; the document rubric scores it if that plan required it. The five modes, one focal mark, the line grammar, the token rules, and the accessibility floors stay in force for both classes.

### Where a miss belongs

Record a miss under the dimension that owns the rule. Name the other dimension in the note when the same miss is visible there. Lower both only when both rules fail.

| If you see this | Score it under |
|---|---|
| A second focal, a dashed divider, type voices mixed, a sheet too dense to read | Visual clarity |
| A renamed mode, a hedge in governed prose, a broken citation, a wrong version string, edited transcript | Comprehensibility |
| A part whose anatomy or states differ from the named component | Component grammar consistency |
| A hex, size, space, radius, stroke, or motion value outside the token file | Token usage |
| A control that moves the wrong thing, drops the shared reference, or adds behavior the grammar does not name | Interaction design |
| Contrast, target size, names, keyboard reach, or reduced motion failing | Accessibility |

Arrow keys that do not move the tabs fail interaction. A tab strip with no tab roles fails accessibility. Motion that continues under `prefers-reduced-motion` fails both: interaction, because the motion is outside the three tokens’ stop rule, and accessibility, because the preference is ignored.

### Baseline tensions

These are disagreements inside the baseline. Apply the owner table. Do not resolve them by grading Version 4, Version 5, or Version 6.

- **Role, way, and bit hues.** Spec sections 11.5 and 12 record one hue per position: Paper `#c8741e` `#3c9447` `#4479c9`, Night `#e8a36a` `#9ad84a` `#5ccfe6`, with `way-*` aliasing the role tokens. `project/tokens.json` still holds the earlier role pairs and the earlier way pairs (`way-1` `#e0b400` / `#f0d35a`, `way-2` `#2f8f4e` / `#6fb08f`, `way-3` `#3a5fbf` / `#8fa0e6`). Token usage follows `tokens.json` until that file is the one that changes. A top token score is one palette, referenced by name. Two palettes at once fail token usage. This rubric does not award the score for either palette by itself.
- **Type snap.** Spec section 2 snaps `.sub` and `.lede` to 19px and sans controls of 12px and 13px to 12.5px. `tokens.json` still has `sub` 19.5px, `lede` 18.5px, and `pill` 12px. Token usage follows the token file until that file changes.
- **Fold and trail padding.** Spec section 4 names fold padding `8px 11px` and trail chips `7px 9px`. Spec section 2 snaps 11, 12, and 13 to 14, and 7 and 9 to 8. Token usage follows the spacing scale. Component grammar and accessibility follow the height: at least `target-min` (24px), and `target-touch` (44px) on a coarse pointer.
- **Three different version fields.** `tokens.json` `"version": 2` is the token file. `design-system.json` `"v": 3` is the file format. The reader-facing edition on the Version 4 baseline is the string `4`, from one source, in the band, the footer, the masthead, and the PDF. The three numbers stay distinct.

## 1. Visual clarity

Whether hierarchy, the current position, and the meaning of a line are visible on the grounds the system names.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | One focal, the line grammar, the three type voices, and both grounds read correctly on a representative view. |
| 3 | One or two local slips, such as a tight gap or a caption, and none of them adds a second focal or changes what a line means. |
| 2 | Hierarchy, focal, or line style is ambiguous in more than one region. The reader hesitates. |
| 1 | Colour, boxes, or extra chrome carry meanings that type and line style are there to carry. |
| 0 | Grounds, type voices, or line styles are improvised per section. |

### Top score

A 4 can be read at a glance.

- Two grounds. Paper (`ground` `#f3efe4`) is the reading ground. Night (`ground` `#0d0e10`) is the same system with tokens swapped. Type, spacing, radii, and line grammar are the same objects on both. The Night banner is separated from the ground by a 1px `rule`.
- Three type voices. Serif carries titles, prose, and node text, titles at weight 650 and prose at 400. Mono carries kickers, codes, routes, legends, and counters, in uppercase with wide tracking. Sans carries pills, buttons, and connector verbs. Nothing on the page is below 10.5px.
- Newsreader is the serif, a variable face with weight axis 200 to 800, so 650 is a real weight, italic included, `font-display: swap`. The stack is `"Newsreader", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif`. A single-file document embeds the face and travels without it installed.
- Hierarchy comes from the type scale and from hairlines. Nodes, control groups, and content panels (figures, tables, cards) have a border and a radius. The inspector is the only surface with a shadow (`lift`).
- One focal mark per view, drawn at `stroke-route` weight. Comprehensive and Descriptive: the current part’s kicker. Illustrative: the route being read, or the return arrow. Interactive: the selected node, or the current step. The keyboard focus ring is visible and is not that mark.
- Eight node fills, `node-1` through `node-8`, each with a 1.6px ink outline (`stroke-node`). Colour names the code at a corner. Numerals and labels on a fill use `on-node`.
- Role colour (`role-act`, `role-decide`, `role-record`) and way colour appear as a dot, a ring, a border, or a stroke. Text that names the role or the way is `ink`, `ink-2`, or `ink-3`. Way colour and focal are different marks.
- The line grammar is in the legend and in the drawing.

| Line | Meaning on the page |
|---|---|
| Solid | Settled, selected, or travelled |
| Dashed | Computed, contingent, needs work, or uncertain. Uncertainty is also marked `[?]` |
| Dotted | Held, unexplored, a path not taken, or a cannot-do |

- Dividers, and the forward edge of a step, are solid hairlines. A cannot-do is dotted `ink-3`, and its strike is `ink-3`.
- A sheet (flowchart, concept map, or master blueprint) is landscape and on the grid, with room around the nodes. A section holds at most about twelve nodes. The footer reads title, version, date, and the legend. Flowchart nodes sit on one axis with a focal path. A concept map places nodes by affinity. A master blueprint has three to five numbered bands.
- Illustrative figures are numbered from `FIG 1` and have a caption. Static matrices and tables that belong to the argument sit in Comprehensive and Illustrative.
- Below 1100px, way pills may read One, Two, and Three. Their colours stay. At 640px and below, tab labels stay the full mode names and the bar scrolls.

### Common failure modes

- Two things are focal in one view, or focal is used as decoration, as status, or as a second way colour.
- Focal text sits on `sunk`. A role colour or a way colour is used as text.
- A node fill has no ink outline, or the numeral on a fill is `ink`.
- A divider is dashed. A cannot-do is dashed, or its strike is focal. A dotted line is used for a computed route.
- Speaker, role, way, or line meaning is carried by colour alone.
- Type falls below 10.5px, the serif renders as a system sans, or weight 650 is synthesized because the variable face is missing.
- A third theme appears, a second shadow appears, or a sheet crowds past the node count with no second sheet.
- The Night banner sits on the Night ground with no separating rule.
- A figure has no caption, or the figure index is missing, so a picture floats beside the argument.
- A retired mode name is used as a view label.

## 2. Comprehensibility

Whether a reader can say which mode this is, what the words claim, and where the same reference lives next.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | Mode, voice, names, and cross-references match the locked grammar. The reader can say what this view is and where the same reference goes. |
| 3 | The wording holds. One local slip does not rename a mode, hedge governed prose, or break a citation. |
| 2 | The reader can follow the page and still mis-name a mode, a body, or the direction of a citation. |
| 1 | Retired labels, hedges, or rewritten authored words change what the system says. |
| 0 | The page does not state its mode, or the words are a different model. |

### Top score

A 4 uses the locked names and keeps the author’s words.

The five modes, in this order, Interactive first:

| Mode | Definition | Kind | Question |
|---|---|---|---|
| Interactive | The live mode where all the forms meet | Combined space | What connects? |
| Illustrative | The visual mode in graphic form | Output | What is seen? |
| Comprehensive | The written mode in full depth form within the scope | Output | What is read? |
| Descriptive | The explanatory mode in narrative enactment form | Output | What is explained? |
| Transcriptive | The recorded mode in text form | Output | What was said? |

Interactive is the live space. It is not an output. Making order, the other way from the tab bar, is Transcriptive, Descriptive, Comprehensive, Illustrative, Interactive. Interactive holds the connection and the four facets. It does not hold a second copy of the full prose. Comprehensive holds the argument, within the part’s scope. Descriptive holds a short enactment tied to one Comprehensive passage. Illustrative holds the graphic. Transcriptive holds the words that were said.

- Voice is declarative. The words *might*, *arguably*, *perhaps*, and *seems* are absent from system chrome and from Interactive, Illustrative, Comprehensive, and Descriptive. *May* appears only as permission, as in “May this proceed?” Unfinished work sits on a list headed *Next*.
- Transcriptive is exempt. Fillers, misspellings, and hedges stay. Doubt is `[?]`. A redaction is `[redacted]` in mono. A missing time is absent. The implementation does not invent one. Colour does not carry the speaker, and role colours are not used on turns. Claude’s turns are `ink-2` and indented `space-4` (24px). A document-specific kicker form is scored on the document rubric. This dimension scores the exemption, the invented-time rule, and the colour rule.
- Seven forms only. Agent nouns take `-er`. No `-al` form. The adverb is the `-ive` adjective plus `ly`.

| Mode | -ive | Verb | -able | Agent -er | -ion | -ing | -ly |
|---|---|---|---|---|---|---|---|
| Interactive | interactive | interact | interactable | interacter | interaction | interacting | interactively |
| Illustrative | illustrative | illustrate | illustratable | illustrater | illustration | illustrating | illustratively |
| Comprehensive | comprehensive | comprehend | comprehendable | comprehender | comprehension | comprehending | comprehensively |
| Descriptive | descriptive | describe | describable | describer | description | describing | descriptively |
| Transcriptive | transcriptive | transcribe | transcribable | transcriber | transcription | transcribing | transcriptively |

- Comprehensive keeps its stem split. `comprehensive`, `comprehension`, and `comprehensively` use comprehens-. `comprehend`, `comprehendable`, `comprehender`, and `comprehending` use comprehend-. Illustrative stays one stem, so the spellings are `illustratable` and `illustrater`.
- Node labels are four words at most. Every connector carries a verb, or it is cut. Coined words stay as the author wrote them.
- One reference, a part or a node, is shared across all five modes. The URL hash stores it, in the form `#m=transcriptive&r=b3`. Switching mode shows that same reference. Passages in Descriptive, Comprehensive, and Illustrative carry `from` ids, and a mono Source link on each passage resolves to those turns. The inspector’s four facets are Said (Transcriptive), Explained (Descriptive), Read (Comprehensive), and Seen (Illustrative).
- Compass labels follow the spec. Body 1’s compass label is Bridge. Bodies 2 to 9 take the collective name of the code they hold on the active way. On way one those names are Consequential, Deterministic, Propositional, Environmental, Reproducible, Contractual, Transmissible, Transformational. Governmental, Legal, Enforcement, and Development are not compass labels.
- There is no narrative mode, no `narrative.txt`, and no voiceover file.
- The reader-facing version string comes from one source and matches in the band, the footer, the masthead, and the PDF. On a document rebuild, the authored words of the Nine Bodies document are unchanged.
- A reader can answer from the page: what the current mode is, what the focal marks, what solid, dashed, and dotted mean, and where the same reference lives in another mode.

### Common failure modes

- Prose is still the name of a mode, or a sixth mode appears (narrative, listen, haptic, scripted).
- A hedge softens system chrome or governed prose. Transcriptive is edited for style, or a clock time is invented.
- An inflection is `descriptionally`, `illustrator`, `interactor`, or any `-al` form. The comprehensive stem is rewritten into one stem.
- Interactive repeats the full argument. A mode switch opens a different reference. A Source link does not resolve.
- Speaker is shown only by colour.
- A compass node is labelled Governmental, Legal, Enforcement, or Development.
- The band, footer, masthead, and PDF print different editions, or a reader-facing stamp copies `"version": 2` or `"v": 3` from the system files.
- A coined term is silently corrected. A connector has no verb. A node label is a sentence.
- The mode hint contradicts the locked definition of that mode.

## 3. Component grammar consistency

Whether every visible part is an instance of a named component, with that component’s anatomy and states.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | Every visible part is an instance of a named component with that component’s anatomy, states, and preview contract. |
| 3 | One component has a local anatomy slip. It does not invent a state or a second spelling of the component. |
| 2 | Several components are one-off markup. States or names diverge from the guide. |
| 1 | Components are renamed, merged, or given a job that belongs to a different component. |
| 0 | The page is bespoke. The component inventory is unused. |

### Top score

A 4 uses the inventory once, the same way in the guide, the preview, and the document.

`components/bundle.js` is one classic script. It assigns `window.FieldNotation`, with no imports and no network, and it covers Compass, NodeRoute, Inspector, Toggle, and ViewTabs. `bundle.css` carries the document CSS for those parts. Each component has a `README.md` and a `preview.html` whose first line is `<!-- @dsCard group="..." height=N -->`. The Inspector card is tall enough to show the Close row and the fact grid (about 320).

Script is a named preview. It follows the same preview contract. It does not name a mode.

| Component | Anatomy a 4 keeps |
|---|---|
| Masthead | Kicker, display title, lede, and the notice band. |
| Toggle | A kicker over a row of pills, one pressed. The pressed pill fills with `ink` and `ground` text. Pills are `white-space: nowrap`. |
| NodeRoute | Up to eight nodes. Each step lights the next node and connector in `focal`. A mono counter reads `STEP 3 OF 8`. The code sequence sits under the diagram. |
| Inspector | A `surface` panel: kicker, serif title, short definition, fact grid, Close pill. Four collapsible facets, mono summaries such as `+ SAID · 6 TURNS`, an excerpt of three lines at most, and an Open pill. The `+` and `−` marker is `ink-3`. The only shadow is `lift`. |
| ViewTabs | Five tabs in pipeline order, with the full tab pattern, at the top (sticky under the band) and again at the bottom. Previous and Next sit on the bottom bar. |
| Compass | A core at the centre, eight nodes around it, dotted spokes. Recentring re-forms the ring. A trail of past references sits under the map. Way roots are borders, dots, or strokes. Focal marks the current body or the current corner. |
| Chip | Mono 10.5px, a 9px dot, a 6px gap. |
| Table | `surface` fill, a 1px `line` border, radius 14, header in `ink` with `ground` text in the chip style, cells padded 10px 14px. In Interactive it sorts and filters. A row click selects and recentres. |
| Spine | A 38px numbered circle, a 1.5px ink line, card radius 14. |
| CanCannot | Yes: 1.5px solid `ink`. No: 1.5px dotted `ink-3` with an `ink-3` strike. |
| Status | A mono chip-style pill. The ok variant uses a `role-decide` dot and `ink` text. |
| Fold | A part folds to its kicker and title. Collapse parts folds them all. The control is at least 24px tall. |
| Trail | Past references, as chips at least 24px tall. The trail persists across modes. |
| Rail | Contents. The current part is the one the rail tracks. |
| Transcript | Turn, kicker, session fold, and Find. Sessions are parts, collapsed by default. |
| Matrix | Bodies as rows, ways as columns. A code-to-name list is a key, not a matrix. Row click selects and recentres. |
| CrossRef | An inline mono chip, code plus label. Click recentres. |

States stay the documented ones: pressed pill, selected tab, current focal, folded part, collapsed session. Interactive behavior lives in Interactive. A static matrix or table that is part of the argument stays available in Comprehensive and Illustrative.

A new control a document plan adds is a composition of these components. It uses their anatomy, their states, and their tokens.

`design-system.json` keeps `title`, `namespace`, and the rest of its keys. `lastChange` is written last when a pass updates it. An empty `sections` object is not a reason to drop the component files.

### Common failure modes

- A preview is blank because `bundle.js` is missing, or the bundle uses imports or the network.
- The tab control is a row of links, has six tabs, or uses a different order. A mode is spelled Prose, Narrative, or Listen.
- Status text is set in `role-decide`. A CanCannot “no” is dashed, or struck in `focal`. The inspector’s `+` / `−` marker is `focal`.
- A chip is below 10.5px, or a role chip has no dot when colour would otherwise be the only signal.
- A code-to-name list is built as a Matrix. A document block reimplements a component with different anatomy.
- The `@dsCard` line is missing, or the Inspector preview clips the Close row and the fact grid.
- Fold or trail controls are shorter than 24px.
- Script, or any added component, introduces narrative, listen, or a retired mode name as a view.

## 4. Token usage

Whether every colour, measure, and motion value comes from `project/tokens.json`, and is used for the job that file states.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | Colour, type, space, radius, stroke, shadow, target, and motion resolve to `tokens.json`. Hex outside `:root` is zero. Font sizes and radii are on token. At least 95% of spacing is on the scale. |
| 3 | A handful of off-scale spaces remain, inside the 5% the acceptance check allows, and no hex sits outside `:root`. |
| 2 | Off-scale values are common, or a token is used for a job its usage string gives to another token. |
| 1 | Hard-coded hex and ad hoc sizes sit beside tokens and contradict them. |
| 0 | Values are literals. The token file is unused. |

### Top score

A 4 has one source for each value.

- Every colour, type size, space, radius, stroke, shadow, target, and motion in the implementation resolves to a named token in `project/tokens.json`. `:root` maps those names to the Paper and Night pairs. Outside `:root`, hard-coded hex is zero.
- Spacing on a document build is at least 95% on the scale. Font sizes are 100% on a named style. Radii are on token.
- The spacing scale is `space-1` 4, `space-tight` 6, `space-2` 8, `space-ctl` 10, `space-3` 14, `space-card` 16, `space-4` 24, `space-5` 48, `space-6` 96. The snap map sends 2 and 3 to 4, 5 to 6, 7 and 9 to 8, 11, 12, and 13 to 14, 15 and 18 to 16, 20, 22, 26, 28, 30, and 34 to 24, 40, 52, 56, and 60 to 48, and 84, 90, and 120 to 96.
- Radii are `radius-chip` 12, `radius-panel` 14, `radius-figure` 16, `radius-pill` 999. Strokes are `stroke-hair` 1, `stroke-held` 1.2 (dasharray 1.5 5), `stroke-link` 1.5, `stroke-node` 1.6, `stroke-dash` 1.6 (dasharray 6 5), `stroke-route` 2.5. The only shadow is `lift`. Targets are `target-min` 24 and `target-touch` 44. Motion is `motion-dash` 6s linear infinite, `motion-glide` 400ms `cubic-bezier(.4,0,.2,1)`, and `motion-fade` 200ms ease-out.
- Families match the file. Serif is the Newsreader stack. Mono is `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`. Sans is `ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif`. Faces in use are listed in `type.fonts[]` and stored under `project/fonts/`.
- Named styles are used for their jobs: `display`, `part`, `section`, `subsection`, `card-title`, `body`, `caption`, `annotation`, `numeral`, `chip`, `kicker`, `legend`, `pill`, `relation`, and the rest of the file. `chip` is 10.5px / 1.3 / 700 / 0.08em. Nothing is introduced below 10.5px.
- `control` is the border for pills, tabs, and buttons. `rule` is for section rules and the 1px line under the Night banner. `on-node` is for numerals and text on node fills. `ink` is not substituted there. `ink-3` stays off `sunk`. Focal text stays off `sunk`.
- Way tokens are a border, a 9px dot, or a stroke. They are not text, and they are not focal. They do not change hex per stage.
- A new value is added to `tokens.json` before a component uses it. The document does not grow a fourth radius, a second shadow, or a motion curve outside the three motion tokens.
- A retint that the spec has ratified and the token file does not yet hold is a change to `tokens.json` first, in one place. Consumers then reference the name. See “Baseline tensions.”

### Common failure modes

- A component or a document rule carries a hex, an `rgb()`, or a raw px for colour, space, radius, stroke, or type size.
- A fallback such as `var(--n1, #ef5a52)` puts a hex outside `:root`.
- `ink-3` is placed on `sunk`, or focal text is placed on `sunk`.
- `rule` is used as a control border.
- A second shadow, a new duration, or a font size under 10.5px appears.
- Theme values are swapped, or a third theme is added.
- Spacing sits next to the scale (15px padding, 22px margins) and ignores the snap map.
- A token is renamed in the document and not in `tokens.json`, or a token is used for a job its usage string reserves (way as text, role as text, node colour as a sequence).
- The section 12 palette is hard-coded in the document while `tokens.json` still holds the earlier pairs, or the reverse, so one value has two sources.
- `design-system.json` `"v"` or the token file’s `"version"` is treated as a colour token or as the reader-facing edition.

## 5. Interaction design

Whether the documented controls do the documented thing, and the artifact adds no behavior the grammar does not name.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | The documented behaviors work, including keyboard tabs, the shared reference, and the three motion tokens. Undocumented behavior is absent. |
| 3 | One secondary behavior is rough, and the primary path still carries the reference across modes. |
| 2 | A primary behavior fails. Mode switch loses the reference, Previous or Next steps in the wrong unit, or a way list shows the wrong options. |
| 1 | Controls are present and do something else: a sixth mode, a listen control, or a gesture that edits the model. |
| 0 | The artifact does not respond. Tabs, travel, and the inspector are static or missing. |

### Top score

A 4 does the listed behaviors and nothing else.

- **Toggle groups.** One pill in a group is pressed. The pressed pill fills with `ink` and `ground` text.
- **Node travel.** Stepping moves along a route of up to eight nodes, lights the next node and connector in `focal`, and updates the mono counter. Span is all eight, the selected node with its neighbours, or the selected node alone. Horizontal travels along a route. Vertical travels across parallel routes at the same position.
- **Inspector.** Choosing a node opens the panel. Close dismisses it. Each facet’s Open pill jumps to that output at that passage. The excerpt is three lines at most.
- **Five view modes.** The tab order is Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive. Interactive is the tab on open. The bar is at the top, sticky under the band, and again at the bottom. Each mode has its own `role="tabpanel"`. Left and Right move between tabs, Home and End jump, with roving tabindex. At 640px and below the bar scrolls, the labels stay in full, and the selected tab scrolls into view.
- **Previous and Next.** They step by part in Transcriptive, Descriptive, Comprehensive, and Illustrative, and by node in Interactive.
- **Shared reference.** The hash holds the mode and the reference. Switching mode scrolls to that passage. The trail of past references persists across modes.
- **Compass and recentring.** Selecting a node previews it. Recentring makes it the reference and re-forms the ring (`motion-glide`). Clicking a way root sets the active way and repaints the compass stroke, the cube, and the option list in that way’s colour. Clicking a body sets the reference and keeps the way.
- **Way one on the cube.** Its label stays `Way one · E leads` on every stage. Its route stays the route the spec locks. Ways two and three rebuild only on the stages the spec names (Legal, Enforcement), and that list is bordered and dotted in the way colour. On the enforcement triad, way two and way three show different options. Governmental keeps the geometric routes for ways two and three.
- **Collapse.** Every part folds to its kicker and title. Collapse parts folds them all. Transcriptive sessions start collapsed.
- **Table, Matrix, CrossRef.** A row click or a cross-reference click selects and recentres the node.
- **Find.** Transcriptive has a pill-shaped Find field in the tool row.
- **Source.** The Source control is visible on touch, and on hover or focus elsewhere.
- **Motion.** Dash travel uses `motion-dash`. Recentring uses `motion-glide`. Step lighting uses `motion-fade`. No other animation is added. Under `prefers-reduced-motion`, animation and smooth scroll stop, and the state change still happens.
- **Keyboard.** A pointer is unnecessary. The five tabs walk with the arrow keys. The inspector opens and closes from the keyboard. Every Interactive node shows a visible focus ring.
- Transcriptive ships in every build, Paper and Night, with no privacy flag.

A control added by a later document plan passes this dimension when it is built from the named components, keeps the five modes, keeps one focal, and uses only the three motion tokens. Whether it is the right document feature is scored on the document rubric.

### Common failure modes

- A listen control, a voiceover, a narrative player, or a sixth mode is present.
- Mode switch clears the reference or scrolls to the top of the document. The hash omits the mode or the reference.
- Arrow keys move the page. Home and End do not jump tabs. Arrowing a tab moves focus into the panel.
- Previous or Next steps by the wrong unit.
- Animation runs past the three tokens, or motion continues under `prefers-reduced-motion`.
- Two pills in one group are pressed. Way colour changes with the stage. Way one is renamed on Legal or Enforcement.
- Ways two and three on the enforcement triad show the same options.
- Source links appear only on hover, so a touch user never sees them.
- Transcriptive is behind a privacy flag.
- Recentring leaves the ring where it was. The trail clears on mode change.
- A page script throws before the modes bind, so a tab is empty or a kicker prints a missing number.
- A facet opens the wrong passage, or a facet summary that should carry a count is blank.

## 6. Accessibility

Whether both themes can be operated from the keyboard, at the target sizes, at the contrast floors, with the motion preference honoured.

### Score scale

| Score | What the artifact does |
|---|---|
| 4 | Both themes meet the contrast floors, the targets, the tab pattern, the names, and the reduced-motion rule. A keyboard walk completes. |
| 3 | One local name or target miss, and contrast, keyboard tabs, and reduced motion still hold. |
| 2 | A class of controls fails contrast, target size, or keyboard reach. |
| 1 | Colour is the only signal for role, way, status, or focus, or motion cannot be stopped. |
| 0 | Language, names, keyboard path, or contrast evidence is missing. |

### Top score

A 4 meets the floors on both grounds, checked rather than estimated.

- `html` is `lang="en-AU"`. The `title` is inside `head`.
- Text meets 4.5:1 on its ground in both themes. `ink-3` is the floor for text, and it stays off `sunk`. Captions and annotations use `ink-2`. There is no focal text on `sunk`.
- Control borders use `control` and meet 3:1 (about 4.75:1 on Paper, about 6.96:1 on Night).
- Node fills, focus rings, and way or role marks are not colour alone. Every node carries its label or code in `on-node`. Numerals on fills meet the `on-node` range, about 4.3:1 to 9.5:1 across all eight nodes. `ink` is not used for those numerals on Night.
- Every control is at least `target-min` (24px). Under `(pointer: coarse)`, pills, tabs, tools, fold, travel, links, and trail chips are at least `target-touch` (44px).
- `:focus-visible` is visible. Nodes do not set `outline: none` on focus. An Interactive node draws a 2px `focal` ring at radius + 6 on `:focus-visible`. The focus ring is exempt from the one-focal rule, and it stays on the page so that rule can be met.
- Tabs use `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, and a `role="tabpanel"` per mode. Toggles expose `aria-pressed`. Groups have names (Ground, Movement, View mode, Contents).
- A figure SVG has `role="img"` or `role="group"`, an accessible name, and a `<title>` and `<desc>`. Decorative marks inside a named figure are hidden from the name.
- Status is a dot plus text. The ok variant is a `role-decide` dot and `ink` text.
- `prefers-reduced-motion` stops animation and smooth scroll.
- Find has an accessible name. Collapse parts exposes pressed state. Inspector Close is a control with a name. Source has a name that includes the passage id.
- Pills do not wrap. Under 1100px the shortened way labels still read One, Two, and Three, and colour is not the only difference among them.
- The check covers Paper and Night, desktop width and 640px, and a coarse pointer for the 44px floor. Evidence is a contrast script, a keyboard walk of all five tabs, the inspector opened and closed from the keyboard, and a visible ring on every Interactive node.

### Common failure modes

- `lang` is missing, or the `title` sits outside `head`.
- `ink-3` is on `sunk`, focal text is on `sunk`, role colour is used as text, or node numerals are `ink`.
- `.nn:focus` sets `outline: none` and `:focus-visible` does not replace it. The focus ring disappears on the fill it sits over.
- A control is under 24px, or coarse-pointer targets stay at 24px.
- Tabs are clickable buttons with no tab pattern. Arrow keys move the page.
- A compass or cube SVG has no accessible name. A figure has no `<title>` and `<desc>`.
- Motion continues under `prefers-reduced-motion`.
- Speaker, way, or status is distinguished only by colour. Dimmed labels fall under 4.5:1.
- Source is disclosed only on hover.
- Contrast is checked on Paper only, or on `ground` only, and not on `surface`, `sunk`, `banner`, and node fills.

## Claude Code implementation

Score a Claude Code pass with the same six scores. The work order in section 9 of the spec is not a dimension. The artifact is.

Section 10 of the spec is the evidence. Map each check onto the dimension that owns it.

| Acceptance check | Dimension |
|---|---|
| Text at least 4.5:1 and control borders at least 3:1, both grounds, computed by script | Accessibility |
| Spacing at least 95% on scale, font sizes 100% on token, radii on token, zero hard-coded hex outside `:root` | Token usage |
| Exactly one focal element per mode view, other than the focus ring | Visual clarity |
| Arrow walk of all five tabs, inspector open and close, visible focus ring on every Interactive node | Interaction design for the walk; Accessibility for the roles, names, and ring |
| Every `from`, `refs`, and Source link resolves, and the reference carries across all five modes | Comprehensibility for the citation; Interaction design for the mode switch |
| One version string, matching in the band, footer, masthead, and PDF | Comprehensibility |
| Animation and smooth scroll stop under `prefers-reduced-motion` | Interaction design and Accessibility |
| Authored words of the Nine Bodies document unchanged | Comprehensibility |
| Component anatomy matches the guide and the previews run | Component grammar consistency |

A pass that edits authored prose to look clearer fails comprehensibility, whatever the other scores are. A pass whose script throws before the modes bind cannot receive a 4 on interaction or on comprehensibility for the views that never render.

A dimension at 0 or 1 means the implementation is not a faithful use of the grammar, even when the other dimensions are 4.

## Score record

Leave this table empty. Do not enter a score for Version 5 or Version 6 in this file. When a later review scores the current draft, the draft is `document/The_Nine_Bodies_of_Authority_v5.html`, and the grammar it is scored against remains Version 4. Record that review somewhere else.

| Dimension | Score (0–4) | Note |
|---|---|---|
| Visual clarity | | |
| Comprehensibility | | |
| Component grammar consistency | | |
| Token usage | | |
| Interaction design | | |
| Accessibility | | |
