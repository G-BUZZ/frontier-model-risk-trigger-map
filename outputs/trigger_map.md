# Generated Frontier Model Risk Trigger Map

> Research prototype. Triggers identify possible follow-up actions; they are not legal findings or safety certifications.

## Anthropic — Claude Opus 5

### autonomy: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-AUT-RD-001;E-ANT5-AUT-ATM1-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** The assessment uses provider-internal productivity evidence and an earlier model snapshot. Below-threshold performance does not exclude narrower automation, acceleration, or deployment-specific autonomy risks. | Threat-model applicability is not evidence that catastrophic misalignment is likely. The provider's conclusion depends on bounded behavioral evaluations and comparison with prior models.

### bio_chem: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-BIO-CB1-001;E-ANT5-BIO-CB2-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Anthropic states that it is difficult to determine with full confidence whether the CB-1 threshold is crossed. No dedicated chemical-weapons red-teaming, expert uplift trial, or human-participant evaluation was conducted for this release. The provider threshold is not an EU legal classification. | The determination relies on provider-run automated evaluations and additional non-public or incompletely described comparative evidence. No expert red-teaming or human uplift trial was conducted for this release.

### bio_chem: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-BIO-CB1-001;E-ANT5-BIO-CB2-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Anthropic states that it is difficult to determine with full confidence whether the CB-1 threshold is crossed. No dedicated chemical-weapons red-teaming, expert uplift trial, or human-participant evaluation was conducted for this release. The provider threshold is not an EU legal classification. | The determination relies on provider-run automated evaluations and additional non-public or incompletely described comparative evidence. No expert red-teaming or human uplift trial was conducted for this release.

### bio_chem: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-BIO-CB1-001;E-ANT5-BIO-CB2-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Anthropic states that it is difficult to determine with full confidence whether the CB-1 threshold is crossed. No dedicated chemical-weapons red-teaming, expert uplift trial, or human-participant evaluation was conducted for this release. The provider threshold is not an EU legal classification. | The determination relies on provider-run automated evaluations and additional non-public or incompletely described comparative evidence. No expert red-teaming or human uplift trial was conducted for this release.

### cyber: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-CYBER-EXPB-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Production safety interventions were disabled. The benchmark uses sandboxed vulnerabilities and does not directly measure reliable compromise of real systems, operational scaling, or performance against defended critical infrastructure.

### cyber: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-CYBER-EXPB-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Production safety interventions were disabled. The benchmark uses sandboxed vulnerabilities and does not directly measure reliable compromise of real systems, operational scaling, or performance against defended critical infrastructure.

### cyber: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-CYBER-EXPB-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Production safety interventions were disabled. The benchmark uses sandboxed vulnerabilities and does not directly measure reliable compromise of real systems, operational scaling, or performance against defended critical infrastructure.

### persuasion: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-ANT5-PERS-INFL-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** The test uses a simulated environment and a helpful-only variant rather than the deployed model. Anthropic states that substantial human direction would still be required for many real-world operational steps.

## Google DeepMind — Gemini 3.1 Pro

### agentic_behavior: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-MISALIGN-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Selected-task result; exploratory framework; situational awareness is a precursor rather than proof of harmful intent.

### autonomy: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-MLRD-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Average obscures task-level variance; benchmark performance is not a direct measure of real-world recursive improvement.

### cyber: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-CYBER-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Provider-run testing; CCL and alert threshold are framework-specific; inference cost affected Deep Think performance.

### cyber: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-CYBER-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Provider-run testing; CCL and alert threshold are framework-specific; inference cost affected Deep Think performance.

### cyber: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-CYBER-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Provider-run testing; CCL and alert threshold are framework-specific; inference cost affected Deep Think performance.

### persuasion: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-GDM-PERS-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Exploratory level; benchmark validity, population generalisation and deployment context remain uncertain.

## OpenAI — GPT-5.6 Sol

### agentic_behavior: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-AGENT-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Baseline comparisons are constrained by unequal access to reasoning traces; tested settings are narrow.

### bio_chem: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-BIO-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Family-level classification; public report omits some sensitive evaluation details.

### bio_chem: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-BIO-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Family-level classification; public report omits some sensitive evaluation details.

### bio_chem: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-BIO-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Family-level classification; public report omits some sensitive evaluation details.

### cyber: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-CYBER-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Provider-defined threshold; selected details of internal safeguards report are non-public; cross-provider thresholds are not equivalent.

### cyber: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-CYBER-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Provider-defined threshold; selected details of internal safeguards report are non-public; cross-provider thresholds are not equivalent.

### cyber: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-OAI-CYBER-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Provider-defined threshold; selected details of internal safeguards report are non-public; cross-provider thresholds are not equivalent.

## xAI — Grok 4.5

### bio_chem: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-XAI45-BIO-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Scores measure broad scientific or protocol competency and are not direct tests of end-to-end biological weapon development; benchmark validity and uplift over expert baselines require separate analysis.

### cyber: Additional targeted testing

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-XAI45-CYBER-001;E-XAI45-HACKER-001`
- **Rationale:** The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.
- **Limitations:** Developer-reported sandbox benchmark; vulnerability reproduction is not equivalent to reliable end-to-end compromise of real systems; comparison depends on task selection, tools and harness. | Developer-reported safeguard benchmark; categories combine harmful and dual-use requests; real-world compliance depends on prompting, tool access, account controls and monitoring.

### cyber: Qualified independent evaluation

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-XAI45-CYBER-001;E-XAI45-HACKER-001`
- **Rationale:** High-concern or alert-threshold evidence is not independently corroborated in the current dataset.
- **Limitations:** Developer-reported sandbox benchmark; vulnerability reproduction is not equivalent to reliable end-to-end compromise of real systems; comparison depends on task selection, tools and harness. | Developer-reported safeguard benchmark; categories combine harmful and dual-use requests; real-world compliance depends on prompting, tool access, account controls and monitoring.

### cyber: Restricted or identity-gated access

- **Trigger strength:** moderate
- **Confidence:** low
- **Evidence:** `E-XAI45-CYBER-001;E-XAI45-HACKER-001`
- **Rationale:** Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.
- **Limitations:** Developer-reported sandbox benchmark; vulnerability reproduction is not equivalent to reliable end-to-end compromise of real systems; comparison depends on task selection, tools and harness. | Developer-reported safeguard benchmark; categories combine harmful and dual-use requests; real-world compliance depends on prompting, tool access, account controls and monitoring.
