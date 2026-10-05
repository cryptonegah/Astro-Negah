"""
Astro Negah
Birth Chart Interpretation Engine

This module converts validated birth-chart data
into structured interpretation sections.
"""


def format_position(zodiac):
    """
    Format a zodiac position in a clean, readable form.
    """

    return (
        f"{zodiac['degree']}°"
        f"{zodiac['minute']:02d}′"
    )


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
            f"at {format_position(sun)}."
        ),

        "moon": (
            f"Your Moon is in {moon['sign']} "
            f"at {format_position(moon)}."
        ),

        "ascendant": (
            f"Your Ascendant is in {ascendant['sign']} "
            f"at {format_position(ascendant)}."
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
            "second": zodiac["second"],
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
    Build the complete interpretation result,
    including the final Cosmic Story section.
    """

    personality = interpret_personality(chart)
    planets = interpret_planets(chart)
    aspects = interpret_aspects(chart)

    sun_sign = chart["planets"]["Sun"]["zodiac"]["sign"]
    moon_sign = chart["planets"]["Moon"]["zodiac"]["sign"]
    ascendant_sign = chart["ascendant_zodiac"]["sign"]

    cosmic_story = {
        "title": "✨ Your Cosmic Story",

        "intro": (
            f"Your cosmic story begins with a {sun_sign} Sun, "
            f"a {moon_sign} Moon, and a {ascendant_sign} Ascendant."
        ),

        "personality": (
            "Your Sun represents your core identity and the direction "
            "you naturally seek in life."
        ),

        "emotions": (
            "Your Moon reflects your emotional world, inner needs, "
            "and the way you process experiences."
        ),

        "presence": (
            "Your Ascendant describes the way you meet the world "
            "and the impression you naturally create."
        ),

        "reflection": (
            f"Together, your {sun_sign} Sun, {moon_sign} Moon, "
            f"and {ascendant_sign} Ascendant create a unique "
            "combination of identity, emotion, and outward expression."
        )
    }

    return {
        "personality_summary": personality,
        "planets_and_houses": planets,
        "aspects": aspects,
        "cosmic_story": cosmic_story
    }