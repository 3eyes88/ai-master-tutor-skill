# Mastery, metacognition, and review

Use this protocol to judge learning, close a concept, plan review, or hand a session to a later tutor.

## Record the highest evidenced level

| Level | Required evidence |
|---|---|
| Exposure | Can follow an explanation with support |
| Remember | Can retrieve the core without the material |
| Understand | Can explain why and distinguish a close alternative |
| Apply | Can independently solve or analyze a representative new case |
| Transfer | Can select and adapt the schema in a surface-different case and justify the mapping |
| Advanced | Can compare neighboring concepts, handle counterexamples, transfer farther, and teach under challenge |

Call a level met only when the learner performs without decisive prompts. One immediate session cannot establish durable retention.

## Apply the basic mastery gate proportionally

Use the full gate only in `mastery` mode or at an explicit course checkpoint. In `quick` and ordinary `guided` work, report the highest evidence observed and mark the rest untested; do not turn every explanation into an exam.

Do not mark a concept basically mastered until independent evidence covers all five:

1. own-words explanation;
2. one correct self-generated example;
3. one rejected example, counterexample, or boundary;
4. one meaningfully varied application;
5. one likely personal error and how to detect it.

Evidence may accumulate across turns or sessions. If the learner has already demonstrated an item, do not repeat it mechanically. If the learner stops or the time budget expires, preserve the partial evidence without claiming the gate passed.

## Build a compact verification sequence

1. **Remember:** one no-notes retrieval.
2. **Understand:** one “why,” causal chain, or close distinction.
3. **Transfer:** one new setting with different surface cues but the same deep structure.
4. **Explain transfer:** ask which feature makes the schema applicable.
5. **Boundary:** ask when the schema would not apply or would need modification.

Do not reuse the worked example as the only check. After any revealed answer, verify with a different item.

## Run the metacognitive close

Have the learner answer briefly:

- What can I now explain or do without help?
- What remains uncertain?
- At which step am I most likely to fail?
- What future signal should make me retrieve this schema?

Contrast predicted mastery with performed evidence. If confidence is high but performance is weak, name the familiarity-versus-mastery gap without moralizing.

## Report evidence without false precision

Prefer:

- “Explains the mechanism independently.”
- “Applies it with one conceptual cue.”
- “Confuses X with Y when surface features change.”
- “Transfer not yet tested.”
- “Retention requires delayed retrieval.”

Avoid arbitrary mastery percentages. Attach any requested score to an explicit item set and rubric.

For persistent evidence, record:

- concept and task IDs;
- observation time and delay since teaching;
- surface or context of the task;
- support level used;
- result and reasoning quality;
- highest level the item actually demonstrates.

Immediate success supports current performance only. Use `delayed_1d`, `delayed_1w`, or a clearly stated longer delay before making a retention claim. Read [learner-continuity.md](learner-continuity.md) when a record is available.

## Create a lightweight spaced-review set

Generate two to five short prompts, dominated by retrieval rather than rereading:

- one core explanation from memory;
- one previously fragile or missed point;
- one changed application or contrast;
- optionally, one boundary or teach-a-novice prompt.

Mark each schema as `secure_now`, `fragile`, or `untested`. Suggest, rather than prescribe, short retrieval:

- later the same day or next day;
- after several days;
- after one to two weeks;
- then lengthen or shorten based on success.

Do not output a long calendar unless requested. Do not claim a reminder was scheduled without a tool confirmation.

## Produce a session handoff

Show this only when the learner requests a record or continuity is needed:

```yaml
learning_goal: ""
mode: quick | guided | mastery | review | course
target_action: ""
success_criterion: ""
application_context: ""
current_concept: ""
current_icap_level: P | A | C | I
prior_knowledge: unknown | novice | partial | established | advanced
misconceptions: []
prerequisite_gaps: []
mastery_level: exposure | remember | understand | apply | transfer | advanced
evidence_of_mastery: []
scaffolding_level: 0 | 1 | 2 | 3 | 4 | 5
transfer_status: untested | near | varied | far
review_items: []
delayed_evidence: []
next_step: ""
```

Keep evidence concrete, for example: “solved a surface-different case without cues,” not “seems to understand.”
