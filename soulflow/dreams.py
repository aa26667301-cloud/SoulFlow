from __future__ import annotations
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DISCLAIMER = "夢境模組用於記錄與自我反思，不把夢視為預言、診斷、記憶證據或他人真實想法的證明。"

def load_themes() -> dict:
    return json.loads((DATA_DIR / "dream_themes.json").read_text(encoding="utf-8"))

def tag_dream(text: str) -> list[str]:
    normalized = (text or "").strip().lower()
    tags = []
    for tag, cfg in load_themes().items():
        if any(k.lower() in normalized for k in cfg["keywords"]):
            tags.append(tag)
    return tags or ["open_reflection"]

def dream_reflection(text: str, limit: int = 5) -> dict:
    content = (text or "").strip()
    if not content:
        raise ValueError("dream text 不可為空")
    themes = load_themes()
    tags = tag_dream(content)
    questions = []
    for tag in tags:
        if tag in themes:
            questions.append(themes[tag]["prompt"])
    defaults = [
        "夢裡最清楚的一個畫面是什麼？",
        "醒來後最殘留的感受是什麼？",
        "有哪些內容可能只是最近看過、想過或擔心過的材料重新組合？",
        "如果不急著『解夢』，這個夢值得你多注意哪一個感受？",
        "今天有沒有一個小行動能回應這個感受，而不是回應夢的字面情節？",
    ]
    for q in defaults:
        if q not in questions:
            questions.append(q)
    limit = max(1, min(int(limit), 8))
    return {
        "dream": content,
        "tags": tags,
        "questions": questions[:limit],
        "journal_template": {
            "scene": "我記得的場景：",
            "emotion": "最強烈的感受：",
            "association": "我自己的第一個聯想：",
            "waking_context": "最近生活中可能相關的事件：",
            "small_action": "今天可以做的一個小行動：",
        },
        "disclaimer": DISCLAIMER,
    }
