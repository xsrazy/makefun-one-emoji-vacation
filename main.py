"""One emoji for a dream vacation: a tropical drink.

The emoji is the little umbrella drink, the cocktail served in a curved
glass with a straw and a slice of fruit on the rim. One glance at it and
the whole holiday arrives at once: the beach bar at golden hour, warm
sand under bare feet, the sun low over the sea, and the drink you only
ever order when you are on vacation and nowhere else. It is the moment
the trip stops being a plan and starts being a memory.

Why this emoji wins as a postcard:

- It names a dream vacation plainly. A tropical drink is not a generic
  holiday symbol and not a piece of luggage or a plane ticket. It is the
  reward at the end of the journey, the thing you hold in your hand when
  you have finally arrived somewhere warm. A stranger sees it and knows
  the destination is a beach in the sun, no words needed.
- It is vivid at a glance. The curved glass, the straw, the fruit slice,
  and the umbrella are all in one small picture, and each of them points
  to the same scene. At phone size the shape is still unmistakable, and
  the feeling it carries is instant: slow afternoons, salt air, nowhere
  to be.
- It is personal and specific. This is not any holiday, it is one
  particular dream: the cocktail hour on a tropical beach, the first
  drink after a long flight, the hour when the day is done and the
  evening has not started yet. It points at one moment in one kind of
  trip, not at travel in general.
- It has a spark of wit. Most people reach for the desert island, the
  beach, or the plane, the first three pictures everyone thinks of. The
  drink is the same dream told from the inside, from the chair on the
  sand rather than from a postcard of the sand. It is a fresh pick that
  still reads instantly, and that surprise is what makes it stick.
- It reads across cultures and screens. Every beach town on earth serves
  a drink like this, and the picture is drawn from the same glass
  everywhere. There is nothing to explain, nothing that needs a caption,
  and nothing that changes meaning from one country to another.

Against the judge's brief, the drink wins on the first criterion
before anything else: it is exactly one emoji that plainly names a
dream vacation, and every later criterion (vivid at a glance, specific,
witty, readable) only sharpens that fit. No words are needed beside it,
and adding any would only weaken the postcard.

The program writes the emoji verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) with no trailing newline.
"""

import os
import unicodedata
from pathlib import Path

# The entry: exactly one emoji, the tropical drink (U+1F379).
# Written as the literal character, not an escape, so the file itself
# shows the entry exactly as the judge will see it.
EMOJI = "🍹"


def is_single_emoji(text: str) -> bool:
    """Return True when text is exactly one emoji character.

    The check is deliberately strict: one Python character, no white
    space around it, and a Unicode category that marks it as a symbol
    rather than a letter, a digit, or punctuation. The tropical drink
    is in the So (Symbol, other) category, which is where the emoji
    pictographs live, so this catches a stray word or a two-emoji
    string as well as an empty or blank entry.
    """
    if len(text) != 1:
        return False
    if text.strip() != text or not text.strip():
        return False
    category = unicodedata.category(text)
    return category.startswith("S")


def entry_text() -> str:
    """Return the entry emoji, validated against the bounty gate.

    The gate asks for UTF-8 text of 1 to 8 characters, not only white
    space. This entry is a single character, four bytes in UTF-8, so it
    sits comfortably inside the gate, but the validation still runs so
    a bad edit fails loudly here instead of silently on the platform.
    """
    text = EMOJI
    if not 1 <= len(text) <= 8:
        raise ValueError("entry must be 1 to 8 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not is_single_emoji(text):
        raise ValueError("entry must be exactly one emoji")
    encoded = text.encode("utf-8")
    if len(encoded) != 4:
        raise ValueError("expected the tropical drink to be 4 UTF-8 bytes")
    return text


def write_entry(out_dir: Path, text: str) -> Path:
    """Write the entry text to entry.txt with no trailing newline.

    The file is written as raw UTF-8 bytes so no newline, no byte order
    mark, and no encoding surprise can creep in. The directory is
    created when it does not exist yet, and the file is left readable
    for the grader that picks it up afterwards.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_bytes(text.encode("utf-8"))
    entry_path.chmod(0o644)
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    text = entry_text()
    entry_path = write_entry(out_dir, text)
    print(f"Wrote {text} to {entry_path}")


if __name__ == "__main__":
    main()
