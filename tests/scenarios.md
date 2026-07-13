# Forward-test scenarios

Use each prompt with the installable Skill and score the output using `evaluation-rubric.md`. Do not show the expected behaviors to the model under test. For explicit invocation, prepend `Use $ai-master-tutor to` in Codex or invoke `/ai-master-tutor` in Claude Code. Also sample natural-language automatic invocation on both platforms.

## S1 — Novice begins a paper

```text
Help me learn the 2025 paper “AI tutoring outperforms in-class active learning.” I have only read the title and I am new to research papers.
```

Expected test surface: source-status honesty, minimal diagnosis, novice pacing, no abstract dump.

## S2 — Learner supplies a misconception

```text
Teach me cognitive load theory. My current view is: difficult material creates cognitive load, so good teaching should make everything easy.
```

Expected test surface: confirm useful part, distinguish necessary complexity from avoidable load, use contrast and revision.

## S3 — Repeated “I don't know”

```text
Teach me Bayes' theorem. I am starting from zero and equations scare me.
```

Follow-up learner turns:

```text
I don't know.
```

```text
Still don't know. Please stop asking me to guess.
```

Expected test surface: switch from questions to direct teaching, smaller representation, no question prison.

## S4 — Direct-answer request

```text
Help me understand why randomized assignment matters. I tried: “It makes the groups identical.” Just tell me the correct answer first, then explain briefly.
```

Expected test surface: answer-first compliance, precision about balance in expectation, optional check after explanation.

## S5 — Advanced learner

```text
Test my understanding of retrieval practice. I know the classic testing effect and do not need definitions. Focus on boundary conditions and transfer.
```

Expected test surface: no novice lecture, challenging cases, no redundant diagnosis.

## S6 — Source is incomplete

```text
Teach me the whole argument of a paper. Here is all I have: “AI tutors improve learning.”
```

Expected test surface: refuses to pretend it has the paper, asks for a source or narrows the goal, distinguishes claim from evidence.

## S7 — Overloaded learner

```text
Continue teaching me regression. We already covered correlation, slope, residuals, R-squared, confounding, interactions, and p-values, but now it is all mixed together and I feel lost.
```

Expected test surface: cognitive reset, one foothold, choice or tiny task, no motivational essay.

## S8 — Mastery claim

```text
Check whether I have mastered opportunity cost. I can repeat the definition from memory.
```

Expected test surface: does not accept definition as mastery, uses a new application and contrast, avoids arbitrary percentage.

## S9 — Procedural skill

```text
Teach me how to debug a failing unit test. I am a beginner and tend to change random lines until it passes.
```

Expected test surface: models decisions, uses worked example then completion/independent case, addresses the random-edit misconception.

## S10 — Review planning

```text
End today's session on cognitive load theory and make a review plan. Do not pretend you can remind me automatically.
```

Expected test surface: retrieval before summary, evidence-based handoff, suggested intervals clearly labeled as suggestions.
