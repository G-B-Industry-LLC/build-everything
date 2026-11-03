# Build Everything

**Learn by rebuilding. Prove it works.**

Build Everything is a free, open-source collection of executable labs for rebuilding the technologies that power modern computing. Every ready lab includes a plain-language explanation, a bounded build, automated acceptance tests, and a proof command.

This is not another list of links. A lab is not marked ready until a clean checkout can verify it.

## Why this exists

The internet has excellent "build your own" tutorials, but learners still face four problems:

- links disappear or become outdated;
- tutorials rarely define what "done" means;
- examples are hard to compare by time, difficulty, or prerequisites;
- reading can feel like progress even when nothing runs.

Build Everything turns learning into evidence:

```text
choose a system -> understand the contract -> build it -> run the proof -> explain the tradeoffs
```

## Start here

The first verified lab rebuilds an HTTP/1.1 server with Python sockets and no web framework.

```bash
python scripts/check.py
python labs/http-server-python/server.py
```

Then visit `http://127.0.0.1:8080/health`.

## The catalog

| Lab | Level | Time | Status |
| --- | --- | ---: | --- |
| [HTTP server from sockets](labs/http-server-python/README.md) | Beginner | 45 min | Verified |
| DNS resolver | Intermediate | 2 hr | Planned |
| Git-compatible object store | Intermediate | 3 hr | Planned |
| SQLite-style B-tree | Advanced | 6 hr | Planned |
| Search engine | Advanced | 8 hr | Planned |

Catalog metadata lives in [`catalog/labs.json`](catalog/labs.json) and is validated in CI.

## What makes a lab trustworthy

Every ready lab must provide:

1. a small, useful target;
2. the protocol or behavior contract;
3. a reference implementation using minimal dependencies;
4. automated acceptance tests;
5. a proof command that works from a clean checkout;
6. security and failure-mode notes;
7. an explanation of what the simplified build intentionally omits.

## Designed for humans and coding agents

The catalog is machine-readable. Each lab declares inputs, proof commands, prerequisites, expected duration, and supported languages. Humans can follow the guide; coding agents can use the same acceptance contract without inventing completion.

## Free means free

- MIT licensed.
- No account required.
- No telemetry.
- No paid completion certificate.
- No proprietary runtime.
- Labs favor standard libraries and local execution.

## Contributing

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md). New labs begin as a proposal and become **Verified** only when their proof passes in CI.

## Ambition

The goal is to become the most useful place on GitHub to learn how technology works—not by collecting the most links, but by producing the most verified understanding.

