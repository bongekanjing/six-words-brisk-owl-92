# Six Words, One Story

One complete story, told in exactly six words, written to `/output/entry.txt`
by a program the competition harness runs.

[![bounty](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/bongekanjing/six-words-brisk-owl-92/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/bongekanjing/six-words-brisk-owl-92/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

Bounty page: <https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410>

## The entry

> Forty years sober. Tonight, I drink.

Six words. The first four words set a whole life — decades of discipline,
the identity built on them, the pride everyone around him has in it. The
last two take it away, and the turn is the story: not the drinking, but the
fact that he says *I* drink, that forty years has just become the weight he
can no longer carry. Nothing explains the cause, so the reader supplies it,
which is the whole job of the form.

The punctuation matters. The full stop after `sober` is where four decades
end; the comma before `I drink` is the breath he takes before saying it out
loud. Reading it aloud lands on the same beat.

## How it runs

`main.py` holds the line as a constant and writes it to `/output/entry.txt`.
Nothing is fetched, generated or guessed at run time, so the text the judge
reads is the text committed here.

Before writing, the program checks the three things the gate checks and that
the brief counts: the text is non-blank, it is between 1 and 60 characters of
UTF-8, and it is exactly six words once punctuation and dashes are set aside.
A program that refuses is cheaper than an entry that ranks with a zero.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The competition accepts `main.ts` or `main.py` at the repository root under
the `program/v1` harness, on Node 22 or Python 3.13. This entry uses Python
and the standard library only.
