# AI Master Tutor v0.2.0 — Cross-platform Compatibility Report

Date: 2026-07-13

Status: **Compatibility implementation passed; authenticated Claude Code generation pending**

## Outcome

Version 0.2.0 migrates the repository to the standard Agent Skills layout and supports installation into both Codex and Claude Code from one canonical Skill. Static structure, host-specific installation, Codex validation, and tutoring behavior regression tests passed. The final authenticated Claude Code response test could not run because the local Claude CLI was not logged in.

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

### T5 — Authenticated Claude Code generation

Claude Code version detected: `2.1.198`.

The direct invocation attempt returned:

```text
Not logged in · Please run /login
```

Result: blocked by external authentication. The test must be repeated after running `/login` in Claude Code. No claim of an authenticated Claude-generated response is made in this report.

## Compatibility changes

1. Renamed the repository package root from `skill/` to the standard `skills/` convention.
2. Added Codex and Claude Code installation commands using `gh skill install`.
3. Added native invocation documentation for `$ai-master-tutor` and `/ai-master-tutor`.
4. Added source-tracked update instructions through `gh skill update`.
5. Added six platform compatibility scenarios and deterministic repository checks.
6. Preserved one shared `SKILL.md` and reference set to prevent platform drift.

## Remaining release gate

Run one authenticated Claude Code direct invocation and one natural-language automatic invocation. If both follow the tutoring contract, mark the compatibility report fully passed and release `v0.2.0`.
