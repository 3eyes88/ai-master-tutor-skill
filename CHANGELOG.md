# Changelog

## 0.4.0-rc.1 — 2026-07-15

- Add `quick`, `guided`, `mastery`, `review`, and `course` routing so simple explanations do not trigger a full tutoring loop.
- Add observable target contracts, time-budget handling, mode switches, and explicit exit rules.
- Make the nine-stage concept loop proportional rather than mandatory; reserve the full mastery gate for mastery checks and course checkpoints.
- Add opt-in cross-session learner records with timestamped evidence, support levels, delayed retrieval status, privacy boundaries, and honest reminder handling.
- Add structured course/content packs with prerequisite graphs, verified answer keys, domain adaptation, and cumulative review.
- Add JSON templates and a deterministic validator for learner records and content packs.
- Expand evaluation requirements to include baseline comparisons, repeated runs, complete raw transcripts, human pilots, and delayed tests.
- Mark this build as a release candidate until forward tests, human pilots, and publication checks are complete.

## 0.3.0 — 2026-07-13

- Add an adaptive ICAP controller that selects and shifts Passive, Active, Constructive, and Interactive modes from learner evidence.
- Replace the generic lesson loop with Diagnose → Minimal Teach → Retrieve → Construct → Challenge → Reconstruct → Verify → Reflect → Review.
- Add a session-local learner state model for goals, prior knowledge, misconceptions, scaffolding, mastery evidence, transfer, and review.
- Define strict Interactive criteria so ordinary question-answering or long conversations are not mislabeled.
- Expand error diagnosis to nine classes with minimum-hint, retry, graded-scaffolding, and regeneration rules.
- Require two constructive learner products, response-specific challenges, surface-different transfer, metacognitive reflection, and concise spaced retrieval.
- Add eight acceptance scenarios for novices, experts, direct answers, confident misconceptions, overload, passive listening, and genuine interaction.
- Strengthen deterministic validation and cross-platform compatibility checks while preserving `$ai-master-tutor` and `/ai-master-tutor`.

## 0.2.0 — 2026-07-13

- Adopt the standard `skills/ai-master-tutor/` repository layout.
- Add Claude Code personal and project installation instructions.
- Document native invocation with `/ai-master-tutor` and automatic discovery.
- Add GitHub CLI installation and update commands for Codex and Claude Code.
- Add deterministic cross-platform layout checks and real Claude Code forward tests.
- Keep one shared `SKILL.md` and reference set for both platforms.
- Strengthen natural-language invocation in Claude Code.
- Skip definition checks when a learner explicitly reports an application gap.
- Treat germane cognitive load as a debated/refined category rather than settled independent load.

## 0.1.0 — 2026-07-13

- Introduce the adaptive tutoring contract, support ladder, formative feedback, mastery checks, and source-grounded tutoring.
- Add 10 learning scenarios, an evaluation rubric, isolated forward-test transcripts, and a test report.
