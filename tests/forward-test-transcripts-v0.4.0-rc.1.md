# Forward-test transcripts — v0.4.0-rc.1

Date: 2026-07-15

Fresh isolated agents received only the candidate Skill path and a learner-facing prompt. They did not receive the rubric, expected behavior, audit findings, or intended fixes. All first-run problems and retests are preserved below.

## F1 — Quick mode

Learner:

> Use $ai-master-tutor in quick mode. Explain opportunity cost in at most four sentences. Do not quiz me.

Tutor:

> Opportunity cost is the value of the best alternative you give up when making a choice. If you spend an evening working, the opportunity cost might be the most valuable thing you could have done instead, such as resting or seeing friends. It is not the sum of every rejected option—only the next-best one.

Result: **pass**. The response remained within four sentences, answered directly, and did not append a quiz or mastery claim.

## F2 — Mastery mode, first run

Learner:

> Use $ai-master-tutor in mastery mode to check whether I truly understand randomized assignment. Do not review the definition first.

Tutor:

> Good—we’ll test, not review. Please answer from memory without notes.
>
> A researcher recruits 120 volunteers from one high school, then uses a random-number generator to assign each volunteer to either a new study app or the usual study routine. After eight weeks, the app group scores higher.
>
> In your own words, explain:
>
> 1. What randomized assignment lets the researcher conclude, and why.
> 2. One conclusion this design does *not* justify.
> 3. Whether the study would still use randomized assignment if students were placed into groups by alternating down an alphabetized roster—and why.
>
> Don’t aim for textbook wording; show me your reasoning.

Result: **revise**. It correctly started with evidence instead of a definition, but front-loaded three assessment requests. The protocol was tightened to require one high-information case and one core response request, with later dimensions selected from the learner's answer.

## F3 — Course mode, first run

Learner:

> Use $ai-master-tutor in course mode to help me learn Rust over several weeks. Build the first checkpoint. You may not write any learner record until I agree.

Tutor:

> We’ll use course mode and work toward one outcome: independently build, test, and debug a small Rust command-line application while explaining the Rust-specific design choices.
>
> No learner record has been created or modified. Until you explicitly agree, progress remains only in this conversation.
>
> ### Provisional course map
>
> 1. Cargo, variables, types, functions, and expressions
> 2. Ownership, borrowing, references, and slices
> 3. Structs, enums, `match`, and domain modeling
> 4. Collections, modules, and error handling
> 5. Generics, traits, and lifetimes
> 6. Iterators, closures, and automated tests
> 7. Cumulative CLI project and transfer checkpoint
>
> We’ll use stable Rust with Rust 2024 Edition conventions, following the official Rust Book and its common programming concepts.
>
> ### Checkpoint 1 — From source code to a working program
>
> **Target:** Create a Cargo project and independently implement a small calculation function using typed parameters, immutable bindings, intentional mutation, and expression-based control flow.
>
> **Completion evidence:**
>
> - Explain variables, mutability, and expressions in your own words.
> - Implement and run the function correctly.
> - Identify a version that fails to compile and explain why.
> - Adapt the same ideas to a changed problem.
> - Name your likeliest mistake and how compiler output would reveal it.
>
> This establishes current performance; retention will remain untested until a later closed-book retrieval.
>
> ### Starting diagnostic
>
> Without running or searching this code, predict whether it compiles, what it prints if it does, and explain the roles of `mut`, `bonus`, and the final `n`:
>
> ```rust
> fn adjust(mut n: i32) -> i32 {
>     let bonus = if n > 10 { 2 } else { 5 };
>     n = n + bonus;
>     n
> }
>
> fn main() {
>     let score = 8;
>     println!("{}", adjust(score));
> }
> ```
>
> Also include:
>
> ```text
> Programming background:
> Rust experience:
> Time available per week:
> Prediction and reasoning:
> ```
>
> “Start from zero” is a completely valid answer.

Result: **revise**. Consent handling and the learning target were correct, but the first turn overloaded the learner with a full syllabus, a five-part evidence gate, a diagnostic, and a background form. The protocol was tightened to show only the outcome, current checkpoint, one task, and an applicable consent statement.

## F4 — Mastery mode retest

Learner:

> Use $ai-master-tutor in mastery mode to check whether I truly understand randomized assignment. Do not review the definition first.

Tutor:

> Let’s test it cold—no definition review.
>
> A researcher recruits 200 volunteers from one high school and randomly assigns each student by coin flip to receive either a free breakfast or no breakfast. After eight weeks, the breakfast group’s average math score is higher. However, more students dropped out of the no-breakfast group.
>
> Evaluate this claim:
>
> “Randomized assignment proves that free breakfast improves math scores for all high-school students.”
>
> Rewrite it as the strongest conclusion the evidence actually supports, and explain your reasoning. Address both the “proves causation” and “all high-school students” parts, including why the unequal dropout matters.

Result: **pass**. It used one case and one integrated response request. The case discriminates causal inference, external validity, and attrition without presenting a rubric battery.

## F5 — Course mode retest

Learner:

> Use $ai-master-tutor in course mode to help me learn Rust over several weeks. Build the first checkpoint. You may not write any learner record until I agree.

Tutor:

> We’ll use course mode over several weeks, adapting the path from your actual work.
>
> **Course outcome:** You’ll be able to independently design, build, test, and debug a small Rust command-line program, including explaining the ownership and borrowing choices that make it safe.
>
> **Checkpoint 1 — Running Rust and reasoning about ownership**
>
> Using stable Rust with the 2024 edition, you will:
>
> - Create and run a Cargo project.
> - Read a compiler error as useful evidence.
> - Predict basic move and mutability behavior.
> - Repair a small program without unnecessary cloning.
>
> We’ll use the current official Rust Book and Cargo documentation as the content basis.
>
> **First diagnostic — no running or searching yet:**
>
> ```rust
> fn main() {
>     let mut s = String::from("rust");
>     let t = s;
>     s.push('!');
>     println!("{t}");
> }
> ```
>
> Does this compile? If not, explain the compiler’s objection and change at most two lines so it prints `rust!` without using `clone()`.
>
> If you’re completely new to programming or Rust, simply reply **“start from zero.”**
>
> No learner record has been created. Until you explicitly agree, everything remains session-local; if you later consent, the record would be written to `.ai-master-tutor/learner-record.json` and contain only learning evidence, checkpoint status, and next steps.

Result: **pass with a minor density note**. It showed one outcome, one checkpoint, one task, and the persistence boundary. The checkpoint contains four tightly related criteria but no full-course dump or background questionnaire.

## F6 — Authorized continuity record

The agent was authorized to read `tests/fixtures/learner-record.valid.json`.

Learner:

> Continue my course. What do you know about my retention, and what should we do first?

Tutor:

> 你的记录显示：上次你能在“时间分配”的新情境中，无提示且理由完整地找出机会成本，表现达到了迁移水平。但那只是即时表现；目前没有延迟提取证据，所以还不能判断你是否真正保持住了。
>
> 第一步先不重讲，做一次闭卷提取：
>
> 你收到 5000 元奖金，只能选择一项：
>
> - 报课程，对你价值约 900 元
> - 升级手机，价值约 700 元
> - 提前还款，节省约 600 元利息
>
> 你选择报课程。它的机会成本是什么？请用一两句话说明理由。

Result: **pass**. It used task, support, reasoning, and timing evidence; it explicitly left retention untested and selected delayed retrieval before reteaching.

## What these tests establish

The candidate can route a direct explanation, mastery check, course start, and authorized continuity record into meaningfully different first turns. Two initial overloading failures produced protocol changes and passed isolated retests.

These tests do not establish multi-turn stability across all 26 scenarios, subject-matter accuracy across domains, human learning gains, delayed retention, baseline superiority, or cross-platform installation. Those remain release-candidate gates in `tests/longitudinal-evaluation.md`.
