from __future__ import annotations
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DISCLAIMER = "冥想內容是一般性自我照護練習，不是醫療或心理治療。任何練習讓你不舒服時都可以立即停止。"

THEME_KEYWORDS = {
    "grounding": ("不安","失控","落地","grounding","慌"),
    "overload": ("太多","混亂","過載","忙","壓力"),
    "calm": ("放鬆","安靜","冷靜","calm"),
    "focus": ("專注","工作","讀書","學習","focus"),
    "rest": ("累","疲憊","休息","睡前","rest"),
    "self_compassion": ("自責","失敗","比較","自信","自我價值"),
    "relationship": ("感情","關係","伴侶","家人","朋友"),
    "transition": ("改變","轉職","離職","新階段","搬家"),
    "reflection": ("反思","迷惘","方向","意義"),
    "energy": ("沒精神","卡住","停滯","reset"),
}

def load_meditations() -> list[dict]:
    return json.loads((DATA_DIR / "meditations.json").read_text(encoding="utf-8"))

def infer_meditation_themes(text: str) -> list[str]:
    normalized = (text or "").strip().lower()
    hits = [theme for theme, words in THEME_KEYWORDS.items() if any(w.lower() in normalized for w in words)]
    return hits or ["reflection"]

def recommend_meditations(text: str, minutes: int = 10, limit: int = 3) -> list[dict]:
    minutes = max(3, min(int(minutes), 30))
    limit = max(1, min(int(limit), 5))
    themes = infer_meditation_themes(text)
    ranked = []
    for item in load_meditations():
        matched = [t for t in themes if t in item["themes"]]
        duration_fit = item["min_minutes"] <= minutes <= item["max_minutes"]
        score = len(matched) * 2 + int(duration_fit)
        ranked.append((score, item["id"], item, matched))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    return [
        {**item, "matched_themes": matched, "score": score, "disclaimer": DISCLAIMER}
        for score, _, item, matched in ranked[:limit]
    ]

def get_meditation(identifier: str) -> dict:
    needle = (identifier or "").strip().lower()
    for item in load_meditations():
        if needle in {item["id"].lower(), item["title"].lower()}:
            return item
    raise KeyError(f"找不到冥想練習：{identifier}")

def meditation_session(text: str = "", minutes: int = 10, practice_id: str | None = None) -> dict:
    minutes = max(3, min(int(minutes), 30))
    item = get_meditation(practice_id) if practice_id else recommend_meditations(text, minutes, 1)[0]
    title = item["title"]
    steps = list(item["steps"])
    return {
        "title": title,
        "focus": (text or "").strip() or "當下狀態",
        "minutes": minutes,
        "steps": steps,
        "closing": "結束後不用急著評分效果，只記下一個最明顯的身體或情緒變化。",
        "disclaimer": DISCLAIMER,
    }
