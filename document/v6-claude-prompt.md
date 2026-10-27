# Version 6 prompt

You are Claude. This prompt is the whole brief. Act on it. Do not ask for another conversation, another decision, or a missing list. The names, the counts, the tabs, the files, and the stop are all here.

Prepared 27 October 2026. The document is *The Nine Bodies of Authority*. The system is Field Notation, locked at Version 4.

## First step, then stop

Do this sitting in this order, and then stop.

1. Read the locked grammar named below. Leave every one of those files as you found it.
2. Read Version 4 only to keep the pairings it already prints. Leave `The_Nine_Bodies_of_Authority_v4.html` untouched.
3. Review the Version 5 draft, the whole file, against this prompt and against that grammar.
4. Write the Version 6 implementation strategy.
5. Write the Version 6 editorial plan.
6. Stop.

The first step creates two new files and no others:

- `<home>\.agents\skills\agents-sdk\design system\document\v6-implementation-strategy.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v6-editorial-plan.md`

They sit beside the document. Write both before any Version 6 HTML exists. Do not build `The_Nine_Bodies_of_Authority_v6.html` in this sitting. Do not edit Version 4. Do not edit Version 5. Do not edit the grammar files, the component files, the Version 5 parts, or the Version 5 plans.

When the two files are written, report their paths and stop. The follow-up execution step is specified later in this prompt. Begin it only when a later message tells you to build Version 6 or to execute the follow-up. That later message does not need a new brief. This prompt remains the spec.

## Locked grammar

Version 4 is the latest locked grammar. Read it. Use it for Version 6. Do not edit it, retoken it, or restyle the system in order to improve the document.

Read these files:

- `<home>\.agents\skills\agents-sdk\design system\spec\Field_Notation_v4_spec.md`
- `<home>\.agents\skills\agents-sdk\design system\project\tokens.json`
- `<home>\.agents\skills\agents-sdk\design system\project\design-system.json`
- `<home>\.agents\skills\agents-sdk\design system\project\README.md`

There is no `README.md` at the repository root. The locked README is `project\README.md`.

Read the components under `<home>\.agents\skills\agents-sdk\design system\project\components\`. Each component’s `README.md` and `preview.html` is part of the locked grammar. The set is Masthead, Toggle, NodeRoute, Inspector, ViewTabs, Compass, Chip, Table, Spine, CanCannot, Status, Fold, Trail, Rail, Transcript, Script, Matrix, and CrossRef. `components/bundle.js` and `bundle.css` cover Compass, NodeRoute, Inspector, Toggle, and ViewTabs.

Take from that grammar, and keep:

- Five modes, tab order left to right: Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive. Interactive opens first. Interactive is the live space. The four outputs are illustrative, comprehensive, descriptive, and transcriptive.
- Seven forms only. No `-al` forms. Agent nouns take `-er`. Descriptive’s adverb is `descriptively`. Transcriptive’s adverb is `transcriptively`. Comprehensive keeps its stem split: `comprehensive`, `comprehension`, and `comprehensively` use comprehens-; `comprehend`, `comprehendable`, `comprehender`, and `comprehending` use comprehend-. Illustrative keeps `illustratable` and `illustrater`.
- Voice: declarative sentences. No might, arguably, perhaps, or seems. May is permission only. Unfinished work goes on a list headed *Next*. Transcriptive is exempt and stays verbatim.
- Tokens, line grammar, grounds, type voices, and the one `focal`. Solid is settled. Dashed is contingent. Dotted is held. Colour is never the only signal.
- The full tab pattern, the shared reference in the URL hash, and the components named above.

`The_Nine_Bodies_of_Authority_v4.html` stays untouched. Its path is `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v4.html`. Read it to keep pairings it already states. Do not rebuild it, restamp it, or copy fixes back into it.

## Review Version 5

Review the current draft at:

`<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v5.html`

Also read, and leave unchanged:

- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\interactive-ledger.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\interactive-matrix.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\name-key.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\transcriptive.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-implementation-strategy.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-editorial-plan.md`

Version 5 is a draft of Version 4’s full five-tab document plus the additions in this prompt. Improve it in any way you see fit inside the fence below. The improvement is planned in the two Version 6 files and, in the follow-up, built into a new HTML file. It is not made by editing Version 5.

Record the review in the strategy and the editorial plan. For each tab, name what you will carry forward and what you will change. A change is a concrete edit: which region, what it says or does now, what it will say or do, and why that is an improvement. If a tab needs nothing, say it is carried forward. Do not leave the improvement as a mood or a question.

Where this prompt and the Version 5 draft disagree, this prompt is the spec. Where this prompt and your two plan files later disagree, this prompt wins.

## Fence

You may clarify, complete, correct an inconsistency, tighten a behaviour to the interaction this prompt names, and bring the document onto the locked components and tokens.

You may not drop a required tab, the travelling map, the one-three-eight window, the public ledger, a required matrix, a Version 4 figure, the cube, the added ledger figure, either name key, a water-case passage, or the 459-turn record.

You may not edit the locked grammar, Version 4, or Version 5.

You may not add a placement control, a code on body 1, a filled way two or way three on the bodies-by-ways matrix, an eighty-one-name count, Liken on the ledger categorical eight, or Analogy on the categorical domain eight.

You may not run the retired-term standards sweep, and you may not remove the public ledger.

You may not stamp Version 6 until Interactive and Transcriptive both have content.

## What Version 6 keeps

Version 6 is Version 5, expanded. It remains one five-tab document.

Interactive opens first. With no mode in the hash, the selected tab is Interactive. Keep the hash behaviour Version 5 already has, so a stored reference still opens its mode.

### Interactive

Keep all of these together:

- Version 4’s travelling map.
- A one-three-eight window on the eight codes. Version 5 already draws this as the sequence *One path of eight*. Scale 8 is the whole path. Scale 3 is the current station and its two neighbours. Scale 1 is the current station. The stations are the eight codes, on bodies 2 through 9. Eight, the whole path, is the scale that starts pressed. Keep one window. Do not add a second.
- The public ledger.
- The matrixes: Version 4’s own matrixes, the domain matrixes, and bodies-by-ways.

Ledger controls are the three role lenses: embodied agent, authoritative body, authoritative agent. Authoritative body starts pressed. The pressed role is the centre line.

The eight centre events are the categorical imposition. A click on a centre event opens an inspection of the position, the categorical name, and the release. That click leaves the pressed role as it is.

Sixteen dashed branches, two per position, sit off that centre. A click on a branch opens an inline preview of the position, the contingent name, and that role’s archive line. The archive line is the line for the role the branch belongs to. Clicking that branch again closes the preview. A branch click leaves the pressed role as it is.

The role pills are the control that changes which role is pressed. Centre clicks and branch clicks are not that control.

There is no placement control. Do not add a pill, a drag, or any other control that places an event on a different position.

The categorical name on the ledger is the ledger categorical eight, with Analogy at the fourth seat, Juxtaposition. Liken is not that name. Keep the release text and the archive lines Version 5 already stores. A new line belongs in the editorial plan, quoted, before it is built.

Domain matrixes use Liken on the categorical eight. Bodies-by-ways keeps body 1 blank, the eight codes on bodies 2 through 9, and way two and way three empty. Version 4’s own matrixes stay, showing what Version 4 already shows.

### Illustrative

Keep Version 4’s figures, including the cube. Keep one further figure: the ledger of eight plus sixteen, the eight codes, and the nine triads.

The figure’s three lines are the ledger lanes, named Disposition, Imposition, and Superposition. Those names on the figure are the ledger. They are not the interactive pills.

24-plus-3 and the set of sets stay marked proposed, and they stay undrawn. 24-plus-3 is the count of the sequence plus meta. The set of sets is its label. Neither is added into the sixty-two.

### Comprehensive

Keep Version 4’s prose. Keep the original name key under its heading, *The collective names*. Keep the corrected 62 name key beside that original key. Both stay. The corrected key is the sum in the next section, not a replacement that deletes *The collective names*.

### Descriptive

Keep Version 4’s water case: one passage for each body, nine passages. Nothing further is required. A passage you still want to add is named in the editorial plan before the follow-up builds it, and the nine water passages stay.

### Transcriptive

Keep the 459-turn record already in the Version 5 Transcriptive tab and in `document\v5-parts\transcriptive.html`. Its source is `<home>\Downloads\Untitled document (15).pdf`.

Kickers are `VOICE` or `TEXT`. Print `CLAUDE · TEXT` only on the turns where that Version 5 page already prints `CLAUDE · TEXT`. Leave every other kicker as `VOICE` or `TEXT`. Add no speaker name to those, and add no clock time.

The session line includes `459 turns · time not recorded`. Keep the line Version 5 already prints: `Session 1 · 459 turns · time not recorded`.

The 127-turn Percy log is `<home>\.agents\skills\agents-sdk\design system\source\transcript.json`. Do not replace the 459-turn record with that log, and do not rebuild Transcriptive from it.

Transcriptive stays verbatim. Fillers, misspellings, hedges, and a word *Claude* inside a turn’s text stay.

## The 62

The sum, in the corrected name key and in the Comprehensive name frame, is this line:

8 codes + 27 ledger names + 27 bodies = 62

Say it as the lede. The three addends follow in that order. The domain eights are not a twenty-seven inside the sum. The three role names are not a fourth addend. The count is not 81.

### Codes · 8

On bodies 2 through 9. Body 1 is blank. No code is written on body 1.

The bit pairing is the one Version 4 and Version 5 already print:

| Body | Code | Bits |
|---|---|---|
| 1 | — | — |
| 2 | Consequential | 101 |
| 3 | Deterministic | 111 |
| 4 | Propositional | 011 |
| 5 | Environmental | 010 |
| 6 | Reproducible | 110 |
| 7 | Contractual | 100 |
| 8 | Transmissible | 000 |
| 9 | Transformational | 001 |

Environmental is the code on body 5. Preservational is the body name in the authoritative-agent column of body 5. The two words stay in those two places.

Propositional is this code. Proposition is a position, in the ledger below. They are not one name.

No code is a meta label. The question of which codes would be the meta labels is closed. Leave no blank slots for it.

### Ledger names · 27

Eight positions, eight categorical names, eight contingent names, and three lanes.

Positions: Supposition, Exposition, Reposition, Juxtaposition, Proposition, Composition, Decomposition, Deposition.

Categorical: Ground, Uphold, Abstract, Analogy, Justify, Simplify, Redefine, Commit.

Contingent: Contest, Undercut, Elaborate, Contrast, Dispute, Complicate, Deconstruct, Withdraw.

Lanes, in the name key: Disposition, Imposition, Superposition.

Analogy stays the fourth categorical name. Liken is not a spelling of Analogy. Proposition stays the fifth position.

The public ledger is the name of this ledger. Keep those words wherever Version 5 already uses them.

The lane names stay in the name key, and they name the three lines of the illustrative ledger figure. They are not the interactive controls. The interactive controls are the three role lenses.

### Bodies · 27

The twenty-seven are these body names, and only these names. Each body shows the three role lenses on top, in Version 4’s column order: embodied agent, authoritative body, authoritative agent.

Embodied agent enacts and submits. Authoritative body approves or denies. Authoritative agent records and reviews and returns the account.

The name under each lens is the name Version 4 already prints in that column. Use this table and no other pairing.

| # | Embodied agent | Authoritative body | Authoritative agent |
|---|---|---|---|
| 1 | Governmental | Constitutional | Diplomatic |
| 2 | Legal | Judicial | Auditorial |
| 3 | Enforcement | Intelligence | Surveillance |
| 4 | Development logistics | Civic welfare | Property stewardship |
| 5 | Energy resources | Sanitation | Preservational |
| 6 | Medical | Scientific | Nutritional provision |
| 7 | Manufacturing | Commercial | Financial |
| 8 | Content creation | Media distribution | News journalism |
| 9 | Cultural | Educational | Religious |

The order runs Governmental, Constitutional, Diplomatic through Cultural, Educational, Religious. The roles are the meta layer of the bodies. They belong on the bodies. They are not names 28, 29, and 30, and they do not turn the twenty-seven into eighty-one.

### Domain eights, beside the sum

The domain eights sit beside the sum, in their own block, after it. They are not either twenty-seven.

Their meta labels are logical, categorical, and contingent. Those three words are the meta labels. No code is a meta label.

The logical eight equals the position eight: Supposition, Exposition, Reposition, Juxtaposition, Proposition, Composition, Decomposition, Deposition.

The categorical eight uses Liken, not Analogy: Ground, Uphold, Abstract, Liken, Justify, Simplify, Redefine, Commit.

The contingent eight equals the ledger contingent eight: Contest, Undercut, Elaborate, Contrast, Dispute, Complicate, Deconstruct, Withdraw.

Analogy stays on the ledger categorical eight. Liken stays on the categorical domain eight. State that the two names are not merged.

## Prohibitions that survive every improvement

Do not apply the retired-term standards sweep. The locked spec retires these as mode labels: haptic, visual, written, spoken, scripted, recorded, network, scriptive, narrative, documentative. A sweep would hunt those words, and might also treat *public ledger* as a term to retire. Do not run it. The five tabs keep their mode names. Version 4 prose that Version 6 carries keeps its words. Transcriptive stays verbatim. *Public ledger* stays.

Do not remove the public ledger. It stays in Interactive, under that name, with the eight centre events and the sixteen dashed branches.

Do not stamp Version 6 until Interactive and Transcriptive both have content. Interactive has content when the travelling map, the one-three-eight window, the public ledger, and the matrixes are in the file. Transcriptive has content when the 459-turn record is in the file, with the session line that includes `459 turns · time not recorded`. Band, masthead, and footer take Version 6 at that point, and not before. Do not write Version 6 into `design-system.json`. That file stays locked.

## The two files you write now

Both files are declarative. No might, arguably, perhaps, or seems. Both name Version 6 as a plan, not as a file already built. Both quote the sum as `8 codes + 27 ledger names + 27 bodies = 62`.

### Implementation strategy

Path: `<home>\.agents\skills\agents-sdk\design system\document\v6-implementation-strategy.md`

State:

- The only document file the follow-up creates: `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v6.html`.
- Version 4, Version 5, the Version 5 parts, the Version 5 plans, and the locked grammar stay byte-for-byte as they are.
- How the new HTML is produced from the Version 5 draft so that Interactive and Transcriptive already contain their content before the version stamp changes.
- The keep-list for each tab, in the terms of this prompt.
- Each improvement you will actually build, as a concrete change, after you have reviewed the draft.
- The interaction the ledger must keep: three role pills, authoritative body pressed at the start, eight centre inspections, sixteen branch previews that close on a second click, neither click changing the pressed role, no placement control.
- The stamp rule, and the check that both tabs have content before band, masthead, and footer read Version 6.
- Checks the follow-up must run: Version 4 unchanged, Version 5 unchanged, the four grammar files unchanged, the component files unchanged, the public ledger still present, the session line still containing `459 turns · time not recorded`, the sum line the same sentence in the name frame and the name key, body 1 blank on the codes and on bodies-by-ways, ways two and three empty there, Liken on the categorical domain eight, Analogy on the ledger categorical eight.

### Editorial plan

Path: `<home>\.agents\skills\agents-sdk\design system\document\v6-editorial-plan.md`

State the words:

- The sum, once, as the lede, addends in order.
- The ledger twenty-seven, with Analogy, Proposition, and the three lanes named in the key.
- The bodies twenty-seven, with the role lenses in Version 4’s column order, and the statement that the count is not eighty-one.
- The domain eights beside the sum, their three meta labels, Liken on the categorical eight, and the closed question that no code is a meta label.
- Proposition as the position and Propositional as the code. Environmental as the code and Preservational as the body name.
- What *The collective names* keeps, and what the corrected 62 key adds beside it.
- Per tab, the words you will change and the words you will leave. Descriptive records that nothing extra is required.
- 24-plus-3 and the set of sets remain proposed and undrawn, outside the sixty-two.
- Transcriptive: `VOICE` or `TEXT`, `CLAUDE · TEXT` only where the page already prints it, no clock times, the session line, verbatim.
- The public ledger stays. The retired-term standards sweep is not applied.
- Voice for anything you write: declarative, specific, short. Node labels at four words at most.

## Follow-up execution step

Do not start this step in the sitting that writes the plans.

When a later message tells you to build Version 6, or to execute the follow-up, build one new file:

`<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v6.html`

It sits beside Version 5. It expands on Version 5. It is a new file. It does not overwrite `The_Nine_Bodies_of_Authority_v4.html` or `The_Nine_Bodies_of_Authority_v5.html`.

Build to this prompt and to the two plan files. Where a plan file drifts from this prompt, follow this prompt.

Produce the HTML so Interactive already holds the travelling map, the one-three-eight window, the public ledger, and the matrixes, and Transcriptive already holds the 459-turn record, before band, masthead, and footer read Version 6. An empty shell is not stamped.

Leave these untouched while you build: the locked spec, `tokens.json`, `design-system.json`, `project\README.md`, every file under `project\components\`, Version 4, Version 5, `document\v5-parts\`, the Version 5 plans, `source\transcript.json`, and this prompt.

Use the locked components and tokens. Do not invent a sixth mode. Do not open a second Version 6 document.

After the file exists, run the checks the strategy names. Confirm Version 4 and Version 5 are unchanged, the grammar files are unchanged, Interactive and Transcriptive both have the content this prompt requires, the public ledger is present, and the Version 6 stamp is on the band, the masthead, and the footer.

Then stop. Report the path of the HTML file and the result of those checks.
