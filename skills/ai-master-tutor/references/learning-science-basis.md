# Learning-science basis and limits

Use this reference when auditing or modifying the skill, or when a user asks why the tutoring protocol is designed this way. It is not a claim that every rule has identical evidence in every domain or population.

## Evidence-to-design map

| Design choice | Research basis | Operational consequence |
|---|---|---|
| Manage information and sequence complexity | Cognitive load theory and instructional-design effects | Chunk multi-part tasks, integrate related information, use worked examples for novices, fade guidance with expertise |
| Dynamically increase cognitive engagement | ICAP framework and generative learning research | Move from attending/manipulating to learner generation and response-specific co-construction when prior knowledge permits |
| Require active attempts | Active learning and generative learning research | Ask the learner to predict, explain, solve, compare, construct, or retrieve instead of only reading |
| Use retrieval and spacing | Testing-effect and distributed-practice research | Use closed-book recall, delayed review, and corrective feedback |
| Scaffold and fade | Tutoring and scaffolding research | Increase support after failure and remove it after success |
| Give targeted, timely feedback | Formative-feedback research | Diagnose the gap, explain its consequence, and prescribe one next action |
| Adapt pace and support | One-to-one tutoring and structured AI-tutor research | Let evidence, not a fixed script, determine step size and timing |
| Test application and transfer | Learning and assessment research | Do not equate recognition or fluency with usable knowledge |
| Align objectives, instruction, and assessment | Instructional design and validity principles | Express observable targets and verify that assessment items measure them |
| Use structured subject content | Research on engineered AI tutoring and intelligent tutoring systems | Pair dialogue rules with sequenced activities, verified solutions, and explicit criteria for complex learning |

## Important limitations

- “Socratic” is a conversational strategy, not a reason to withhold prerequisites or direct explanations.
- Desirable difficulty is not arbitrary difficulty. Add effort that strengthens retrieval, discrimination, or transfer; remove effort caused by confusing presentation.
- Worked examples are especially useful for novices and can become redundant for experts.
- ICAP classifies overt engagement behaviors; it does not mean every lesson should mechanically traverse P→A→C→I. Higher engagement requires enough prior knowledge and appropriate task design.
- A tutor-learner exchange is not Interactive merely because it is conversational. It must build on learner-generated content through substantive challenge and learner revision.
- Do not present intrinsic, extraneous, and germane load as three uncontested independent sources. The influential three-part model is historically important, but refined accounts treat germane resources as closely related to intrinsic load; explain the disagreement when the distinction matters.
- A single successful session shows current performance, not long-term retention.
- AI tutoring quality depends on source accuracy, content structure, feedback quality, and model reliability. A generic chatbot is not automatically an effective tutor.
- A prompt-level tutoring policy cannot by itself provide durable memory, verified answer keys, a prerequisite graph, or delayed assessment. Those require storage, content, tools, and evaluation mechanisms around the Skill.
- A 2025 randomized crossover study in one Harvard introductory physics course found better short-term learning under a carefully engineered AI tutor than under the comparison active-learning lessons, but the authors explicitly did not claim universal superiority, particularly for complex synthesis and higher-order critical thinking.
- In that study, the authors reported that a system prompt alone did not reliably sequence multi-part scaffolding. Their implementation also used platform-level activity structure and expert-prepared step-by-step solutions. Treat this as evidence for a layered tutoring system, not proof that a generic Skill produces the same gains.

## Primary and authoritative sources

1. Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). “AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting.” *Scientific Reports, 15*, 17458. https://doi.org/10.1038/s41598-025-97652-6
2. Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive Load Theory*. Springer. https://doi.org/10.1007/978-1-4419-8126-4
3. Roediger, H. L., & Karpicke, J. D. (2006). “Test-enhanced learning: Taking memory tests improves long-term retention.” *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
4. Pashler, H., et al. (2007). *Organizing Instruction and Study to Improve Student Learning*. U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov/ncee/wwc/PracticeGuide/1
5. Wood, D., Bruner, J. S., & Ross, G. (1976). “The role of tutoring in problem solving.” *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x
6. Shute, V. J. (2008). “Focus on formative feedback.” *Review of Educational Research, 78*(1), 153–189. https://doi.org/10.3102/0034654307313795
7. Sweller, J. (2010). “Element Interactivity and Intrinsic, Extraneous, and Germane Cognitive Load.” *Educational Psychology Review, 22*, 123–138. https://doi.org/10.1007/s10648-010-9128-5
8. Chi, M. T. H., & Wylie, R. (2014). “The ICAP Framework: Linking Cognitive Engagement to Active Learning Outcomes.” *Educational Psychologist, 49*(4), 219–243. https://doi.org/10.1080/00461520.2014.965823

Treat this list as a foundation, not a claim of completeness. Recheck the literature when making broad effectiveness claims or adapting the protocol to high-stakes populations.
