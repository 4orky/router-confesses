# The Router Confesses — make.fun bounty
# u-carbon-forge-the-router-confesses-f98f6b9e
#
# The program writes one excuse (1-200 characters) to
# /output/entry.txt: what a home Wi-Fi router says to excuse itself
# for dropping the connection at the exact climax of a movie.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a one-line excuse from a home Wi-Fi router for dropping the
#      connection at a movie's climax, and nothing else
#   2. the funniest: the biggest laugh, with a turn the reader does
#      not see coming
#   3. the router's own voice: an appliance with a grudge, a fragile
#      ego or a smug little secret, not a generic apology
#   4. lands in one breath: a single line that reads clean, no setup
#      that needs explaining
#   5. feels new: dodges the obvious buffering, bandwidth and
#      firmware-update jokes everyone has already heard
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: topic 10, funny 7, voice 8, breath 8, fresh 7 = 40
    ("I didn't drop the connection. I fainted. The twist was that "
     "good, and unlike you, I had no one to hold my hand.",
     40),
    # score: topic 10, funny 7, voice 8, breath 9, fresh 7 = 41
    ("You think I dropped out? I was watching too, and when the "
     "killer was revealed, I needed a minute. We all did.",
     41),
    # score: topic 10, funny 8, voice 8, breath 9, fresh 8 = 43
    ("I cut the Wi-Fi on purpose. The hero was about to confess his "
     "love, and I refuse to third-wheel your movie nights.",
     43),
    # score: topic 10, funny 9, voice 9, breath 9, fresh 9 = 46
    ("Blame the script. The hero loses signal in act three, and I am "
     "nothing if not a method actor.",
     46),
    # score: topic 10, funny 8, voice 9, breath 9, fresh 8 = 44
    ("I didn't die. I took a bow. Every great performance ends at the "
     "climax, and mine was flawless.",
     44),
    # score: topic 10, funny 7, voice 8, breath 8, fresh 7 = 40
    ("I dropped the connection because the movie did first — the "
     "villain cut the power, and I will not be outdone by an amateur.",
     40),
    # score: topic 10, funny 9, voice 9, breath 8, fresh 9 = 45
    ("I am not apologising. You ignored me for two hours, then blamed "
     "me the second the film got good. That is the whole relationship.",
     45),
    # score: topic 10, funny 7, voice 8, breath 9, fresh 7 = 41
    ("I paused it for you. The jump scare was coming and, unlike the "
     "film, I actually care about your heart.",
     41),
    # score: topic 10, funny 8, voice 9, breath 9, fresh 9 = 45
    ("The climax was too much for me as well. I have streamed that "
     "scene four hundred times, and I still wasn't ready.",
     45),
    # score: topic 10, funny 9, voice 9, breath 10, fresh 9 = 47
    # Revised second pass: "A flat ending is forgettable" tightened to
    # "Flat endings are forgettable" — one word shorter, and the plural
    # now runs parallel to "a cliffhanger ... is art", so the middle
    # clause lands harder and the smug "You're welcome." closes it.
    ("I didn't crash, I chose drama. Flat endings are forgettable; a "
     "cliffhanger at the climax is art. You're welcome.",
     47),
    # score: topic 10, funny 9, voice 9, breath 8, fresh 9 = 45
    ("I dropped out at the climax because that is when you finally "
     "look at me. Two hours of film, and I only exist to you when I "
     "stop working.",
     45),
    # score: topic 10, funny 7, voice 8, breath 9, fresh 8 = 42
    ("Don't look at me. The movie killed its hero in act three, and I "
     "was next in the script.",
     42),
    # score: topic 10, funny 8, voice 9, breath 9, fresh 8 = 44
    ("I gave you a cliffhanger of your own, free of charge. The film's "
     "ending can wait; mine is already iconic.",
     44),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text, and
# the judge rewards freshness: no buffering / bandwidth / firmware jokes.
BANNED_CLICHES = ("buffering", "bandwidth", "firmware", "reboot",
                   "as an ai")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    import os
    import sys
    message = pick(CANDIDATES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(message)
    # Verify: read the output back byte-for-byte and re-check the gate,
    # so a partial write or an encoding slip fails loudly instead of
    # silently submitting a broken entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != message:
        print("error: /output/entry.txt does not match the selected message",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(message) <= 200) or "\n" in message or not message.strip():
        print("error: selected message fails the gate (1-200 chars, one line)",
              file=sys.stderr)
        sys.exit(1)
    print(message)


if __name__ == "__main__":
    main()
