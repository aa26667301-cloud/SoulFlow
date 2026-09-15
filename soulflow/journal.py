from __future__ import annotations

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_prompts() -> dict[str, list[str]]:
    with open(DATA_DIR / "journal_prompts.json", "r", encoding="utf-8") as f:
        return json.load(f)


def infer_theme(theme: str) -> str:
    text = (theme or "").lower()
    mapping = {
        "work": ["工作", "職場", "專案", "上班", "事業"],
        "relationship": ["感情", "關係", "朋友", "伴侶", "家人", "吵架"],
        "self_worth": ["自信", "價值", "自卑", "比較", "失敗"],
        "meaning": ["迷惘", "方向", "人生", "意義", "未來"],
    }
    for key, words in mapping.items():
        if any(word in text for word in words):
            return key
    return "default"


def generate_prompts(theme: str = "", limit: int = 4) -> list[str]:
    prompts = load_prompts()
    key = infer_theme(theme)
    selected = prompts.get(key, prompts["default"])
    return selected[: max(1, min(limit, len(selected)))]
