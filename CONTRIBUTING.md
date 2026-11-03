# Contributing

Build Everything accepts small, testable learning labs.

The public catalog has Beginner, Advanced, and Expert filters that learners can turn on independently. Choose the honest level from the prerequisites and expected reasoning—not from how impressive the topic sounds.

## A good contribution

- rebuilds one recognizable technology or subsystem;
- works without paid services;
- starts with a plain-language explanation and familiar real-life examples;
- defines age guidance, prerequisites, the finished result, and where the idea is applied;
- teaches the underlying contract rather than hiding it behind a framework;
- has a bounded scope that a learner can finish;
- includes automated acceptance tests;
- includes a glossary and an “explain it back” check;
- states security limitations and intentional omissions;
- uses original writing or properly licensed sources.

## Lab lifecycle

1. **Proposed** — the catalog entry defines the outcome and proof.
2. **In progress** — guide, implementation, and tests are under review.
3. **Verified** — the explanation contract is complete and the proof command passes in CI from a clean checkout.
4. **Needs repair** — the lab no longer passes or its guidance is stale.

## Required files

Each ready lab needs a `README.md`, an implementation, and tests. Its guide must contain **The big idea**, **Where this is used**, **What you will make**, **Before you start**, **Build it**, **Prove it works**, **Explain it back**, **Glossary**, and **Safety and limits**. Add its audience and application metadata to `catalog/labs.json`, then run:

```bash
python scripts/check.py
```

Do not submit generated filler, copied tutorials, referral links, or projects that require secrets to verify.

