# AI Master Tutor v0.4.0-rc.1 — Test Report

Date: 2026-07-15
Status: **RELEASE CANDIDATE — structural pass, targeted behavior pass after two refinements**

## Outcome

The candidate adds proportional session routing, observable targets, opt-in learner continuity, structured content packs, artifact validation, and a longitudinal evaluation protocol. Official Skill validation, deterministic repository checks, Python compilation, valid/invalid learner-record checks, and valid content-pack checks pass.

Six isolated first-turn traces were retained. Quick routing and continuity passed initially. Mastery and course routing each exposed one overload problem, the protocol was revised, and both isolated retests passed.

The candidate was then copied to the Codex user Skill directory. Official validation and the bundled artifact validator passed against the installed copy, and a recursive diff confirmed that the installed runtime matches the candidate runtime.

## Verified in this candidate

- `quick` mode answers directly without a compulsory quiz;
- `mastery` mode begins with one discriminating case rather than a definition review or full rubric battery;
- `course` mode shows one outcome, one checkpoint, one task, and an explicit persistence boundary;
- an authorized learner record is interpreted from task, support, result, and observation timing;
- immediate transfer is not mislabeled as retention;
- learner-record and content-pack JSON artifacts have deterministic validation;
- the source Skill has valid frontmatter and remains below 500 lines;
- the local Codex user installation matches the validated candidate;
- the test suite contains 26 scenarios and a 30-point rubric including routing, content validity, and continuity integrity.

Raw evidence: `tests/forward-test-transcripts-v0.4.0-rc.1.md`.

## Not yet verified

- repeated samples across all scenarios and supported models;
- complete multi-turn behavior for the new modes;
- a no-Skill baseline and v0.3 comparison;
- human learning outcomes or abandonment rates;
- retrieval after roughly one day and one week;
- subject-matter expert validation of generated content packs;
- Codex and Claude Code installation from the eventual remote release tag;
- default-branch and remote-version alignment.

## Release decision

Keep version `0.4.0-rc.1`. It is suitable for local dogfooding and targeted human pilots. Do not publish learning-gain claims or promote it to stable `v0.4.0` until the gates in `tests/longitudinal-evaluation.md` are completed or the stable release is explicitly labeled experimental.
