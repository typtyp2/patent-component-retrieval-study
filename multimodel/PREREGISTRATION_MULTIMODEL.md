# Multi-model replication of the name-recovery experiment (pre-specification)

Written 2026-11-10 before any generation call of this run. The SHA-256 of this file is recorded in
`outputs/manifest.json` before generation starts. This is an exploratory robustness extension added
after the primary results were known; it is reported in full regardless of outcome.

## Question

Do the main naming findings hold for other vision-language models and for a judge from another
provider?

1. Drawing gain on Targeted text: correct(Targeted text + drawings) − correct(Targeted text).
2. Drawing gain on Opening text: correct(Opening text + drawings) − correct(Opening text).
3. Text selection versus drawing access: correct(Targeted text) versus correct(Opening text + drawings).
4. Of numerals abstained under Targeted text and answered under Targeted text + drawings, the share
   that is correct.

## Items and inputs (unchanged)

- The 106 numerals in 42 patents of the main set. The 38-patent additional sample is not re-run.
- Four main conditions only: A = Opening text, B = Opening text + drawings, R = Targeted text,
  RI = Targeted text + drawings. Controls are not re-run.
- Prompts are byte-identical to the frozen prompts (A from `baselines/outputs/ablation_text_inputs.jsonl`,
  R from `baselines/outputs/ablation_inputs_frozen.jsonl`); the run asserts their SHA-256.
- Drawing pages, rendering and cropping are identical to the original runner (200 dpi, grayscale crop,
  RGB PNG, document order). Providers may resize images internally; this is not controlled.

## Generators

| ID | Model alias | Provider and access | Role |
|---|---|---|---|
| G0 | gpt-5.6-luna | recorded answers of 2026-09 (not regenerated) | original run |
| G1 | gpt-5.6-luna | OpenAI, Codex CLI, isolated configuration | rerun of the original model |
| G2 | gpt-6.1-terra | OpenAI, Codex CLI, isolated configuration | other OpenAI model, not a judge |
| G3 | claude-sonnet-5-5 | Anthropic, Claude Code CLI, tools disabled | other provider |
| G4 | claude-haiku-5-5 | Anthropic, Claude Code CLI, tools disabled | other provider, smaller model |

Isolated configuration: Codex runs with a separate configuration directory that holds only the login
file and `model_reasoning_effort = "medium"`, so no user instructions, memories, plugins or developer
instructions enter the prompt. Claude runs with `--setting-sources ""`, `--tools ""` and the original
system prompt. Both append the same closing line ("Return only the requested JSON object. Do not use
tools or add commentary."), which the original adapter also appended.

A response is valid only if it parses as a JSON object containing every requested numeral. Invalid
responses are retried up to four times and are never recorded as abstentions. A call that still fails
is reported as a failure.

## Scoring

- Judges: J1 gpt-5.6-luna and J2 gpt-6.1-sol (the original judges, same prompt) and J3 claude-opus-5-5
  (other provider, not a generator).
- All answers of G0–G4 for the four conditions are pooled, shuffled with a fixed seed and judged in
  batches of ten, with generator and condition hidden. Each judge scores the pool twice with different
  shuffles; the lower verdict is kept. Partial and "unknown" count as not correct.
- Primary score for this extension: majority of the three judges (correct if at least two judges give
  correct). Each judge is also reported separately, giving a generator × judge table.
- Judge calls that fail are retried and never recorded as incorrect.
- Snapshot check: agreement of the new J1 verdicts on G0 answers with the verdicts recorded in 2026-09.
- No human review for this extension.

## Analysis

- Per generator: correct, wrong and abstained counts per condition; contrasts 1–3 with the exact
  patent-level sign-flip test and 10,000 patent-level bootstrap 95% intervals (code reused from
  `baselines/ablation_oauth_run.py`); proportion 4.
- Across generators: per-patent net gain averaged over G1–G4, tested over the 42 patents. Generators are
  not pooled as independent samples.
- Interpretation: the drawing gain is called reproduced for a generator if its majority-judge RI − R
  net gain is positive with sign-flip p < 0.05. Non-significant results are reported as such, not as
  evidence of no effect. If results differ by model, the manuscript's claims are revised accordingly.
- The retrieval experiment is not repeated with other generators; this is stated as a limitation.
