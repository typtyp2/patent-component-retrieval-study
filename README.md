# Patent component names: retrieval analysis artifacts

This repository accompanies the manuscript **Naming Reference Numerals in Patent Drawings with Vision-Language Models** (work in preparation; not accepted or peer-reviewed).

## Scope

This release contains 3,708 rows of derived per-query retrieval metrics, identifiers for 26 evaluation patents, source-file hashes, and a dependency-free descriptive reaggregation script. It supports the additional metric and translation-exposure subset analysis in Supplementary Section S16. It is **not a complete reproduction of the generation, indexing, statistical testing or human naming experiments**.

It also contains the outputs of the multi-model replication of name recovery (manuscript Section 4.6, Supplementary Section S17) in `multimodel/`:

- `PREREGISTRATION_MULTIMODEL.md`: the plan fixed before generation (SHA-256 `c68367e2...`, recorded in `manifest.json`).
- `answers_G1.jsonl` to `answers_G4.jsonl`: 168 generation calls each (42 patents, four conditions) for gpt-5.6-luna (rerun), gpt-6.1-terra, claude-sonnet-5-5 and claude-haiku-5-5. Each line holds the patent file identifier, condition (A = Opening text, B = Opening text + drawings, R = Targeted text, RI = Targeted text + drawings), the answers by numeral, the prompt SHA-256, token usage and the UTC time of the call.
- `judgments_J1.jsonl` to `judgments_J3.jsonl`: verdicts of gpt-5.6-luna, gpt-6.1-sol and claude-opus-5-5 on all pooled answers, two passes each. Keys are `generator|patent|numeral|condition`; G0 denotes the original 2026-09 answers, whose text is not included in this release.
- `multimodel_results.json`, `multimodel_report.txt`: aggregate counts, paired contrasts and agreement checks as reported in the manuscript.
- `manifest.json`: plan and runner hashes, model aliases, tool versions, prompt hashes and drawing-page selections.

Prompts, patent text, drawing images and reference-sign lists are not included, so the verdicts cannot be recomputed from this release alone.

No patent full text or drawing PDFs, credentials, reviewer identities, personal review records, model-access wrappers, or unrelated application code are included. Redistribution rights for the underlying document corpus have not been established. Numeric query keys retain the local patent file identifiers and target numerals for traceability; identifiers have not been independently verified against patent-office registries.

## Reproduce

Run `python reproduce.py` with Python 3.10 or later. No third-party packages or API calls are required. The script writes `reproduced_means.json` and verifies the full-sample means against `data/expected_means.json` to absolute tolerance 1e-12.

The CSV contains these query sets:

- `name`: 138 English component-name queries, original-language documents, 26 patents.
- `free_worded`: 137 model-written questions, all-English setting, 26 patents.
- `name_containing`: 137 model-written name-containing questions, all-English setting, 26 patents.

Each query has scores for BM25, text-embedding-3-small and text-embedding-3-large under C0 (no insertion), C1 (text-derived names), and C2 (drawing-assisted names). Metrics are nDCG@10, MRR@10, and Recall@10 with the original automatic relevance labels. Means are calculated within patent, then averaged equally across patents. These are stored metrics, not reranked documents.

`translation_exposed=1` marks seven query identifiers affected by the prior translation audit (nine item–chunk pairs). The exclusion analysis applies only to the two all-English question sets, leaving 130 queries and 26 patents. It excludes queries without rebuilding indexes, so cross-numeral insertion effects remain. The flag is included on name-query rows for traceability, not as evidence that the original-language corpus had translation exposure.

## Limitations

No new significance tests are performed. Descriptive differences must not be reported as statistically significant on the basis of this code. Independent human questions and expert relevance labels are not yet collected. One residual reference-list item remains unresolved. The release omits historical result JSON fields whose primary/exploratory roles or multiplicity labels do not reflect the final protocol; consult the manuscript for those distinctions.

## Reuse

No open-source or data license has yet been assigned. Public access does not itself grant an unrestricted reuse license. A licensing decision is pending rights-holder confirmation.
