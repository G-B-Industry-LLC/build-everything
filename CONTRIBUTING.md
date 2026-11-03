# Contributing

Build Everything accepts small, testable learning labs.

## A good contribution

- rebuilds one recognizable technology or subsystem;
- works without paid services;
- teaches the underlying contract rather than hiding it behind a framework;
- has a bounded scope that a learner can finish;
- includes automated acceptance tests;
- states security limitations and intentional omissions;
- uses original writing or properly licensed sources.

## Lab lifecycle

1. **Proposed** — the catalog entry defines the outcome and proof.
2. **In progress** — guide, implementation, and tests are under review.
3. **Verified** — the proof command passes in CI from a clean checkout.
4. **Needs repair** — the lab no longer passes or its guidance is stale.

## Required files

Each ready lab needs a `README.md`, an implementation, and tests. Add its metadata to `catalog/labs.json`, then run:

```bash
python scripts/check.py
```

Do not submit generated filler, copied tutorials, referral links, or projects that require secrets to verify.

