#!/usr/bin/env python3
"""Deterministic repository and Skill integrity checks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ai-master-tutor"


def check(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS  {message}")
    else:
        print(f"FAIL  {message}")
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        ROOT / "VERSION",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "source-grounded-tutoring.md",
        SKILL / "references" / "intervention-ladder.md",
        SKILL / "references" / "mastery-and-review.md",
        SKILL / "references" / "interaction-patterns.md",
        SKILL / "references" / "learning-science-basis.md",
        ROOT / "tests" / "scenarios.md",
        ROOT / "tests" / "evaluation-rubric.md",
        ROOT / "tests" / "forward-test-transcripts-v0.1.0.md",
        ROOT / "tests" / "forward-test-transcripts-v0.2.0.md",
        ROOT / "tests" / "platform-compatibility.md",
        ROOT / "docs" / "test-report-v0.1.0.md",
        ROOT / "docs" / "test-report-v0.2.0.md",
    ]
    for path in required:
        check(path.is_file(), f"required file: {path.relative_to(ROOT)}", failures)

    if failures:
        print(f"\nFAILED early: {len(failures)} required files missing")
        return 1

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
    check(frontmatter is not None, "SKILL.md has YAML frontmatter", failures)
    if frontmatter:
        keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter.group(1), re.MULTILINE)
        check(keys == ["name", "description"], "frontmatter contains only name and description", failures)
        check("name: ai-master-tutor" in frontmatter.group(1), "skill name is normalized", failures)
        description_match = re.search(r"^description:\s*(.+)$", frontmatter.group(1), re.MULTILINE)
        check(bool(description_match and len(description_match.group(1)) >= 100), "trigger description is specific", failures)

    check(len(skill_text.splitlines()) < 500, "SKILL.md stays under 500 lines", failures)
    check("TODO" not in skill_text, "SKILL.md contains no TODO placeholders", failures)
    check("one substantive question at a time" in skill_text, "question-load guardrail is present", failures)
    check("After two unsuccessful attempts" in skill_text, "anti-question-prison escalation is present", failures)
    check("Never infer mastery" in skill_text, "mastery-evidence guardrail is present", failures)
    check("Ground claims in the supplied source" in skill_text, "source-grounding guardrail is present", failures)
    check("begin with an application or discrimination task" in skill_text, "stated application gaps bypass redundant definition checks", failures)
    check("when teaching learning-science concepts themselves" in skill_text, "learning-science topics route to the evidence reference", failures)
    skill_entrypoints = sorted(ROOT.glob("skills/*/SKILL.md"))
    check(skill_entrypoints == [SKILL / "SKILL.md"], "one canonical Agent Skills entrypoint exists", failures)
    check(not (ROOT / "skill").exists(), "legacy singular skill directory is absent", failures)

    reference_links = re.findall(r"\]\((references/[^)]+)\)", skill_text)
    check(len(reference_links) >= 5, "SKILL.md routes to conditional references", failures)
    for link in sorted(set(reference_links)):
        check((SKILL / link).is_file(), f"reference link resolves: {link}", failures)

    all_runtime_text = "\n".join(
        path.read_text(encoding="utf-8") for path in SKILL.rglob("*") if path.is_file()
    )
    check("[TODO" not in all_runtime_text, "runtime files contain no template placeholders", failures)
    check("three uncontested independent sources" in all_runtime_text, "cognitive-load terminology guardrail is present", failures)

    yaml_text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    check('display_name: "AI Master Tutor"' in yaml_text, "UI display name is configured", failures)
    check("$ai-master-tutor" in yaml_text, "default prompt explicitly invokes the skill", failures)

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("--agent codex --scope user" in readme_text, "README documents Codex installation", failures)
    check("--agent claude-code --scope user" in readme_text, "README documents Claude Code installation", failures)
    check("$ai-master-tutor" in readme_text, "README documents Codex invocation", failures)
    check("/ai-master-tutor" in readme_text, "README documents Claude Code invocation", failures)

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    check(version == "0.2.0", "repository version is 0.2.0", failures)
    scenarios = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
    check(len(re.findall(r"^## S\d+", scenarios, re.MULTILINE)) >= 10, "at least 10 forward-test scenarios exist", failures)
    platform_scenarios = (ROOT / "tests" / "platform-compatibility.md").read_text(encoding="utf-8")
    check(len(re.findall(r"^## P\d+", platform_scenarios, re.MULTILINE)) >= 6, "at least 6 platform scenarios exist", failures)

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)} checks failed)")
        return 1
    print("RESULT: PASS (all repository checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
