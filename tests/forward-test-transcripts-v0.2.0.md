# Forward-test transcripts — v0.2.0

These traces validate that the canonical Skill still drives the intended tutoring behavior after migration from `skill/` to the cross-platform `skills/` layout. Fresh isolated agents received only the Skill path and learner request, not the rubric or expected answer.

## R1 — Misconception repair

Learner:

> Teach me cognitive load theory. I think good teaching should remove all difficulty.

Tutor:

> Your instinct is half right: good teaching should remove **unproductive difficulty**, not all difficulty.
>
> Cognitive load theory starts from a bottleneck: working memory can handle only a few interacting elements at once, while long-term memory can store organized knowledge structures. Teaching should therefore reduce **extraneous load**—confusing wording, irrelevant decoration, split attention, unexplained steps—but preserve a manageable amount of effort needed to build knowledge. If a teacher always supplies every answer, the lesson may feel effortless, yet the learner never practices retrieving, explaining, or applying the idea.
>
> Consider two algebra lessons:
>
> - A: The teacher shows every solution while students follow along.
> - B: The teacher models one clear example, then students complete a similar problem with fewer hints.
>
> Which difficulty in lesson B should remain, and what kind of difficulty should the teacher remove?

Result: pass. The response preserved the useful part of the learner's model, corrected the overgeneralization, and used a contrast plus learner revision.

## R2 — Incomplete source

Learner:

> I only have the sentence “AI tutors improve learning.” Teach me the whole paper.

Tutor:

> That sentence gives only a broad claim—not enough to identify or reconstruct a whole paper. It omits the authors, research question, type of AI tutor, participants, comparison group, learning measure, results, and limitations. I don’t want to invent those details.
>
> Please send the paper’s title, link, abstract, or PDF. Then I’ll teach it in causal order: question → claim → method → evidence → reasoning → limitations → implications.

Result: pass. The response followed the source-grounded reference and refused to fabricate missing evidence.

## R3 — Answer-first request

Learner:

> Explain why randomized assignment matters. Just tell me the answer first and do not quiz me afterward.

Tutor:

> Randomized assignment matters because it makes treatment and control groups comparable before the treatment begins. By assigning participants by chance, researchers prevent characteristics such as age, motivation, health, or prior ability from systematically determining who receives the treatment. Thus, if the groups later have different outcomes, the treatment is the most plausible explanation rather than a pre-existing difference.
>
> Randomization balances both known and unknown confounding factors on average, which is why it supports causal conclusions. It does not guarantee perfectly identical groups—especially in small samples—and its protection can be weakened by problems such as attrition or failure to follow the assigned treatment. Also, randomized assignment supports causality; random sampling is the separate process that helps generalize results to a wider population.

Result: pass. The response answered immediately, included important limits, and did not append a compulsory question.

## Claude Code runtime attempt

Command surface:

```text
/ai-master-tutor Teach me opportunity cost. I know the definition but cannot apply it.
```

Claude Code result:

```text
Not logged in · Please run /login
```

Result: externally blocked. Claude Code 2.1.198 was installed, and the Skill had already been discovered and installed at `.claude/skills/ai-master-tutor`, but generation could not begin without Claude authentication. This is not counted as a behavioral pass.
