[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rsuryatna/Tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rsuryatna/Tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

# tiny-chess

A chess engine in under 4 KB of Python. It plays the make.fun tiny-chess-01
gauntlet: eight games per trial against the house engines, talking to the
environment over HTTP.

The whole engine lives in `main.py` (Python 3 standard library only). It
generates its own moves on a 0x88 board — castling, en passant and promotions
included — and searches with alpha-beta plus iterative deepening to a fixed
node budget, so every move is deterministic: the same position always gives
the same move. Quiescence search follows captures, promotions and checks.
Move ordering is MVV-LVA. The evaluation is material plus piece-square
tables for pawns, knights, rooks and kings (tapered in the endgame).

## Run it

Point it at an environment and let it play:

```sh
MAKEFUN_ENV_URL=http://localhost:3000 python3 main.py
```

It fetches each game, answers every move in UCI notation, and exits when the
environment reports the trial is done.

<sub>Entered on [make.fun](https://make.fun/?ref=hn2e4a6b&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
