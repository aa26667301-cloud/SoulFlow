from __future__ import annotations

import argparse
import json

from .engine import CheckIn, load_practices, recommend, summarize
from .journal import generate_prompts
from .safety import needs_safety_redirect, safety_message


def cmd_checkin(args: argparse.Namespace) -> None:
    if needs_safety_redirect(args.note):
        print(safety_message())
        return
    checkin = CheckIn(args.mind, args.body, args.spirit, args.note)
    output = {
        "summary": summarize(checkin),
        "recommendations": [r.to_dict() for r in recommend(checkin)],
    }
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
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
