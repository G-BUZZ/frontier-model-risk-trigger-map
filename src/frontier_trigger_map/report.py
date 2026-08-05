from pathlib import Path
import csv
from datetime import date


ROOT = Path(__file__).resolve().parents[2]

MODELS = ROOT / "data/models/models.csv"
EVIDENCE = ROOT / "data/evidence/evidence.csv"
TRIGGERS = ROOT / "outputs/trigger_map.csv"

OUTPUT = ROOT / "outputs/frontier_risk_governance_report.md"


def count_rows(path):
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def main():

    models = count_rows(MODELS)
    evidence = count_rows(EVIDENCE)
    triggers = count_rows(TRIGGERS)

    report = f"""# Frontier Risk Governance Report

Generated: {date.today()}

## Overview

This report summarizes the current state of the
Frontier Model Risk Trigger Map.

## Coverage

- Models analysed: {models}
- Evidence records: {evidence}
- Generated triggers: {triggers}

## Governance Interpretation

The project does not produce a universal risk score.

Instead, it connects:

Evidence
→ Evaluation
→ Trigger
→ Governance action

## Uncertainty

Important limitations:

- provider disclosures may use different thresholds;
- evaluations may not be directly comparable;
- independent replication remains limited;
- absence of evidence is not evidence of absence.

## Recommended Actions

Possible governance responses include:

- additional evaluation;
- independent review;
- deployment reassessment;
- monitoring escalation.

"""

    OUTPUT.write_text(report, encoding="utf-8")

    print(f"Built {OUTPUT}")


if __name__ == "__main__":
    main()
