# Patent component names: retrieval analysis artifacts

This repository accompanies the manuscript **Recovering the Meanings of Patent Drawing Reference Numerals with a Vision-Language Model: Drawing Access versus Text Selection** (work in preparation; not accepted or peer-reviewed).

## Scope

This initial release contains 3,708 rows of derived per-query retrieval metrics, identifiers for 26 evaluation patents, source-file hashes, and a dependency-free descriptive reaggregation script. It supports the additional metric and translation-exposure subset analysis in Supplementary Section S16. It is **not a complete reproduction of the generation, indexing, statistical testing or human naming experiments**.

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
