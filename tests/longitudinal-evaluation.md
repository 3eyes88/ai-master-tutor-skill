# Longitudinal and comparative evaluation protocol

Use this protocol before promoting a release candidate as an effective long-term tutor. Structural validation and simulated tutoring traces are necessary but insufficient.

## Evaluation questions

1. Does the Skill improve first-session understanding over the same model without the Skill?
2. Does it improve independent transfer rather than only conversation quality?
3. Does it improve retrieval after roughly one day and one week?
4. Does routing reduce unnecessary questioning and session abandonment?
5. Does a persistent record improve adaptation without inventing learner history?

## Conditions

Run at least:

- `baseline`: same model and materials without this Skill;
- `v0.3`: prior released protocol when available;
- `candidate`: current release candidate.

Keep the model, source material, task, tool access, and learner instructions constant. Randomize condition order when the same learner experiences more than one condition.

## Repeated model runs

For each automated scenario:

- run at least five independent samples per model/host configuration;
- preserve complete raw prompts, responses, tool calls, follow-up turns, model/version, and timestamp;
- score blind to condition when practical;
- report all failures, not only a representative successful trace;
- distinguish deterministic structural checks from sampled behavioral evidence.

Do not summarize learner replies in place of raw transcripts. Redact personal data without changing the cognitive content.

## Human pilot

Recruit a small, diverse pilot before efficacy claims. Record informed consent and avoid high-stakes experimentation without appropriate review.

At minimum collect:

- prior-knowledge pretest aligned to the target;
- immediate independent post-test;
- changed-surface transfer item;
- delayed retrieval at roughly 24 hours;
- delayed retrieval and transfer at roughly seven days;
- time on task, completion/abandonment, perceived load, and learner preference;
- qualitative reports of over-questioning, confusion, loss of agency, and incorrect feedback.

Use assessment items that were not shown during teaching. Score with explicit answer criteria. Where possible, have a subject-matter expert validate items and score a sample of responses.

## Minimum release evidence

An RC may become a stable release when:

1. structural and artifact validators pass;
2. no critical rubric failure appears across repeated routing, correction, source, continuity, and high-stakes boundary scenarios;
3. complete raw forward-test traces are published for the candidate;
4. baseline comparison shows no regression in direct-answer compliance, accuracy, or abandonment;
5. at least a small human pilot has been run, or the release is explicitly labeled experimental without learning-gain claims;
6. delayed evidence is reported separately from immediate performance;
7. default-branch installation resolves to the intended version and the release tag exists.

## Reporting

Report sample sizes, missing follow-ups, scoring rules, model versions, prompts, materials, exclusions, and uncertainty. Do not convert a handful of successful conversations into a population-level learning claim.
