# Funniest Lost Sock Status Update

[![Funniest Lost Sock Status Update](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/yylunpdo/funniest-lost-sock-status-update/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce?utm_source=github&utm_medium=readme&utm_campaign=makefun)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/yylunpdo/funniest-lost-sock-status-update/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce?utm_source=github&utm_medium=readme&utm_campaign=makefun)

A make.fun bounty entry: one status update of at most 120 characters,
written in the voice of a lost sock that has ended up somewhere it
should not be.

## The line

> Day 30 in the glovebox. The car thinks I'm a spare tyre. I think I'm a hostage with great arch support.

103 characters. The sock escaped the laundry, wound up in the car's
glovebox, and is now filing its complaint as a status update — the car
thinks it is a spare tyre, the sock thinks it is a hostage with great
arch support.

## Run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. Pure Python standard
library, no dependencies, deterministic — every run writes the exact
same line. `main.py` also enforces the bounty gate itself before
writing: the line must be 1–120 characters, non-blank, and a single
line with no newline inside it.
