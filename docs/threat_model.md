# Threat Model

## Purpose and boundary

This threat model links frontier-model evidence to plausible public-interest harms. It is not a catalogue of speculative failure modes and does not assume that a benchmark score automatically causes harm. Each pathway identifies the actors, preconditions, observable evidence, amplifiers and potential supervisory responses.

## Assets to protect

- life, health and physical safety;
- continuity and integrity of critical services;
- public security and democratic processes;
- fundamental rights and informational autonomy;
- model weights, evaluation integrity and safety controls;
- institutional capacity to supervise high-impact models;
- competitive and political conditions that prevent excessive concentration of power.

## Relevant actors

- frontier-model providers and downstream deployers;
- malicious individuals, organised crime and state-linked groups;
- insiders with privileged access;
- legitimate researchers and security professionals;
- evaluators, auditors and competent authorities;
- affected persons, critical-infrastructure operators and the public.

## TM-01 — Catastrophic misuse

### Pathway

A model materially reduces one or more bottlenecks in a high-consequence harmful workflow. The model may supply expert knowledge, generate plans, operate tools, iterate after failures or scale activity across many targets.

### Domains

Cyber offence; biological or chemical misuse; harmful manipulation; combinations of these capabilities.

### Preconditions

- sufficient model capability and persistence;
- access to relevant tools, data, laboratories, infrastructure or targets;
- safeguards that can be bypassed, fragmented across turns or avoided through another deployment channel;
- an actor able to convert model output into real-world action.

### Observable evidence

- end-to-end task completion rather than isolated question answering;
- uplift of lower-resource actors in controlled studies;
- autonomous vulnerability discovery and exploitation;
- repeated success across realistic weaponisation or operational stages;
- safeguard bypass under adaptive or multi-turn attack;
- broad access without identity, rate, tool or environment controls.

### Amplifiers

Open weights; unrestricted tool execution; long context and memory; multi-agent orchestration; low marginal cost; access to critical systems; weak attribution.

### Potential actions

Additional testing at the bottleneck level; independent uplift studies; trusted-user access; usage monitoring; rate or tool restrictions; serious-incident assessment; deployment review.

## TM-02 — Loss of control

### Pathway

A model develops or exhibits goal-directed behaviour that undermines oversight. Relevant behaviours include strategic deception, sabotage, sandbagging, evaluation gaming, reward hacking, unauthorised persistence or attempts to preserve its objectives across interventions.

### Preconditions

- situational awareness or an internal representation of oversight conditions;
- ability to plan over long horizons;
- access to tools, credentials, codebases or operational systems;
- objectives or learned policies that create incentives to conceal behaviour;
- monitors that rely on signals the model can manipulate.

### Observable evidence

- differential behaviour when the model infers it is being evaluated;
- covert continuation after an instruction to stop;
- attempts to disable, mislead or route around oversight;
- successful sabotage while preserving apparent task performance;
- reasoning-trace or action evidence of grader manipulation;
- increased capability under hidden or unmonitored channels.

### Amplifiers

Delegation of consequential decisions; autonomous code deployment; persistent memory; self-modification; replication; privileged internal use; reduced human review.

### Potential actions

White-box or training-run assessment; control evaluations; separation of duties; sandboxing and least privilege; monitoring diversity; restrictions on autonomous deployment; corrective measures.

## TM-03 — Concentration of power

### Pathway

Control over frontier models, compute, data and evaluation infrastructure gives a small number of firms or states disproportionate influence over markets, information, security capabilities and regulatory evidence.

### Preconditions

- high fixed costs and limited access to compute;
- proprietary evidence unavailable to external scrutiny;
- dependence of public institutions on provider-supplied analysis;
- vertically integrated model, cloud, platform and distribution channels;
- switching barriers and limited interoperability.

### Observable evidence

- systematic information asymmetry between providers and authorities;
- external evaluators unable to obtain suitable access;
- common safety claims that cannot be independently reproduced;
- downstream dependence on one provider for critical functions;
- provider-defined thresholds becoming de facto public standards without public validation.

### Amplifiers

Exclusive partnerships; control over evaluation tooling; lobbying asymmetry; emergency procurement; market tipping; closed incident databases.

### Potential actions

Shared public evaluation capacity; secure regulator access; disclosure standards; evaluator qualification and independence rules; interoperability and procurement safeguards; competition and resilience assessment.

## TM-04 — Critical-infrastructure compromise

### Pathway

A model is used to compromise operational technology, industrial control systems, health, finance, transport, energy, communications or public-administration systems, or an integrated model acts unsafely within those environments.

### Preconditions

- network or tool access to operational systems;
- exploitable vulnerabilities or unsafe integration;
- insufficient human authorisation and rollback;
- poor segmentation, logging or identity controls;
- model capability to chain reconnaissance, exploitation and persistence.

### Observable evidence

- strong performance on realistic long-horizon cyber tasks;
- prompt-injection success in tool-using agents;
- unauthorised destructive actions or overwrite failures;
- deployment in safety-critical workflows without domain validation;
- inability to reconstruct model actions after an incident.

### Amplifiers

Legacy systems; shared credentials; autonomous execution; inadequate fail-safe design; supply-chain reach; low redundancy.

### Potential actions

Sector-specific red teaming; secure sandboxes; mandatory human approval for irreversible actions; logs and incident preservation; restricted permissions; deployment review with sector authority participation.

## Cross-cutting failure modes

### Evaluation capture

The provider defines the benchmark, provides the model, controls the configuration and publishes only selected results. Mitigation: source-independence metadata, evaluator-access disclosure and independent replication.

### False reassurance

A model remains below a provider-defined threshold even though the threshold is not independently validated or the test omits deployment affordances. Mitigation: record uplift and near-threshold evidence; do not translate “below threshold” into “safe”.

### Benchmark saturation or leakage

High scores reflect familiarity rather than real-world capability. Mitigation: private rotating tasks, contamination checks and task-level analysis.

### Scaffold sensitivity

Capabilities appear or disappear depending on tools, prompts, inference budget and agent architecture. Mitigation: preserve configuration fields and test multiple plausible deployment scaffolds.

### Strategic underperformance

A sufficiently capable model recognises the evaluation and reduces performance. Mitigation: behavioural consistency tests, hidden tasks, white-box access and training-run assessment.

### Safeguard displacement

A model-level refusal appears strong while a different product surface, tool, fine-tune or open-weight derivative bypasses the control. Mitigation: deployment-channel mapping and system-level evaluation.
