# Audit for Version 7

Prepared 27 October 2026. Reviewed the Version 4 grammar references, Version 4 rendering, Version 5 file and parts, Version 6 prompt, rubrics and plans, Version 6 HTML, and the existing Version 7 HTML. The Version 7 HTML was already present and was read without replacement. No scrape was attached. No rubric score is entered; both score tables remain blank.

## Strengths

- **The grammar has one readable route.** `spec/Field_Notation_v4_spec.md`, §5, puts Interactive first, marks it as the live space, and gives the four outputs distinct jobs. The Version 6 and existing Version 7 tab bars preserve that order and the shared mode/reference hash.
- **The census is explicit.** Version 6 and Version 7 each print `8 codes + 27 ledger names + 27 bodies = 62` in the key and the Comprehensive name frame. The domain eights sit beside that sum rather than inside it. This meets the Version 6 prompt and the document rubric’s census criteria.
- **The ledger keeps roles separate from position names.** The page preserves the three role lenses, the position Proposition, code Propositional, the lane names, and the public ledger. This matches the locked frame and `project\README.md` interaction grammar.
- **The record remains attributable.** The Transcriptive content retains the 459-turn record and the exact session line. The existing Version 7 page has no clock times in the session line and does not substitute the 127-turn Percy source log.
- **The Example is bounded.** The existing Version 7 HTML already has an “Outside the sixty-two” Example with the three line meanings, a single focal mark, and one pointer to each tab. It adds no census item.
- **The page preserves Version 6 while carrying the edition stamp.** The existing Version 7 file is separate from Versions 4–6, has a single `data-version` source reflected in band, masthead, and footer, and was not replaced in this sitting.

## Non-negotiables

- Keep Version 4’s five labels and order: Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive. Interactive is first and live; the other four are outputs. Keep the shared hash reference across modes. Source: `spec\Field_Notation_v4_spec.md`, §5; `project\README.md`, “Interaction”.
- Keep the census at eight codes, twenty-seven ledger names, and twenty-seven bodies. Keep the exact sum sentence and addends in that order. The domain eights are beside the sum, not an addend; the count is not eighty-one. Source: Version 6 prompt, “The 62”.
- Keep body 1 blank for code and ways 2 and 3 empty on Bodies by ways. Way one is scored on bodies 2–9. Keep Liken on the categorical domain eight and Analogy on the ledger categorical eight. No code is a meta label. Source: Version 6 prompt, “Codes”, “Domain eights”, and “Matrixes and ways”.
- Keep the 27 ledger names and three lane names Disposition, Imposition, and Superposition in their assigned key. Keep Proposition as a position, Propositional as a code, Environmental as a code, and Preservational as a body name. Source: Version 6 prompt, “Ledger names” and “Bodies”.
- Keep the three role lenses in Version 4 column order. Start with Authoritative body pressed. Preserve the three role pills, eight centre inspections, sixteen branch previews, preview close on a second click, and no placement control. Selecting or inspecting a body does not change the pressed role. Source: Version 6 prompt, “Ledger behaviour”.
- Keep the 459-turn Untitled document (15) record, `Session 1 · 459 turns · time not recorded`, VOICE/TEXT kickers, the existing CLAUDE · TEXT labels only where already present, and verbatim turn words. Keep the 127-turn Percy log out of Transcriptive. Source: Version 6 prompt, “Transcriptive”.
- Keep the existing public ledger. Do not apply the retired-term standards sweep. Do not remove Version 4 prose merely to make it look clearer. Source: Version 6 prompt, “Prohibitions”.
- Keep the grammar, token file, component files, rubrics, Version 4, Version 5, Version 6, and the Version 7 prompt unchanged. Token use follows `project\tokens.json`; the four recorded baseline tensions below do not authorize token edits.
- Keep Version 7 separate. The existing file is preserved; no later version stamp is applied to `design-system.json`.

## Optional changes

No optional stylistic change survives the test of being insignificant while leaving the locked frame, rubric failures, and behaviours untouched.

## Weaknesses, areas to improve, and tensions to resolve

- **Whole-file status is stale in the Version 6 plans.** `document\v6-editorial-plan.md` and `document\v6-implementation-strategy.md` say no Version 6 HTML exists, while `document\The_Nine_Bodies_of_Authority_v6.html` is present and stamped 6. That mismatch makes the handoff state unreliable. The Version 7 plan must use the file on disk as the current draft and record the stale sentence here; it must not repeat it.
- **Interactive is sound against the locked tab and ledger rules.** The Version 6 and existing Version 7 pages keep Interactive first, the three roles, centre/branch inspection, and the public ledger. Preserve these controls and their current reference behaviour.
- **Illustrative is sound against the tab contract.** The existing cube and route figure remain under Illustrative. The Version 7 Example’s line swatches state the full locked meanings and do not add a ledger item or a second mode.
- **Comprehensive is sound against the census contract.** Its name frame and key retain the required sum, 27 names, and the proposition/code distinctions. Keep their text aligned.
- **Descriptive is sound against the output contract.** The water case remains in body order, including the already named passage “Before the loop”. Keep each passage linked to its sources and do not add an unnamed passage.
- **Transcriptive is sound against the locked record.** The current file retains the 459 turns and session line. Keep it verbatim and keep added time values out.
- **The Version 7 audit prompt’s old “no Version 7 file” premise is stale on disk.** `document\The_Nine_Bodies_of_Authority_v7.html` exists. The correct response is to read and preserve it, then continue with absent planning files and checks; replacing it would destroy an existing artifact without need.
- **Recorded baseline tensions remain.** In `document\v6-rubric-design-system.md`, “Role, way, and bit hues” records that spec sections 11.5/12 use Paper `#c8741e #3c9447 #4479c9` and Night `#e8a36a #9ad84a #5ccfe6`, while tokens retain earlier role and way pairs. “Type snap” records spec `.sub`/`.lede` at 19px and sans controls at 12.5px while tokens retain 19.5px, 18.5px, and 12px. “Fold and trail padding” records spec values `8px 11px` and `7px 9px` against the spacing scale. “Three different version fields” keeps token version 2, file format 3, and reader-facing edition 4 distinct. The owner rule says token usage follows `tokens.json`; leave the file unchanged.
- **Transcriptive examples differ across sources.** Version 4 §5 gives example kickers with clock values (`PERCY · VOICE · 14:02`, `CLAUDE · TEXT · 14:03`); the Version 7 prompt’s record rule says VOICE/TEXT, existing CLAUDE · TEXT only, and no clock times. The Version 7 locked record rule controls this page; preserve the discrepancy as documented source tension and keep the existing transcript’s words.

## Decisions to lock before Version 7

- **Question:** Do 24-plus-3 and the set of sets stay proposed, become canonical and drawn while remaining outside the sixty-two, or drop out of the document?
- **Options:** stay proposed and undrawn, outside the sixty-two; ratify and draw them, still outside the sixty-two; remove the proposal.
- **Settlement:** stay proposed and undrawn, outside the sixty-two. The existing Version 7 Example already states this sentence: “24-plus-3 and the set of sets stay proposed and undrawn, outside the sixty-two.”
- **Source:** No scrape was attached and no caller line stated a choice, so this sitting applies the prompt’s first option.
- **Blocked until answered:** none for this question after the settlement; any future change to draw, fold into the sixty-two, or remove the proposal requires a new decision. The four baseline tensions do not authorize a grammar or token edit.

## Decisions to lock before Version 7

- **Question:** Do 24-plus-3 and the set of sets stay proposed, become canonical and drawn while remaining outside the sixty-two, or drop out of the document?
- **Options:** stay proposed and undrawn, outside the sixty-two; ratify and draw them, still outside the sixty-two; remove the proposal.
- **Settlement:** stay proposed and undrawn, outside the sixty-two.
- **Source:** No scrape was attached and no caller line stated a choice, so this sitting applies the prompt’s first option.
- **Blocked until answered:** none after this settlement; a later change to draw, include, or remove them requires a new decision.

