
"""
Astro Negah
Birth Chart Interpretation Engine

This module converts validated birth-chart data
into structured interpretation sections.
"""


def interpret_personality(chart):
    """
    Create a high-level personality summary
    from the core birth-chart placements.
    """

    sun = chart["planets"]["Sun"]["zodiac"]
    moon = chart["planets"]["Moon"]["zodiac"]
    ascendant = chart["ascendant_zodiac"]

    return {
        "title": "Personality Summary",
        "sun": (
            f"Your Sun is in {sun['sign']} "
            f"at {sun['degree']}°{sun['minute']:02d}′."
        ),
        "moon": (
            f"Your Moon is in {moon['sign']} "
            f"at {moon['degree']}°{moon['minute']:02d}′."
        ),
        "ascendant": (
            f"Your Ascendant is in {ascendant['sign']} "
            f"at {ascendant['degree']}°{ascendant['minute']:02d}′."
        )
    }


def interpret_planets(chart):
    """
    Create structured planet and house information.
    """

    interpretations = []

    for planet_name, planet_data in chart["planets"].items():

        zodiac = planet_data["zodiac"]

        interpretations.append({
            "planet": planet_name,
            "sign": zodiac["sign"],
            "degree": zodiac["degree"],
            "minute": zodiac["minute"],
            "house": planet_data["house"],
            "retrograde": planet_data["retrograde"]
        })

    return interpretations


def interpret_aspects(chart):
    """
    Create structured aspect information.
    """

    interpretations = []

    for aspect in chart["aspects"]:

        interpretations.append({
            "planet1": aspect["planet1"],
            "planet2": aspect["planet2"],
            "aspect": aspect["aspect"],
            "angle": aspect["angle"],
            "orb": aspect["orb"]
        })

    return interpretations


def build_cosmic_story(chart):
    """
    Combine all interpretation sections into one result.
    """

    return {
        "personality_summary": interpret_personality(chart),
        "planets_and_houses": interpret_planets(chart),
        "aspects": interpret_aspects(chart)
    }

