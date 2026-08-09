# Nelson Stack

> **AI safety audit · local-first tooling · evidence-backed engineering.**
> The connective tissue across the repos Nelson ships under
> [`taipei49314`](https://github.com/taipei49314).

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Status: living index](https://img.shields.io/badge/status-living%20index-orange.svg)](#what-this-repo-is)
[![Project repos: 17](https://img.shields.io/badge/project%20repos-17-blue.svg)](#repo-map)

This is not a portfolio. Each repo here earns its place by either (a) implementing
a piece of the AI-safety-audit stack, or (b) being the tool the audit stack
itself was built with. Nothing ships here that a reproducible harness has not
produced on a clean checkout. Nothing claims a status it has not held under
that harness.

---

## What this repo is

A **living index**. Not a monorepo. Not a curated list. It exists so that the
relationship between the 17 linked project repos is legible in one read, and
so that anyone auditing Nelson's work can navigate from the principles down to
the evidence in one pass.

Last reconciled against GitHub repository, archive, release, and CI metadata:
**2026-08-09**.

The headline principle across everything here:

> **Declarations are not evidence. The workload does not judge itself. Models
> may propose; only the verifier decides. `UNKNOWN` / `INCOMPLETE` is better
> than a false pass.**

That sentence is from
[`RepoPassport`](https://github.com/taipei49314/RepoPassport). It is also the
operating principle of every other repo on this page.

---

## The core: AI safety audit

Nelson's primary research target is **how to audit an AI-driven system in a way
that the system itself cannot fake**. The full stack breaks into six audit
questions; each repo answers one or more of them, and the questions line up
with `RepoPassport`'s six questions.

| # | Audit question | Primary repo | Supporting repos |
|---|---|---|---|
| 1 | Did the declared journey **work**? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | — |
| 2 | Did the workload stay within its declared **capabilities**? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | [`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) (capability token bridge) |
| 3 | Was the result **reproducible**? | [`stateweaver`](https://github.com/taipei49314/stateweaver) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (deterministic plans) |
| 4 | Was **cleanup** complete? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | [`stateweaver`](https://github.com/taipei49314/stateweaver) (reality replay) |
| 5 | What **evidence** exists, and who signed it? | [`stateweaver`](https://github.com/taipei49314/stateweaver) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (attestation bundles) |
| 6 | Is that evidence still **current**? | [`tomorrowci`](https://github.com/taipei49314/tomorrowci) · [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (verdict staleness) |

`RepoPassport` answers questions 1, 2, and 4 — the *workload-side* invariants
(capability conformance, cleanup, declared journey). `stateweaver` answers
questions 3 and 5 — the *verifier-side* invariants (reproducibility of the
oracle, signed evidence of the finding). `tomorrowci` answers question 6 —
*will this evidence still be valid tomorrow?* — by forecasting dependency /
runtime breakage.

### A worked example

Suppose an agent makes CI green by weakening a test. The audit chain is:

1. [`greenwash`](https://github.com/taipei49314/greenwash) **detects** the
   tampering at the diff level — assertion strength weakened, golden file
   rewritten, CI runner script quieted. Zero LLM, zero network, byte-identical
   verdict.
2. [`RepoPassport`](https://github.com/taipei49314/RepoPassport) **re-runs the
   declared scenario** in a sandbox where the workload cannot self-judge, and
   produces a structured verdict (functional / capability / cleanup).
3. [`stateweaver`](https://github.com/taipei49314/stateweaver) **replays the
   finding** against a clean root and demands the patched build blocks the
   same path; only then does `SYNTHETIC_REPRODUCED` advance.
4. [`tomorrowci`](https://github.com/taipei49314/tomorrowci) **forecasts** the
   earliest concrete breakage horizon — the moment the patched build's
   dependencies or runtime stop supporting the verification path.

A finding that survives all four stages is publishable. Any stage that fails
must be re-run from the previous stage's clean root.

---

## Repo map

Every repo is pre-alpha or pre-release unless otherwise noted. Status badges
on each repo are authoritative; this map is secondary.

### Audit stack (the core)

| Repo | Language | Role in the stack |
|---|---|---|
| [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | Go | Workload-side audit: capabilities, cleanup, attestation bundles. |
| [`stateweaver`](https://github.com/taipei49314/stateweaver) | Python | Verifier-side audit: deterministic replays, oracle verdicts, signed evidence. |
| [`tomorrowci`](https://github.com/taipei49314/tomorrowci) · [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) | Rust | Time-side audit: dependency / runtime breakage forecasting. |
| [`greenwash`](https://github.com/taipei49314/greenwash) | Python | Diff-level detector for AI agent tampering with verification layers. |
| [`persona-consistency-checker`](https://github.com/taipei49314/persona-consistency-checker) | Python | **Archived historical prototype.** PersonaChain experiments for persona drift under adversarial prompts. |
| [`null-city`](https://github.com/taipei49314/null-city) | TypeScript | Deterministic, partially observable crisis-response sandbox for agent eval. |
| [`NormShift`](https://github.com/taipei49314/NormShift) | Python | Evidence-backed semantic diff for technical standards (M0 local HTML slice). |

### Local-first tools (the substrate)

| Repo | Language | What it does |
|---|---|---|
| [`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) | TypeScript / Electron | Personal AI coding IDE; timeline as backbone; reversible sessions. Powers the audit loop locally. |
| [`md-brain`](https://github.com/taipei49314/md-brain) | Python | Model-independent continuity runtime for AI memory. |
| [`github-radar`](https://github.com/taipei49314/github-radar) | Python | GitHub research with measured uncertainty; can submit hashed findings to Frontier Atlas. |
| [`receiptradar`](https://github.com/taipei49314/receiptradar) | Rust | Local receipt → ledger CLI. No cloud, no account. |
| [`nelson-release-studio`](https://github.com/taipei49314/nelson-release-studio) | Python | Music creation, asset management, and release workbench — Windows-first. |
| [`tw-stock-lab`](https://github.com/taipei49314/tw-stock-lab) | Python | **Archived legacy prototype.** Local TW stock research; superseded in active work by TradingAgents-TW. *Research simulation, not investment advice.* |
| [`aurora`](https://github.com/taipei49314/aurora) | Python | Finds unnamed industries from evidence — deterministic, no LLM at runtime, no stock tips. |
| [`FutureShow-pet`](https://github.com/taipei49314/FutureShow-pet) | Python | Personal fork of HKUDS/FutureShow: local desktop pet (Taiwan news + GitHub AI-repo tracker) on Ollama / Qwen. |
| [`universe-explorer`](https://github.com/taipei49314/universe-explorer) | Python | **Archived proof of concept.** Epistemically honest science system separating known from unknown. |

---

## Operating principles

These are not aspirations. Every repo in the stack has been measured against
them on a clean checkout, and the failures are kept in the repo as evidence
(`FAILURES.md`, `benchmarks/decoy/`, `CYCLE*-VERDICT.md`, etc.).

1. **Deterministic over LLM-judged.** Whenever a verdict can be reached by
   deterministic analysis of the diff, the artifact, or the replay, it is.
   LLM judges are advisory.
2. **Measured, not asserted.** Every headline number — false-positive rate,
   detection count, replay latency — comes out of a reproducible harness.
   Nothing is hand-typed into a README.
3. **Honest about out-of-sample.** The detectors and verifiers in this stack
   are reported to perform worse on corpora they have never seen. That
   degradation is published, not hidden.
4. **Fail-closed by default.** A missing observation is `incomplete`. A
   capability violation outranks a functional pass. A signature without a
   trust key is `unknown`, not `valid`.
5. **Local-first, zero network.** Tools in this stack run on the operator's
   hardware. The audit trail does not phone home.
6. **Trust boundaries written into the repo.** `SECURITY.md`, `AGENTS.md`,
   `ABUSE_POLICY.md`, `THREATMODEL.md`, and traceability matrices are not
   optional. They are part of the deliverable.
7. **Verdicts are immutable history.** A `VERDICT.md` file is rewritten only
   by a later cycle that explicitly supersedes it. Earlier verdicts are kept
   so the next reader can see the dead ends.

---

## Honest status

This index repo is itself pre-release. Specifically:

- The grouping above is the author's current model of how the repos relate.
  It is open to revision if a repo's own README claims a different role.
- "Primary repo" / "supporting repo" in the audit table reflects what is
  shipped today, not what is intended. Future repos may swap the
  responsibilities.
- No repo here has been independently audited by a third party, except where
  its own README states otherwise
  ([`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) v0.2.0
  has an external audit with a NO-GO verdict, which is kept on the README).
- External adoption is still minimal and is not used as a quality claim. Stars,
  downloads, and README assertions do not replace reproducible evidence.

What you can rely on: every link above resolves to a real repo, every repo's
README states its own status honestly, and the principles above are
demonstrably applied — including in the cases where the measurement showed
the principle was not yet met.

---

## How to read this stack

If you are auditing Nelson's work, the recommended reading order is:

1. [`RepoPassport`](https://github.com/taipei49314/RepoPassport) — for the
   workload-side invariants and the attestation model.
2. [`stateweaver`](https://github.com/taipei49314/stateweaver) — for the
   verifier-side model (state before chat, reality as final oracle).
3. [`greenwash`](https://github.com/taipei49314/greenwash) — for a concrete
   worked example of how a single detected failure is reported.
4. [`tomorrowci`](https://github.com/taipei49314/tomorrowci) ·
   [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) — for
   how time-horizon forecasts are produced.
5. [`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) — for
   the developer-facing surface where the audit loop is actually run.

If you are using Nelson's work, start with the `quickstart` in the repo that
matches your target question. The audit table above tells you which one.

---

## Contributing

This index repo is a directory. Pull requests that correct the mapping (a
repo's role has changed, a repo has been retired, a new repo has joined the
stack) are welcome. Pull requests that soften the honest-status section are
not.

## License

Apache-2.0. Each repo in the stack carries its own license; the audit-stack
repos are uniformly Apache-2.0, the local-first tools are a mix of Apache-2.0
and MIT — see each repo's `LICENSE`.
