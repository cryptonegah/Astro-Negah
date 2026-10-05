# Astro Negah — Project Continuity

## Project

- Name: Astro Negah
- Local path: `C:\Users\ASUS\Astro-Negah`
- GitHub: `https://github.com/cryptonegah/Astro-Negah.git`
- Main branch: `main`
- Current local HEAD: `499f1bb`
- Remote `origin/main`: `f95646b`
- Local commits ahead of origin: 2
- Goal: Build a real, expandable global astrology platform, initially with Persian content/UI.
- Principle: No paid services, paid APIs, or subscriptions if a reliable free/open-source/local alternative exists.

## Working Style

- Work one step at a time.
- Give only one command/action per step.
- Wait for the user's output before continuing.
- Prefer simple, practical, testable solutions.
- Before changing any existing file, inspect its current state first.
- When editing code, prefer complete file replacement when practical.
- Preserve the existing Astro Negah visual design.

## Current Website State

- Astro project is installed and runs locally.
- Development server works at `http://localhost:4321/`.
- Homepage has a dark navy/purple visual direction.
- Main headline: `Your Story Is Written In The Stars`.
- Zodiac section contains the 12 signs.
- Custom SVG zodiac symbols are being used instead of the old Unicode zodiac symbols.
- `public\zodiac\aries.svg` exists.
- Homepage feature areas include Birth Chart, Daily Horoscope, and Zodiac Signs.
- Birth Chart page exists at `/birth-chart`.
- Birth Chart page is Persian and uses RTL layout.
- Persian rendering was verified in the browser.
- Website design should be preserved while functionality is expanded.

## Astrology Calculation Engine

### Status

The Birth Chart calculation engine has been implemented and validated.

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

It provides:

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

### Important Rule

Swiss Ephemeris is the authoritative calculation engine for Astro Negah.

Do not replace it with manual astronomical formulas.

Do not modify `birth_chart.py` unless a specific validated reason is established.

## Validation

### Test File

`test_birth_chart.py`

The automatic validation checks:

- Ascendant sign and degree
- MC sign and degree
- Houses for all 10 planets
- Sun-Saturn aspect
- Sun-Saturn orb precision
- Tehran timezone conversion
- New York DST conversion
- Mercury retrograde detection

Current result:

`Birth Chart Validation: PASSED`

### Reference Sample

- Date: `2000-01-01`
- Time: `12:00 UTC`
- Location: Tehran

Validated Ascendant:

`Gemini 20.52°`

The previous manual Ascendant calculation that produced approximately Sagittarius 20.52° was rejected and is not used.

## Birth Chart Integration

Birth Chart calculation has now been connected to the Astro Negah website.

### API

File:

`src/pages/api/birth-chart.js`

The API:

1. Receives birth date.
2. Receives birth time.
3. Receives timezone.
4. Receives latitude.
5. Receives longitude.
6. Calls `calculate_birth_chart_local(...)`.
7. Calls `build_cosmic_story(...)`.
8. Returns chart data and interpretation as JSON.

The API uses Python 3.11 and explicitly configures stdout as UTF-8 so Persian/Unicode interpretation output works correctly on Windows.

### API Validation

A real API request was tested successfully using:

- Birth date: `2000-01-01`
- Birth time: `15:30`
- Timezone: `Asia/Tehran`
- Latitude: `35.6892`
- Longitude: `51.3890`

Result:

`{"ok":true,...}`

The response contained:

- `chart`
- `interpretation`
- `personality_summary`
- `planets_and_houses`
- `aspects`
- `cosmic_story`

## Interpretation Engine

### File

`interpretation.py`

Current role:

- Converts validated chart data into structured interpretation sections.
- Formats zodiac positions correctly.
- Produces personality summary data.
- Produces planet/house data.
- Produces aspect data.
- Produces a `Your Cosmic Story` section.

Current output structure:

- `personality_summary`
- `planets_and_houses`
- `aspects`
- `cosmic_story`

The current interpretation layer is intentionally simple and structured.

A future phase can make the interpretation more detailed and user-friendly without changing the underlying astronomical calculations.

## Birth Chart UI

### File

`src/pages/birth-chart.astro`

Current status:

- Integrated with the Birth Chart API.
- Persianized.
- RTL layout enabled.
- Browser rendering verified.
- Existing visual design preserved.

The page is currently functional and connected to the calculation/interpretation pipeline.

## Git History

Important commits:

- `cd45fb1` — Add validated Swiss Ephemeris birth chart engine
- `f95646b` — Add birth chart interpretation and UI
- `9e01590` — Persianize birth chart page
- `499f1bb` — Fix interpretation output formatting

Current local HEAD:

`499f1bb`

Current remote:

`origin/main` → `f95646b`

Local branch is currently 2 commits ahead of `origin/main`.

Working tree was confirmed clean before updating this continuity document.

## Current Exact Checkpoint

Completed:

1. Python 3.11 environment confirmed.
2. Swiss Ephemeris installed successfully.
3. `birth_chart.py` implemented.
4. `test_birth_chart.py` implemented.
5. Automatic Birth Chart validation passed.
6. Swiss Ephemeris confirmed as authoritative calculation engine.
7. Birth Chart API integration completed.
8. Interpretation engine integrated.
9. Real API request tested successfully.
10. Birth Chart page integrated with the API.
11. Birth Chart page Persianized.
12. Persian browser rendering verified.
13. Interpretation output formatting fixed.
14. Local Git history is clean.
15. Current local HEAD is `499f1bb`.

## Current Phase

The project is now beyond calculation-engine validation.

Current phase:

**Birth Chart product integration and interpretation refinement**

The next work should focus on improving the actual user experience and interpretation quality while keeping the validated Swiss Ephemeris calculation layer stable.

## Important Project Rules

- Do not replace Swiss Ephemeris with manual astronomical formulas.
- Do not modify `birth_chart.py` unnecessarily.
- Preserve validated calculation results.
- Preserve the existing dark navy/purple visual direction.
- Keep the website Persian/RTL where appropriate.
- Keep implementation simple and local where possible.
- Avoid paid APIs and services when reliable free/local alternatives exist.
- Test each meaningful change locally before committing.
- Work one step at a time.

## Next Planned Phase

The next logical phase is to improve the Birth Chart interpretation experience.

Potential sequence:

1. Inspect the current Birth Chart page and API output together.
2. Identify the smallest useful UX improvement.
3. Improve interpretation wording and presentation.
4. Test with the existing sample birth data.
5. Verify the API still returns valid JSON.
6. Run the Astro build.
7. Commit the verified change.
8. Push the completed local commits to GitHub when appropriate.

No change to the validated astronomical calculation engine is planned unless a real issue is discovered.

## Resume Phrase

If a new chat is opened, start with:

`ادامه پروژه Astro Negah — از وضعیت ثبت‌شده در ASTRO-NEGAH-CONTINUITY.md ادامه بده.`

Then review this checkpoint before giving the next command.