from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

DISCLAIMER = (
    "水晶內容只作為文化與象徵式自我反思素材；"
    "不代表礦石具有經科學證實的醫療、心理治療、能量治療或預測效果。"
)

THEME_KEYWORDS: dict[str, tuple[str, ...]] = {
    "clarity": ("清楚", "混亂", "選擇", "決定", "方向", "釐清", "clarity", "decision"),
    "focus": ("專注", "拖延", "工作", "讀書", "學習", "效率", "focus", "study"),
    "rest": ("休息", "累", "疲憊", "睡", "安靜", "放鬆", "rest"),
    "relationship": ("感情", "伴侶", "關係", "家人", "朋友", "溝通", "relationship"),
    "self_compassion": ("自責", "自信", "自我價值", "比較", "失敗", "self worth"),
    "boundaries": ("界線", "拒絕", "責任", "被要求", "壓力", "boundary"),
    "grounding": ("不安", "飄", "失控", "落地", "穩定", "grounding"),
    "transition": ("改變", "轉職", "離職", "搬家", "轉換", "新階段", "transition"),
    "creativity": ("創作", "靈感", "設計", "卡住", "作品", "creative"),
    "communication": ("說不出口", "表達", "溝通", "訊息", "談話", "communication"),
    "resources": ("資源", "金錢", "預算", "人脈", "工具", "resources"),
    "agency": ("行動", "勇氣", "開始", "推進", "主動", "action"),
    "values": ("價值", "意義", "人生", "原則", "values"),
    "release": ("放下", "結束", "捨不得", "放不下", "release"),
    "organization": ("整理", "資訊", "雜亂", "分類", "organization"),
}


@dataclass(frozen=True)
class CrystalReflection:
    id: str
    zh_name: str
    en_name: str
    color: str
    themes: list[str]
    reflection_prompt: str
    micro_action: str
    matched_themes: list[str]
    score: int

    def to_dict(self) -> dict:
        data = asdict(self)
        data["disclaimer"] = DISCLAIMER
        return data


def load_crystals() -> list[dict]:
    with open(DATA_DIR / "crystals.json", "r", encoding="utf-8") as f:
        return json.load(f)


def infer_themes(text: str) -> list[str]:
    normalized = (text or "").strip().lower()
    hits: list[str] = []
    for theme, keywords in THEME_KEYWORDS.items():
        if any(keyword.lower() in normalized for keyword in keywords):
            hits.append(theme)
    return hits or ["clarity"]


def get_crystal(identifier: str) -> dict:
    needle = (identifier or "").strip().lower()
    for item in load_crystals():
        if needle in {item["id"].lower(), item["zh_name"].lower(), item["en_name"].lower()}:
            return item
    raise KeyError(f"找不到水晶：{identifier}")


def recommend_crystals(text: str, limit: int = 3) -> list[CrystalReflection]:
    limit = max(1, min(int(limit), 5))
    themes = infer_themes(text)
    ranked: list[tuple[int, str, dict, list[str]]] = []
    for item in load_crystals():
        matched = [theme for theme in themes if theme in item["themes"]]
        score = len(matched)
        ranked.append((score, item["id"], item, matched))

    ranked.sort(key=lambda row: (-row[0], row[1]))
    results: list[CrystalReflection] = []
    for score, _, item, matched in ranked[:limit]:
        results.append(
            CrystalReflection(
                id=item["id"],
                zh_name=item["zh_name"],
                en_name=item["en_name"],
                color=item["color"],
                themes=item["themes"],
                reflection_prompt=item["reflection_prompt"],
                micro_action=item["micro_action"],
                matched_themes=matched,
                score=score,
            )
        )
    return results


def reflection_card(text: str, crystal_id: str | None = None) -> dict:
    item = get_crystal(crystal_id) if crystal_id else recommend_crystals(text, 1)[0].to_dict()
    if crystal_id:
        themes = infer_themes(text)
        matched = [t for t in themes if t in item["themes"]]
        card = {
            **item,
            "matched_themes": matched,
            "score": len(matched),
            "disclaimer": DISCLAIMER,
        }
    else:
        card = item
    return {
        "focus": text,
        "crystal": card,
        "how_to_use": [
            "把水晶視為提醒物件，不必相信它具有特殊力量。",
            "閱讀反思問題，寫下第一個真實答案。",
            "完成一個 micro_action，讓反思落到可觀察的行動。",
        ],
        "disclaimer": DISCLAIMER,
    }


def build_ritual(text: str, minutes: int = 10, crystal_id: str | None = None) -> dict:
    minutes = max(5, min(int(minutes), 30))
    card = reflection_card(text, crystal_id)
    settle = max(1, round(minutes * 0.2))
    reflect = max(2, round(minutes * 0.45))
    act = max(1, minutes - settle - reflect - 1)
    return {
        "title": "象徵式自我反思練習",
        "focus": text,
        "minutes": minutes,
        "symbol": card["crystal"]["zh_name"],
        "steps": [
            {"minutes": settle, "step": "坐好、自然呼吸，注意腳底或椅子的支撐感。"},
            {"minutes": reflect, "step": card["crystal"]["reflection_prompt"]},
            {"minutes": act, "step": card["crystal"]["micro_action"]},
            {"minutes": 1, "step": "用一句話記下：我現在願意帶走的提醒是＿＿＿。"},
        ],
        "disclaimer": DISCLAIMER,
    }
