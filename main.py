"""Six-word story: a man comes home, but the house has forgotten him.

A quiet homecoming in reverse: he returns, yet the place he once belonged
to no longer recognizes him at all."""

import os

STORY = "He returned. The house remembered nobody."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
