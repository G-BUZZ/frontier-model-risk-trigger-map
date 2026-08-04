from __future__ import annotations

import unittest

from frontier_trigger_map.rules import generate_triggers
from frontier_trigger_map.validate import validate_repository


class RepositoryTest(unittest.TestCase):
    def test_repository_validates(self) -> None:
        self.assertEqual(validate_repository(), [])

    def test_generates_triggers(self) -> None:
        triggers = generate_triggers()
        self.assertGreater(len(triggers), 0)
        self.assertTrue(any(t.action == "independent_evaluation" for t in triggers))
        self.assertTrue(any(t.action == "restricted_access" for t in triggers))

    def test_no_automatic_incident_trigger_without_incident(self) -> None:
        triggers = generate_triggers()
        self.assertFalse(any(t.action == "incident_assessment" for t in triggers))

    def test_no_composite_score(self) -> None:
        triggers = generate_triggers()
        self.assertFalse(any(hasattr(t, "risk_score") for t in triggers))


if __name__ == "__main__":
    unittest.main()
