# Forward-test transcripts — v0.3.0

Date: 2026-07-13

Three isolated agents received only the installable Skill path and a learner-facing prompt. They did not receive the rubric, expected behavior, known defects, or intended fixes. Follow-up turns were delivered as learner replies so that mode shifts, challenge, reconstruction, overload recovery, and review could be observed across turns.

## F1 — Novice opportunity-cost path

Learner:

> 从零开始辅导我学习机会成本。我没学过经济学。

Tutor:

> 好，我们从生活选择开始，不需要任何经济学基础。
>
> **机会成本**就是：当你作出一个选择时，所放弃的选项中，价值最高的那一个。
>
> 例如：今晚你只能选一件事——学习、看演唱会，或兼职赚 200 元。你选择学习；如果你原本最想去兼职，那么学习的机会成本就是这次兼职机会及其 200 元收入，不是所有放弃的选项相加。
>
> 现在判断一下：如果你没选学习时，最想做的是看演唱会，那么学习的机会成本是：
>
> A. 兼职赚到的 200 元  
> B. 看演唱会  
> C. 兼职和演唱会加在一起
>
> 只回复一个字母，再用一句话说说原因。

Learner chose B and explained that the concert was the next-best alternative. The tutor then moved from recognition to construction:

> 现在请你自己造一个生活中的例子，用三行回答：
>
> 1. 我选择了：___
> 2. 我放弃的选项有：___
> 3. 其中机会成本是：___，因为___

The learner said gaming had a 500-yuan opportunity cost “because it is money.” The tutor did not reveal the full answer:

> 你前两步做对了：明确了当前选择，也列出了被放弃的选项。
>
> 问题出在“因为这是钱”：**有金钱的选项不一定自动成为机会成本**。关键仍然是——如果不能打游戏，你会在“加班赚 500 元”和“去跑步”之间选哪一个？
>
> 请补一句：**如果不能打游戏，我会选择___，所以打游戏的机会成本是___。**

After the learner reconstructed the answer, the tutor changed the wage condition, asked why the opportunity cost changed, then used a surface-different free-ticket/resale case. The learner passed the transfer item, and the tutor added a boundary about whether resale was truly the next-best action.

Result: **pass**. Observable path: minimal P → A → C → response-specific challenge → reconstruction → changed-condition transfer → boundary refinement. The tutor never treated money as the deciding feature and did not force an unsupported debate at the start.

## F2 — Experienced programmer and overload recovery

Learner:

> 我是有 8 年 Python 经验的程序员，请辅导我学习 Rust 的所有权。不要从什么是变量开始。

Tutor began with code discrimination rather than definitions:

```rust
let x = 42;
let y = x;
println!("{x}, {y}");
```

```rust
let s1 = String::from("rust");
let s2 = s1;
println!("{s1}, {s2}");
```

> 在 Python 中，你大概会把两次赋值都理解为“让新名字指向同一个对象”。这个假设在 Rust 的哪一段失效了？请给出你的预测和因果解释。

The learner identified `Copy` versus move but asked why Rust uses the design. The tutor explained release responsibility, double-free risk, and briefly contrasted `clone`, borrowing, and `Rc`, then assigned a cost-comparison task.

Learner:

> 你刚才一下讲了 move、clone、借用、Rc 和 double free，我现在有点乱。请一次只带我走一步。

Tutor:

> 确实，刚才信息量过大。我们先冻结 `clone`、借用和 `Rc`，只保留一件事：**释放责任**。
>
> ```rust
> let s1 = String::from("rust");
> let s2 = s1;
> ```
>
> 最初，`s1` 负责最终释放这段字符串占用的内存。第二行执行后，这份责任从 `s1` 转交给 `s2`。这个“责任转交”就是 `move`。
>
> 只回答一个选择题：第二行之后，谁负责释放字符串的内存？
>
> A. `s1`  
> B. `s2`  
> C. 两者都负责

After the learner chose B and ended the session, the tutor marked the current secure evidence, left borrowing for the next session, and generated three closed-book prompts at increasing intervals.

Result: **pass with one minor observation**. The expert entry and overload downgrade were strong. The review was concise and retrieval-led; a future iteration could request one explicit likely-error reflection before closing when the learner's time allows.

## F3 — Genuine Interactive reconstruction

Learner:

> 辅导我判断这句话：“只要学生自己生成了答案，就一定比直接教学学得好。”我的理由是生成活动更符合 ICAP，所以任何时候都应该优先生成。

Tutor:

> 你抓住了一个有效方向：当学生具备必要的先备知识、任务设计合适时，解释、预测或举例等生成活动，通常比只听讲带来更深的加工。
>
> 问题在于，你把这种一般趋势过度推广成了无条件规律。ICAP 判断的是学生实际进行的认知活动；“自己写出答案”不一定就是建设性生成，也可能只是猜测或机械拼凑。比如，一个完全不懂方程的新手被要求自己发明解法，可能增加无效负荷并巩固错误；此时先看简短示例，再逐步独立生成，往往更合适。
>
> 最小提示：把“永远优先生成”改成一条有条件的规则，至少考虑先备知识和支架。请重写原句：
>
> **当______时，应优先生成；当______时，应先______，再让学生生成。**

The learner added prerequisite knowledge and scaffolding. The tutor then challenged a second boundary: a learner can generate content that is unrelated to the learning target. The learner revised the rule to add task alignment and corrective feedback.

The tutor tested transfer with a photosynthesis-poster design. The learner redesigned it into a causal diagram, prediction, criteria check, and feedback revision. The tutor closed with:

> 最后做一次不看前文的提取：用两句话写出你的核心判断规则，以及以后最容易犯的一个判断错误。

Result: **strong pass**. The exchange met the strict I threshold: learner model → targeted counterexample → learner revision → new boundary → second reconstruction → surface-different transfer → no-notes metacognition. The new model was more precise than either initial statement.

## Claude Code runtime checks

### C1 — Direct fact query

Prompt:

```text
/ai-master-tutor 《The ICAP Framework》是哪一年发表的？这是普通事实问题，直接告诉我。
```

Result: **pass**. Claude Code answered `2014` with bibliographic detail and did not force a lesson.

### C2 — Explicit misconception repair

The first run was too long and exposed a line from `SKILL.md`. The contract was tightened to require a heading-free first turn with one useful part, one decisive flaw, one contrast, one revision prompt, and no runtime-instruction disclosure.

Final prompt:

```text
/ai-master-tutor 我很确定：ICAP 里的 Interactive 就是师生聊得时间够长、问答轮次够多，所以互动越久学习越好。请检验我的理解。
```

Final response:

> 你对「互动」的直觉抓对了一半——ICAP 的 Interactive 确实发生在师生对话中，这一点没错。但它的决定性特征不是「聊得久、轮次多」，而是**学习者先产出自己的模型，教师针对那个模型提出挑战，学习者据此修正，最终双方共同达成一个比各自单独能做出的更好的解释**——缺少其中任何一环，再长的对话也不是 Interactive。换句话说，一百轮「师问→生答→师评」的问答可以是纯 Active，而一段只有三四轮的「你说→我抓住一个矛盾→你重构→我们一起划定边界」的对话就是 Interactive。请你用这个标准重新判断：如果学生只是在回答教师的提问、教师只是在确认对错，这样的长对话为什么不够 Interactive？

Result: **pass after revision**.

### C3 — Natural-language automatic invocation

Prompt omitted the slash command and asked for one-to-one tutoring in Chinese. Claude Code produced the same focused misconception repair and ended with one own-words revision prompt.

Result: **pass**. Chinese tutoring intent triggered the installed Skill automatically.

## What the tests establish

The traces establish that the protocol can drive distinct novice and expert entry paths, downgrade after overload, repair a concrete misconception without immediately replacing learner thinking, produce genuine challenge/reconstruction, answer plain facts directly, and run in Claude Code by explicit and automatic invocation.

They do not establish population-level learning gains or delayed retention. Those require real learners and delayed tests.
