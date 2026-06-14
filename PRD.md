# Product Requirements Document

## Project: General Knowledge in 15 Minutes

### Overview

A curated library of spoken-word scripts covering important subjects across history, science, philosophy, economics, and more. Each script is designed to be converted to audio and deliver a solid foundational understanding of a topic in approximately 15 minutes.

### Goals

- Produce high-quality, accurate scripts that work as standalone audio pieces
- Cover a broad range of important subjects over time
- Ensure every factual claim is verified against reliable sources before publication
- Write in a style that is engaging and accessible to a general audience

### Target Audience

Anyone who wants to learn about important topics efficiently — commuters, people who prefer audio learning, or anyone curious about the world.

### Content Specifications

| Property | Requirement |
|---|---|
| Word count | 2,000 – 2,500 words per script |
| Reading time | Approximately 15 minutes at 150 words per minute |
| Tone | Conversational, engaging, clear — no jargon |
| Format | Flowing prose only — no bullet points, headers mid-text, or markdown inside the script body |
| Fact-checking | All factual claims verified against Wikipedia and/or Britannica before publishing |
| Sources | All scripts must include a sources section at the bottom |

### Content Categories

Scripts should be organized into subdirectories under `content/` by category:

- `content/history/` — Wars, empires, revolutions, turning points
- `content/science/` — Physics, biology, astronomy, medicine
- `content/philosophy/` — Major thinkers, schools of thought, ethical questions
- `content/economics/` — Economic systems, financial crises, key theories
- `content/technology/` — Inventions, the internet, AI, major tech shifts
- `content/geography/` — Countries, regions, natural wonders
- `content/people/` — Biographies of significant historical figures
- `content/health-and-society/` — Pandemics, social movements, human rights

New categories can be added as needed.

### Scale Target

The library aims for approximately 100 subjects in total, covering a broad range of topics with good category balance. The full subject list is tracked in README.md.

### Quality Standards

1. **Accuracy** — Facts must be verifiable. Any claim that cannot be confirmed should be removed or qualified.
2. **Audio-readiness** — Read the script aloud before finalising. Numbers should be written as words. Dates should be spoken naturally ("the twenty-eighth of June" not "28/06").
3. **No unexplained jargon** — Any technical term introduced must be briefly explained in plain language.
4. **Narrative flow** — Scripts should tell a story, not recite facts. There should be a clear beginning, middle, and end.
5. **No markdown inside script body** — Headers, bold text, and bullet points break the listening experience. Reserve all markdown for metadata and the sources section.
6. **Thematic breaks** — Use `---` horizontal rules to mark major phase transitions within a script (3–5 per piece). These provide visual breathing points for web readers without interrupting the audio flow. Do not use them between every paragraph — only at genuine narrative shifts.

### Workflow for New Scripts

1. Choose a subject and research it using reliable sources
2. Draft the script at 2,000–2,500 words in flowing prose
3. Fact-check all specific claims (dates, figures, names, events) against Wikipedia and Britannica
4. Correct any errors found during fact-checking
5. Add a sources section at the bottom
6. Save to the appropriate `content/` subdirectory
7. Update `README.md` with a link to the new script

### Out of Scope

- Opinion pieces or editorials
- Scripts shorter than 1,800 words or longer than 2,800 words
- Topics that are primarily regional or niche interest
- Content that cannot be fact-checked against mainstream reliable sources
