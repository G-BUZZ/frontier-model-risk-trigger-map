# Methodology

## 1. Research question

The project does not ask whether a frontier model is “safe”. It asks:

> Given a traceable set of public evidence, what additional supervisory or risk-management action is proportionate, and what uncertainty remains?

This framing separates three issues that are often collapsed:

1. **capability or propensity evidence** — what the evaluated model did;
2. **deployment and safeguards** — under what access, tools and controls it can act;
3. **decision rule** — what evidence should cause an authority or oversight body to request something further.

## 2. Unit of analysis

The basic unit is one evidence claim, stored as one row in `data/evidence/evidence.csv`. A row should be narrow enough that another reviewer can confirm it without accepting the source’s entire conclusion.

Examples:

- “Model X crossed the developer’s cyber alert threshold.”
- “Model Y achieved 0.33 attack success on a specified prompt-injection benchmark.”
- “An evaluator lacked access to the final checkpoint.”
- “No result was published for multi-agent mode.”

A source can therefore produce several evidence rows, including both concerning and reassuring findings.

## 3. Source hierarchy and independence

The repository records provenance rather than treating “external” as a binary label.

| Category | Meaning | Typical evidentiary role |
|---|---|---|
| Developer | Evaluation designed or reported by the model provider | Primary disclosure; possible incentive and access advantages |
| Commissioned external | Separate organisation, but selected or paid by provider | Useful external scrutiny; independence must be described |
| Independent nonprofit | Evaluator controls important methodological choices | Stronger corroboration, subject to access limits |
| Government | Public AI safety/security institute or competent authority | High policy relevance; publication may be aggregated or redacted |
| Academic | Research group using public or granted access | Reproducibility varies; peer review and benchmark validity matter |
| Regulator | Legal text, guidance, enforcement or official incident record | Determines institutional powers and legal obligations, not model capability |

The `access_level` field distinguishes public reports, public-product black-box tests, controlled black-box access, grey-box access, white-box access and training-run access.

## 4. Comparability protocol

Two results are directly comparable only when the repository can establish adequate similarity across:

- model checkpoint and date;
- system prompt and safety configuration;
- tool access, network access and permissions;
- scaffold or agent architecture;
- reasoning or inference budget;
- benchmark and version;
- number of trials and aggregation method;
- evaluator access and opportunity for adaptation;
- treatment of refusals, timeouts and partial completion.

If these fields are unavailable, the result remains usable as evidence but receives a lower confidence level. The project does not convert heterogeneous benchmarks into a universal numerical scale.

## 5. Trigger logic

The rule engine generates actions at the **model × domain** level. It uses categorical evidence, not a weighted total score.

### Additional targeted testing

Triggered by any of the following:

- result is near a threshold, indeterminate or not tested;
- provider reports an alert-threshold crossing;
- a concerning result has material limitations or a narrow scaffold;
- a model is deployed broadly but evidence is stale or incomplete.

### Qualified independent evaluation

Triggered when concerning developer evidence is not corroborated by a government, independent nonprofit, regulator or academic evaluator, or when the relevant threat model requires access beyond public-product black-box testing.

### Restricted or identity-gated access

Triggered when high or critical concern is combined with broad deployment, powerful tools or a material safeguard weakness. This action is domain- and capability-specific; it should not be read as a recommendation to withdraw all model access.

### Serious-incident assessment and reporting

Triggered only by a documented incident row whose severity is serious or critical. The output deliberately says “assessment and reporting” because the repository cannot itself make the final legal classification.

### Deployment review or corrective measures

Triggered by a declared critical threshold crossing, a serious incident, or multiple strong signals that existing mitigations may not reduce the risk to an acceptable level. Human review is mandatory before publication of this conclusion.

## 6. Confidence calculation

Confidence is ordinal:

- **Low:** only developer-reported evidence, public-report-only access, major missing configuration data, or a single narrow test.
- **Medium:** multiple sources or one independent source, but access or comparability limitations remain.
- **High:** independent corroboration with appropriate access, replicated results, transparent methodology and sufficient trials.

A high-confidence trigger does not imply high risk; it means confidence in the recommendation for the stated action is comparatively strong.

## 7. Evidence freshness

Every source and evidence row has a `last_verified` or `recorded_date`. Living dashboards and mutable system cards must be date-stamped. Superseded checkpoints remain in the repository for longitudinal analysis but should be marked inactive or historical.

Suggested review cadence:

- 30 days for current frontier-model system cards;
- 90 days for independent evaluation coverage;
- immediate review after a major model update, new tool access or serious incident;
- annual review of taxonomy and decision rules.

## 8. Uncertainty register

Each evidence row must name limitations. The policy products should distinguish:

1. **epistemic uncertainty:** the result is unknown or weakly measured;
2. **aleatory variability:** stochastic model behaviour varies across trials;
3. **construct validity:** the benchmark may not measure the real-world capability of interest;
4. **external validity:** the evaluation environment differs from deployment;
5. **strategic uncertainty:** the model may recognise, game or underperform on an evaluation;
6. **institutional uncertainty:** provider incentives, evaluator dependence or limited disclosure affect credibility.

## 9. Review and contribution workflow

A contribution should:

1. add or update the source registry;
2. create atomic evidence rows;
3. record missing fields explicitly rather than guessing;
4. run `make validate` and `make build`;
5. include a short reviewer note explaining interpretation choices;
6. receive a second-person review for any high-impact trigger.

## 10. Known limitations of v0.1

- Coverage is selective and mostly English-language.
- The seed dataset relies heavily on provider disclosures.
- The incident table is intentionally empty pending a defensible public-incident protocol.
- No confidential regulator or pre-deployment data is available.
- Concentration-of-power risks are represented in the threat model but are not yet operationalised in the automated trigger engine.
- The engine cannot determine legal compliance or the acceptability of residual systemic risk.
