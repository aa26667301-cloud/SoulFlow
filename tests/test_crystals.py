import unittest

from soulflow.crystals import build_ritual, get_crystal, infer_themes, recommend_crystals, reflection_card


class CrystalReflectionTests(unittest.TestCase):
    def test_theme_inference(self):
        self.assertIn("focus", infer_themes("最近工作很難專注"))
        self.assertIn("relationship", infer_themes("我和伴侶最近溝通卡住"))

    def test_recommendation_is_deterministic(self):
        first = [x.id for x in recommend_crystals("工作需要專注和整理", 3)]
        second = [x.id for x in recommend_crystals("工作需要專注和整理", 3)]
        self.assertEqual(first, second)
        self.assertEqual(len(first), 3)

    def test_lookup(self):
        self.assertEqual(get_crystal("粉晶")["id"], "rose_quartz")
        self.assertEqual(get_crystal("Amethyst")["zh_name"], "紫水晶")
        with self.assertRaises(KeyError):
            get_crystal("不存在的石頭")

    def test_card_has_safety_disclaimer(self):
        card = reflection_card("最近對自己太苛刻")
        self.assertIn("不代表礦石具有", card["disclaimer"])
        self.assertTrue(card["crystal"]["reflection_prompt"])

    def test_ritual_bounds_minutes(self):
        short = build_ritual("想整理方向", 1)
        long = build_ritual("想整理方向", 99)
        self.assertEqual(short["minutes"], 5)
        self.assertEqual(long["minutes"], 30)
        self.assertEqual(len(short["steps"]), 4)


if __name__ == "__main__":
    unittest.main()
