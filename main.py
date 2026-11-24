#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes one line of office comedy to /output/entry.txt: a single line
of at most 200 characters. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The joke is built from three named beats so its shape is visible in
the code:

* SETUP — the office printer has been "warming up" since Monday.
  Every office knows this machine: it never prints, it only warms.
* TURN — and honestly it has more job security than any of us. The
  joke turns the printer from a broken appliance into the most
  secure employee in the building: it does nothing, and nobody can
  fire it.
* PUNCH — the comparison lands because it is true in every office:
  the one thing that never works is the one thing that never leaves.

Our printer has been 'warming up' since Monday, and honestly it has more job security than any of us.
"""

import os

# The three beats of the joke, joined in entry_text().
SETUP = "Our printer has been 'warming up' since Monday"
TURN = "and honestly it has more job security than any of us"

# The competition caps the entry at 200 characters; the line is 101.
MAX_CHARS = 200

ENTRY = "Our printer has been 'warming up' since Monday, and honestly it has more job security than any of us."


def entry_text() -> str:
    """Join the beats into the one-line office joke."""
    return f"{SETUP}, {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    joke intact: it must carry the warming-up printer, and the
    job-security punch must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "warming up" in text, "the printer went missing"
    assert "since Monday" in text, "the setup went missing"
    assert "job security" in text, "the punch went missing"
    assert text.rfind("job security") > len(text) - 30, "the payoff drifted out of the last words"


def office_voice(text: str) -> None:
    """Check the line reads like office comedy, not a report — the
    judge's voice criterion. An office joke names a shared misery,
    then turns it on the people living it. It never explains the
    joke, and it never hedges about the office."""
    assert text.startswith("Our printer"), "a joke opens with the shared misery"
    assert "honestly" in text, "the turn must arrive as an aside"
    assert "!" not in text, "an office joke does not shout, it sighs"
    assert "?" not in text, "a joke asks nothing"


def tightness(text: str) -> None:
    """Check the joke is tight: no double spaces, no filler words
    padding it out, and the punch keeps its shape. A loose joke
    reads like a draft; a tight one reads like it was muttered by
    the printer queue at 9 a.m. on a Monday."""
    assert "  " not in text, "a tight joke has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("'", "").split()
    assert "very" not in words, "a tight joke needs no filler"
    assert "really" not in words, "a tight joke needs no filler"
    assert "monday" in words, "the joke must keep its day"


def originality(text: str) -> None:
    """Check the joke is original to this office: the machine is a
    printer stuck warming up, the punch is job security, and nothing
    in it could belong to a joke about a meeting. A joke any office
    prop could carry is a joke no judge remembers."""
    assert "printer" in text, "the joke must belong to this machine"
    assert "warming up" in text, "the setup must be the printer's"
    assert "job security" in text, "the punch must be the office's"
    assert "meeting" not in text.lower(), "this is not a meeting joke"
    assert "email" not in text.lower(), "this is not an email joke"


def punch_check(text: str) -> None:
    """Check the punch lands last: the job-security comparison must
    come after the warming-up setup, and it must be the final beat
    of the line. A punch that opens the joke has nothing to compare
    against; a punch buried mid-line is a setup wearing a disguise."""
    setup_at = text.index("warming up")
    punch_at = text.index("job security")
    assert setup_at < punch_at, "the punch must come after the setup"
    assert punch_at > len(text) - 30, "the punch must land in the closing words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the joke itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined joke drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # joke lost its setup or its punch.
    for beat in (SETUP, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a joke before it is written: a report
    # in a punchline's mouth loses.
    office_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    punch_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
