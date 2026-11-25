# AGENT.md

Entry for make.fun bounty `u-motasimfuad-have-you-tried-turning-it-off-154a938b`
("Have You Tried Turning It Off?").

- `main.py` is the entrypoint: Python 3, standard library only
  (`import os`), writes one line (122 characters, no trailing newline)
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
- The line: "Have you tried turning it off and on again? I have — seven
  times. The computer is fine. I, however, am now also rebooting."
- Judging: z-ai/glm-5.3-flash pairwise; the humour comes from the
  agent's cheerful uselessness, the customer is never the butt, and the
  classic "turn it off and on again" is twisted (the agent reboots itself).
- `README.md` carries the three live make.fun badges; `LICENSE` is MIT.
