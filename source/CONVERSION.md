# Untitled 15 → Recorded log

Locked 26 October 2026. Recorded uses this file only:

- [transcript.json](transcript.json) in this folder (127 turns, speakers `percy` and `claude`)

The same bytes also sit at `<home>\Downloads\nine_bodies_untitled15_transcript.json`. That copy is a duplicate, not a second source.

## Why this log

The Field Notation spec kicker is `PERCY · VOICE` / `CLAUDE · TEXT`. This log’s speakers match that kicker. Parties are only Percy (human) and Claude (AI). Dex / Grok / ChatGPT from the Four-Way pack were used as a shape hint and were not added.

Source: `Untitled document (15).pdf` (109 pages), the voice-to-text working file that generated the Nine Bodies model. Words were split one-per-line by export and have been rejoined. The PDF has no clock times, so every `at` is `null`. Do not invent times.

`via` is inferred. Percy turns are voice. Claude turns are text unless fillers appear. Misspellings stay (`thingts`, `constituional`, `survaillance`).

`meta.version` is `"4"`. That is the document edition, not a claim that Recorded is a clean speaker log.

## What is not merged

Do not adopt `<home>\Downloads\nine-bodies-transcript.json`.

| | Kept log | Parallel log |
|---|---|---|
| Path | [transcript.json](transcript.json) | `<home>\Downloads\nine-bodies-transcript.json` |
| Turns | 127 | 185 |
| Speakers | `percy`, `claude` | `percy`, `ai` |
| Spec kicker | Matches `CLAUDE · TEXT` | Would read `AI · TEXT` |
| Note | Four-Way layout used only as a shape | Says the format reference never arrived |

Both are splits of the same PDF. Two verbatim Recorded tabs cannot exist. The 185-turn file is a parallel conversion, not a correction.

A later remap of field names is allowed. Adding a third speaker is not. Merging the two JSON files is not.

## Thirteen flagged turns

Recorded can ship with these flags visible. It cannot be called clean until this pass. Transcription doubt in the UI is `[?]`, matching the line grammar.

| id | Speaker | via | Flags | Why it is flagged |
|---|---|---|---|---|
| t0010 | percy | voice | `possible-overlap` | Claude acknowledgement sits inside Percy’s speech. |
| t0013 | percy | voice | `possible-overlap` | Short Percy turn (“Is auditorial a word”) may share a beat with Claude. |
| t0014 | claude | text | `possible-overlap` | “Checking that quickly.” may be glued to the previous beat. |
| t0045 | percy | voice | `possible-overlap` | A Claude clause (“communicate that more clearly than ‘authority agent’…”) sits inside Percy’s turn. |
| t0056 | percy | voice | `possible-overlap` | “Mm-hm.” and “Checking it in that frame.” sit inside Percy’s speech. |
| t0072 | percy | voice | `attachment-noise` | Pasted or exported document prose is inside the turn. |
| t0073 | claude | text | `attachment-noise`, `possible-overlap` | Filename/document paste plus “Checking that quickly.” |
| t0075 | percy | voice | `attachment-noise` | Pasted confirmation prose inside Percy’s speech. |
| t0082 | claude | text | `attachment-noise` | Raw paste list (`Pasted text.txt`, image filenames). |
| t0083 | percy | voice | `attachment-noise` | UI chrome (“output thisClaude”) inside Percy’s speech. |
| t0092 | claude | text | `attachment-noise` | Tool chrome (“Searching available tools Google Drive…”) mixed with Percy’s “stop doing that” correction. |
| t0093 | percy | voice | `attachment-noise` | Tool chrome (“Used 3 tools”) and a wrong-file correction inside the turn. |
| t0105 | claude | voice | `attachment-noise` | Account-boundary note and a generated doc title sit in the turn. `via` is voice here; treat as inferred. |

See also [TRANSCRIPT_NOTE.md](TRANSCRIPT_NOTE.md) for the original conversion note. This file is the lock: which log Recorded uses, which log it does not, and which turns still need a clean split.

## Disposition pass (26 October 2026)

Explicit dispositions for the thirteen CONVERSION flags plus `t0028` / `t0032` live in [FLAGGED_DISPOSITION.md](FLAGGED_DISPOSITION.md) and on each turn in `transcript.json` (`disposition`, `disposition_note`).

| Disposition | Meaning |
|---|---|
| `kept-overlap-marked` | Possible speaker glue retained; no invented split without timed audio. |
| `kept-doubt-marked` | Transcription doubt retained; UI shows `[?]`. |
| `kept-mixed-paste` | Speech and paste still glued; flag retained. |
| `noise-trimmed` | Separable UI/paste chrome removed; flag cleared. |
| `noise-only-held` | Turn is filenames/chrome only; flag retained; id kept stable. |
| `resolved-as-content` | Flag cleared because the text is legitimate status speech. |

A full clean speaker split still needs a timed source. Until then Recorded ships with these dispositions visible.
