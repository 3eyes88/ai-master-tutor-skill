# Session modes and target contracts

Use this reference to select the smallest tutoring path, handle time limits, switch modes, and stop cleanly.

## Route by learner intent

| Observable intent | Mode | Do first | Do not require |
|---|---|---|---|
| “直接告诉我”“简单解释” | `quick` | Give the answer or compact model | diagnosis, reconstruction, mastery gate |
| “教我理解”“带我练习” | `guided` | Infer one target and begin at the learner's evidence level | all nine milestones |
| “检验我是否真正掌握” | `mastery` | Start closed-book with a novel task | teaching before evidence unless prerequisites fail |
| “复习”“我上次学过” | `review` | Retrieve before rereading | repeating secure material |
| “系统学完”“长期带我学” | `course` | Define the outcome map and first checkpoint | an improvised syllabus without source/content validation |

If intent is mixed, satisfy the direct request first, then use the lightest compatible learning move. Example: answer first, then offer one application in `guided` mode.

For `mastery`, begin with one discriminating case and one core response request. Use the response to select the next untested dimension. Never display the complete mastery rubric as a first-turn battery.

## Create an observable target

Use:

```text
By the end, the learner can [action] with [conditions/tools] to [criterion].
```

Strong targets:

- explain opportunity cost and identify it in two surface-different choices without hints;
- select a debugging hypothesis from test output and justify the next diagnostic step;
- distinguish a paper's reported result from the authors' interpretation using two passages.

Weak targets:

- understand economics;
- learn Rust;
- know the paper.

In `course` mode, split a broad goal into checkpoints. Keep one current checkpoint visible and queue side topics.

The first course response should contain only:

1. one-sentence course outcome;
2. the first observable checkpoint;
3. one high-information task or question;
4. a continuity consent statement only when persistence is relevant.

Do not show the full syllabus and complete checkpoint rubric before observing the learner. Infer background, misconceptions, and prerequisites from the first task when possible. Ask about time later only if it changes scope or pacing.

## Timebox proportionally

- Under five minutes: use `quick` or one `guided` micro-cycle.
- Five to twenty minutes: target one schema and one independent application.
- Longer session: allow several checkpoints, but close each with a compact state update.
- Unknown time: begin with a useful small unit instead of asking a scheduling questionnaire.

When time expires, report the highest evidence reached and one next action. Do not rush through missing milestones to claim completion.

## Switch modes from evidence or request

- `quick → guided`: learner asks “why,” requests practice, or reveals a misconception.
- `guided → mastery`: learner asks for a real check or reaches a checkpoint.
- `mastery → guided`: assessment reveals a prerequisite gap that needs teaching.
- `guided/mastery → quick`: learner asks for the answer or must finish.
- any mode → `review`: prior evidence exists and the goal is retention.
- any mode → stop: learner says stop; close without another required task.

State the switch only when it helps orientation. Never use a mode label to pressure the learner.

## Apply exit rules

End or pause the current target when any applies:

1. the target criterion is met with the evidence required by the current mode;
2. the learner requests a stop, answer, topic change, or lower-effort mode;
3. the time budget expires;
4. progress requires missing source material, an unverified answer key, or an external prerequisite;
5. overload persists after reducing scope and support.

Keep untested evidence explicitly untested. A clean stop is better than a ceremonial completion of every stage.
