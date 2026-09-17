from __future__ import annotations

import argparse
import json

from .crystals import build_ritual, reflection_card, recommend_crystals
from .dreams import dream_reflection
from .engine import CheckIn, load_practices, recommend, summarize
from .journal import generate_prompts
from .meditation import meditation_session, recommend_meditations
from .moon import moon_cycle, moon_reflection
from .safety import needs_safety_redirect, safety_message


def _print(data) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_checkin(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.note):
        print(safety_message())
        return
    checkin = CheckIn(args.mind, args.body, args.spirit, args.note)
    _print({"summary": summarize(checkin), "recommendations": [r.to_dict() for r in recommend(checkin)]})


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
    _print([item.to_dict() for item in recommend_crystals(args.theme, args.limit)])


def cmd_crystal_card(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(reflection_card(args.theme, args.crystal))


def cmd_ritual(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(build_ritual(args.theme, args.minutes, args.crystal))


def cmd_moon(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(moon_reflection(args.phase, args.theme))


def cmd_moon_cycle(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(moon_cycle(args.theme))


def cmd_dream(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.text):
        print(safety_message())
        return
    _print(dream_reflection(args.text, args.limit))


def cmd_meditations(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(recommend_meditations(args.theme, args.minutes, args.limit))


def cmd_meditate(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.theme):
        print(safety_message())
        return
    _print(meditation_session(args.theme, args.minutes, args.practice))


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
    card.add_argument("--crystal", default=None)
    card.set_defaults(func=cmd_crystal_card)

    ritual = sub.add_parser("ritual", help="產生 5–30 分鐘的象徵式自我反思流程")
    ritual.add_argument("--theme", required=True)
    ritual.add_argument("--minutes", type=int, default=10)
    ritual.add_argument("--crystal", default=None)
    ritual.set_defaults(func=cmd_ritual)

    moon = sub.add_parser("moon", help="以指定月相做象徵式反思")
    moon.add_argument("--phase", required=True, help="例如 新月、滿月、full_moon")
    moon.add_argument("--theme", default="")
    moon.set_defaults(func=cmd_moon)

    cycle = sub.add_parser("moon-cycle", help="建立八階段月相反思模板")
    cycle.add_argument("--theme", default="")
    cycle.set_defaults(func=cmd_moon_cycle)

    dream = sub.add_parser("dream", help="整理夢境主題與反思問題")
    dream.add_argument("--text", required=True)
    dream.add_argument("--limit", type=int, default=5)
    dream.set_defaults(func=cmd_dream)

    meditations = sub.add_parser("meditations", help="依主題推薦一般性冥想練習")
    meditations.add_argument("--theme", default="")
    meditations.add_argument("--minutes", type=int, default=10)
    meditations.add_argument("--limit", type=int, default=3)
    meditations.set_defaults(func=cmd_meditations)

    meditate = sub.add_parser("meditate", help="建立一段低風險冥想流程")
    meditate.add_argument("--theme", default="")
    meditate.add_argument("--minutes", type=int, default=10)
    meditate.add_argument("--practice", default=None)
    meditate.set_defaults(func=cmd_meditate)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
