"""Local tests of public examples and publication data, never original exploits."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pocs"))
sys.path.insert(0, str(ROOT / "scripts"))
import offline_models as models
from review_results import validate_results
from validate_publication import audit_model_source, review_tree


class ModelTests(unittest.TestCase):
    def test_partial_state_exposes_invalid_assumption(self):
        self.assertEqual(models.partial_state(True, False).result, "cleanup_assumption_violated")

    def test_partial_state_control(self):
        self.assertEqual(models.partial_state(True, True).result, "incomplete_state_not_consumed")

    def test_complete_initialization(self):
        self.assertEqual(models.partial_state(False, False).result, "initialized_state")

    def test_lifetime_mismatch(self):
        self.assertEqual(models.request_lifetime(1, 2, False).result, "stale_reference_model")

    def test_lifetime_reset(self):
        self.assertEqual(models.request_lifetime(1, 2, True).result, "reference_cleared")

    def test_same_lifetime(self):
        self.assertEqual(models.request_lifetime(1, 1, False).result, "same_lifetime")

    def test_bad_generation(self):
        for value in (-1, True, "1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                models.request_lifetime(value, 2, False)

    def test_format_agreement(self):
        self.assertEqual(models.format_agreement("format-A", "format-A").result, "format_consistent")

    def test_format_rejection(self):
        self.assertEqual(models.format_agreement("format-A", "format-B").result, "mismatch_rejected")

    def test_format_model_without_guard(self):
        self.assertEqual(models.format_agreement("format-A", "format-B", False).result, "interpretation_boundary_changed")

    def test_no_arbitrary_format_input(self):
        with self.assertRaises(ValueError):
            models.format_agreement("unrecognized", "format-A")

    def test_stored_data_not_reader(self):
        self.assertEqual(models.reader_boundary(True, False).result, "stored_data_without_reader")

    def test_independent_application_requirement(self):
        self.assertEqual(models.reader_boundary(True, True).result, "independent_application_boundary_needed")

    def test_no_record(self):
        self.assertEqual(models.reader_boundary(False, True).result, "no_record")

    def test_missing_application_prerequisite(self):
        self.assertEqual(models.application_requirements(False, True, True).result, "incomplete_claim")

    def test_conditions_not_execution_proof(self):
        self.assertEqual(models.application_requirements(True, True, True).result, "assumptions_present_not_execution_proof")

    def test_all_outputs_explicitly_non_reproductions(self):
        self.assertTrue(all(item.is_php_reproduction is False for item in models.demonstration()))
        self.assertEqual(len(models.demonstration()), 10)


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/results.json").read_text(encoding="utf-8"))

    def test_selected_counts(self):
        self.assertEqual(validate_results(self.data), {"target_effects": 26, "negative_controls": 61})

    def test_duplicate_cohort_rejected(self):
        self.data["cohorts"][1]["id"] = self.data["cohorts"][0]["id"]
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_wrong_total_rejected(self):
        self.data["counts"]["target_effects"] += 1
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_boolean_count_rejected(self):
        self.data["cohorts"][0]["target_effects"] = True
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_negative_count_rejected(self):
        self.data["cohorts"][0]["negative_controls"] = -1
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_bad_original_digest_rejected(self):
        self.data["cohorts"][0]["original_sha256"] = "not-a-digest"
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_fresh_reproduction_claim_rejected(self):
        self.data["runtime_reproduced_for_public_edition"] = True
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_extra_payload_field_rejected(self):
        self.data["cohorts"][0]["extra_data"] = "not permitted by this export schema"
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_missing_proof_limit_rejected(self):
        self.data["mechanisms"][0]["limitation"] = ""
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_duplicate_mechanism_rejected(self):
        self.data["mechanisms"][1]["id"] = self.data["mechanisms"][0]["id"]
        with self.assertRaises(ValueError):
            validate_results(self.data)

    def test_unknown_root_field_rejected(self):
        self.data["unexpected"] = {}
        with self.assertRaises(ValueError):
            validate_results(self.data)


class PublicationTests(unittest.TestCase):
    def test_current_model_imports(self):
        audit_model_source((ROOT / "pocs/offline_models.py").read_text(encoding="utf-8"))

    def test_network_import_rejected(self):
        with self.assertRaises(ValueError):
            audit_model_source("import socket\n")

    def test_dynamic_execution_rejected(self):
        with self.assertRaises(ValueError):
            audit_model_source("eval('1 + 1')\n")

    def test_file_write_rejected(self):
        with self.assertRaises(ValueError):
            audit_model_source("open('example', 'w')\n")

    def test_complete_public_tree(self):
        result = review_tree()
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["runtime_reproduced"])


if __name__ == "__main__":
    unittest.main()
