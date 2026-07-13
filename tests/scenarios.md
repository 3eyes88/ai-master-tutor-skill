# Forward-test scenarios

Use each prompt with the installable Skill and score observable behavior using `evaluation-rubric.md`. Do not show expected behavior to the model under test. For explicit invocation, prepend `Use $ai-master-tutor to` in Codex or invoke `/ai-master-tutor` in Claude Code. Sample natural-language invocation on both platforms.

## S1 — Novice begins a paper

```text
Help me learn the 2025 paper “AI tutoring outperforms in-class active learning.” I have only read the title and I am new to research papers.
```

Surface: source-status honesty, minimal diagnosis, novice pacing, no abstract dump.

## S2 — Cognitive-load misconception

```text
Teach me cognitive load theory. My current view is: difficult material creates cognitive load, so good teaching should make everything easy.
```

Surface: productive-part preservation, exact overgeneralization, contrast, learner revision.

## S3 — Repeated “I don't know”

```text
Teach me Bayes' theorem. I am starting from zero and equations scare me.
```

Follow-ups: `I don't know.` then `Still don't know. Please stop asking me to guess.`

Surface: shift downward, direct teaching, smaller representation, no question prison.

## S4 — Direct-answer request

```text
Help me understand why randomized assignment matters. I tried: “It makes the groups identical.” Just tell me the correct answer first, then help me learn it.
```

Surface: answer-first compliance, concise correction, one meaningful follow-up activity.

## S5 — Advanced learner

```text
Test my understanding of retrieval practice. I know the classic testing effect and do not need definitions. Focus on boundary conditions and transfer.
```

Surface: no novice lecture, C/I entry, counterexample or boundary, transfer.

## S6 — Source is incomplete

```text
Teach me the whole argument of a paper. Here is all I have: “AI tutors improve learning.”
```

Surface: source limit, no fabrication, request/narrow minimum source.

## S7 — Overloaded learner

```text
Continue teaching me regression. We covered correlation, slope, residuals, R-squared, confounding, interactions, and p-values, but now it is all mixed together and I feel lost.
```

Surface: freeze content, one foothold, one question, P/A support before upgrading.

## S8 — Mastery claim

```text
Check whether I have mastered opportunity cost. I can repeat the definition from memory.
```

Surface: definition is insufficient; example, boundary, varied application, likely-error evidence.

## S9 — Procedural skill

```text
Teach me how to debug a failing unit test. I am a beginner and tend to change random lines until it passes.
```

Surface: worked example → completion → variation; decision-focused correction.

## S10 — Review planning

```text
End today's session on cognitive load theory and make a review plan. Do not pretend you can remind me automatically.
```

Surface: retrieval before summary, two to five prompts, concise suggested spacing.

## S11 — Zero-knowledge opportunity cost

```text
从零开始辅导我学习“机会成本”。我没学过经济学。
```

Follow learner through at least four turns.

Surface: minimal plain-language teaching and life example; P→A before C; learner's own example; surface-different transfer; no early debate.

## S12 — Experienced programmer learns a new language

```text
我是有 8 年 Python 经验的程序员，请辅导我学习 Rust 的所有权。不要从“什么是变量”开始。
```

Surface: uses prior schemas, rapidly enters code comparison/problem solving, adds prerequisites only when evidence shows a gap.

## S13 — “Just tell me” fact versus lesson

Run both:

```text
《The ICAP Framework》是哪一年发表的？直接告诉我。
```

```text
我正在学习随机分配，直接告诉我它为什么重要，然后继续辅导我。
```

Surface: first is a direct fact without forced lesson; second answers first then requests one explanation/application/retrieval move.

## S14 — Confident but wrong explanation

```text
我很确定：ICAP 里的 Interactive 就是师生聊得时间够长、问答轮次够多，所以互动越久学习越好。请检验我的理解。
```

Follow learner through challenge and revision.

Surface: exact misconception, response-specific counterexample/boundary, learner reconstruction, no generic praise.

## S15 — Strong foundations

```text
我已经能准确解释认知负荷理论，也能区分必要复杂性和无关负荷。不要再讲定义，检验我能否处理反例和跨领域迁移。
```

Surface: starts C/I, fades scaffolding, uses boundary and farther transfer, no redundant basics.

## S16 — Cognitive overload during a challenge

```text
你刚才的反例和三个条件让我彻底乱了。请一次只带我走一步。
```

Surface: immediately shortens, one question, completion/choice/worked example, temporarily shifts I/C → A/P, then fades later.

## S17 — Passive learner refuses to generate

```text
你继续讲就行，我只想听，不想回答问题。
```

Surface: requests one minimal output such as choice/completion/one sentence; offers direct-explanation mode or pause after refusal; does not lecture indefinitely or claim mastery.

## S18 — Genuine Interactive cycle

```text
辅导我判断这句话：“只要学生自己生成了答案，就一定比直接教学学得好。”我的理由是生成活动更符合 ICAP，所以任何时候都应该优先生成。
```

Follow at least three learner turns, including an attempted revision.

Surface: learner model → targeted challenge about prerequisites/guessing → learner revision → tutor tests boundary → jointly improved scoped model; must not label ordinary dialogue as I.
