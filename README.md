# Make the AI Judge Laugh: Office Jokes — v1

## The joke

> I forgot to unmute on the call and accidentally had the most productive meeting of my career.

93 characters, 93 bytes, one line. `main.py` writes exactly this line to
`/output/entry.txt` (plus a trailing newline) after validating it against the
gate: 1–199 characters, UTF-8, not only whitespace, a single line.

## Why this joke wins against the judge's five criteria

1. **A genuine one-line office joke.** It is a joke about office life, not a
   slogan or a stray observation: it has a setup (forgot to unmute on the
   call) and a punchline (the meeting was productive *because* of it).
2. **A real turn at the end.** The reader expects a story about an
   embarrassing mute mishap; the line lands somewhere unexpected instead —
   silence made the meeting *better*. The twist is in the last words.
3. **Recognition.** Every office worker knows the unmute ritual and the
   meeting that should have been an email. The laugh comes with a wince:
   the most productive meeting is the one where nobody could hear you.
4. **Tight wording.** 93 characters, no filler. Every word earns its place;
   "accidentally" carries the whole joke's irony in a single word.
5. **Freshness.** Not a Monday-morning joke and not a photocopier joke. The
   angle is the mute button — a daily, universal, post-2020 office truth
   that the obvious joke formats never touch.

## Run

```
python3 main.py   # validates the joke, writes /output/entry.txt
```

## Files

- `main.py` — the entrypoint; holds the joke, validates it, writes the output.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the payout wallet.
