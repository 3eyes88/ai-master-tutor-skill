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
