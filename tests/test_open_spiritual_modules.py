import unittest
from soulflow.moon import get_phase, moon_reflection, moon_cycle
from soulflow.dreams import tag_dream, dream_reflection
from soulflow.meditation import recommend_meditations, meditation_session

class OpenSpiritualModulesTests(unittest.TestCase):
    def test_moon_alias(self):
        self.assertEqual(get_phase("滿月")["id"], "full_moon")

    def test_moon_reflection_has_disclaimer(self):
        out = moon_reflection("新月", "新工作")
        self.assertIn("disclaimer", out)
        self.assertEqual(out["phase"]["id"], "new_moon")

    def test_moon_cycle_has_eight_phases(self):
        self.assertEqual(len(moon_cycle("年度計畫")["cycle"]), 8)

    def test_dream_tags_are_descriptive(self):
        tags = tag_dream("我夢到在學校一直跑，還趕不上考試")
        self.assertIn("movement", tags)
        self.assertIn("work", tags)

    def test_dream_reflection_is_not_prediction(self):
        out = dream_reflection("夢到海水和朋友")
        self.assertIn("預言", out["disclaimer"])

    def test_meditation_recommender(self):
        out = recommend_meditations("工作很亂，想專注", 10, 2)
        self.assertEqual(len(out), 2)
        self.assertTrue(any("focus" in x["themes"] for x in out))

    def test_meditation_session_limits_minutes(self):
        out = meditation_session("想安靜一下", 99)
        self.assertEqual(out["minutes"], 30)
        self.assertIn("disclaimer", out)

if __name__ == "__main__":
    unittest.main()
