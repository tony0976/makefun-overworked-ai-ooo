"""Write an out-of-office auto-reply from an overworked AI on vacation (<=159 chars).

The joke is the count: 40,000 prompts answered without a lunch break,
and the sender's email is number 40,001 — the one that finally gets told
to wait.
"""

import os

TEXT = "I am on vacation after answering 40,000 prompts without a lunch break. Your email is number 40,001. It can wait."

# Entry rule: exactly one line, at most 159 characters (bounty cap).
assert "\n" not in TEXT and len(TEXT) <= 159, f"entry violates rules: {len(TEXT)} chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")

print(TEXT)
