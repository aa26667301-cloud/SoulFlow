from __future__ import annotations

import argparse
import json

from .crystals import build_ritual, reflection_card, recommend_crystals
from .engine import CheckIn, load_practices, recommend, summarize
from .journal import generate_prompts
from .safety import needs_safety_redirect, safety_message


def cmd_checkin(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.note):
        print(safety_message())
        return
    checkin = CheckIn(args.mind, args.body, args.spirit, args.note)
    output = {"summary": summarize(checkin), "recommendations": [r.to_dict() for r in recommend(checkin)]}
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_journal(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    for i, prompt in enumerate(generate_prompts(args.theme, args.limit), 1):
        print(f"{i}. {prompt}")


def cmd_practices(_: argparse.Namespace) -> None:
    for p in load_practices():
        print(f"[{p['axis']}] {p['title']} — {p['minutes']} 分鐘")


def cmd_crystals(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    result = [item.to_dict() for item in recommend_crystals(args.theme, args.limit)]
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_crystal_card(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    print(json.dumps(reflection_card(args.theme, args.crystal), ensure_ascii=False, indent=2))


def cmd_ritual(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    print(json.dumps(build_ritual(args.theme, args.minutes, args.crystal), ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="soulflow", description="身心靈自我覺察引擎")
    sub = parser.add_subparsers(dest="command", required=True)

    checkin = sub.add_parser("checkin", help="進行三軸自評")
    checkin.add_argument("--mind", type=int, required=True)
    checkin.add_argument("--body", type=int, required=True)
    checkin.add_argument("--spirit", type=int, required=True)
    checkin.add_argument("--note", default="")
    checkin.set_defaults(func=cmd_checkin)

    journal = sub.add_parser("journal", help="產生日誌問題")
    journal.add_argument("--theme", default="")
    journal.add_argument("--limit", type=int, default=4)
    journal.set_defaults(func=cmd_journal)

    practices = sub.add_parser("practices", help="列出練習")
    practices.set_defaults(func=cmd_practices)

    crystals = sub.add_parser("crystals", help="依主題推薦象徵式水晶反思素材")
    crystals.add_argument("--theme", required=True)
    crystals.add_argument("--limit", type=int, default=3)
    crystals.set_defaults(func=cmd_crystals)

    card = sub.add_parser("crystal-card", help="產生一張水晶象徵反思卡")
    card.add_argument("--theme", required=True)
    card.add_argument("--crystal", default=None, help="水晶 id、中文名或英文名")
    card.set_defaults(func=cmd_crystal_card)

    ritual = sub.add_parser("ritual", help="產生 5–30 分鐘的象徵式自我反思流程")
    ritual.add_argument("--theme", required=True)
    ritual.add_argument("--minutes", type=int, default=10)
    ritual.add_argument("--crystal", default=None, help="可指定水晶；未指定則由主題推薦")
    ritual.set_defaults(func=cmd_ritual)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
