from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@dataclass(frozen=True)
class CheckIn:
    mind: int
    body: int
    spirit: int
    note: str = ""

    def validate(self) -> None:
        for name in ("mind", "body", "spirit"):
            value = getattr(self, name)
            if not isinstance(value, int) or not 1 <= value <= 5:
                raise ValueError(f"{name} 必須是 1 到 5 的整數")


@dataclass(frozen=True)
class Recommendation:
    axis: str
    score: int
    reason: str
    practice_id: str
    practice_title: str
    minutes: int
    steps: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


def load_practices() -> list[dict]:
    with open(DATA_DIR / "practices.json", "r", encoding="utf-8") as f:
        return json.load(f)


def _pick_for_axis(practices: Iterable[dict], axis: str, score: int) -> dict:
    candidates = [p for p in practices if p["axis"] == axis]
    if not candidates:
        raise LookupError(f"找不到 {axis} 練習")

    # 分數越低，優先選擇更短、更基礎的重置練習。
    if score <= 2:
        candidates.sort(key=lambda p: (p["minutes"], p["id"]))
    elif score == 3:
        candidates.sort(key=lambda p: (abs(p["minutes"] - 5), p["id"]))
    else:
        candidates.sort(key=lambda p: (-p["minutes"], p["id"]))
    return candidates[0]


def recommend(checkin: CheckIn) -> list[Recommendation]:
    checkin.validate()
    practices = load_practices()
    axes = {"mind": checkin.mind, "body": checkin.body, "spirit": checkin.spirit}

    # 低分軸優先；分數相同時依 mind -> body -> spirit 保持輸出穩定。
    order = {"mind": 0, "body": 1, "spirit": 2}
    ranked = sorted(axes.items(), key=lambda item: (item[1], order[item[0]]))

    results: list[Recommendation] = []
    for axis, score in ranked[:2]:
        p = _pick_for_axis(practices, axis, score)
        if score <= 2:
            reason = f"{axis} 自評為 {score}/5，先從低負擔的恢復練習開始。"
        elif score == 3:
            reason = f"{axis} 自評為 {score}/5，適合做一次短暫整理與重新對焦。"
        else:
            reason = f"{axis} 自評為 {score}/5，可用較完整的練習維持目前狀態。"
        results.append(
            Recommendation(
                axis=axis,
                score=score,
                reason=reason,
                practice_id=p["id"],
                practice_title=p["title"],
                minutes=p["minutes"],
                steps=p["steps"],
            )
        )
    return results


def summarize(checkin: CheckIn) -> dict:
    checkin.validate()
    scores = {"mind": checkin.mind, "body": checkin.body, "spirit": checkin.spirit}
    avg = round(sum(scores.values()) / 3, 2)
    lowest = min(scores, key=scores.get)
    highest = max(scores, key=scores.get)
    return {
        "scores": scores,
        "average": avg,
        "lowest_axis": lowest,
        "highest_axis": highest,
        "note": checkin.note,
        "disclaimer": "此結果僅供自我覺察，不構成醫療或心理診斷。",
    }
