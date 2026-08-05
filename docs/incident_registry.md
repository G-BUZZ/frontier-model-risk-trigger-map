# Incident Registry

## Purpose

The incident registry records publicly documented events involving frontier
models after deployment or during evaluation.

The registry separates:
- model capability evidence;
- evaluation results;
- observed incidents.

An incident does not automatically prove model-level risk.
It provides deployment-context evidence.

---

## Fields

| Field | Description |
|---|---|
| incident_id | Unique identifier |
| model_id | Related model |
| incident_type | Category of event |
| deployment_context | Where the event occurred |
| impact | Observed consequence |
| response | Mitigation or remediation |
| verification_status | Evidence confidence |

---

## Incident Categories

Examples:

- jailbreak;
- harmful output;
- data leakage;
- tool misuse;
- autonomous action failure;
- cybersecurity misuse.

---

## Limitations

Only publicly documented and verifiable incidents should be included.

Unverified reports and social-media claims should not be treated as evidence.
