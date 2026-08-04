# Data dictionary

## `models.csv`

| Field | Description |
|---|---|
| `model_id` | Stable lowercase identifier used by evidence and incident records. |
| `provider` | Organisation that provides the model. |
| `model_name` | Public model name. |
| `release_date` | ISO date for the covered release or checkpoint. |
| `weights_access` | Closed, open-weight, open-source or unknown. |
| `deployment_channels` | API, consumer, enterprise, on-premise or other channels. |
| `deployment_scope` | Limited, controlled, broad or unknown. |
| `system_card_source_id` | Source registry reference. |
| `status` | Active, historical, superseded or withdrawn. |

## `sources.csv`

| Field | Description |
|---|---|
| `source_id` | Stable identifier. |
| `source_kind` | System card, model card, independent evaluation, regulatory guidance, etc. |
| `source_independence` | Developer, commissioned external, independent nonprofit, government, academic or regulator. |
| `access_level` | Access available to the evaluator or evidence producer. |
| `last_verified` | Date on which the URL and relevant content were checked. |
| `status` | Active, superseded, corrected, withdrawn or unavailable. |

## `evidence.csv`

| Field | Description |
|---|---|
| `evidence_id` | Stable atomic claim identifier. |
| `model_id` | Model reference; blank for cross-model evidence. |
| `scope` | `model`, `family`, `deployment` or `frontier_aggregate`. |
| `domain` | Taxonomy domain key. |
| `evidence_type` | Capability, propensity, safeguard, incident, deployment, limitation or trend. |
| `claim` | Narrow factual statement attributable to the source. |
| `metric_name`, `result_value`, `result_unit` | Original reported metric; do not silently normalise. |
| `threshold_reference` | Provider framework, statutory concept or evaluation-specific criterion. |
| `threshold_status` | Not tested, below alert, alert reached, near threshold, threshold reached, etc. |
| `concern_level` | Researcher-coded triage category, not a legal risk finding. |
| `source_id` | Source registry reference. |
| `evaluated_configuration` | Model mode, scaffold, tools, reasoning effort and other relevant setup. |
| `safeguards_state` | With safeguards, without safeguards, mixed or unknown. |
| `independent_replication` | Yes, no, partial or unknown. |
| `result_direction` | Concerning, reassuring, mixed or indeterminate. |
| `limitations` | Mandatory statement of uncertainty and comparability constraints. |
| `status` | Draft, verified, disputed, corrected or withdrawn. |

## `incidents.csv`

The table is empty in v0.1. Add only publicly documented events with a defensible link to a model and deployment version. Do not include rumours, private victim data or unverified social-media allegations.
