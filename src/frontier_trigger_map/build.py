from __future__ import annotations

from dataclasses import asdict

from .io import ROOT, write_csv
from .rules import generate_triggers


FIELDS = [
    "model_id", "provider", "model_name", "domain", "action", "action_label",
    "trigger_strength", "confidence", "evidence_ids", "rationale", "limitations"
]


def build_outputs() -> tuple[str, str]:
    triggers = generate_triggers()
    rows = [asdict(item) for item in triggers]
    csv_path = write_csv("outputs/trigger_map.csv", FIELDS, rows)

    md_path = ROOT / "outputs/trigger_map.md"
    lines = [
        "# Generated Frontier Model Risk Trigger Map",
        "",
        "> Research prototype. Triggers identify possible follow-up actions; they are not legal findings or safety certifications.",
        "",
    ]
    current = None
    for item in triggers:
        heading = (item.provider, item.model_name)
        if heading != current:
            current = heading
            lines.extend([f"## {item.provider} — {item.model_name}", ""])
        lines.extend([
            f"### {item.domain}: {item.action_label}",
            "",
            f"- **Trigger strength:** {item.trigger_strength}",
            f"- **Confidence:** {item.confidence}",
            f"- **Evidence:** `{item.evidence_ids}`",
            f"- **Rationale:** {item.rationale}",
            f"- **Limitations:** {item.limitations}",
            "",
        ])
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return str(csv_path), str(md_path)
