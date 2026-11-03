# Build Everything

**Learn by rebuilding. Prove it works.**

[Open the learning catalog](https://g-b-industry-llc.github.io/build-everything/) · [Start the verified beginner project](labs/http-server-python/README.md)

[Explore the Zinvyl Community Lab](https://zinvyl.com/community/) · [Contribute an improvement](CONTRIBUTING.md)

[![Listed on Launchpadly](https://launchpadly.co/embed/badges/startup/build-everything.svg?variant=listed-on)](https://launchpadly.co/startup/build-everything?ref=badge)

Build Everything is a free, open-source collection of guided projects for rebuilding the technologies that power modern computing. Every ready lab explains the idea in ordinary language, shows where people use it, guides one small build, and includes an automatic check that proves it works.

This is not another list of links. A lab is not marked ready until a new learner can understand its purpose and a clean checkout can verify the result.

## Start without feeling lost

You do not need to understand the whole internet before you begin.

1. Pick a **Beginner** lab.
2. Read **The big idea** and **Where this is used**.
3. Follow one step at a time.
4. Run **Prove it works**.
5. Change one small thing and explain what happened.

Teen learners can use the beginner track independently if they are comfortable running a command. Younger learners should work with a parent, teacher, or mentor. The guide explains the ideas, but an adult should still supervise software installation and terminal use.

### Turn learning tracks on or off

The catalog provides three independent filters:

- **Beginner** — analogies, guided steps, expected results, glossary, and safety prompts.
- **Advanced** — design decisions, fewer hints, extension work, and stronger failure testing.
- **Expert** — protocol limits, security analysis, performance measurement, and defensible tradeoffs.

Turn on one track to focus or combine tracks to compare how systems grow in complexity. These are learning views, not age gates; each lab still states its actual prerequisites.

## Why this exists

The internet has excellent "build your own" tutorials, but learners still face four problems:

- links disappear or become outdated;
- tutorials rarely define what "done" means;
- examples are hard to compare by time, difficulty, or prerequisites;
- reading can feel like progress even when nothing runs.

Build Everything turns learning into understanding you can demonstrate:

```text
see it in real life -> understand the idea -> build a small version -> prove it works -> explain it back
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
| DNS resolver | Advanced | 2 hr | Planned |
| Git-compatible object store | Advanced | 3 hr | Planned |
| SQLite-style B-tree | Expert | 6 hr | Planned |
| Search engine | Expert | 8 hr | Planned |

Catalog metadata lives in [`catalog/labs.json`](catalog/labs.json) and is validated in CI.

## What makes a lab understandable and trustworthy

Every ready lab must provide:

1. a one-paragraph big idea with no unexplained jargon;
2. familiar examples showing where the technology is used;
3. the learner's age guidance, prerequisites, result, and expected time;
4. short steps with a visible result after each meaningful stage;
5. a small reference implementation using minimal dependencies;
6. an automatic proof command that works from a clean checkout;
7. a plain-language glossary, safety notes, and intentional limitations;
8. a short “explain it back” check so running code is not mistaken for understanding.

The machine-readable catalog includes the same audience, prerequisite, result, application, and proof information. That lets websites, teachers, and coding agents present a lab without inventing missing context.

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

The goal is to become the most useful place on GitHub to learn how technology works—not by collecting the most links, but by making the ideas understandable and the results provable.

