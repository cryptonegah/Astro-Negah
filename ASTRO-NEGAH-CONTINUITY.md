# Astro Negah — Project Continuity

## Project

- Name: Astro Negah
- Local path: `C:\Users\ASUS\Astro-Negah`
- GitHub: `https://github.com/cryptonegah/Astro-Negah.git`
- Main branch: `main`
- Current validated engine commit: `cd45fb1`
- Goal: Build a real, expandable global astrology platform, initially with Persian content/UI.
- Principle: No paid services, paid APIs, or subscriptions if a reliable free/open-source/local alternative exists.

## Working Style

- Work one step at a time.
- Give only one command/action per step.
- Wait for the user's output before continuing.
- Prefer simple, practical, testable solutions.
- Before changing any existing file, inspect its current state first.
- Do not change the Astro Negah website while the calculation engine is being validated.
- When editing code, prefer complete file replacement when practical.

## Current Website State

- Astro project is installed and runs locally.
- Development server has previously worked at `http://localhost:4321/`.
- Homepage has a dark navy/purple visual direction.
- Main headline direction: "Your Story Is Written In The Stars".
- Zodiac section contains the 12 signs.
- Custom SVG zodiac symbols are being used instead of the old Unicode zodiac symbols.
- `public\zodiac\aries.svg` exists.
- Homepage feature areas include Birth Chart, Daily Horoscope, and Zodiac Signs.
- Website files were intentionally kept unchanged during calculation-engine validation.

## Astrology Calculation Engine

### Status

The independent Birth Chart calculation engine has now been implemented and validated.

### Engine

- Python: `3.11.9`
- Swiss Ephemeris Python package: `pyswisseph 2.10.3.2`
- Swiss Ephemeris version: `2.10.03`
- Zodiac: Tropical
- House system: Placidus
- Placidus code: `P`
- Timezone conversion: Python `zoneinfo`
- Timezone data: `tzdata`

### Main Engine File

`birth_chart.py`

It currently provides:

- Local birth time → UTC conversion
- Julian Day calculation
- Swiss Ephemeris planetary positions
- Placidus house cusps
- Ascendant
- Midheaven (MC)
- Zodiac sign / degree / minute / second formatting
- Planetary house placement
- Retrograde detection
- Major aspects:
  - Conjunction
  - Sextile
  - Square
  - Trine
  - Opposition
- Aspect orb calculation

### Validation Test

Test file:

`test_birth_chart.py`

The automatic validation currently checks:

- Ascendant sign and degree
- MC sign and degree
- Houses for all 10 planets
- Sun–Saturn Sextile
- Sun–Saturn orb precision
- Tehran timezone conversion
- New York DST conversion
- Mercury retrograde detection

Current result:

`Birth Chart Validation: PASSED`

### Reference Sample

A Swiss Ephemeris sample for:

- Date: 2000-01-01
- Time: 12:00 UTC
- Location: Tehran

was used during validation.

The validated Ascendant is approximately:

`Gemini 20.52°`

The previous manual Ascendant formula that produced approximately Sagittarius 20.52° was rejected and is not used.

Swiss Ephemeris is the authoritative calculation engine for Astro Negah.

## Git Status

Validated engine commit:

`cd45fb1 Add validated Swiss Ephemeris birth chart engine`

Files included in that commit:

- `birth_chart.py`
- `test_birth_chart.py`

Website files were not modified by this commit.

At the last checkpoint, the only untracked file was:

`ASTRO-NEGAH-CONTINUITY.md`

This continuity file is intentionally being updated separately.

## Important Project Rules

- Do not replace Swiss Ephemeris with manual astronomical formulas for the production Birth Chart engine.
- Do not integrate the calculation engine into the website until the current validation checkpoint is explicitly accepted.
- Do not modify existing website files unnecessarily.
- Keep the implementation simple and local where possible.
- Avoid paid APIs and services when a reliable free/local alternative exists.

## Current Exact Checkpoint

Completed:

1. Python 3.11 environment confirmed.
2. Swiss Ephemeris installed successfully.
3. `birth_chart.py` implemented.
4. `test_birth_chart.py` implemented.
5. Automatic validation passed.
6. Website accidental modification was detected and restored.
7. `birth_chart.py` and `test_birth_chart.py` committed as:
   `cd45fb1`
8. Git status confirmed no modified website files.

Current state:

- Calculation engine: VALIDATED
- Automatic test: PASSED
- Website integration: NOT STARTED
- Main website files: PROTECTED / UNCHANGED

## Next Planned Phase

The next phase is to decide how the validated calculation engine should be connected to Astro Negah.

Before making any website changes:

1. Inspect the current Birth Chart page.
2. Decide the smallest integration path.
3. Preserve the existing website design.
4. Connect the validated engine without replacing its calculation logic.
5. Test the result locally.
6. Only then commit the integration.

## Resume Phrase

If a new chat is opened, start with:

"ادامه Astro Negah از فایل ASTRO-NEGAH-CONTINUITY.md"

Then review this checkpoint before giving the next command.