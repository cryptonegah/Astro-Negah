"""
Astro Negah
Birth Chart Interpretation Engine

This module converts validated birth-chart data
into a structured, professional, warm, and personalized
astrological interpretation.

Important:
- This module does not calculate astronomical positions.
- Swiss Ephemeris remains the authoritative calculation engine.
"""


def format_position(zodiac):
    """
    Format a zodiac position in a clean, readable form.
    """

    return (
        f"{zodiac['degree']}°"
        f"{zodiac['minute']:02d}′"
    )


def house_label(house):
    """
    Return a readable ordinal house label.
    """

    if house == 1:
        return "1st"
    if house == 2:
        return "2nd"
    if house == 3:
        return "3rd"

    return f"{house}th"


def interpret_personality(chart):
    """
    Create a professional but warm personality interpretation
    from the Sun, Moon, and Ascendant.
    """

    sun = chart["planets"]["Sun"]["zodiac"]
    moon = chart["planets"]["Moon"]["zodiac"]
    ascendant = chart["ascendant_zodiac"]

    sun_house = chart["planets"]["Sun"]["house"]
    moon_house = chart["planets"]["Moon"]["house"]

    return {
        "title": "Personality Summary",

        "sun": (
            f"Your Sun is in {sun['sign']} at {format_position(sun)}, "
            f"placed in the {house_label(sun_house)} house. "
            "This combination points toward a strong sense of purpose, "
            "responsibility, and a desire to create something meaningful "
            "and lasting. You are likely to value progress that has real "
            "substance rather than temporary recognition."
        ),

        "moon": (
            f"Your Moon is in {moon['sign']} at {format_position(moon)}, "
            f"placed in the {house_label(moon_house)} house. "
            "This suggests a deep and emotionally perceptive inner world. "
            "You may feel things more intensely than you immediately show, "
            "and you may need private time to process important experiences. "
            "A sense of purpose in everyday life can help you feel emotionally "
            "grounded."
        ),

        "ascendant": (
            f"Your Ascendant is in {ascendant['sign']} "
            f"at {format_position(ascendant)}. "
            "This gives your outward presence a curious, adaptable, and "
            "observant quality. You may naturally approach life through "
            "questions, conversation, learning, and the exploration of "
            "different perspectives."
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
    Build the complete personalized Cosmic Story.
    """

    personality = interpret_personality(chart)
    planets = interpret_planets(chart)
    aspects = interpret_aspects(chart)

    sun = chart["planets"]["Sun"]["zodiac"]
    moon = chart["planets"]["Moon"]["zodiac"]
    ascendant = chart["ascendant_zodiac"]

    sun_house = chart["planets"]["Sun"]["house"]
    moon_house = chart["planets"]["Moon"]["house"]

    sun_sign = sun["sign"]
    moon_sign = moon["sign"]
    ascendant_sign = ascendant["sign"]

    cosmic_story = {
        "title": "✨ Your Cosmic Story",

        "intro": (
            f"Your chart brings together a {sun_sign} Sun, "
            f"a {moon_sign} Moon, and a {ascendant_sign} Ascendant. "
            "Together, these three points create the foundation of your "
            "astrological personality: how you express yourself, how you "
            "experience life internally, and how you meet the world."
        ),

        "personality": (
            f"With your Sun in {sun_sign} in the {house_label(sun_house)} house, "
            "your sense of identity is closely connected with purpose, "
            "growth, and the relationships or experiences that help you "
            "understand your own direction. You are not simply looking for "
            "activity; you are looking for something that feels worthwhile."
        ),

        "emotions": (
            f"Your {moon_sign} Moon in the {house_label(moon_house)} house "
            "adds emotional depth and sensitivity to this picture. "
            "Your inner world may be more complex than people first realize. "
            "You may need trust, privacy, and meaningful routines before you "
            "feel completely comfortable opening up."
        ),

        "presence": (
            f"Your {ascendant_sign} Ascendant shapes the way others first "
            "experience you. It gives your presence a more curious, flexible, "
            "and mentally active quality. You may naturally observe your "
            "surroundings, gather information, and adapt your communication "
            "to the person or situation in front of you."
        ),

        "reflection": (
            f"The most interesting part of this combination is the contrast "
            f"between your {sun_sign} Sun, {moon_sign} Moon, and "
            f"{ascendant_sign} Ascendant. There is a meeting here between "
            "purpose, emotional depth, and curiosity. Your chart suggests "
            "that your personal story is not about fitting into one simple "
            "description, but about learning how these different sides of "
            "your personality can work together."
        )
    }

    return {
        "personality_summary": personality,
        "planets_and_houses": planets,
        "aspects": aspects,
        "cosmic_story": cosmic_story
    }