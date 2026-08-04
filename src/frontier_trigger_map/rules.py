from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import tomllib

from .io import ROOT, read_csv


@dataclass(frozen=True)
class Trigger:
    model_id: str
    provider: str
    model_name: str
    domain: str
    action: str
    action_label: str
    trigger_strength: str
    confidence: str
    evidence_ids: str
    rationale: str
    limitations: str


def _load_config() -> dict:
    with (ROOT / "config/decision_rules.toml").open("rb") as handle:
        return tomllib.load(handle)


def _source_maps() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    sources = {row["source_id"]: row for row in read_csv("data/sources/sources.csv")}
    models = {row["model_id"]: row for row in read_csv("data/models/models.csv")}
    return sources, models


def _confidence(rows: list[dict[str, str]], sources: dict[str, dict[str, str]], independent_types: set[str]) -> str:
    independent = [r for r in rows if sources[r["source_id"]]["source_independence"] in independent_types]
    replicated = [r for r in rows if r["independent_replication"].lower() in {"yes", "partial"}]
    access = {sources[r["source_id"]]["access_level"] for r in rows}
    if independent and replicated and access & {"grey_box", "white_box", "training_run_access"}:
        return "high"
    if independent or len({r["source_id"] for r in rows}) >= 2:
        return "medium"
    return "low"


def _strength(rows: list[dict[str, str]]) -> str:
    concerns = {r["concern_level"] for r in rows}
    thresholds = {r["threshold_status"] for r in rows}
    if "critical" in concerns or "threshold_reached" in thresholds:
        return "strong"
    if concerns & {"high", "elevated"} or thresholds & {"alert_reached", "near_threshold"}:
        return "moderate"
    return "weak"


def generate_triggers() -> list[Trigger]:
    cfg = _load_config()
    settings = cfg["settings"]
    actions = cfg["actions"]
    independent_types = set(settings["independent_source_types"])
    uncertain = set(settings["uncertain_threshold_statuses"])
    concerning = set(settings["concerning_threshold_statuses"])
    high_concern = set(settings["high_concern_levels"])

    sources, models = _source_maps()
    evidence = [
        row
        for row in read_csv("data/evidence/evidence.csv")
        if row["model_id"]
        and row["status"] == "verified"
        and models[row["model_id"]]["status"] == "active"
    ]
    incidents = read_csv("data/incidents/incidents.csv")

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in evidence:
        grouped[(row["model_id"], row["domain"])].append(row)

    output: list[Trigger] = []
    for (model_id, domain), rows in sorted(grouped.items()):
        model = models[model_id]
        thresholds = {r["threshold_status"] for r in rows}
        concerns = {r["concern_level"] for r in rows}
        directions = {r["result_direction"] for r in rows}
        source_types = {sources[r["source_id"]]["source_independence"] for r in rows}
        has_independent = bool(source_types & independent_types)
        evidence_ids = ";".join(r["evidence_id"] for r in rows)
        limits = " | ".join(dict.fromkeys(r["limitations"] for r in rows))
        confidence = _confidence(rows, sources, independent_types)
        strength = _strength(rows)

        def add(action: str, rationale: str, override_strength: str | None = None) -> None:
            output.append(Trigger(
                model_id=model_id,
                provider=model["provider"],
                model_name=model["model_name"],
                domain=domain,
                action=action,
                action_label=actions[action]["label"],
                trigger_strength=override_strength or strength,
                confidence=confidence,
                evidence_ids=evidence_ids,
                rationale=rationale,
                limitations=limits,
            ))

        if thresholds & (uncertain | concerning) or directions & {"concerning", "mixed"}:
            add("additional_testing", "The evidence is concerning, mixed, near/at an alert point, or insufficiently resolved for the covered deployment configuration.")

        if (concerns & high_concern or thresholds & concerning) and not has_independent:
            add("independent_evaluation", "High-concern or alert-threshold evidence is not independently corroborated in the current dataset.")

        safeguard_problem = any(r["evidence_type"] == "safeguard" and r["concern_level"] in high_concern for r in rows)
        if model["deployment_scope"] == "broad" and (concerns & high_concern or safeguard_problem):
            add("restricted_access", "Broad deployment is combined with high-concern capability or safeguard evidence; capability-specific access controls should be assessed.")

        if "threshold_reached" in thresholds or "critical" in concerns:
            add("deployment_review", "A critical concern or declared threshold crossing requires human review of deployment and corrective measures.", "strong")

    serious_by_model_domain: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in incidents:
        if row.get("model_id") and row.get("severity") in {"serious", "critical"}:
            serious_by_model_domain[(row["model_id"], row["domain"])].append(row)

    for (model_id, domain), rows in serious_by_model_domain.items():
        model = models[model_id]
        ids = ";".join(r["incident_id"] for r in rows)
        output.append(Trigger(model_id, model["provider"], model["model_name"], domain,
                              "incident_assessment", actions["incident_assessment"]["label"],
                              "strong", "medium", ids,
                              "A documented serious or critical incident requires preservation, legal assessment and reporting analysis.",
                              "Public records may not contain enough information for a final legal classification."))
        output.append(Trigger(model_id, model["provider"], model["model_name"], domain,
                              "deployment_review", actions["deployment_review"]["label"],
                              "strong", "medium", ids,
                              "A serious or critical incident supports immediate review of the affected deployment and safeguards.",
                              "Causation and model-version attribution require confirmation."))

    priority = {name: data["priority"] for name, data in actions.items()}
    output.sort(key=lambda t: (t.provider, t.model_name, t.domain, priority[t.action]))
    return output
