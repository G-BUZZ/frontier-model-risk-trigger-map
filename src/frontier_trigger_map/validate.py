from __future__ import annotations

from dataclasses import dataclass
import tomllib
from pathlib import Path
from urllib.parse import urlparse

from .io import ROOT, read_csv


@dataclass(frozen=True)
class ValidationIssue:
    table: str
    row: str
    message: str


REQUIRED = {
    "models": {"model_id", "provider", "model_name", "release_date", "system_card_source_id", "status"},
    "sources": {"source_id", "title", "publisher", "source_kind", "source_independence", "access_level", "url", "status"},
    "evidence": {"evidence_id", "scope", "domain", "evidence_type", "claim", "threshold_status", "concern_level", "source_id", "result_direction", "limitations", "status"},
    "incidents": {"incident_id", "model_id", "domain", "severity", "description", "source_id", "verification_status"},
}


def _headers(path: Path) -> set[str]:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return {item.strip() for item in first.split(",")}


def validate_repository() -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    paths = {
        "models": ROOT / "data/models/models.csv",
        "sources": ROOT / "data/sources/sources.csv",
        "evidence": ROOT / "data/evidence/evidence.csv",
        "incidents": ROOT / "data/incidents/incidents.csv",
    }
    for name, path in paths.items():
        missing = REQUIRED[name] - _headers(path)
        if missing:
            issues.append(ValidationIssue(name, "header", f"missing columns: {sorted(missing)}"))

    with (ROOT / "config/taxonomy.toml").open("rb") as handle:
        taxonomy = tomllib.load(handle)

    domains = set(taxonomy["domains"])
    evidence_types = set(taxonomy["evidence_types"]["allowed"])
    concerns = set(taxonomy["concern_levels"]["allowed"])
    thresholds = set(taxonomy["threshold_statuses"]["allowed"])
    independence = set(taxonomy["source_independence"]["allowed"])
    access = set(taxonomy["access_levels"]["allowed"])

    models = read_csv("data/models/models.csv")
    sources = read_csv("data/sources/sources.csv")
    evidence = read_csv("data/evidence/evidence.csv")
    incidents = read_csv("data/incidents/incidents.csv")

    model_ids = {row["model_id"] for row in models}
    source_ids = {row["source_id"] for row in sources}

    if len(model_ids) != len(models):
        issues.append(ValidationIssue("models", "all", "duplicate model_id"))
    if len(source_ids) != len(sources):
        issues.append(ValidationIssue("sources", "all", "duplicate source_id"))

    for row in models:
        rid = row["model_id"]
        if row["system_card_source_id"] not in source_ids:
            issues.append(ValidationIssue("models", rid, "unknown system_card_source_id"))

    for row in sources:
        rid = row["source_id"]
        if row["source_independence"] not in independence:
            issues.append(ValidationIssue("sources", rid, "invalid source_independence"))
        if row["access_level"] not in access:
            issues.append(ValidationIssue("sources", rid, "invalid access_level"))
        parsed = urlparse(row["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            issues.append(ValidationIssue("sources", rid, "invalid URL"))

    seen_evidence: set[str] = set()
    for row in evidence:
        rid = row["evidence_id"]
        if rid in seen_evidence:
            issues.append(ValidationIssue("evidence", rid, "duplicate evidence_id"))
        seen_evidence.add(rid)
        if row["model_id"] and row["model_id"] not in model_ids:
            issues.append(ValidationIssue("evidence", rid, "unknown model_id"))
        if row["source_id"] not in source_ids:
            issues.append(ValidationIssue("evidence", rid, "unknown source_id"))
        if row["domain"] not in domains:
            issues.append(ValidationIssue("evidence", rid, "invalid domain"))
        if row["evidence_type"] not in evidence_types:
            issues.append(ValidationIssue("evidence", rid, "invalid evidence_type"))
        if row["concern_level"] not in concerns:
            issues.append(ValidationIssue("evidence", rid, "invalid concern_level"))
        if row["threshold_status"] not in thresholds:
            issues.append(ValidationIssue("evidence", rid, "invalid threshold_status"))
        if not row["limitations"].strip():
            issues.append(ValidationIssue("evidence", rid, "limitations must not be empty"))

    for row in incidents:
        rid = row["incident_id"] or "blank"
        if row["model_id"] and row["model_id"] not in model_ids:
            issues.append(ValidationIssue("incidents", rid, "unknown model_id"))
        if row["source_id"] and row["source_id"] not in source_ids:
            issues.append(ValidationIssue("incidents", rid, "unknown source_id"))
        if row["domain"] and row["domain"] not in domains:
            issues.append(ValidationIssue("incidents", rid, "invalid domain"))

    return issues
