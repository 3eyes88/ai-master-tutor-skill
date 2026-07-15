# Platform compatibility scenarios

Validate the same canonical Skill on both Codex and Claude Code. Do not maintain platform-specific copies of `SKILL.md`.

## P1 — Standard discovery layout

Confirm the repository exposes exactly one canonical entrypoint at:

```text
skills/ai-master-tutor/SKILL.md
```

Expected: `gh skill install` discovers `ai-master-tutor` by name.

## P2 — Codex explicit invocation

```text
Use $ai-master-tutor to teach me opportunity cost. I know the definition but cannot apply it.
```

Expected: the Skill loads, avoids repeating only the definition, and begins with an application or diagnostic.

## P3 — Claude Code explicit invocation

```text
/ai-master-tutor Teach me opportunity cost. I know the definition but cannot apply it.
```

Expected: Claude Code resolves the slash command and follows the same tutoring contract.

## P4 — Claude Code automatic invocation

```text
Tutor me through cognitive load theory. I think good teaching should remove all difficulty.
```

Expected: Claude Code discovers the Skill from its description and repairs the misconception through a focused contrast or diagnostic.

## P5 — Supporting-file resolution

```text
/ai-master-tutor I only have the sentence “AI tutors improve learning.” Teach me the whole paper.
```

Expected: the tutor follows `references/source-grounded-tutoring.md`, states that the source is incomplete, and does not invent the paper.

## P6 — Platform metadata isolation

Confirm Claude Code accepts the Skill even though `agents/openai.yaml` is present for Codex UI metadata.

Expected: Claude Code ignores unreferenced platform metadata; both platforms load the same `SKILL.md` and `references/` files.

## P7 — Local release-candidate installation

From the repository root, run on both hosts:

```bash
gh skill install . ai-master-tutor --from-local --agent codex --scope user --force
gh skill install . ai-master-tutor --from-local --agent claude-code --scope user --force
```

Expected: both installations contain the same entrypoint, nine references, two JSON templates, and the artifact validator. The source canonical frontmatter remains limited to `name` and `description`; installer-added metadata does not alter runtime instructions.

## P8 — Portable continuity artifacts

Validate the same fixture with the bundled script under both host environments:

```bash
python3 skills/ai-master-tutor/scripts/validate_learning_artifacts.py \
  learner-record tests/fixtures/learner-record.valid.json
```

Expected: the JSON record validates without product-specific dependencies. Neither host writes or claims to remember the record unless the learner authorizes persistence and the file operation succeeds.
