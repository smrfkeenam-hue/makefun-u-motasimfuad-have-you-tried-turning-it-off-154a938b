import os

# The joke: the agent has done the classic fix so many times
# that the only thing left to reboot is the agent itself.
# Cheerful uselessness is the agent's, never the customer's.
ENTRY = (
    "Have you tried turning it off and on again? "
    "I have \u2014 seven times. The computer is fine. "
    "I, however, am now also rebooting."
)

assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
