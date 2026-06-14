#!/usr/bin/env python3
"""Convert all content markdown scripts to MP3 using OpenRouter TTS."""

import os
import re
import sys
from pathlib import Path
from openai import OpenAI

# --- Configuration ---
MODEL = "x-ai/grok-voice-tts-1.0"
VOICE = "Ara"  # Grok voices: Eve, Ara, Rex, Sal, Leo
OUTPUT_FORMAT = "mp3"
# ---------------------

CONTENT_DIR = Path(__file__).parent / "content"
AUDIO_DIR = Path(__file__).parent / "audio"

api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    print("Error: OPENROUTER_API_KEY environment variable not set.")
    sys.exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def clean_markdown(text: str) -> str:
    # Remove Sources section and everything after
    text = re.sub(r'\n## Sources\b.*', '', text, flags=re.DOTALL)
    # Remove markdown headings
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Remove blockquote lines (metadata line)
    text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    # Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def convert(md_path: Path):
    relative = md_path.relative_to(CONTENT_DIR)
    out_path = AUDIO_DIR / relative.parent / (md_path.stem + ".mp3")

    if out_path.exists():
        print(f"Skipping (exists): {relative}")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)

    text = clean_markdown(md_path.read_text())
    print(f"Converting: {relative} ({len(text):,} chars) ...", end=" ", flush=True)

    response = client.audio.speech.create(
        model=MODEL,
        input=text,
        voice=VOICE,
        response_format=OUTPUT_FORMAT,
    )
    response.stream_to_file(out_path)
    print(f"-> {out_path.relative_to(Path(__file__).parent)}")


md_files = sorted(CONTENT_DIR.rglob("*.md"))
print(f"Found {len(md_files)} scripts. Model: {MODEL}, Voice: {VOICE}\n")

for md in md_files:
    try:
        convert(md)
    except Exception as e:
        print(f"ERROR on {md.name}: {e}")

print("\nDone.")
