#!/usr/bin/env bash
set -euo pipefail

CONTENT_DIR="$(dirname "$0")/content"
AUDIO_DIR="$(dirname "$0")/audio"

mkdir -p "$AUDIO_DIR"

find "$CONTENT_DIR" -name "*.md" | sort | while read -r md_file; do
  # Mirror the category subdirectory structure under audio/
  relative="${md_file#$CONTENT_DIR/}"
  category="$(dirname "$relative")"
  basename="$(basename "$relative" .md)"

  out_dir="$AUDIO_DIR/$category"
  mkdir -p "$out_dir"

  out_file="$out_dir/$basename.m4a"

  if [[ -f "$out_file" ]]; then
    echo "Skipping (already exists): $relative"
    continue
  fi

  echo "Converting: $relative"

  # Strip markdown before passing to say:
  #   - Stop at ## Sources
  #   - Remove headings, blockquotes, horizontal rules
  cleaned="$(sed '/^## Sources/,$d' "$md_file" \
    | sed -E 's/^#+[[:space:]]*//' \
    | sed '/^>[[:space:]]*/d' \
    | sed '/^---$/d')"

  say -v Samantha \
      --data-format=aac \
      -o "$out_file" \
      "$cleaned"

  echo "  -> $out_file"
done

echo "Done."
