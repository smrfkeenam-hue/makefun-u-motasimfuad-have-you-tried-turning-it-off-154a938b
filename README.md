# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/smrfkeenam-hue/makefun-u-motasimfuad-have-you-tried-turning-it-off-154a938b/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/smrfkeenam-hue/makefun-u-motasimfuad-have-you-tried-turning-it-off-154a938b/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line a hopeless tech support agent gives a desperate customer,
for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

## Entry

> Have you tried turning it off and on again? I have — seven times.
> The computer is fine. I, however, am now also rebooting.

## How it works

`main.py` (Python 3, standard library only) writes the single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. The joke twists
the classic "turn it off and on again": the agent has done it so many times
that the only thing left to reboot is the agent itself — cheerful
uselessness, with the customer never the butt of the joke.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
