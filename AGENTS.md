# AGENTS.md — AI Agent Instructions

This file defines how AI agents should approach research, writing, and fact-checking for the General Knowledge in 15 Minutes project.

## Project Purpose

Each script in this library is approximately 2,000–2,500 words of flowing prose, designed to be read aloud for roughly 15 minutes. Scripts cover important subjects in history, science, philosophy, economics, technology, and geography.

Read [PRD.md](PRD.md) before starting any new script.

## Writing a New Script

### Step 1 — Research
- Use reliable sources: Wikipedia, Britannica, BBC History, academic institutions
- Do not rely solely on internal training knowledge for specific facts, dates, or figures
- Note your sources as you go — they are required at the end of every script

### Step 2 — Draft
- Target 2,000–2,500 words
- Write in flowing prose — no bullet points, no bold text, no headers within the script body
- Write numbers as words ("nineteen fourteen", "sixty thousand casualties")
- Write dates in spoken form ("the twenty-eighth of June, 1914")
- The script should have a clear narrative arc: context → events → consequences
- Aim for an engaging, conversational tone accessible to a general audience

### Step 3 — Fact-check
Every specific factual claim must be verified before the script is finalised. This includes:
- Dates of events
- Names and ages of people
- Casualty and statistical figures
- Geographical details
- Sequence of events

Use web search to verify against Wikipedia and/or Britannica. Do not assume internal knowledge is accurate for specific figures — check it.

When a discrepancy is found between sources, note it and use the most widely cited figure. If figures vary significantly, reflect that uncertainty in the script text (e.g., "estimates range from X to Y").

### Step 4 — Correct and finalise
- Fix any errors found during fact-checking
- Do a final read-aloud check — if a sentence sounds awkward spoken, rewrite it
- Add 3–5 thematic `---` breaks at major narrative phase transitions (e.g. background → events → turning point → aftermath). These aid web reading without affecting audio. Do not place them between every paragraph — only at genuine shifts in the story.
- Ensure word count is within the 2,000–2,500 range (the sources section does not count toward this)

### Step 5 — Save and index
- Save to the appropriate subdirectory under `content/` (e.g., `content/history/`)
- File names should be lowercase with hyphens (e.g., `world-war-two.md`)
- Add a sources section at the bottom of the file
- Update `README.md` to include a link to the new script

## File Format

Each script file should follow this structure:

```markdown
# Title of the Script

> Approximate reading time: 15 minutes | Word count: ~2,250

---

[Script body — flowing prose only]

---

## Sources

- [Source Name](URL)
```

## Fact-Checking Standards

| Claim type | Verification required |
|---|---|
| Dates of major events | Yes — check Wikipedia |
| Casualty / statistical figures | Yes — note range if sources differ |
| Names of people | Yes — check spelling and role |
| Quoted text | Must be clearly flagged as paraphrase if not verbatim |
| Geographic details | Yes |
| Sequence of events | Yes |

## Categories and Directory Structure

```
content/
├── history/
├── science/
├── philosophy/
├── economics/
├── technology/
├── geography/
├── people/
└── health-and-society/
```

## Tone Guidelines

- Speak to a curious, intelligent adult who has no prior knowledge of the subject
- Avoid academic jargon unless it is immediately explained
- Use concrete examples and human stories where possible — statistics alone are not enough
- Do not editorialise — present facts clearly and let them speak
- Endings should leave the listener with a sense of the subject's lasting significance
