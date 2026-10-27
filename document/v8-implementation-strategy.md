# Version 8 implementation strategy

Prepared 27 October 2026, revised the same evening against the page on disk. The document is *The Nine Bodies of Authority*. The system is Field Notation, locked at Version 4.

Version 8 is a plan in this file. A later sitting builds it. The only document file that sitting creates is `document\The_Nine_Bodies_of_Authority_v8.html`. It starts from `document\The_Nine_Bodies_of_Authority_v7.html` (commit `8510d2c` on `nine-bodies-v7`) and writes a new file beside it. It does not overwrite Version 4, 5, 6, or 7.

The words for every new or changed string are in `document\v8-editorial-plan.md`. This file says what changes, where, and how it is checked. The sum is unchanged: `8 codes + 27 ledger names + 27 bodies = 62`.

This revision replaces the earlier Version 8 draft. That draft diagnosed the Example focal line as colourless, pulled the Example toward the footer, snapped a 16px gap off `space-card`, named a 16px radius `radius-panel`, snapped 34px to 48px, and left a backfill question open after the Version 7 plans were already on disk. Those readings do not match the files. This file follows the files.

## Editorial assessment of Version 7

These A–F grades answer the owner’s request for an editorial read. They are not entries in either rubric and do not fill either score table. They are based on the local HTML source and the locked frame. I could not confirm the browser rendering or click interactions in this sitting, so interaction-dependent grades are provisional.

| Tab / section | Grade | What works and why | Components and grades |
|---|---:|---|---|
| **Interactive** | **B+** | It carries the live model and the most important controls, and the census-related content is present. This tab has the most simultaneous concepts, so it asks the most of a first-time reader. | Five-tab navigation and shared-reference structure: **A−** (correct order and one hash reference); travelling map and “One path of eight” window: **B** (clear core idea, but the paired map/window creates a dense control area); public ledger and three role lenses: **A−** (clear role separation and the intended default); Version 4 matrixes, domain matrixes, and bodies-by-ways: **A** for structural/census fidelity (body 1 blank, ways 2 and 3 blank). Runtime behavior still needs browser verification. |
| **Illustrative** | **B+** | The figures give the abstract system a visual route and preserve the cube and ledger figure. The Example block is useful onboarding, but its focal specimen currently competes with the live current-position mark, and its short labels omit distinctions supplied in the README table. | Cube and route figures: **A−** (strong conceptual anchors; appearance not browser-verified); ledger figure: **A−** (keeps the eight-plus-sixteen structure and three lane names); Example line key: **B** (good purpose and full paragraph/description, but the visible short labels are incomplete and the focal swatch can read as a second current mark); five tab pointers: **A−** structurally (targets exist in markup; click/visibility still unverified). |
| **Comprehensive** | **B+** | The corrected census and domain eights make the naming logic inspectable while retaining the original collective-names material. The legacy key beside the corrected key may make it unclear which key is authoritative unless the relationship is stated right where they meet. | Version 4 prose: **A−** (broad context and retained wording); *The collective names* plus corrected key: **B+** (useful preservation and correction, with duplicate-key hierarchy to keep explicit); domain eights: **A−** (Liken and Analogy remain distinct). |
| **Descriptive** | **B+** | Nine body-ordered passages give the model an enacted reading and follow the required order. The main opportunity is navigation and cross-linking through a long sequence, not rewriting the case. | Water case: **B+** (complete and ordered; passage-to-body/source wayfinding should stay visible); nine body passages: **A−** for coverage/order; source-turn affordances: **B+** (present in markup; interaction not browser-verified). |
| **Transcriptive** | **A−** | The 459-turn record and session line preserve the record’s identity and avoid inventing clock time. The sheer length makes navigation the relevant usability concern; the transcript itself is non-negotiable. | Transcript turns and VOICE/TEXT kickers: **A** for fidelity; session line and no-clock treatment: **A**; transcript navigation/findability: **B** (a long record benefits from clearer orientation, while edits to the turn text remain prohibited). |

### Overall first reaction

This is an unusually coherent document system: the interactive layer, named outputs, census, and transcript point back to one another rather than behaving like five unrelated exports. The strongest achievement is its disciplined separation of codes, ledger names, bodies, roles, and domain eights. Version 7 is already a substantial, content-complete edition; Version 8 should be a small consistency pass, not a redesign. The real risk is local semantic drift in explanatory shorthand, plus density and unverified browser behavior. Do not alter settled content just to make the page look newer.

## 1. What stays, because it already works

These stay exactly as Version 7 has them. A Version 8 line that moves one of them is not a Version 8 line.

1. **Five tabs.** Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive, in that order, at the top and the bottom. Interactive opens first when the hash has no mode. The hash carries one reference across all five.
2. **The sum.** `8 codes + 27 ledger names + 27 bodies = 62`, the same sentence in `#name-frame` and in `#name-key`.
3. **Codes · 8.** On bodies 2 to 9 with Version 4's bits: 101, 111, 011, 010, 110, 100, 000, 001. Body 1 has no code. Environmental is the code. Preservational is the body name. Propositional is the code. Proposition is the position. No code is a meta label.
4. **Ledger names · 27.** Eight positions, eight categorical names with Analogy in the fourth seat, eight contingent names, and the lanes Disposition, Imposition, and Superposition in the name key. The lanes name the illustrative figure's lines. They are not the controls.
5. **Bodies · 27.** Role lenses in Version 4's column order: embodied agent, authoritative body, authoritative agent. The count is not 81.
6. **Domain eights.** Beside the sum, in their own block. Meta labels: logical, categorical, contingent. Liken is on the categorical domain eight. Analogy is on the ledger. The two stay apart.
7. **The public ledger.** That name, in Interactive (`#ledger`). Three role pills. Authoritative body pressed at the start. A centre click inspects and leaves the pressed role. A branch click previews, and a second click closes. No placement control.
8. **Interactive keeps** the travelling map, the window *One path of eight* with Eight pressed, the public ledger, Version 4's matrixes, the domain matrixes, and bodies-by-ways. Body 1 is blank there. Ways 2 and 3 are empty there.
9. **Illustrative keeps** Version 4's figures, including the cube (`#cube`, which contains `figure#figCube`), and the ledger figure. 24-plus-3 is ratified and drawn beside that ledger figure as `#figSetOfSets`, outside the sixty-two. The author locked that on 27 October 2026. Do not return it to Proposed and do not delete the figure.
10. **Comprehensive keeps** Version 4's prose word for word, *The collective names*, and the corrected key beside it.
11. **Descriptive keeps** the water case, one passage per body, in body order.
12. **Transcriptive keeps** the 459 turns r001–r459, verbatim; kickers `VOICE` or `TEXT`; `CLAUDE · TEXT` only where the page already prints it; no clock time; the line `Session 1 · 459 turns · time not recorded`. The 127-turn log stays out. Spec section 5 shows a kicker shape that includes a clock when a time exists. This record has no times. Section 11.2 says a missing time is absent. The page already follows that. Version 8 does not add clocks and does not rename the tab.
13. **The Example paragraph stays.** It already states the line-grammar table in `project\README.md`: settled, selected, or travelled; computed, contingent, needs work, or uncertain, with `[?]`; held, unexplored, a path not taken, or a cannot-do. Version 8 does not shorten it to the footer.
14. **The Example's five pointers stay,** with the labels the page already prints: Public ledger; The cube and its routes; The collective names; The water case, enacted; Session 1 · 459 turns · time not recorded.
15. **One reader-facing edition.** `<html data-version>` feeds the band, the masthead, and the footer. Token `"version": 2` and file format `"v": 3` stay in their own files. Spec section 4's clause "Today they read 2, 3 and 5" is the defect that row was written to close. It is not an instruction to stamp 2, 3, or 5. This build does not edit the spec.
16. **The page's way hues stay.** `:root` already paints the palette spec sections 11.5 and 12 ratified: Paper `#c8741e` `#3c9447` `#4479c9`, Night `#e8a36a` `#9ad84a` `#5ccfe6`, with `way-*` aliasing the role tokens. Version 8 does not paint the page back to the earlier pairs still sitting in `tokens.json`.
17. **Prohibitions.** No retired-term sweep. No edit to a grammar file, a component, a rubric, a prompt, or Versions 4–7. No score is filled. `design-system.json` gets no edition stamp. Version 4 figures are not restroked in this build. Focal inside those carried figures is on *Next*, not in this file's change list.

## 2. Changes for Version 8

Each item says where, what Version 7 does now, what Version 8 does, and why. Words are quoted in the editorial plan under the same id.

### Major

**A1 · The Example inherits a live focal, and the key must not be a second current position.**

- *Where:* `#example .ex-svg`, against `:root` and `figure.fig`.
- *Now:* `:root` sets `--mark:var(--focal)`. `.s-focal` strokes `var(--mark)`. `figure.fig` resets `--mark` to `var(--ink)`, and only the current illustrative figure sets it back to focal. The Example SVG is not a `figure.fig`, so its focal line inherits the live focal from `:root`. The line has a colour. The colour is the view's current-position colour. The Example sits on Interactive after the travelling map, so the view holds two focal marks.
- *Version 8:* **Transform** the Example figure into a legend key, using the page's existing `.legend` pattern (`i`, `i.d`, `i.o`, and a labelled specimen). The three grammar swatches use ink and ink-3, the same way `.s-line`, `.s-dash`, and `.s-held` do. The focal item is text only: it names the rule without drawing a second focal mark or using focal colour. The current position on Interactive stays the travelling map's route. The keyboard-focus-ring exception does not apply to an explanatory specimen. Do not use `.s-focal` inside the Example.
- *Why:* `project\README.md` says one focal, and "If two things are focal, neither is." The mechanism the page already uses is `--mark`. The Example joins that mechanism. It does not invent a second one, and it does not leave a route painted as the current position.

**A2 · One legend vocabulary, taken from the line-grammar table.**

- *Where:* the Example key, and the footer legend. The Example paragraph stays.
- *Now:* the paragraph matches the README table. The key abbreviates the three line rows to "SOLID · SETTLED", "DASHED · CONTINGENT", and "DOTTED · HELD"; its focal row shows a focal-coloured line beside "ONE PER VIEW". The footer says "Solid = settled or travelled · Dashed = channel or contingent · Dotted = held or unused". "Channel" is not in the README table. "Unused" is not the dotted row. The footer is the string that drifted.
- *Version 8:* **Adjust** the footer and the key to the words in the editorial plan. Leave the Example paragraph as Version 7 prints it.
- *Why:* the table is the grammar. The paragraph already follows it. The footer and the key follow the paragraph.

**A3 · Confirm the five pointers against the markup, then in a browser.**

- *Where:* `[data-ex]` and the script at the end of the page.
- *Now:* each button names a real id. `#cube` contains `figure#figCube`, so the illustrative rule that hides a `section.sec` with no `figure.fig` does not hide `#cube`. The script opens the tab, opens a `details` target, scrolls, and focuses the heading or the summary. No browser pass has clicked them. The local browser pane does not load this file.
- *Version 8:* **Apply** a browser check of all five pointers, Paper and Night. The labels stay. A retarget is allowed only when that check shows the target hidden, and the editorial plan then quotes the new id before the file is written. The static markup does not call for a retarget.
- *Why:* a pointer that opens a tab and lands on a hidden region fails the Example's job.

### Minor

**B1 · Ratify and draw 24-plus-3.**

- *Where:* the name frame, Figure 9's caption, `#example .ex-settle`, and a new figure `#figSetOfSets` in Illustrative.
- *Now, on Version 7:* the chip "Proposed" is followed by "stay proposed and undrawn".
- *Version 8:* **Draw** the three domain eights, logical, categorical with Liken, and contingent, plus their three meta labels. The chip reads "Ratified". The strings are the ones in the editorial plan. The figure states `24 NAMES + 3 META LABELS = 27 = 3 × 3 × 3 · NOT ADDED TO THE 62`.
- *Why:* the author locked this one item on 27 October 2026. 27 is 3 × 3 × 3. The census stays 62. This twenty-seven is the domain count, not the bodies twenty-seven.

**B2 · Put the Example's new spacing on the scale the token file actually holds.**

- *Where:* the Example's `<style>`.
- *Now:* `margin:34px 0 8px`, `padding-top:22px`, `gap:16px`, `margin-top:12px`, button `padding:8px 13px`, `border-radius:16px`.
- *Version 8:* **Apply** the snap map and the tokens that exist. 34 snaps to 24 (`space-4`). 22 snaps to 24 (`space-4`). 12 snaps to 14 (`space-3`). 13 snaps to 14, which is also what `.pills button` already uses (`8px 14px`). `gap:16px` is `space-card` and stays. `border-radius:16px` is `radius-figure` and stays. `radius-panel` is 14px and is not this radius. `gap:6px` is `space-tight` and stays. The button's 12px size stays, because the pill token is 12px and the page's other pills are 12px.
- *Why:* token usage. A value that is already a token stays. A value the snap map moves is moved to the value the map names.

**B3 · Kicker source case. Drop.**

The rendered kicker is uppercase either way, so changing only source capitalization has no reader-facing benefit. Version 8 keeps "Example · Outside the sixty-two" byte for byte.

**B4 · Keep the programmatic tabindex behavior unless browser testing shows a defect.**

- *Where:* the pointer script.
- *Now:* a target heading that had no tabindex receives `tabindex="-1"` and keeps it after focus.
- *Version 8:* **Keep** the current behavior unless keyboard testing demonstrates a failure or a persistent tab stop. Do not change focus handling speculatively.
- *Why:* the pointer must land accessibly, and focus behavior is not safely changed without a keyboard check.

## 3. Settled 24-plus-3 ruling

The author locked D1 on 27 October 2026. 24-plus-3 and the set of sets are ratified and drawn, outside the sixty-two: three domain eights plus three meta labels, 24 + 3 = 27 = 3 × 3 × 3. Version 7's proposed, undrawn wording is the history of the question. It is not the Version 8 page. The page at commit `2b5158d` on `nine-bodies-v8` is the lock. A later change requires a new explicit decision and a revised editorial plan before any page edit.

**Recorded, and not a block on the document stamp.**

- Spec section 4 says one version feeds the band, the footer, the masthead, and the PDF, and then "Today they read 2, 3 and 5". The "today" clause records the defect. Version 8 stamps 8 from `data-version`. The grammar file stays as it is in this build.
- The four baseline tensions in `v6-rubric-design-system.md` stay recorded. This build does not edit `tokens.json`. It does not retint the page to the earlier role and way pairs. A grammar sitting that writes the ratified hues into `tokens.json` first, then points consumers at the names, is the path the rubric already names. That sitting is not this HTML file.
- Type snap for `.sub`, `.lede`, and `pill`, and the fold and trail padding pair (`8px 11px` against the snap of 11 to 14, and `7px 9px` against the snap of 7 and 9 to 8), stay in the rubric. Version 8 does not open that grammar edit. The Example's own off-scale numbers are in B2 because they are new to the Example and the snap map already names their targets.
- `document\v7-audit.md`, `document\v7-implementation-strategy.md`, and `document\v7-editorial-plan.md` are on disk. Version 8 does not backfill them and does not rewrite them.
- `fn\` at the repository root is a nested copy, including `field-notation-spec-v3.md`. It is not the live grammar. This build does not read it and does not delete it.

## 4. Build rules

- Copy `The_Nine_Bodies_of_Authority_v7.html` to `document\The_Nine_Bodies_of_Authority_v8.html` and apply the changes above. Edit no other file.
- Stamp: `<html data-version="8">` is the one field. The three `<span data-version>` fallbacks read `8`. The band, masthead, and footer read 8. `design-system.json` stays untouched.
- Stamp 8 only when Interactive still holds the map, the window, the public ledger, and the matrixes, and Transcriptive still holds 459 turns and the session line.
- Each replacement is counted before the file is written.
- Commit on a branch named for Version 8. Do not merge into `nine-bodies-v7` in this plan. This file does not commit.

## 5. Checks the build runs

Every item reports PASS or FAIL. This plan does not run them. The Version 8 HTML does not exist yet.

1. Versions 4, 5, 6, and 7, the grammar files, the components, and the rubrics are byte-identical to the hashes taken before the copy.
2. The public ledger is present, under that name.
3. The session line contains `459 turns · time not recorded`. There are 459 turns, r001–r459. No clock time is added.
4. The sum sentence is the same in `#name-frame` and `#name-key`.
5. Body 1 has no code, in the codes table and on bodies-by-ways.
6. Ways 2 and 3 are empty on bodies-by-ways. Bodies 2–9 carry Version 4's bits.
7. Liken is on the categorical domain eight. Analogy is on the ledger categorical eight.
8. Authoritative body is the only role pill pressed at the start.
9. There is no placement control.
10. The five tabs are in order at the top and the bottom. Interactive opens first. No retired name is a tab label.
11. 24-plus-3 matches the lock: chip "Ratified", figure `#figSetOfSets` present, outside the sixty-two, and the census sentence still appears twice.
12. The Example block is present, outside the sixty-two, and its paragraph is the Version 7 paragraph.
13. The band, masthead, and footer read 8 from one field. The page has no duplicate ids.
14. On Interactive, the Example contains no focal-coloured line or `.s-focal` route. The travelling map's current route remains the only focal position; the Example names the focal rule in neutral text.
15. The footer legend and the Example key preserve every distinction in the README line-grammar table, including `[?]` for uncertainty and held, unexercised power for cannot-do. The string "channel" is absent from the footer.
16. The Example's margin, padding, gap, and radius are the B2 values. `gap:16px` and `border-radius:16px` are still present.
17. All five pointers open their tab and land on a visible target, in a browser, Paper and Night.
18. With `prefers-reduced-motion: reduce`, the dashed key does not animate.
19. Way hues on the page are still the ratified set named in section 1 item 16. `tokens.json` is unchanged.
20. Every script in the page parses.

## Next

- Keep `#figSetOfSets` ratified and outside the sixty-two. Do not redraw it as the nine bodies.
- A grammar sitting for `tokens.json`: write the ratified hues into the token file first. Leave the document's painted hues as they are until that file changes.
- A focal pass over Version 4 figures that still paint `--mark` as text or as a second route. Not this build.
- Build Version 8 from section 4 and run section 5.
