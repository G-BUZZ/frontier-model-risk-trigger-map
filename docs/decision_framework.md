# Frontier Model Decision Framework

## Purpose

This framework maps documented frontier-model evidence to possible governance
actions.

It does not create a universal risk score.

The same evidence may require different responses depending on:
- deployment context;
- model access;
- evaluator independence;
- affected systems;
- regulatory obligations.

---

## Decision Pipeline

Evidence

↓

Trigger condition

↓

Review action

↓

Responsible actor

↓

Deployment decision

---

## Trigger Categories

| Evidence signal | Possible trigger | Suggested action |
|---|---|---|
| Capability reaches provider-defined alert threshold | Capability review required | Independent evaluation or additional testing |
| Independent evaluator identifies unexpected behaviour | External validation trigger | Replication and safety review |
| Agentic capability increases with tool access | Deployment-context trigger | Restrict permissions and evaluate safeguards |
| Cyber capability improves significantly | Critical capability review | Security assessment before wider deployment |
| Missing evaluation data for high-impact domain | Evidence gap trigger | Require additional disclosure |

---

## Governance Actions

### Additional Testing

Used when:
- evidence exists but uncertainty remains;
- methodology limitations are significant.

### Independent Evaluation

Used when:
- provider evaluation is the only available evidence;
- capability appears near a meaningful threshold.

### Access Restriction

Used when:
- deployment creates unacceptable uncertainty;
- safeguards cannot be independently verified.

### Incident Reporting

Used when:
- harmful behaviour occurs after deployment;
- evidence connects behaviour to model operation.

### Deployment Review

Used before:
- high-impact deployment;
- critical infrastructure use;
- autonomous tool access.

---

## Uncertainty Handling

Absence of evidence should not be interpreted as evidence of safety.

Important uncertainty sources:
- unpublished evaluation details;
- non-comparable benchmarks;
- provider incentives;
- limited external replication.

---

## Future Development

Future versions should map this framework to:
- EU AI Act obligations;
- national AI safety institutes;
- incident reporting mechanisms.
