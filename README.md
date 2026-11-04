# Embedding-model migration for retrieval: a critical review of compatibility targets and evaluation evidence

**Authors:** Tripti Tiwari (first author) and Mohit Tiwari (corresponding author).

**Manuscript status:** Prepared for submission to *Computing* (Springer Nature). This repository does not claim acceptance or publication.

## Purpose
The review compares 20 purposively selected full-text studies covering backward-compatible training, vector translation, mixed-gallery refresh/backfilling, threshold calibration, and graph-index migration. It distinguishes five evidence targets: coordinate approximation, same-item correspondence, judged task relevance, threshold behavior, and serving-index fidelity.

## Reproducibility
The study's numerical examples are **constructed mathematical counterexamples**, not tests of trained embedding models or production retrieval systems. The paper reports 5,000 randomized arithmetic checks with seed 20261104; 3,338 certified stable top-three sets, 667 changed uncertified sets, and zero certificate violations. The program in `code/constructed_checks.py` regenerates the constructed results.

## Evidence
**Public now:** `evidence/study_summary.csv`, `code/constructed_checks.py`, `evidence/constructed_results.json`, and `evidence/randomized_cases.json`. The remaining source-level records (the complete assessment ledger, source hashes, reference-verification records, and search log) are contained in the journal supplementary archive `ESM_1_Embedding_Migration.zip`. Once that ZIP is uploaded at the repository root, `.github/workflows/publish-evidence.yml` will validate its inventory, reproduce the 5,000 arithmetic checks, and publish the source records as browsable files. **The complete ledger is not publicly hosted here until those extracted files appear.**

Full-text third-party publications are not redistributed. This is a critical, purposive review; not a systematic literature census, independent replication, or new algorithm evaluation.

## Suggested data availability text (after repository population is verified)
"The study-extraction ledger, citation verification records, source manifest, search records, comparison tables, constructed analytical examples, and executable verification code supporting this critical review are available at https://github.com/profmohit-edu/embedding-model-migration-review. The corresponding supplementary material is also provided as Online Resource 1 with the manuscript. Third-party full texts are accessible via their original publishers and repositories, subject to access conditions."
