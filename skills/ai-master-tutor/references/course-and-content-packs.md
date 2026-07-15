# Course maps and verified content packs

Use this reference for multi-concept learning, complex procedures, accuracy-sensitive subjects, cumulative review, or any request to “systematically learn” a domain.

## Separate pedagogy from subject content

The tutoring protocol controls interaction. A content pack controls what is taught, in what dependency order, and how answers are checked. Do not treat a fluent model-generated syllabus as validated subject structure.

Use an existing authoritative syllabus, textbook structure, specification, or instructor-provided objective map when available. If none exists, build a provisional pack and label its unverified parts.

Start from `assets/content-pack.template.json` and validate with `scripts/validate_learning_artifacts.py` when tools permit.

## Define the outcome map

Represent the course as observable outcomes and concept dependencies:

```text
course outcome
├── checkpoint A
│   ├── concept A1
│   └── concept A2 → prerequisite for B1
└── checkpoint B
    ├── concept B1
    └── cumulative application
```

For every checkpoint specify:

- observable target and success criterion;
- prerequisite concept IDs;
- authoritative sources or supplied material;
- representative example and non-example;
- common misconceptions or failure modes;
- worked example or model solution when appropriate;
- independent item, changed-surface item, and answer key;
- cumulative links to earlier concepts.

## Validate answer keys and examples

Before using an item as mastery evidence:

1. confirm that it measures the intended concept rather than an unstated prerequisite;
2. solve or inspect it independently;
3. verify calculations, code, citations, or factual claims with an appropriate tool or authoritative source;
4. record acceptable answer variants and decisive reasoning criteria;
5. identify ambiguity, hidden assumptions, and boundary conditions;
6. avoid using an item whose answer remains disputed unless evaluating the dispute is the objective.

For mathematics and science, verify calculations. For code, run tests or inspect executable behavior. For papers, anchor answer criteria in passages, figures, or data. For high-stakes domains, use current primary or authoritative guidance and state professional limits.

## Select the next concept

Choose the next checkpoint from:

1. prerequisites required for the learner's goal;
2. demonstrated gaps that block transfer;
3. due cumulative retrieval;
4. the shortest path to the learner's application context.

Do not simply follow document order. Do not skip a prerequisite because the learner recognizes its name.

## Adapt by domain

- **Mathematics:** representations, worked solutions, completion steps, independent variation, error localization.
- **Programming:** prediction, execution, debugging evidence, tests, design tradeoffs, changed constraints.
- **Language learning:** comprehension, retrieval, production, corrective feedback, spaced lexical and structural review.
- **Paper/book learning:** question, claim, evidence, reasoning, limitations, competing interpretation, application.
- **Procedural/physical skills:** decisions, cues, sequence, observable performance criteria; acknowledge actions the tutor cannot observe.
- **Creative work:** criteria, first attempt, critique tied to criteria, revision, comparison; do not force a single correct answer.

## Run cumulative review

After each checkpoint, include at most one or two earlier concepts that are due or structurally related. Interleave only after component concepts are understandable. Use a new combination task to test integration; do not infer synthesis from isolated item success.

## Handle incomplete content packs

If sources, answer keys, or prerequisites are missing:

- continue with low-risk, clearly supported material;
- label provisional content;
- avoid mastery claims on unverified items;
- request the smallest missing artifact that changes instruction;
- record the unresolved content risk in the learner handoff.
