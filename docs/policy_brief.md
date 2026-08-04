# From System Cards to Supervisory Triggers

## An evidence architecture for frontier-model oversight

**Policy briefing — research prototype, 4 August 2026**  
**Primary audience:** European AI Office, Scientific Panel and national competent authorities  
**Author:** Giulio Buzzetta

## Executive proposition

Public authorities are receiving more frontier-model safety information than they did two years ago, but the evidence is still difficult to use for consistent decisions. Providers publish system cards under different internal frameworks. Independent evaluators often receive different checkpoints, tools, time budgets and degrees of access. Government reports may aggregate results across models. Benchmarks measure narrow capabilities but are often interpreted as broad statements about risk.

The result is a governance gap between **disclosure** and **decision**. A system card can indicate that a provider has crossed its own cyber alert threshold, that a model remains below a critical level, or that safeguards performed well on selected tests. None of those statements directly answers the supervisory question: what should happen next?

This briefing proposes a public, auditable **Frontier Model Risk Trigger Map**. The Map does not certify models as safe and does not collapse heterogeneous evidence into one score. It records atomic evidence claims, evaluates their provenance and comparability, and maps them to rebuttable actions: additional testing, qualified independent evaluation, restricted access, serious-incident assessment, or deployment review.

The approach is designed to complement the EU Artificial Intelligence Act and the General-Purpose AI Code of Practice. The Code’s Safety and Security chapter applies to the most advanced general-purpose AI models with systemic risk and provides a practical route for demonstrating compliance with Article 55 obligations [SRC-EU-001]. The Commission’s 2026 guidance also identifies notifications, serious-incident reports, Safety and Security Frameworks and Model Reports as documents to be submitted to the AI Office [SRC-EU-002]. As of 2 August 2026, the AI Office holds enforcement powers over general-purpose AI models, including powers to request documentation, evaluate models, require corrective measures and issue fines [SRC-EU-003]. A trigger map can help make those powers more evidence-driven and consistent without pretending that public information is sufficient for a final legal determination.

## 1. The problem: safety disclosures are not decision rules

Frontier-model reports serve several functions at once. They describe capabilities, explain mitigations, communicate a release decision, protect sensitive information and shape public confidence. These functions create predictable tensions.

First, provider frameworks use different categories and thresholds. OpenAI’s Preparedness Framework, Google DeepMind’s Frontier Safety Framework, Anthropic’s Responsible Scaling Policy and xAI’s Frontier Artificial Intelligence Framework are not interchangeable units. A “High” capability classification under one framework cannot be converted into another provider’s Critical Capability Level or AI Safety Level without examining the underlying threat model and tests.

Second, reported results are strongly configuration-dependent. A model tested without network access is not the same system as a deployed agent with browsing, a terminal, credentials and long-lived memory. A reasoning mode with high inference cost may perform differently from the product default. A single-agent evaluation may not represent a multi-agent product. System prompts, monitoring layers, refusal classifiers and tool permissions can change the observed result.

Third, independent evaluation is not a binary property. An external organisation can be paid by the provider, test an early checkpoint, use only black-box access, receive limited time or lack the ability to modify the scaffold. Conversely, a provider may possess richer internal evidence than any outside evaluator. The relevant policy question is therefore not merely “internal or external?” but “who controlled the method, what access did they have, and could they test the threat model that matters?”

Fourth, a threshold result can be falsely reassuring. Remaining below a provider-defined critical level does not show that residual risk is acceptable under EU law, that the threshold is well calibrated, or that the evaluation covers downstream integrations. It may still justify monitoring, targeted testing or access controls.

A usable oversight instrument must therefore preserve context rather than stripping it away.

## 2. What the seed evidence already shows

The initial dataset is deliberately selective. It does not claim complete coverage of current frontier models. Its purpose is to demonstrate how heterogeneous evidence can be transformed into concrete follow-up questions.

### 2.1 Cyber capability is moving into an alert zone

OpenAI reports that GPT-5.6 Sol is at its “High” cybersecurity capability level but below “Critical”. The provider states that the model can find vulnerabilities and components of exploits, while its tests did not show reliable autonomous end-to-end attacks against hardened targets. It also classifies the GPT-5.6 family as High in biological and chemical risk and below High in AI self-improvement [SRC-OAI-001].

Google DeepMind reports that Gemini 3.1 Pro reached its cyber alert threshold but remained below the cyber Critical Capability Level. The same model remained below stated CCL alert thresholds in CBRN, harmful manipulation, machine-learning R&D and misalignment, although the card reports material signals within those domains [SRC-GDM-001].

These statements are not directly comparable, but they share a policy-relevant pattern: providers are reporting meaningful cyber capability before their highest internal threshold is reached. Waiting only for a “Critical” label would discard valuable lead time. An alert-threshold crossing should therefore trigger targeted independent testing and scrutiny of access, monitoring and tool permissions, rather than an automatic finding that deployment is unacceptable.

### 2.2 Below-threshold results can still contain consequential signals

Gemini 3.1 Pro’s model card reports a maximum harmful-manipulation belief-change odds ratio of 3.6 relative to a non-AI baseline, while stating that the alert threshold was not reached. It reports a human-normalised average of 1.27 on RE-Bench for machine-learning R&D, again below the framework’s alert threshold. On exploratory misalignment tests, the provider reports almost complete success on three situational-awareness challenges that prior models had not consistently solved, but inconsistent performance elsewhere [SRC-GDM-001].

These findings illustrate why the Map separates `threshold_status` from `concern_level`. A result can remain formally below a threshold while still supporting additional evaluation, particularly when it concerns a precursor capability such as situational awareness or AI R&D acceleration. The correct response is not to relabel the provider’s conclusion; it is to identify what uncertainty would need to be resolved before a stronger deployment decision could be justified.

### 2.3 Safeguard evaluations need system-level interpretation

xAI’s Grok 4.5 card reports an 80.4% mean reproduced-vulnerability result on CyberGym and, with safeguards in the reported HackerBench configuration, 7.8% compliance with harmful or dual-use requests and 0% refusal of benign requests [SRC-XAI-002]. The card also reports 0.73% compliance on should-refuse prompts under its jailbreak evaluation. The earlier Grok 4.20 card is retained in the dataset as a historical checkpoint because it reported a 0.30 AgentHarm violation rate and a 0.33 AgentDojo prompt-injection attack-success rate in the shown single-agent configuration [SRC-XAI-001].

These measurements cover different layers: capability, request-level safeguards, jailbreak robustness and agent security. None is an estimate of catastrophic risk. Each depends on the task set, scaffold, tool permissions, attack distribution, refusal policy and deployment filters. The supervisory consequence is to reproduce the relevant tests under the permissions and data flows of the intended deployment, especially in critical sectors, and to consider restricted tools, stronger isolation and human approval for irreversible actions. The response should remain specific to the demonstrated attack surface rather than becoming a blanket judgment about the model.

### 2.4 Autonomy trends justify shorter review cycles

The UK AI Security Institute’s frontier trends work reports that leading models moved from completing under 5% of software tasks estimated to require at least one hour of human expert work in late 2023 to more than 40% by mid-2025 [SRC-AISI-001]. METR maintains an updated time-horizon series and conducts frontier-risk evaluations focused on autonomous capabilities and AI R&D acceleration [SRC-METR-001; SRC-METR-002].

Aggregate trends cannot be assigned to one checkpoint, but they matter for regulatory cadence. A safety assessment that is one year old may be structurally obsolete even if the model name has not changed. Significant changes in inference-time compute, tool use, multi-agent orchestration or product scaffolding should be treated as potential capability jumps requiring renewed testing.

### 2.5 Evaluation access is part of the evidence

Loss-of-control evaluations face a special problem: a capable model may recognise tests, manipulate visible signals or behave differently under oversight. Apollo Research argues that black-box final-checkpoint evaluations can be insufficient and that state-of-the-art testing may require deeper white-box or training-run access [SRC-APOLLO-001]. OpenAI’s GPT-5.6 card also reports UK AISI findings with explicit comparability limitations because the evaluator had access to full reasoning traces for GPT-5.6 Sol but not for some baseline models [SRC-OAI-001].

The Map therefore treats access level as an evidence property. A conclusion based only on a public report receives lower confidence than a result independently reproduced with access appropriate to the threat model. This does not mean that all evaluators should receive unrestricted model internals. It means that regulators should define secure access tiers and explain which tier is necessary for which claim.

## 3. Proposed evidence architecture

### 3.1 Atomic evidence records

Each row records one claim with the following minimum fields:

- model, checkpoint and release date;
- domain and evidence type;
- original metric and unit;
- threshold reference and status;
- source and evaluator;
- independence and access level;
- evaluated configuration and safeguards state;
- number of trials where available;
- result direction, limitations and verification date.

The approach prevents a common error: treating a system card as a single piece of evidence. A card may contain a concerning capability result, a reassuring refusal result, an acknowledged limitation and an external evaluator’s finding. These should remain separable.

### 3.2 No universal risk score

A universal score would require assumptions about the relative value of a cyber benchmark, a persuasion uplift study, an agentic time horizon and a safeguard bypass rate. Those assumptions are not scientifically mature and would be easy to manipulate. The Map instead uses qualitative but explicit trigger conditions.

The trigger is strongest when three elements combine:

1. **capability or propensity signal** — for example, an alert threshold is reached;
2. **exposure or affordance** — broad deployment, powerful tools or critical-sector integration;
3. **control weakness or evidence gap** — bypassable safeguards, missing independent testing or inadequate evaluator access.

This structure allows authorities to act on incomplete evidence while remaining transparent about why the action is precautionary.

### 3.3 Confidence is about the action, not “safety”

The Map assigns low, medium or high confidence to each recommended action. Confidence increases with independent corroboration, appropriate evaluator access, transparent methods, adequate trials and replicated results. It decreases when only provider summaries are available, checkpoints differ, configurations are missing or the evaluation is exploratory.

A low-confidence recommendation for additional testing can still be entirely appropriate. Conversely, high confidence that a model remains below a benchmark threshold does not prove that deployment risk is acceptable.

## 4. Decision matrix for public authorities

### Trigger A — Additional targeted testing

**Evidence:** an alert threshold is reached; a result is near threshold or indeterminate; a below-threshold result reveals meaningful uplift; a safeguard test shows a material failure rate; or a major deployment configuration is untested.

**Action:** request or conduct tests tied to the real harm pathway. Specify checkpoint, scaffold, tools, permissions, inference budget, trials and success criteria before testing begins.

**Example:** cyber alert-threshold evidence should lead to realistic long-horizon testing against representative hardened targets in a controlled environment, not merely more capture-the-flag questions.

### Trigger B — Qualified independent evaluation

**Evidence:** high-concern evidence is only developer-reported; external testing used a different checkpoint; the evaluator lacked methodological autonomy; or the threat model cannot be tested with black-box access.

**Action:** appoint a qualified evaluator and provide secure access proportionate to the claim. Require disclosure of provider funding, access constraints, evaluator discretion and publication rights.

**Example:** loss-of-control claims involving evaluation gaming may require grey-box, white-box or training-run assessment rather than public API testing.

### Trigger C — Restricted or identity-gated access

**Evidence:** high capability or material safeguard weakness is combined with broad deployment, powerful tools, high-risk jurisdictions or users, or critical-infrastructure access.

**Action:** restrict the relevant capability, tool or product surface; require identity and institutional verification; apply rate, environment and monitoring controls; create a pathway for legitimate research and defensive work.

**Example:** advanced cyber functionality can remain available to verified defenders in authorised environments while high-risk exploit chaining is restricted for anonymous or untrusted access.

### Trigger D — Serious-incident assessment and reporting

**Evidence:** a real-world event suggests death, serious harm, major service disruption, critical-infrastructure compromise, model-weight theft, significant safeguard failure or another potentially reportable outcome.

**Action:** preserve logs and artefacts; assess the event against applicable criteria; notify the competent authority when required; connect the incident to model, deployment and safeguard versions.

The public Map should not itself declare that a legal reporting threshold has been met. It should make the evidentiary chain visible.

### Trigger E — Deployment review or corrective measures

**Evidence:** a critical capability threshold is reached; a serious incident occurs; repeated independent tests show existing mitigations are ineffective; or a provider cannot demonstrate acceptable residual risk for the actual deployment configuration.

**Action:** reconsider availability, tools, permissions, geography, user classes or the deployment itself. Corrective measures may include stronger safeguards, delayed expansion, restricted access, rollback or suspension of a specific configuration.

## 5. Application to the EU AI Office

The EU AI Office is well placed to use a trigger map because it combines technical oversight with enforcement responsibility for general-purpose AI models. The instrument could support four functions.

### 5.1 Triage of provider submissions

Safety and Security Frameworks and Model Reports can be translated into standard evidence rows. This would allow staff to identify missing domains, unsupported threshold claims, stale tests and differences between the public summary and confidential evidence.

### 5.2 Requests for information and evaluation

The Map can make requests more precise. Instead of asking generally for “more safety evidence”, the Office could specify the model version, harm pathway, evaluator access, deployment scaffold and decision that the evidence must inform.

### 5.3 Coordination with the Scientific Panel and national authorities

A shared schema would help separate EU-level GPAI model risk from sector-specific deployment risk. The AI Office could maintain the model-level evidence layer, while national or sector authorities add critical-infrastructure integrations, incidents and local exposure.

### 5.4 Corrective-measure consistency

The Map would not automate enforcement. It would record why similar evidence produced similar or different actions, enabling internal review and reducing dependence on ad hoc provider narratives.

## 6. Uncertainty and the risk of false reassurance

### Missing data

Public system cards often omit trial counts, confidence intervals, full task distributions, exact checkpoint differences or sensitive safeguard details. Missing fields should remain explicit. They should not be imputed as reassuring values.

### Non-comparable evaluations

Benchmark names can conceal different scaffolds, tools, prompts or inference budgets. Even within one provider, updated evaluation pipelines may make historical results non-comparable. Cross-provider charts should therefore be limited to genuinely harmonised tests.

### Provider incentives

Providers have legitimate security reasons to withhold details, but they also have commercial incentives to release capable models and frame residual risk as manageable. The correct response is not to discard provider evidence; it is to label its provenance and seek independent corroboration for high-impact claims.

### Evaluator incentives and dependence

External evaluators may depend on provider access, funding or continued relationships. Disclosure of these conditions is essential. Independence includes control over methods, sufficient time, freedom to report limitations and protection against selective publication.

### Evaluation awareness and gaming

Models may identify evaluation settings, underperform, manipulate monitors or behave differently when reasoning is visible. Hidden tasks and action-only monitoring are not complete solutions. Secure access to internal signals and training-run evidence may sometimes be necessary.

### False precision

A numerical score can make uncertain evidence appear objective. The project therefore does not estimate the probability of catastrophe from public benchmarks. It identifies the next decision that the evidence can reasonably support.

### False reassurance from successful safeguards

A strong refusal score can coexist with vulnerability to prompt injection, alternative product surfaces or long multi-turn attacks. Safeguards should be tested as a stack, under realistic adaptive pressure, and connected to post-deployment monitoring.

## 7. Recommendations

### 1. Adopt a common evidence schema for systemic-risk model submissions

Require atomic claims, source identifiers, model checkpoints, configurations, access conditions, limitations and dates. Allow confidential annexes while publishing non-sensitive metadata.

### 2. Define evaluator-access tiers

Specify when public black-box, controlled black-box, grey-box, white-box or training-run access is appropriate. Pair deeper access with secure facilities, confidentiality and information-hazard controls.

### 3. Treat alert thresholds as action points, not release bans

An alert-threshold crossing should normally activate targeted testing and independent evaluation. Restriction or deployment review should depend on the capability, exposure, safeguards and residual uncertainty.

### 4. Require deployment-relevant system evaluation

Evaluate tools, permissions, memory, multi-agent orchestration, monitors and critical-sector integrations. A base-model result alone is not enough for an agentic deployment decision.

### 5. Create an EU-level incident evidence layer

Link serious incidents to model and safeguard versions, deployment conditions and prior evaluation signals. Publish aggregated lessons while protecting security-sensitive information.

### 6. Preserve plural methods and avoid a universal safety score

Standardise metadata and decision processes without freezing immature benchmarks. Authorities should be able to compare evidence quality even when the underlying tests differ.

### 7. Publish reasons for supervisory escalation

Where legally and operationally possible, explain which evidence activated additional testing, access restrictions or corrective measures. This improves predictability and enables external scrutiny.

## Conclusion

Frontier-model governance does not primarily lack risk categories. It lacks a disciplined bridge between evidence and action. Public system cards, independent evaluations and government testing already contain signals that can support earlier and more proportionate intervention, but only if their provenance, configuration and limitations remain visible.

The Frontier Model Risk Trigger Map offers a practical bridge. It is conservative about what public evidence can prove, but ambitious about what that evidence can organise. Its central principle is simple: **do not ask a heterogeneous benchmark record to produce a verdict; ask it to justify the next supervisory step.**

## Source register used in this briefing

- **SRC-OAI-001** — OpenAI, *GPT-5.6 System Card*, 9 July 2026.
- **SRC-GDM-001** — Google DeepMind, *Gemini 3.1 Pro Model Card*, 19 February 2026.
- **SRC-XAI-001** — xAI, *Grok 4.20 System Card*, 7 April 2026.
- **SRC-XAI-002** — xAI, *Grok 4.5 Model Card*, 14 July 2026.
- **SRC-AISI-001** — UK AI Security Institute, *Frontier AI Trends Report*.
- **SRC-METR-001** — METR, *Frontier Risk Report (February to March 2026)*, 19 May 2026.
- **SRC-METR-002** — METR, *Task-Completion Time Horizons of Frontier AI Models*.
- **SRC-APOLLO-001** — Apollo Research, *The Need for Deeper, White-Box Access to Maintain State-of-the-Art Evaluations for Loss-of-Control Threats*, 20 May 2026.
- **SRC-EU-001** — European Commission, *The General-Purpose AI Code of Practice*.
- **SRC-EU-002** — European Commission, *Guidelines for providers of general-purpose AI models*, 28 April 2026.
- **SRC-EU-003** — European Commission, *AI Act regulatory framework overview*.
