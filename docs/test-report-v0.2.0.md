# AI Master Tutor v0.2.0 — Cross-platform Compatibility Report

Date: 2026-07-13

Status: **PASS**

## Outcome

Version 0.2.0 migrates the repository to the standard Agent Skills layout and supports installation into both Codex and Claude Code from one canonical Skill. Static structure, host-specific installation, Codex validation, tutoring behavior regression, Claude Code direct invocation, and Claude Code automatic invocation all passed after one test-driven revision.

## Official requirements checked

Claude Code's documented personal Skill path is `~/.claude/skills/<skill-name>/SKILL.md`; project Skills live at `.claude/skills/<skill-name>/SKILL.md`. A Skill uses YAML frontmatter plus Markdown instructions, may include referenced supporting files, and can be invoked directly as `/<skill-name>` or automatically from its description.

The canonical package now lives at:

```text
skills/ai-master-tutor/SKILL.md
```

It retains only `name` and `description` in canonical frontmatter, which is accepted by both Codex and Claude Code. Codex-only UI metadata remains in `agents/openai.yaml` as an unreferenced supporting file and does not fork the tutoring protocol.

Official reference: https://code.claude.com/docs/en/slash-commands

## Tests performed

### T1 — Codex structural validation

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/ai-master-tutor
```

Result: pass (`Skill is valid!`).

### T2 — Standard repository discovery

```bash
gh skill install . ai-master-tutor --from-local --dir <isolated-dir> --force
```

Result: pass. GitHub CLI discovered `ai-master-tutor` by name from the standard `skills/*/SKILL.md` layout and installed the entrypoint, all five references, and Codex UI metadata.

### T3 — Host-specific installation

Using an isolated temporary HOME, the same local repository was installed with:

```bash
gh skill install . ai-master-tutor --from-local \
  --agent codex --scope user --force

gh skill install . ai-master-tutor --from-local \
  --agent claude-code --scope user --force
```

Result: pass. Files landed at both expected locations:

```text
~/.codex/skills/ai-master-tutor/SKILL.md
~/.claude/skills/ai-master-tutor/SKILL.md
```

### T4 — Tutoring behavior regression

Three fresh isolated agent instances loaded the migrated canonical Skill and handled:

- a cognitive-load misconception;
- an incomplete paper source;
- a direct-answer request that prohibited follow-up quizzing.

Result: 3/3 pass with no critical rubric failure. Raw traces are in `tests/forward-test-transcripts-v0.2.0.md`.

### T5 — Authenticated Claude Code direct invocation

Claude Code version detected: `2.1.198`.

The final direct invocation used:

```text
/ai-master-tutor Teach me opportunity cost. I know the definition but cannot apply it.
```

Result: pass. Claude Code resolved the slash command, skipped the redundant definition check, and presented an application case with one focused question.

### T6 — Authenticated Claude Code automatic invocation

The final natural-language prompt used:

```text
Tutor me through cognitive load theory. I think good teaching should remove all difficulty.
```

Result: pass. Claude Code automatically discovered the Skill, loaded the learning-science reference, and began with one concise diagnostic question.

### Test-driven revision

The first authenticated run exposed two quality issues: a redundant definition check after the learner reported an application gap, and an automatic response that became a long lecture using the contested three-load model as settled terminology. The Skill was revised to strengthen its trigger description, route application gaps directly to application tasks, and load the evidence reference when teaching learning-science concepts. Both Claude tests then passed.

## Compatibility changes

1. Renamed the repository package root from `skill/` to the standard `skills/` convention.
2. Added Codex and Claude Code installation commands using `gh skill install`.
3. Added native invocation documentation for `$ai-master-tutor` and `/ai-master-tutor`.
4. Added source-tracked update instructions through `gh skill update`.
5. Added six platform compatibility scenarios and deterministic repository checks.
6. Preserved one shared `SKILL.md` and reference set to prevent platform drift.

## Release decision

All v0.2.0 compatibility gates passed. The version is ready to merge, tag, install from the GitHub release, and publish.
