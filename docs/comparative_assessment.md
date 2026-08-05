# Frontier Model Comparative Assessment

## Purpose

This document provides a qualitative comparison of publicly documented
frontier-model risk evidence.

The comparison does not produce a universal risk score. Model capabilities,
evaluation methodologies, provider thresholds and deployment contexts are not
directly comparable without strong assumptions.

The purpose is to identify:
- documented capability signals;
- provider-defined thresholds;
- missing evidence;
- potential triggers for additional review.

---

## Coverage Matrix

| Model | Cyber | Bio/Chem | Autonomy | Agentic Behaviour | Persuasion / Manipulation | Evidence Source |
|---|---|---|---|---|---|---|
| GPT-5.6 Sol | High capability classification; below Critical threshold | High capability classification | Below provider AI self-improvement threshold | Mixed signals in safety-research sabotage evaluations | Not publicly extracted in current coverage | OpenAI System Card; UK AISI evaluation |
| Claude Opus 5 | ExploitBench capability signals including ACE-related results | CB-1 treated as applicable; CB-2 below stated threshold | AI R&D threshold below alert level; autonomy threat models assessed | Prompt-injection and agentic evaluations conducted | Influence-operation evaluations available on helpful-only configurations | Anthropic System Card |
| Gemini 3.1 Pro | Cyber alert signals reported below Critical Capability Level | Below stated CCL threshold | AI R&D and misalignment evaluations reported below alert thresholds | Situational-awareness evaluations reported | Harmful manipulation evaluations reported | Google DeepMind Model Card |

---

## Interpretation Principles

### No Universal Ranking

A higher result in one evaluation does not imply a higher overall risk profile.

Examples:
- Cyber benchmarks measure different tasks and environments.
- Bio evaluations may use different capability definitions.
- Agentic behaviour depends heavily on tools, permissions and deployment context.

---

## Evidence Independence

Current repository coverage primarily relies on:

| Evidence Type | Current Coverage |
|---|---|
| Provider system cards | Available |
| Provider model cards | Available |
| Independent evaluations | Limited |
| Regulatory assessments | Not yet systematically collected |

The distinction between provider disclosure and independent assessment is
central to future development.

---

## Decision-Relevant Gaps

Current gaps include:

- inconsistent evaluation methodologies;
- limited cross-provider replication;
- incomplete information about deployment safeguards;
- lack of standardized incident reporting.

These gaps should be treated as uncertainty signals rather than evidence of safety.

---

## Future Development

Planned improvements:

1. Add independent evaluation sources.
2. Track evaluation methodology differences.
3. Add deployment-context fields.
4. Map evidence to regulatory decision points.
