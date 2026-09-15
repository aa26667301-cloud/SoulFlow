import unittest

from soulflow.engine import CheckIn, recommend, summarize
from soulflow.journal import generate_prompts, infer_theme
from soulflow.safety import needs_safety_redirect


class SoulFlowTests(unittest.TestCase):
    def test_validate(self):
        CheckIn(1, 3, 5).validate()
        with self.assertRaises(ValueError):
            CheckIn(0, 3, 5).validate()

    def test_lowest_axis_first(self):
        items = recommend(CheckIn(2, 4, 5))
        self.assertEqual(items[0].axis, "mind")

    def test_summary(self):
        result = summarize(CheckIn(2, 3, 4))
        self.assertEqual(result["average"], 3.0)
        self.assertEqual(result["lowest_axis"], "mind")

    def test_journal_theme(self):
        self.assertEqual(infer_theme("最近工作很焦慮"), "work")
        self.assertTrue(len(generate_prompts("感情", 2)) == 2)

    def test_safety_keyword(self):
        self.assertTrue(needs_safety_redirect("我有想死的念頭"))
        self.assertFalse(needs_safety_redirect("今天有點累"))


if __name__ == "__main__":
    unittest.main()
