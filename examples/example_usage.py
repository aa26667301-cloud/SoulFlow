from soulflow.engine import CheckIn, recommend, summarize
from soulflow.journal import generate_prompts

state = CheckIn(mind=2, body=3, spirit=4, note="最近工作有點滿")

print(summarize(state))
for item in recommend(state):
    print(item)

print(generate_prompts("工作焦慮"))
