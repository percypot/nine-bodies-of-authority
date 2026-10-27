# Version 7 audit prompt

You are Claude Code. This prompt is the whole brief for this sitting. Act on it. Do not ask for another conversation, and do not wait for a decision. The names, the counts, the tabs, the files, the open questions, and the stop are all here.

Prepared 27 October 2026. The document is *The Nine Bodies of Authority*. The system is Field Notation, locked at Version 4.

This sitting reviews what you designed and created, writes a critique, and writes the two plans for Version 7. Then it stops. A later prompt will build Version 7. This prompt is not that prompt. Do not build Version 7 in this sitting.

## This sitting, then stop

Do this sitting in this order, and then stop.

1. Read the files named below. Leave every one of them as you found it.
2. Write the audit. The four critique sections come first, in the order given.
3. Write the Version 7 implementation strategy.
4. Write the Version 7 editorial plan.
5. Return to the audit and write its last section, the decisions list.
6. Stop.

The sitting creates three files and no others:

- `<home>\.agents\skills\agents-sdk\design system\document\v7-audit.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v7-implementation-strategy.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v7-editorial-plan.md`

Write all three before any Version 7 HTML exists. Do not create `The_Nine_Bodies_of_Authority_v7.html`. Do not overwrite `The_Nine_Bodies_of_Authority_v4.html`, `The_Nine_Bodies_of_Authority_v5.html`, or `The_Nine_Bodies_of_Authority_v6.html`.

When the three files are written and the decisions list closes the audit, stop. Report their paths and stop. A later prompt will build Version 7. Begin that build only when a later message tells you to build Version 7. That later message is not this prompt. A sentence in this prompt that names the future HTML file is a path for the plans to cite. It is not permission to create the file.

## Read these files

Read them. They are the work under review. Do not edit them. Do not score them into the rubric files.

### Locked grammar baseline

Version 4 is the locked grammar. Read it and use it. Do not retoken it, restyle it, or edit it in order to improve the document.

- `<home>\.agents\skills\agents-sdk\design system\spec\Field_Notation_v4_spec.md`
- `<home>\.agents\skills\agents-sdk\design system\project\tokens.json`
- `<home>\.agents\skills\agents-sdk\design system\project\design-system.json`
- `<home>\.agents\skills\agents-sdk\design system\project\README.md`
- `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v4.html`

There is no `README.md` at the repository root. The locked README is `project\README.md`.

Read every component under `<home>\.agents\skills\agents-sdk\design system\project\components\`. Each component’s `README.md` and `preview.html` is part of the locked grammar. Read `components\bundle.js` and `components\bundle.css`. The folders present are Toggle, NodeRoute, Inspector, ViewTabs, Compass, Chip, Table, Spine, CanCannot, Status, Fold, Trail, Rail, Transcript, Script, Matrix, and CrossRef. Masthead is specified in `project\README.md` and has no component folder. `bundle.js` and `bundle.css` cover Compass, NodeRoute, Inspector, Toggle, and ViewTabs.

`The_Nine_Bodies_of_Authority_v4.html` is the reference rendering of that grammar. Read it to keep the pairings it already prints. The design-system rubric does not grade that HTML. The audit may say what the rendering holds and where the draft departs from it. That is a critique of the relationship. It is not a score of Version 4.

### Current draft

Version 6 is the current draft. `The_Nine_Bodies_of_Authority_v6.html` is Version 5 revised: it keeps Version 5’s content and the fixes already in Version 6. Read the whole file.

- `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v6.html`

Read Version 5 as the file Version 6 revises. Leave it unchanged. If Version 6 is missing Version 5 content, the later build folds that content in. Do not throw away Version 6’s existing fixes. This sitting does not edit either HTML file.

- `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v5.html`

Read these companions and leave them unchanged. They are fragments and earlier plans, not a second draft to build from.

- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\interactive-ledger.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\interactive-matrix.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\name-key.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-parts\transcriptive.html`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-implementation-strategy.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v5-editorial-plan.md`

### Version 6 prompt, rubrics, and plans

Read these if they are present. They are present in this repository unless a path fails. If a path is absent, say so in the audit lede and continue with the files that are there. Do not invent a missing rubric. Do not edit any of them.

- `<home>\.agents\skills\agents-sdk\design system\document\v6-claude-prompt.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v6-rubric-design-system.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v6-rubric-document.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v6-implementation-strategy.md`
- `<home>\.agents\skills\agents-sdk\design system\document\v6-editorial-plan.md`

`v6-claude-prompt.md` is the brief of the previous sitting. The two rubric files are the criteria for this audit. The Version 6 strategy and editorial plan are that sitting’s plan for the Version 6 HTML. `The_Nine_Bodies_of_Authority_v6.html` is present. It is the current draft, and it is Version 5 revised.

Test the Version 6 plan against the files you read. Carry a line into the Version 7 plans when the audit finds the line still true. Replace a line when the audit finds it wrong. Do not treat those plans as a reason to skip the reading.

The 459-turn record is the one already in the Version 6 Transcriptive tab, carried from Version 5 and from `document\v5-parts\transcriptive.html`. Its source is Untitled document (15). `<home>\.agents\skills\agents-sdk\design system\source\transcript.json` is the 127-turn Percy log. Do not replace the 459-turn record with that log, and do not rebuild Transcriptive from it.

## Leave these files untouched

Leave these byte-for-byte as you found them:

- the four grammar files, every file under `project\components\`, and any font files you open under `project\fonts\`
- `document\The_Nine_Bodies_of_Authority_v4.html`
- `document\The_Nine_Bodies_of_Authority_v5.html`
- `document\The_Nine_Bodies_of_Authority_v6.html`
- `document\v5-parts\` and both Version 5 plans
- `document\v6-claude-prompt.md`, both rubric files, and both Version 6 plans
- `source\transcript.json`
- this prompt

Do not edit Version 4. Do not edit Version 5. Do not edit Version 6. Do not edit the rubrics. Do not fill either score record. Do not write a Version 7 score into a rubric. Do not apply the retired-term standards sweep to any file.

## Order of authority

Use this order when two sources disagree.

1. The locked frame in this prompt, for the tabs, the census, the roles, the ledger controls, the domain eights, the record, the public ledger, and the prohibitions.
2. The Version 4 grammar files, for mode mechanics, voice, tokens, components, line grammar, and interaction the frame does not restate. Where a sentence in this prompt and a grammar file disagree on a fact of the grammar, the grammar file wins, and the audit records the disagreement as a tension.
3. The two rubrics, as criteria. Where a rubric sentence and a grammar file disagree on a fact of the grammar, the grammar file wins. Where a rubric sentence and this locked frame disagree on the census, the tabs, the ledger, or the record, this locked frame wins, and the audit records the tension.
4. `v6-claude-prompt.md` and the earlier plans, as work to review. They do not override this prompt.
5. The two Version 7 plans you write in this sitting. Where a plan drifts from this prompt, this prompt wins. Correct the plan before you stop.

Version 6 is the draft under review. It is Version 5 revised. It is not an authority over the locked frame.

## Locked frame

Carry this frame into the audit, both plans, and the decisions list. Version 7 keeps it. A plan line that moves it is not a plan line.

### Five tabs

Five modes, tab order left to right: Interactive, Illustrative, Comprehensive, Descriptive, Transcriptive. Interactive opens first. With no mode in the hash, the selected tab is Interactive. Keep the hash behaviour Version 6 already has, carried from Version 5, so a stored reference still opens its mode.

Interactive is the live space. The four outputs are illustrative, comprehensive, descriptive, and transcriptive. Do not add a sixth mode. Do not rename a mode. Do not reorder the tabs.

### The 62

The sum, in the corrected name key and in the Comprehensive name frame, is this line, said once as the lede:

8 codes + 27 ledger names + 27 bodies = 62

The three addends follow in that order. The domain eights are not a twenty-seven inside the sum. The three role names are not a fourth addend. The count is not 81.

24-plus-3 and the set of sets stay proposed until decided. 24-plus-3 is the count of the sequence plus meta. The set of sets is its label. Both stay outside the sixty-two. Both stay undrawn. This sitting does not decide them. The decisions list asks the question. Until that question is answered, the plans keep them proposed, undrawn, and outside the sixty-two.

### Codes · 8

The eight codes sit on bodies 2 through 9. Body 1 has no code. No code is written on body 1. Body 1 still carries its three role names.

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

Categorical, with Analogy in the fourth seat: Ground, Uphold, Abstract, Analogy, Justify, Simplify, Redefine, Commit.

Contingent: Contest, Undercut, Elaborate, Contrast, Dispute, Complicate, Deconstruct, Withdraw.

Lanes, in the name key: Disposition, Imposition, Superposition.

Analogy stays the fourth categorical name on the ledger. Liken is not that name. Proposition stays the fifth position. These twenty-seven, including the three lane names, stay in the name key.

The lane names stay in the name key, and they name the three lines of the illustrative ledger figure. They are not the interactive controls.

The public ledger stays. Keep that name wherever Version 6 already uses it, as Version 5 did. It stays in Interactive, with the eight centre events and the sixteen dashed branches.

### Bodies · 27

The twenty-seven are these body names, and only these names. Each body shows the three role lenses on top, in Version 4’s column order: embodied agent, authoritative body, authoritative agent.

Embodied agent enacts and submits. Authoritative body approves or denies. Authoritative agent records and reviews and returns the account.

The name under each lens is the name Version 4 already prints in that column.

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

Liken stays on the categorical domain eight. Analogy stays on the ledger. State that the two names are not merged.

### Ledger behaviour

Ledger controls are the three role lenses: embodied agent, authoritative body, authoritative agent. Authoritative body starts pressed. The pressed role is the centre line.

The role pills are the control that changes which role is pressed.

The eight centre events are the categorical imposition. A click on a centre event inspects the position, the categorical name, and the release. That click leaves the pressed role as it is.

Sixteen dashed branches, two per position, sit off that centre. A click on a branch previews the position, the contingent name, and that role’s archive line. The archive line is the line for the role the branch belongs to. Clicking that branch again closes the preview. A branch click leaves the pressed role as it is.

Centre clicks and branch clicks are not the control that changes the pressed role.

There is no placement control. Do not add a pill, a drag, or any other control that places an event on a different position.

Disposition, Imposition, and Superposition are not the ledger controls. Those lane names stay in the name key and on the illustrative figure.

### Matrixes and ways

Interactive keeps Version 4’s travelling map, one window, the public ledger, and the matrixes: Version 4’s own matrixes, the domain matrixes, and bodies-by-ways.

The window is *One path of eight*, on the eight codes. Scale 8 is the whole path. Scale 3 is the current station and its two neighbours. Scale 1 is the current station. Eight, the whole path, is the scale that starts pressed. Keep one window. Do not add a second.

Domain matrixes use Liken on the categorical eight. Bodies-by-ways keeps body 1 blank, the eight codes on bodies 2 through 9, and way two and way three empty. Ways 2 and 3 stay empty. Version 4’s own matrixes stay, showing what Version 4 already shows.

Way one, way two, and way three stay the three routes Version 4 draws.

### What each tab keeps

**Interactive.** The travelling map is live. The one window, the public ledger, and the matrixes are on this tab, with the ledger behaviour and the ways rule above.

**Illustrative.** Version 4’s figures stay, including the cube. One further figure shows the ledger of eight plus sixteen, the eight codes, and the nine triads. The figure’s three lines are Disposition, Imposition, and Superposition. Those line names are the figure. The role lenses remain the controls on Interactive. 24-plus-3 and the set of sets stay marked proposed, and they stay undrawn, until the decision says otherwise.

**Comprehensive.** Version 4’s prose stays. The original name key remains under the heading *The collective names*. The corrected 62 name key sits beside that key. The corrected key is the census. It does not delete *The collective names*. The sum is the lede of the name frame. The domain eights follow in their own block.

**Descriptive.** The water case is nine passages, one for each body, in body order. The nine stay. A passage Version 4 already prints besides those nine stays, and the editorial plan names it. A further passage is named in the editorial plan before a later build adds it.

**Transcriptive.** The tab holds the 459-turn record of Untitled document (15). Kickers are voice or text: `VOICE` or `TEXT`. Print `CLAUDE · TEXT` only on the turns where Version 6 already prints `CLAUDE · TEXT`, carried from Version 5. Add no speaker name to the other kickers. Add no clock time. The session line includes `459 turns · time not recorded`. Keep the line Version 6 already prints: `Session 1 · 459 turns · time not recorded`. Transcriptive stays verbatim. Fillers, misspellings, hedges, and a word *Claude* inside a turn’s text stay. The 127-turn Percy log stays out of this tab.

### Grammar locks the plans keep

Take these from the grammar files, and keep them. Where this list and a grammar file disagree, the grammar file wins.

- Seven forms only. No `-al` forms. Agent nouns take `-er`. Descriptive’s adverb is `descriptively`. Transcriptive’s adverb is `transcriptively`. Comprehensive keeps its stem split: `comprehensive`, `comprehension`, and `comprehensively` use comprehens-; `comprehend`, `comprehendable`, `comprehender`, and `comprehending` use comprehend-. Illustrative keeps `illustratable` and `illustrater`.
- Voice: declarative sentences. No might, arguably, perhaps, or seems. May is permission only. Unfinished work goes on a list headed *Next*. Transcriptive is exempt and stays verbatim.
- Tokens, line grammar, grounds, type voices, and the one `focal`. Solid is settled. Dashed is contingent. Dotted is held. Colour is never the only signal.
- The full tab pattern, the shared reference in the URL hash, and the components named above.

### Prohibitions

Do not apply the retired-term standards sweep. The locked spec retires these as mode labels: haptic, visual, written, spoken, scripted, recorded, network, scriptive, narrative, documentative. A sweep hunts those words, and it treats *public ledger* as a term to retire. Do not run it. The five tabs keep their mode names. Version 4 prose that Version 7 carries keeps its words. Transcriptive stays verbatim. *Public ledger* stays.

Do not remove the public ledger.

Do not add a code on body 1, a filled way two or way three on the bodies-by-ways matrix, an eighty-one-name count, Liken on the ledger categorical eight, or Analogy on the categorical domain eight.

Do not stamp a Version 7 file in this sitting. There is no Version 7 file. The strategy may state the later stamp rule: band, masthead, and footer read Version 7 only when Interactive and Transcriptive both have the content this prompt requires, from one version source. `design-system.json` is not given a Version 7 stamp. That file stays locked.

## Rubrics are the criteria

Use both rubrics as the audit’s criteria. Do not use them as a score of Version 7. Version 7 does not exist yet, so it has no score.

`v6-rubric-design-system.md` scores a design system on six dimensions: visual clarity, comprehensibility, component grammar consistency, token usage, interaction design, accessibility.

`v6-rubric-document.md` scores a five-tab document on six dimensions: conceptual originality, significance, quality of prose, idea coherence, structural integrity of the five tabs, fidelity to the locked frame.

Read each dimension’s top-score conditions and failure modes. Apply them in prose. Name the dimension when a claim uses it. A criterion is a test. It is not a number you award.

Do not record a score from 0 to 4 for Version 7. Do not record a score from 0 to 4 for Version 4 or Version 5 in this sitting. Do not fill the score record in either rubric. Do not edit the rubrics. The audit is a review and a critique. The plans say what must change so a later file can meet these criteria. They do not pretend the file has already met them.

The design-system rubric’s section *Baseline tensions* names disagreements inside the grammar. Apply the owner table in that rubric. Do not resolve those tensions by grading Version 4 or Version 5, and do not resolve them by editing a grammar file. If a Version 7 choice is blocked until one of those tensions is decided, put the question on the decisions list.

A pass that would edit authored prose only to look clearer fails the design-system rubric’s comprehensibility criterion. Version 4 prose that this frame says to carry stays word for word. A new sentence belongs in the editorial plan, quoted, before a later build writes it.

## How every claim is tied

Every claim in the audit and in both plans needs a rationale tied to a file, a tab, or a named rule.

A file tie names the path and the region: a heading, a selector, a component, a table, or a quoted string you found there. A tab tie names one of the five tabs. A rule tie names the rule and where it is written: a heading in this prompt’s locked frame, a section of the spec, a rubric dimension, or a component README.

A claim you cannot tie is not written. A claim about a region you did not open is not written. Write the rationale in the same breath as the claim.

The three files you write are declarative. No might, arguably, perhaps, or seems. May is permission only. Transcriptive quotations, if you must quote a turn, stay verbatim.

## The audit

Path: `<home>\.agents\skills\agents-sdk\design system\document\v7-audit.md`

Title it *Audit for Version 7*. Open with a short lede: the date, the files you reviewed, and the statement that Version 7 has no score because the HTML does not exist. The lede is not one of the sections below.

Then write these sections, in this order, and no other critique sections. This is a review and a critique of the grammar, the Version 4 rendering, the Version 5 draft, the Version 6 prompt, the rubrics, and the Version 6 plans. It is not a rebuild and not a score sheet.

### Strengths

What is working well. For each strength, say where it is working and which rule or criterion it already meets. The plans carry these forward. A feature that breaks the locked frame is not a strength. It belongs under weaknesses.

### Non-negotiables

What must not change at all. Include every item in the locked frame of this prompt. Add a grammar rule when a baseline file locks it and Version 7 would break the author’s intent by moving it. Each item names the rule and the file, the tab, or the heading that shows it in force. A non-negotiable does not appear on the decisions list. This sitting does not reopen it.

### Optional changes

Stylistic changes, and other changes that are not significant. Mark every item optional. Begin each item with the word Optional. Say what would change, where, and why it is not significant.

An optional change does not alter the locked frame, does not answer a rubric failure, and does not repair a broken behaviour. If it would, it belongs under weaknesses. If you find no optional change that survives that test, say so in one sentence. Do not invent nits.

The plans repeat each optional item and keep it marked optional. A later build may leave it undone.

### Weaknesses, areas to improve, and tensions to resolve

What is wrong, what falls short of a named criterion, and what is in tension between files. For each item write all of these:

- What is wrong, or what the tension is.
- Where it sits: file, tab, or rule.
- The criterion it fails, or the two rules that disagree.
- What to do to resolve it.
- Why that resolution makes the work a clearer form of the author’s intent.

A resolution the locked frame forbids is not written. A resolution that needs a choice the frame does not already make is marked blocked. The choice waits for the decisions list. The plans do not smuggle that choice in as a settled change.

Cover the five tabs. If a tab has no weakness, say it is sound and name the rule it meets. Do not leave a tab unmentioned.

## What Version 7 is

Version 7 is a plan in this sitting and a new file in a later sitting. The later file is:

`<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v7.html`

It sits beside Version 6. It is a new file. It does not overwrite Version 4, Version 5, or Version 6. This sitting does not create it.

The author’s intent is the locked frame in this prompt together with the Version 4 grammar. Polished means a surface that can meet the design-system rubric’s criteria. Comprehensive means all five tabs doing the jobs this prompt names, with the census, the ledger, and the record intact. Clear means each name in the place this prompt gives it, in declarative sentences, with one path through the document.

The two plans say what Version 7 must change, adjust, apply, and transform so the work becomes that form. Use those four words for the actions you actually specify:

- **Change** a concrete edit from what the current draft does now.
- **Adjust** a behaviour so it matches a rule it already nearly follows.
- **Apply** a locked rule or a rubric criterion the draft does not yet meet.
- **Transform** a region so the author’s intent reads as one system across the tabs.

Each action names where, what the draft does now, what Version 7 will do, and why. Each action cites the audit item it comes from. An action the audit marked blocked stays blocked in the plan and points at the decision. It is not carried out in prose as if it were chosen.

Both plans quote the sum as `8 codes + 27 ledger names + 27 bodies = 62`. Both name Version 7 as a plan, not as a file already built. Both say that a later prompt builds the HTML and that this sitting does not.

## Implementation strategy

Path: `<home>\.agents\skills\agents-sdk\design system\document\v7-implementation-strategy.md`

State:

- The only document file a later prompt creates: the Version 7 HTML path above. This sitting does not create it.
- Version 4, Version 5, the Version 5 parts, the Version 5 plans, the Version 6 HTML, the Version 6 prompt, the Version 6 plans, both rubrics, and the locked grammar stay as they are.
- The later build starts from the Version 6 file and writes a new file. It does not start from Version 5, and it does not start from an empty shell. It does not overwrite Version 5 or Version 6. Version 6 is Version 5 revised: it keeps Version 5’s content and the fixes already in Version 6. If Version 6 is missing Version 5 content, the later build folds that content in. Do not throw away Version 6’s existing fixes. Interactive already holds the travelling map, the one window, the public ledger, and the matrixes, and Transcriptive already holds the 459-turn record, before band, masthead, and footer read Version 7.
- The keep-list for each tab, in the terms of this prompt.
- Each change, adjustment, application, and transformation you will actually have the later build do, after the audit. Optional items stay marked optional.
- The ledger behaviour this prompt locks: three role pills, authoritative body pressed at the start, eight centre inspections, sixteen branch previews that close on a second click, neither click changing the pressed role, no placement control. Lane names stay in the name key.
- The stamp rule, and the check that both tabs have content before the version string reads 7, from one source. `design-system.json` stays untouched.
- What is blocked until a decision in the audit is answered. Point at that section. Do not answer it here.
- Checks the later build must run, and the statement that this sitting does not run them because the Version 7 HTML does not exist. If `<home>\.agents\skills\agents-sdk\design system\tools\` already contains a build script or a check for content, behaviour, focal, tokens, or accessibility, you may re-run the scripts that are present. Do not invent a script that is not there. Re-running a present script does not permit this sitting to build Version 7 HTML. The checks include: Version 4 unchanged, Version 5 unchanged, Version 6 unchanged, the grammar files unchanged, the component files unchanged, the rubrics unchanged, the public ledger still present, the session line still containing `459 turns · time not recorded`, the sum line the same sentence in the name frame and the name key, body 1 blank on the codes and on bodies-by-ways, ways 2 and 3 empty there, Liken on the categorical domain eight, Analogy on the ledger categorical eight, authoritative body pressed at the start, no placement control, the retired-term sweep not applied, and 24-plus-3 still proposed unless the decision has been answered before the build.

## Editorial plan

Path: `<home>\.agents\skills\agents-sdk\design system\document\v7-editorial-plan.md`

State the words:

- The sum, once, as the lede, addends in order.
- The ledger twenty-seven, with Analogy, Proposition, and the three lanes named in the key.
- The bodies twenty-seven, with the role lenses in Version 4’s column order, and the statement that the count is not eighty-one.
- The domain eights beside the sum, their three meta labels, Liken on the categorical eight, and the closed question that no code is a meta label.
- Proposition as the position and Propositional as the code. Environmental as the code and Preservational as the body name.
- What *The collective names* keeps, and what the corrected 62 key adds beside it.
- Per tab, the words Version 7 will change and the words it will leave. Any new or changed string is quoted here before a later build writes it. Descriptive records the nine water passages and names any further passage the draft already carries. Nothing extra is added unless the audit’s resolution requires it, and that sentence is quoted.
- 24-plus-3 and the set of sets remain proposed and undrawn, outside the sixty-two, until the decision says otherwise.
- Transcriptive: `VOICE` or `TEXT`, `CLAUDE · TEXT` only where the page already prints it, no clock times, the session line, verbatim. A fix that makes the record parse keeps the turn’s words. It does not rewrite them.
- The public ledger stays. The retired-term standards sweep is not applied.
- Voice for anything the later build writes: declarative, specific, short. Node labels at four words at most.
- What is blocked until a decision is answered. Point at the audit. Do not answer it here.

## Decisions to lock before Version 7

Write this section last, after both plans exist. It is the last section of `v7-audit.md`, under the heading *Decisions to lock before Version 7*. It is not one of the four critique sections, and it does not replace them. The implementation strategy and the editorial plan do not keep a second list. They point here.

These are the decisions to determine, lock, ratify, or change and make canonical before creating Version 7. This sitting records them. It does not answer them. It does not build past them.

Each item has three parts:

- **Question.** One question.
- **Options.** The real options. Include leaving the current practice in place when that is a real option.
- **Blocked until answered.** The plan line, the region, or the check that cannot be settled until the question is answered.

Include this question even if the rest of the plan is clear:

- Question: Do 24-plus-3 and the set of sets stay proposed, become canonical and drawn while remaining outside the sixty-two, or drop out of the document?
- Options: stay proposed and undrawn, outside the sixty-two; ratify them and draw them, still outside the sixty-two; remove the proposal.
- Blocked until answered: any Version 7 figure, sentence, or count that would draw them, fold them into the sixty-two, or delete the proposal. Until the question is answered, both plans keep them proposed, undrawn, and outside the sixty-two.

Add every other question the audit cannot settle from this locked frame and the grammar files. A disagreement the design-system rubric already names under *Baseline tensions* belongs here when a Version 7 choice would require a locked grammar file to change, or when the document cannot meet a criterion without that change. The HTML build does not edit those grammar files either way. Say which choice is blocked: the grammar edit, the document’s colour or type, or both.

Do not put a locked-frame item on this list as if it were open. The tab names, the sum, the role lenses, Liken and Analogy in their two places, the ledger controls, the lane names in the key, authoritative body starting pressed, the eight inspections, the sixteen previews, empty ways 2 and 3, body 1 with no code, the 459-turn record, the voice and text kickers, the absence of clock times, the closed meta-label question, the public ledger, and the refusal of the retired-term sweep are already canonical. They are non-negotiables.

If the audit finds no further question, say that the 24-plus-3 question is the only decision still open, and say what that leaves unblocked.

## Stop

Stop here.

Do not build Version 7. Do not create `<home>\.agents\skills\agents-sdk\design system\document\The_Nine_Bodies_of_Authority_v7.html`. Do not overwrite Version 4, Version 5, or Version 6. Do not edit the grammar, the components, the rubrics, the Version 6 prompt, the Version 6 plans, or this prompt. Do not score Version 7. Do not fill a score record.

If `<home>\.agents\skills\agents-sdk\design system\tools\` contains a build script or checks for content, behaviour, focal, tokens, or accessibility, you may re-run the scripts that are present. Do not invent a script that is not there. That permission ends at those files. It does not extend to building Version 7 HTML.

The three files this sitting writes are the audit, the implementation strategy, and the editorial plan. The decisions list is the last section of the audit. When those are written, this sitting is over.

A later prompt will build Version 7. Wait for that prompt. This file does not contain the build, and it does not authorise you to start one.
