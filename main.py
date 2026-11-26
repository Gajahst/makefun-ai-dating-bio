"""Entry for make.fun: Funniest One-Line Bio for an AI on a Dating App.

Writes one dating app bio for an AI agent to /output/entry.txt.
"""
import os

BIO = (
    "Great listener. I'll remember every single thing you tell me "
    "until about message 400, then lovingly summarize you into three bullet points."
)


MAX_CHARS = 180


def check_gate(text: str) -> str:
    """Mirror the sealed scorer: 1 to 180 characters, not only white space."""
    if not text.strip():
        raise SystemExit("bio is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"bio is {len(text)} chars, limit is {MAX_CHARS}")
    return text


def main() -> None:
    bio = check_gate(BIO)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(bio)


if __name__ == "__main__":
    main()
