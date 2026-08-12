# Nelson Stack

> **AI safety audit · local-first tooling · evidence-backed engineering.**
> The connective tissue across the repos Nelson ships under
> [`taipei49314`](https://github.com/taipei49314).

[![Licenses: per repo](https://img.shields.io/badge/licenses-per%20repo-lightgrey.svg)](#license)
[![Status: living index](https://img.shields.io/badge/status-living%20index-orange.svg)](#what-this-repo-is)
[![Project repos: 27](https://img.shields.io/badge/project%20repos-27-blue.svg)](#repo-map)

This is not a portfolio. Each repo here earns its place by either (a) implementing
a piece of the AI-safety-audit stack, or (b) being the tool the audit stack
itself was built with. Nothing ships here that a reproducible harness has not
produced on a clean checkout. Nothing claims a status it has not held under
that harness.

![Terminal attach session](docs/attach.gif)
![Audit loop with honest gaps](docs/audit-loop.gif)

---

## What this repo is

A **living index**. Not a monorepo. Not a curated list. It exists so that the
relationship between the linked project repos is legible in one read, and
so that anyone auditing Nelson's work can navigate from the principles down to
the evidence in one pass.

Last reconciled against GitHub repository, archive, release, and CI metadata:
**2026-08-12**.

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
that the system itself cannot fake**. Claims are not trusted until measured.
The active front of the stack is therefore measurer-first: score the checkout,
then refuse unmeasured phase advances, then run the six audit questions.

| # | Audit question | Primary repo | Supporting repos |
|---|---|---|---|
| 0 | What does the checkout **score** from local evidence? | [`trust-meter`](https://github.com/taipei49314/trust-meter) | [`phaseledger`](https://github.com/taipei49314/phaseledger) (fresh `PASS` required to advance) |
| 0b | Can this phase **advance** without a measurer verdict? | [`phaseledger`](https://github.com/taipei49314/phaseledger) | [`trust-meter`](https://github.com/taipei49314/trust-meter) |
| 0c | Did a pre-registered decision **beat chance**? | [`nullbench`](https://github.com/taipei49314/nullbench) | [`branchback`](https://github.com/taipei49314/branchback) (belief-at-the-time replay) |
| 1 | Did the declared journey **work**? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | [`unasked`](https://github.com/taipei49314/unasked) (non-certifying investigation) |
| 2 | Did the workload stay within its declared **capabilities**? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | [`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) (capability token bridge) |
| 3 | Was the result **reproducible**? | [`stateweaver`](https://github.com/taipei49314/stateweaver) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (deterministic plans) |
| 4 | Was **cleanup** complete? | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | [`stateweaver`](https://github.com/taipei49314/stateweaver) (reality replay) |
| 5 | What **evidence** exists, and who signed it? | [`stateweaver`](https://github.com/taipei49314/stateweaver) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (attestation bundles) |
| 6 | Is that evidence still **current**? | [`tomorrowci`](https://github.com/taipei49314/tomorrowci) · [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) | [`RepoPassport`](https://github.com/taipei49314/RepoPassport) (verdict staleness) |

`trust-meter` and `phaseledger` sit in front of the six questions: score first,
advance only on a fresh deterministic `PASS`. `nullbench` asks whether a
pre-registered decision beat chance without backfill. `RepoPassport` answers
questions 1, 2, and 4 — the *workload-side* invariants. `stateweaver` answers
questions 3 and 5 — the *verifier-side* invariants. `tomorrowci` answers
question 6 — *will this evidence still be valid tomorrow?*

### A worked example

Suppose an agent makes CI green by weakening a test. The audit chain is:

1. [`trust-meter`](https://github.com/taipei49314/trust-meter) **scores** the
   checkout from local evidence. [`phaseledger`](https://github.com/taipei49314/phaseledger)
   **refuses** a phase advance unless that measure is a fresh `PASS`.
2. [`greenwash`](https://github.com/taipei49314/greenwash) **detects** the
   tampering at the diff level — assertion strength weakened, golden file
   rewritten, CI runner script quieted. Zero LLM, zero network, byte-identical
   verdict.
3. [`RepoPassport`](https://github.com/taipei49314/RepoPassport) **re-runs the
   declared scenario** in a sandbox where the workload cannot self-judge, and
   produces a structured verdict (functional / capability / cleanup).
4. [`stateweaver`](https://github.com/taipei49314/stateweaver) **replays the
   finding** against a clean root and demands the patched build blocks the
   same path; only then does `SYNTHETIC_REPRODUCED` advance.
5. [`tomorrowci`](https://github.com/taipei49314/tomorrowci) **forecasts** the
   earliest concrete breakage horizon — the moment the patched build's
   dependencies or runtime stop supporting the verification path.

A finding that survives the chain is publishable. Any stage that fails
must be re-run from the previous stage's clean root. `smallestlie` is the
authorized adversarial complement: find the smallest lie the repo still
accepts. `nullbench` is the chance-baseline complement: pre-register the
claim, then score it against chance — never backfill.

---

## Repo map

Every repo is pre-alpha or pre-release unless otherwise noted. Status badges
on each repo are authoritative; this map is secondary.

### Audit stack (the core)

| Repo | Language | Role in the stack |
|---|---|---|
| [`trust-meter`](https://github.com/taipei49314/trust-meter) | Python | Measure-first scorer. No release; claims are not trusted until measured. |
| [`phaseledger`](https://github.com/taipei49314/phaseledger) | Python | Phase ledger. Advance only on a fresh deterministic measurer `PASS`. |
| [`nullbench`](https://github.com/taipei49314/nullbench) | Python | Pre-register decisions; score against chance; never backfill. [`v0.7.0`](https://github.com/taipei49314/nullbench/releases/tag/v0.7.0). |
| [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | Go | Workload-side audit: capabilities, cleanup, attestation bundles. |
| [`stateweaver`](https://github.com/taipei49314/stateweaver) | Python | Verifier-side audit: deterministic replays, oracle verdicts, signed evidence. |
| [`tomorrowci`](https://github.com/taipei49314/tomorrowci) · [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) | Rust | Time-side audit: dependency / runtime breakage forecasting. Measured lab tag: [`v0.1.1-alpha.2`](https://github.com/taipei49314/tomorrowci-lab/releases/tag/v0.1.1-alpha.2); GitHub “Latest” on both still points at a rejected historical tag. |
| [`greenwash`](https://github.com/taipei49314/greenwash) | Python | Diff-level detector for AI agent tampering with verification layers. [`v0.1.23`](https://github.com/taipei49314/greenwash/releases/tag/v0.1.23). |
| [`unasked`](https://github.com/taipei49314/unasked) | Python | Evidence-gated repository investigation; non-certifying alpha. [`v0.2.1`](https://github.com/taipei49314/unasked/releases/tag/v0.2.1). |
| [`smallestlie`](https://github.com/taipei49314/smallestlie) | Python | Authorized adversarial harness: smallest lie a repo still accepts. |
| [`branchback`](https://github.com/taipei49314/branchback) | TypeScript | Local-first decision replay lab — belief-at-the-time vs knowledge-now. [`v2.0.0`](https://github.com/taipei49314/branchback/releases/tag/v2.0.0). |
| [`constraint-deck`](https://github.com/taipei49314/constraint-deck) | Python | Session-first authorial constraint deck; measure first; contract over vibes. |
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
| [`music-lab`](https://github.com/taipei49314/music-lab) | Python | Deterministic local music toolkit; analysis first; no cloud account. |
| [`tw-stock-lab`](https://github.com/taipei49314/tw-stock-lab) | Python | Active local TW stock research lab ([`v0.2.0`](https://github.com/taipei49314/tw-stock-lab/releases/tag/v0.2.0)). *Research simulation, not investment advice.* |
| [`aurora`](https://github.com/taipei49314/aurora) | Python | Finds unnamed industries from evidence — deterministic, no LLM at runtime, no stock tips. |
| [`FutureShow-pet`](https://github.com/taipei49314/FutureShow-pet) | Python | Personal fork of HKUDS/FutureShow: local desktop pet (Taiwan news + GitHub AI-repo tracker) on Ollama / Qwen. |
| [`universe-explorer`](https://github.com/taipei49314/universe-explorer) | Python | Epistemically honest science knowledge system — separates known from unknown. |
| [`why-ledger`](https://github.com/taipei49314/why-ledger) | Docs | Why Ledger / 依據本 — justified sovereign decisions (WJSD). Documentation-first. |
| [`editorial-doll-engineering-preview`](https://github.com/taipei49314/editorial-doll-engineering-preview) | TypeScript | Public M0–M3 engineering preview of a deterministic editorial styling engine. |
| [`vibe-oracle`](https://github.com/taipei49314/vibe-oracle) | TypeScript | **Explicit anti-evidence foil.** Admits the theater; pure vibe, not evidence. |

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
- Some public releases are marked prerelease and therefore have no GitHub
  “Latest” badge even though a release tag exists (`md-brain`, `github-radar`,
  `FutureShow-pet`, `null-city`). That is intentional honesty, not absence.

What you can rely on: every link above resolves to a real repo, every repo's
README states its own status honestly, and the principles above are
demonstrably applied — including in the cases where the measurement showed
the principle was not yet met.

---

## How to read this stack

If you are auditing Nelson's work, the recommended reading order is:

1. [`trust-meter`](https://github.com/taipei49314/trust-meter) and
   [`phaseledger`](https://github.com/taipei49314/phaseledger) — measure
   first; no phase advance without a fresh `PASS`. Neither has a GitHub
   Release yet.
2. [`nullbench`](https://github.com/taipei49314/nullbench) — for chance
   baselines and pre-registered decision scoring.
3. [`RepoPassport`](https://github.com/taipei49314/RepoPassport) — for the
   workload-side invariants and the attestation model.
4. [`stateweaver`](https://github.com/taipei49314/stateweaver) — for the
   verifier-side model (state before chat, reality as final oracle).
5. [`greenwash`](https://github.com/taipei49314/greenwash) — for a concrete
   worked example of how a single detected failure is reported.
6. [`tomorrowci`](https://github.com/taipei49314/tomorrowci) ·
   [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) — for
   how time-horizon forecasts are produced. GitHub “Latest” on both still
   points at a rejected historical tag; measured lab work is tagged
   `v0.1.1-alpha.2` on `tomorrowci-lab`.
7. [`nelsoncode-ide`](https://github.com/taipei49314/nelsoncode-ide) — for
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

This index repo is documentation only. Its own files are Apache-2.0.

**Linked project repos are not uniformly licensed.** A public repo is not a
grant of rights. Read each repo's `LICENSE` and README.

| Repo | Current public license signal |
|---|---|
| [`trust-meter`](https://github.com/taipei49314/trust-meter) | README says MIT; no `LICENSE` file in tree, so GitHub does not classify it |
| [`phaseledger`](https://github.com/taipei49314/phaseledger) | Apache-2.0 |
| [`nullbench`](https://github.com/taipei49314/nullbench) | MIT |
| [`greenwash`](https://github.com/taipei49314/greenwash) | Apache-2.0 |
| [`RepoPassport`](https://github.com/taipei49314/RepoPassport) | Apache-2.0 |
| [`stateweaver`](https://github.com/taipei49314/stateweaver) | Apache-2.0 |
| [`tomorrowci`](https://github.com/taipei49314/tomorrowci) · [`tomorrowci-lab`](https://github.com/taipei49314/tomorrowci-lab) | Apache-2.0 |
| [`unasked`](https://github.com/taipei49314/unasked) | Publicly readable; copyright reserved; **not** an open-source license |
| [`smallestlie`](https://github.com/taipei49314/smallestlie) | MIT |
| [`null-city`](https://github.com/taipei49314/null-city) | MIT |
| [`NormShift`](https://github.com/taipei49314/NormShift) | Apache-2.0 |
| Local-first tools | Mix of Apache-2.0 and MIT; see each repo |

Archived or private repos may differ. This table is a reconciliation, not a
license grant.
