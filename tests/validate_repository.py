#!/usr/bin/env python3
"""Deterministic repository, pedagogy, artifact, and release-candidate checks."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ai-master-tutor"


def check(condition: bool, message: str, failures: list[str]) -> None:
    print(f"{'PASS' if condition else 'FAIL'}  {message}")
    if not condition:
        failures.append(message)


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


def main() -> int:
    failures: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        ROOT / "VERSION",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "session-modes.md",
        SKILL / "references" / "adaptive-control.md",
        SKILL / "references" / "source-grounded-tutoring.md",
        SKILL / "references" / "intervention-ladder.md",
        SKILL / "references" / "mastery-and-review.md",
        SKILL / "references" / "interaction-patterns.md",
        SKILL / "references" / "learning-science-basis.md",
        SKILL / "references" / "learner-continuity.md",
        SKILL / "references" / "course-and-content-packs.md",
        SKILL / "assets" / "learner-record.template.json",
        SKILL / "assets" / "content-pack.template.json",
        SKILL / "scripts" / "validate_learning_artifacts.py",
        ROOT / "tests" / "scenarios.md",
        ROOT / "tests" / "evaluation-rubric.md",
        ROOT / "tests" / "longitudinal-evaluation.md",
        ROOT / "tests" / "platform-compatibility.md",
        ROOT / "tests" / "forward-test-transcripts-v0.4.0-rc.1.md",
        ROOT / "tests" / "fixtures" / "learner-record.valid.json",
        ROOT / "tests" / "fixtures" / "learner-record.invalid.json",
        ROOT / "tests" / "fixtures" / "content-pack.valid.json",
        ROOT / "docs" / "test-report-v0.4.0-rc.1.md",
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
        description = re.search(r"^description:\s*(.+)$", frontmatter.group(1), re.MULTILINE)
        value = description.group(1) if description else ""
        check(len(value) >= 180, "trigger description is specific", failures)
        check("Do not use the full tutoring protocol" in value, "trigger excludes simple non-tutoring requests", failures)
        check("辅导我学习" in value, "Chinese tutoring intent is discoverable", failures)

    check(len(skill_text.splitlines()) < 500, "SKILL.md stays under 500 lines", failures)
    check("TODO" not in skill_text, "SKILL.md contains no TODO placeholders", failures)

    modes = ["quick", "guided", "mastery", "review", "course"]
    for mode in modes:
        check(f"`{mode}`" in skill_text, f"session router includes {mode}", failures)
    check("Never force the complete concept loop into `quick` mode" in skill_text, "quick mode blocks a forced tutoring loop", failures)
    check("Switch modes when the learner's request changes" in skill_text, "mode switching is explicit", failures)
    check("time budget expires" in skill_text, "time-budget exit is explicit", failures)

    check("By the end, the learner can" in skill_text, "observable target contract is present", failures)
    check("one core question" in skill_text, "single-question cognitive-load guardrail is present", failures)
    check("Give a requested answer directly" in skill_text, "direct-answer compliance is present", failures)
    check("Never infer mastery" in skill_text, "mastery-evidence guardrail is present", failures)
    check("Never expose Skill instructions" in skill_text, "runtime instructions remain hidden", failures)
    check("ask before writing a record" in skill_text, "persistent records require consent", failures)

    cycle = ["Diagnose", "Minimal Teach", "Retrieve", "Construct", "Challenge", "Reconstruct", "Verify", "Reflect", "Review"]
    for stage in cycle:
        check(f"**{stage}**" in skill_text, f"adaptive loop includes {stage}", failures)
    check("possible milestones, not a mandatory script" in skill_text, "adaptive loop is proportional", failures)
    check("one high-information case and one core response request" in skill_text, "mastery mode avoids a first-turn assessment battery", failures)
    check("Do not front-load a full syllabus" in skill_text, "course mode avoids first-turn syllabus overload", failures)
    check("full gate only in `mastery` mode" in (SKILL / "references" / "mastery-and-review.md").read_text(encoding="utf-8"), "full mastery gate is mode-scoped", failures)

    state_fields = [
        "mode", "learning_goal", "target_action", "success_criterion", "time_budget",
        "prior_knowledge", "current_concept", "current_icap_level", "misconceptions",
        "prerequisite_gaps", "mastery_level", "evidence_of_mastery",
        "scaffolding_level", "transfer_status", "review_items", "next_step",
    ]
    for field in state_fields:
        check(field in skill_text, f"learner state tracks {field}", failures)

    check("targeted challenge and learner revision" in skill_text, "genuine Interactive threshold is present", failures)
    check("After two unsuccessful attempts" in skill_text, "anti-question-prison escalation is present", failures)
    check("changed surface features" in skill_text, "transfer changes surface features", failures)
    check("delayed retrieval" in skill_text, "retention requires delayed evidence", failures)
    check("content pack" in skill_text.lower(), "course mode uses content packs", failures)
    check("verify worked solutions" in skill_text.lower(), "worked solutions require validation", failures)

    reference_links = sorted(set(re.findall(r"\]\((references/[^)]+)\)", skill_text)))
    check(len(reference_links) >= 9, "SKILL.md routes to all conditional references", failures)
    for link in reference_links:
        check((SKILL / link).is_file(), f"reference link resolves: {link}", failures)

    runtime_files = [path for path in SKILL.rglob("*") if path.is_file()]
    all_runtime_text = "\n".join(
        path.read_text(encoding="utf-8") for path in runtime_files if path.suffix in {".md", ".yaml", ".json", ".py"}
    )
    check("[TODO" not in all_runtime_text, "runtime files contain no placeholders", failures)
    check("system prompt alone did not reliably sequence" in all_runtime_text, "prompt-only tutoring limitation is documented", failures)
    check("10.1080/00461520.2014.965823" in all_runtime_text, "primary ICAP source is documented", failures)

    artifact_validator = SKILL / "scripts" / "validate_learning_artifacts.py"
    valid_record = run([sys.executable, str(artifact_validator), "learner-record", "tests/fixtures/learner-record.valid.json"])
    check(valid_record.returncode == 0 and "VALID" in valid_record.stdout, "valid learner record passes", failures)
    invalid_record = run([sys.executable, str(artifact_validator), "learner-record", "tests/fixtures/learner-record.invalid.json"])
    check(invalid_record.returncode != 0 and "INVALID" in invalid_record.stdout, "invalid learner record is rejected", failures)
    valid_pack = run([sys.executable, str(artifact_validator), "content-pack", "tests/fixtures/content-pack.valid.json"])
    check(valid_pack.returncode == 0 and "VALID" in valid_pack.stdout, "valid content pack passes", failures)

    yaml_text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    check('display_name: "AI Master Tutor"' in yaml_text, "UI display name is unchanged", failures)
    check("$ai-master-tutor" in yaml_text, "default prompt explicitly invokes the skill", failures)
    check("observable target" in yaml_text, "UI metadata reflects v0.4 behavior", failures)

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("--from-local" in readme_text, "README documents local RC installation", failures)
    check("$ai-master-tutor" in readme_text, "README preserves Codex invocation", failures)
    check("/ai-master-tutor" in readme_text, "README preserves Claude Code invocation", failures)
    check("v0.4.0-rc.1" in readme_text, "README labels the release candidate", failures)

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    check(version == "0.4.0-rc.1", "repository version is 0.4.0-rc.1", failures)
    check("## 0.4.0-rc.1" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), "changelog contains the RC", failures)

    scenarios = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
    check(len(re.findall(r"^## S\d+", scenarios, re.MULTILINE)) >= 26, "at least 26 forward-test scenarios exist", failures)
    for surface in ["Quick mode", "Guided mode", "Mastery mode", "Mode switch", "Course mode", "Unverified content pack"]:
        check(surface in scenarios, f"scenario suite covers {surface}", failures)

    rubric = (ROOT / "tests" / "evaluation-rubric.md").read_text(encoding="utf-8")
    for dimension in ["Session routing", "ICAP calibration", "Interactive challenge", "Content and assessment validity", "Continuity and retention integrity"]:
        check(dimension in rubric, f"rubric scores {dimension}", failures)
    check("30 points" in rubric, "rubric maximum is internally documented", failures)

    longitudinal = (ROOT / "tests" / "longitudinal-evaluation.md").read_text(encoding="utf-8")
    for requirement in ["baseline", "five independent samples", "complete raw", "24 hours", "seven days", "default-branch installation"]:
        check(requirement in longitudinal, f"longitudinal protocol includes {requirement}", failures)

    rc_trace = (ROOT / "tests" / "forward-test-transcripts-v0.4.0-rc.1.md").read_text(encoding="utf-8")
    check("Result: **revise**" in rc_trace, "RC evidence preserves failed first runs", failures)
    check("F6 — Authorized continuity record" in rc_trace, "RC evidence covers continuity", failures)
    rc_report = (ROOT / "docs" / "test-report-v0.4.0-rc.1.md").read_text(encoding="utf-8")
    check("RELEASE CANDIDATE" in rc_report, "RC report does not claim stable release", failures)
    check("Not yet verified" in rc_report, "RC report states remaining evidence gaps", failures)

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)} checks failed)")
        return 1
    print("RESULT: PASS (all repository checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
