#!/usr/bin/env python3
"""Validate AI Master Tutor learner records and content packs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


MODES = {"quick", "guided", "mastery", "review", "course"}
GOAL_STATUSES = {"active", "paused", "complete", "archived"}
PACK_STATUSES = {"provisional", "verified", "deprecated"}
ITEM_KINDS = {"retrieval", "independent", "boundary", "transfer", "cumulative"}
VERIFICATION_STATUSES = {"unverified", "checked", "authoritative"}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_learner_record(data: Any) -> list[str]:
    errors: list[str] = []
    require(isinstance(data, dict), "record must be a JSON object", errors)
    if not isinstance(data, dict):
        return errors

    require(data.get("schema_version") == "1.0", "schema_version must be 1.0", errors)
    require(isinstance(data.get("goals"), list), "goals must be a list", errors)
    require(isinstance(data.get("concepts"), dict), "concepts must be an object", errors)
    require(isinstance(data.get("evidence"), list), "evidence must be a list", errors)
    require(isinstance(data.get("review_queue"), list), "review_queue must be a list", errors)

    preferences = data.get("preferences", {})
    if isinstance(preferences, dict) and preferences.get("default_mode"):
        require(preferences["default_mode"] in MODES, "preferences.default_mode is invalid", errors)

    for index, goal in enumerate(data.get("goals", [])):
        prefix = f"goals[{index}]"
        require(isinstance(goal, dict), f"{prefix} must be an object", errors)
        if not isinstance(goal, dict):
            continue
        require(is_nonempty_string(goal.get("goal_id")), f"{prefix}.goal_id is required", errors)
        require(is_nonempty_string(goal.get("outcome")), f"{prefix}.outcome is required", errors)
        require(is_nonempty_string(goal.get("success_criterion")), f"{prefix}.success_criterion is required", errors)
        require(goal.get("status") in GOAL_STATUSES, f"{prefix}.status is invalid", errors)

    for index, item in enumerate(data.get("evidence", [])):
        prefix = f"evidence[{index}]"
        require(isinstance(item, dict), f"{prefix} must be an object", errors)
        if not isinstance(item, dict):
            continue
        for field in ("concept_id", "observed_at", "task_id", "result", "evidence_level"):
            require(is_nonempty_string(item.get(field)), f"{prefix}.{field} is required", errors)
        support = item.get("support_level")
        require(isinstance(support, int) and 0 <= support <= 5, f"{prefix}.support_level must be 0..5", errors)

    return errors


def validate_content_pack(data: Any) -> list[str]:
    errors: list[str] = []
    require(isinstance(data, dict), "pack must be a JSON object", errors)
    if not isinstance(data, dict):
        return errors

    require(data.get("schema_version") == "1.0", "schema_version must be 1.0", errors)
    require(is_nonempty_string(data.get("pack_id")), "pack_id is required", errors)
    require(is_nonempty_string(data.get("title")), "title is required", errors)
    require(data.get("status") in PACK_STATUSES, "status is invalid", errors)
    require(isinstance(data.get("sources"), list), "sources must be a list", errors)
    require(isinstance(data.get("concepts"), list) and bool(data.get("concepts")), "concepts must be a non-empty list", errors)

    concept_ids: set[str] = set()
    concepts = data.get("concepts", [])
    for index, concept in enumerate(concepts):
        prefix = f"concepts[{index}]"
        require(isinstance(concept, dict), f"{prefix} must be an object", errors)
        if not isinstance(concept, dict):
            continue
        concept_id = concept.get("concept_id")
        require(is_nonempty_string(concept_id), f"{prefix}.concept_id is required", errors)
        if is_nonempty_string(concept_id):
            require(concept_id not in concept_ids, f"duplicate concept_id: {concept_id}", errors)
            concept_ids.add(concept_id)
        require(is_nonempty_string(concept.get("target_action")), f"{prefix}.target_action is required", errors)
        require(is_nonempty_string(concept.get("success_criterion")), f"{prefix}.success_criterion is required", errors)
        require(isinstance(concept.get("prerequisites"), list), f"{prefix}.prerequisites must be a list", errors)
        items = concept.get("assessment_items")
        require(isinstance(items, list) and bool(items), f"{prefix}.assessment_items must be non-empty", errors)
        if not isinstance(items, list):
            continue
        for item_index, item in enumerate(items):
            item_prefix = f"{prefix}.assessment_items[{item_index}]"
            require(isinstance(item, dict), f"{item_prefix} must be an object", errors)
            if not isinstance(item, dict):
                continue
            require(is_nonempty_string(item.get("item_id")), f"{item_prefix}.item_id is required", errors)
            require(item.get("kind") in ITEM_KINDS, f"{item_prefix}.kind is invalid", errors)
            require(is_nonempty_string(item.get("prompt")), f"{item_prefix}.prompt is required", errors)
            require(is_nonempty_string(item.get("answer_key")), f"{item_prefix}.answer_key is required", errors)
            require(item.get("verification_status") in VERIFICATION_STATUSES, f"{item_prefix}.verification_status is invalid", errors)

    for index, concept in enumerate(concepts):
        if not isinstance(concept, dict):
            continue
        for prerequisite in concept.get("prerequisites", []):
            require(prerequisite in concept_ids, f"concepts[{index}] has unknown prerequisite: {prerequisite}", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("learner-record", "content-pack"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1

    errors = validate_learner_record(data) if args.kind == "learner-record" else validate_content_pack(data)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"INVALID ({len(errors)} errors)")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
