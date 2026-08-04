# Frontier Model Risk Trigger Map

## One-page executive summary for the European AI Office

**Date:** 4 August 2026  
**Status:** open-source research prototype

### Supervisory problem

System cards and independent evaluations are growing, but their results are not directly comparable. Providers use different taxonomies, thresholds, benchmarks, safeguards and release criteria. External evaluators receive different checkpoints, tools, time budgets and access. “Below threshold” may therefore be accurate within one framework while remaining insufficient for a public decision.

The EU AI Office can request documentation, evaluate general-purpose AI models, require corrective measures and issue fines. The General-Purpose AI Code of Practice provides a route for systemic-risk providers to document evaluation, mitigation, security and incident-reporting measures [SRC-EU-001; SRC-EU-002; SRC-EU-003]. A consistent triage layer is still needed to convert heterogeneous evidence into proportionate follow-up.

### Proposed instrument

The **Frontier Model Risk Trigger Map** is an auditable evidence registry and decision-support matrix. It neither certifies safety nor produces a composite risk score. Each claim retains the model checkpoint, deployment configuration, original metric and threshold status, source, evaluator independence, access level, safeguards state, limitations and verification date.

The rule engine produces rebuttable, domain-specific actions:

1. **Additional targeted testing** for alert crossings, material below-threshold signals, indeterminate results or untested deployment configurations.
2. **Qualified independent evaluation** when high-concern evidence is provider-only or black-box access cannot test the threat model.
3. **Restricted or identity-gated access** when high capability or safeguard weakness is combined with broad deployment, powerful tools or critical-sector exposure.
4. **Serious-incident assessment and reporting** for documented events that may meet applicable criteria.
5. **Deployment review or corrective measures** after a critical threshold, serious incident or strong evidence of inadequate mitigation.

### Evidence signal

Public disclosures already justify action before the highest internal threshold. OpenAI classifies GPT-5.6 Sol as High in cyber but below Critical. Google DeepMind reports that Gemini 3.1 Pro reached its cyber alert threshold but not its Critical Capability Level, alongside material below-threshold signals in manipulation, AI R&D and situational awareness. xAI reports an 80.4% CyberGym result for Grok 4.5, residual harmful or dual-use compliance of 7.8% on HackerBench and low average jailbreak compliance in the tested setup [SRC-OAI-001; SRC-GDM-001; SRC-XAI-002]. These figures cannot support a cross-provider ranking, but they can justify targeted replication, access scrutiny and deployment-specific controls.

### Recommended use

Use the schema as a common intake and triage layer for Safety and Security Frameworks, Model Reports, independent evaluations and incident submissions. Define secure evaluator-access tiers from controlled black-box to white-box and training-run assessment. Treat alert thresholds as triggers for scrutiny, not automatic bans. Link model evidence to sector-specific deployment assessments with national and critical-infrastructure authorities.

### Central safeguard

Uncertainty must remain visible. Missing data must remain missing; provider conclusions must stay attributed; and “below threshold” must never be translated automatically into “safe”. The normal output of public evidence is not a verdict, but a justified next supervisory step.
