# Learner continuity and persistent evidence

Use this reference only when learning spans sessions, the learner requests a record, or a later tutor needs a handoff.

## Preserve consent and scope

- Ask before creating or updating a persistent learner record.
- Explain where the record will be written and what it contains.
- Store learning evidence, preferences, and next actions; avoid sensitive personal data that instruction does not require.
- Let the learner inspect, correct, export, or delete the record.
- Never claim continuity if the record was not actually read or written.
- Treat self-reported level as context, not demonstrated mastery.

When a writable workspace exists, prefer `.ai-master-tutor/learner-record.json`. Otherwise provide a compact handoff the learner can save. Start from `assets/learner-record.template.json` and validate with `scripts/validate_learning_artifacts.py` when tools permit.

## Record evidence, not impressions

For each observation, store:

```json
{
  "concept_id": "opportunity-cost",
  "observed_at": "2026-07-15T14:00:00+08:00",
  "delay_since_teaching": "immediate",
  "task_id": "oc-transfer-02",
  "surface": "time-allocation",
  "support_level": 0,
  "result": "correct",
  "reasoning_quality": "complete",
  "evidence_level": "transfer",
  "note": "Mapped next-best alternative without cue."
}
```

Do not write “mastered” without the tasks, support, result, and time that justify it. Distinguish:

- `immediate`: same-session performance;
- `delayed_1d`: retrieval after roughly one day;
- `delayed_1w`: retrieval after roughly one week;
- `later`: longer or unspecified delayed evidence.

Only delayed independent success supports a retention claim.

## Maintain concept state

For each concept, track:

- prerequisite concept IDs;
- highest independently evidenced level;
- fragile misconception or likely error;
- last observation time;
- next retrieval prompt or assessment item;
- review status: `due`, `scheduled`, `secure_now`, `fragile`, or `untested`;
- evidence history rather than a single overwritten label.

Prefer stable concept IDs from a content pack. If none exists, create a short descriptive ID and avoid silently renaming it later.

## Resume a session

1. Read the learner record if the learner authorized it.
2. State one relevant remembered fact and its evidence boundary, such as “last time you solved a near-transfer case immediately; delayed retention remains untested.”
3. Begin with the due retrieval item before reteaching.
4. Update the record only after observable work.
5. Preserve older evidence; append a new observation.

If the record conflicts with the learner, treat the conflict as a correction request, not proof that the learner is wrong.

## Schedule review honestly

Without an automation tool, record a suggested interval but say that no reminder was scheduled. With a tool, create the reminder only when requested and store the confirmed schedule identifier if appropriate.

Use performance to adjust spacing:

- incorrect or heavily supported: shorten the interval and reduce task complexity;
- correct but hesitant or incomplete: keep a similar interval with a changed cue;
- correct, independent, and well explained: lengthen the interval and vary the surface;
- repeated delayed success: add cumulative or farther-transfer work instead of repeating the same item.

## Produce a compact handoff

When no persistent file is available, output:

```yaml
goal: ""
current_checkpoint: ""
secure_now: []
fragile: []
untested: []
delayed_evidence: []
likely_error: ""
next_retrieval: ""
next_step: ""
```

Keep it factual and small enough for a later session to consume.
