# Prompt Engineering and Production LLM Systems

A practical curriculum for understanding, designing, evaluating, securing, and operating prompt-based language and generative media systems.

## Learning path

Read the files in order. Each chapter uses the same pattern:

- Mental model and analogy
- Core mechanics
- Worked prompt examples
- Failure modes
- Practice lab
- Takeaway

| Chapter | Focus | Mental model |
|---|---|---|
| [1. Foundations](01-foundations.md) | LLMs, tokens, context, parameters, prompt contracts | An improviser with working memory |
| [2. Essential Strategies](02-essential-strategies.md) | Zero-shot, few-shot, roles, personas, delimiters | Teaching by demonstration |
| [3. Reasoning Techniques](03-reasoning-techniques.md) | CoT, self-consistency, plan-and-solve, chain-of-draft | A pilot's checklist |
| [4. Orchestration](04-orchestration.md) | System 2 attention, chaining, meta prompting, refinement | A team with typed handoffs |
| [5. Multimodal and Applied](05-multimodal-and-applied.md) | Vision, audio, RAG, image, and video prompting | A detective combining evidence |
| [6. Security](06-security-and-robustness.md) | Jailbreaks, injection, exfiltration, tool abuse, defenses | An intern with a powerful keyboard |
| [7. Management](07-prompt-management.md) | Planning, drafting, evaluation, versioning, DeepEval | A recipe in a commercial kitchen |

## Production systems layer

The first seven chapters explain core prompt engineering. These chapters extend the curriculum into the engineering disciplines required to build reliable production LLM systems:

| Chapter | Focus | Mental model |
|---|---|---|
| [8. Context and Structured Outputs](08-context-engineering-and-structured-outputs.md) | Context selection, schemas, parsing, validation, retries | A briefing folder and shipping label |
| [9. Tools, Agents, and Human Approval](09-tools-agents-and-human-approval.md) | Tool schemas, agent loops, permissions, approvals | A capable assistant |
| [10. RAG Engineering](10-rag-engineering-in-depth.md) | Chunking, metadata, retrieval, reranking, grounding | An open-book exam |
| [11. Evaluation and Dataset Design](11-evaluation-and-dataset-design.md) | Test sets, annotation, metrics, judge calibration | An exam and laboratory |
| [12. Operations](12-observability-cost-latency-and-operations.md) | Tracing, cost, latency, retries, drift, rollback | A delivery fleet |
| [13. Memory and State](13-conversation-memory-and-state.md) | Conversation history, durable memory, compaction, deletion | A case file |
| [14. Privacy and Responsible AI](14-privacy-compliance-and-responsible-ai.md) | Data minimization, compliance, fairness, transparency, human control | A confidential envelope |

Together, Chapters 1-7 cover prompt engineering and Chapters 8-14 cover production LLM systems.

## Working rule

Treat every prompt as an interface contract:

```text
objective + context + procedure + output contract + evaluation
```

The goal is not a prompt that sounds clever. The goal is measurable improvement on representative work, with controlled failure when the system does not know enough.
