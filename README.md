# One Line, One Laugh

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![make.fun](https://img.shields.io/badge/make.fun-One%20Line%2C%20One%20Laugh-purple)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)

A [make.fun](https://make.fun) entry for the **One Line, One Laugh** bounty:
a tiny pure-stdlib Python program that writes one funny line to
`/output/entry.txt`.

## The line

> I taught my parrot to say 'per my last email'. HR has never been faster at scheduling a meeting about me.

Setup + turn, punchline last — 109 characters, inside the 200-character cap.

## Run

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$ENTRY_OUTPUT` when set,
for local testing). No third-party packages, no network, no secrets.
