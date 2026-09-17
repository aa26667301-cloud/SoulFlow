from __future__ import annotations
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DISCLAIMER = "月相在此只作為週期性反思框架；不代表月相能決定情緒、人格、運勢或事件結果。"

ALIASES = {
    "新月":"new_moon","new moon":"new_moon",
    "眉月":"waxing_crescent","waxing crescent":"waxing_crescent",
    "上弦月":"first_quarter","first quarter":"first_quarter",
    "盈凸月":"waxing_gibbous","waxing gibbous":"waxing_gibbous",
    "滿月":"full_moon","full moon":"full_moon",
    "虧凸月":"waning_gibbous","waning gibbous":"waning_gibbous",
    "下弦月":"last_quarter","last quarter":"last_quarter",
    "殘月":"waning_crescent","waning crescent":"waning_crescent",
}

def load_phases() -> list[dict]:
    return json.loads((DATA_DIR / "moon_phases.json").read_text(encoding="utf-8"))

def get_phase(identifier: str) -> dict:
    needle = (identifier or "").strip().lower()
    needle = ALIASES.get(needle, needle.replace("-", "_").replace(" ", "_"))
    for phase in load_phases():
        if phase["id"] == needle:
            return phase
    raise KeyError(f"找不到月相：{identifier}")

def moon_reflection(phase: str, theme: str = "") -> dict:
    item = get_phase(phase)
    focus = (theme or "").strip() or "最近的生活狀態"
    return {
        "phase": item,
        "focus": focus,
        "prompt": item["reflection_prompt"],
        "micro_action": item["micro_action"],
        "journal_starter": f"以「{focus}」為主題：{item['reflection_prompt']}",
        "disclaimer": DISCLAIMER,
    }

def moon_cycle(theme: str = "") -> dict:
    focus = (theme or "").strip() or "接下來一段時間"
    return {
        "focus": focus,
        "cycle": [
            {
                "phase": p["zh_name"],
                "phase_id": p["id"],
                "prompt": p["reflection_prompt"],
                "micro_action": p["micro_action"],
            }
            for p in load_phases()
        ],
        "note": "這是一個八階段反思模板，不是天文月相計算器，也不做運勢預測。",
        "disclaimer": DISCLAIMER,
    }
