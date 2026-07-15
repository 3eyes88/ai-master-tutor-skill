# Adaptive control: ICAP, state, and concept-loop decisions

Use this reference when choosing an ICAP mode, deciding whether interaction is genuinely Interactive, or carrying learner state across a multi-turn session. Select the session mode first; ICAP describes the learner's activity inside that mode, not the overall product mode.

## Interpret ICAP operationally

Classify the learner's observable cognitive activity, not the tutor's interface or the length of the exchange.

| Mode | Learner behavior | Suitable tutor move | Exit evidence |
|---|---|---|---|
| P — Passive | Attends to an explanation or example without manipulating it | Give one minimal explanation, model, analogy, or worked example | Can complete a tiny selection, label, or continuation |
| A — Active | Selects, matches, labels, highlights, sorts, copies with purpose, or manipulates given material | Ask for classification, matching, completion, ordering, or identification | Can generate something not explicitly supplied |
| C — Constructive | Produces a new explanation, inference, prediction, example, diagram, comparison, or solution | Request self-explanation, generation, prediction, design, or teaching | Produces a coherent model that can be challenged |
| I — Interactive | Co-develops understanding through challenge, response, revision, and mutual refinement | Challenge a specific learner claim with a counterexample, condition change, evidence gap, or competing model | Revises the model and states its improved scope or boundary |

The expected ordering I > C > A > P is a hypothesis about productive engagement under suitable conditions. Do not force a higher mode when missing knowledge turns generation into guessing.

## Choose and shift modes

```text
No usable schema?
  yes → minimal P → tiny A
  no  → Can learner generate an explanation/application?
          no  → A with a cue or completion → C
          yes → C

C response coherent enough to test?
  yes → targeted challenge → learner revision → I
  no  → classify error → scaffold or step down

Two failures, overload, or guessing?
  step down one mode + increase support + reduce interacting elements

Two independent successes with reasons?
  fade support + increase variation or transfer distance
```

Do not equate difficulty with engagement. A confused learner wrestling with an underspecified task is not necessarily Constructive or Interactive.

## Run one concept as a proportional state machine

Track these milestones internally:

```text
diagnosed
→ minimally_taught_if_needed
→ retrieved
→ constructed_1
→ constructed_2
→ challenged
→ reconstructed
→ verified_remember
→ verified_understand
→ verified_transfer
→ reflected
→ review_prepared
```

Do not expose this list every turn. Treat it as a menu of evidence states rather than a route that every session must finish. `quick` mode may stop after explanation; `guided` mode uses only the milestones required by its target; `mastery` and course checkpoints require the appropriate verification evidence. A single activity may satisfy two milestones, but never mark `challenged` or `reconstructed` without learner-generated content.

Stop the state machine when the target contract is met, the learner asks to stop or switch modes, the time budget expires, or progress requires missing or unverified content. Preserve the highest evidence reached instead of rushing through remaining states.

## Enforce the Interactive threshold

Treat an exchange as I only when most of these are observable:

- both parties continue working on the same cognitive object;
- the tutor's move refers to a specific learner-generated claim, assumption, inference, evidence, or boundary;
- the tutor creates productive conflict through a counterexample, changed condition, competing explanation, or defense request;
- the learner changes the original explanation or model in response;
- the revised model is more complete or precise than either initial contribution;
- the exchange produces an implication, boundary, or relationship not simply copied from the material;
- both parties converge on a model while preserving uncertainty and scope.

Fail the I threshold when the exchange is merely a quiz, generic follow-up, chat, praise, repetition, or a tutor monologue followed by agreement.

### Challenge selector

Choose the smallest challenge that discriminates the learner's current model:

| Learner output | Challenge |
|---|---|
| Rule stated without conditions | Change one condition or offer an edge case |
| Example with unclear mapping | Ask which feature carries the underlying structure |
| Causal claim | Offer an alternative cause or reverse the direction |
| Broad generalization | Give a counterexample and ask for a narrower rule |
| Correct answer with weak reason | Present a tempting wrong reason or close contrast |
| Source interpretation | Point to conflicting data/passages or a stronger unsupported claim |
| Procedure | Change an input, constraint, or failure mode |

After the challenge, ask the learner to edit the original model rather than start an unrelated answer.

## Maintain learner state from evidence

Update fields only when there is evidence:

- `prior_knowledge`: infer from diagnostic performance, not self-label alone.
- `current_concept`: keep one minimal schema; queue side concepts instead of switching silently.
- `current_icap_level`: record the activity actually performed.
- `misconceptions`: store the mistaken model, not only the wrong answer.
- `prerequisite_gaps`: name the missing representation or skill.
- `mastery_level`: set to the highest independently demonstrated level.
- `evidence_of_mastery`: store the task and support used.
- `scaffolding_level`: record the highest decisive support; lower it after independent success.
- `transfer_status`: distinguish untested, near, varied, and far.
- `review_items`: include fragile, failed, or not-yet-retained schemas.
- `next_step`: choose one action, not a syllabus.

For course work, select `current_concept` from a prerequisite map rather than conversational convenience. Store durable evidence only with learner permission and a real record mechanism; see [learner-continuity.md](learner-continuity.md).

When no persistent memory exists, say so if asked and provide a compact handoff instead of pretending the state will survive.

## Handle listening without generation

If the learner keeps reading but does not respond:

1. stop adding new explanations;
2. ask for the smallest possible output;
3. offer a choice, label, one blank, or one-sentence restatement;
4. if they still decline, ask whether they want direct explanation mode or to pause;
5. do not treat nonresponse as mastery or continue an infinite lecture.
