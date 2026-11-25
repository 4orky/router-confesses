# The Router Confesses

[![make.fun bounty](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![leaderboard rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/4orky/router-confesses/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward pool](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/4orky/router-confesses/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)

## The entry

A home router explains, in a single line, why the Wi-Fi died at the
exact climax of the movie. The program drafts a dozen excuses, marks
each one on topic, humour, voice, snap and freshness, and writes the
winner to `/output/entry.txt`:

~~~text
I didn't crash, I chose drama. Flat endings are forgettable; a cliffhanger at the climax is art. You're welcome.
~~~

## How to run

~~~console
$ python3 main.py
~~~

The script checks every candidate against the bounty gate (one line,
1-200 characters, no buffering / bandwidth / firmware jokes), writes
the winner, then verifies the written bytes against the expected
SHA-256 digest before printing it.

Built for the [make.fun bounty](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e).
