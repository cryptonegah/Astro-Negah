import swisseph as swe
from datetime import datetime
from zoneinfo import ZoneInfo


ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


ASPECTS = {
    "Conjunction": 0,
    "Sextile": 60,
    "Square": 90,
    "Trine": 120,
    "Opposition": 180,
}


PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
}


def local_to_utc(year, month, day, hour, minute, timezone_name):
    local_time = datetime(
        year,
        month,
        day,
        hour,
        minute,
        tzinfo=ZoneInfo(timezone_name)
    )

    return local_time.astimezone(ZoneInfo("UTC"))


def format_zodiac(longitude):
    longitude = longitude % 360

    sign_index = int(longitude // 30)
    within_sign = longitude % 30

    degree = int(within_sign)

    minutes_total = (within_sign - degree) * 60
    minute = int(minutes_total)

    second = round((minutes_total - minute) * 60)

    if second == 60:
        second = 0
        minute += 1

    if minute == 60:
        minute = 0
        degree += 1

    return {
        "sign": ZODIAC_SIGNS[sign_index],
        "degree": degree,
        "minute": minute,
        "second": second
    }


def angular_distance(longitude1, longitude2):
    difference = abs(longitude1 - longitude2)

    return min(
        difference,
        360 - difference
    )


def detect_aspects(planets, max_orb=8.0):
    aspects = []

    planet_names = list(planets.keys())

    for i in range(len(planet_names)):
        for j in range(i + 1, len(planet_names)):

            planet1 = planet_names[i]
            planet2 = planet_names[j]

            longitude1 = planets[planet1]["longitude"]
            longitude2 = planets[planet2]["longitude"]

            distance = angular_distance(
                longitude1,
                longitude2
            )

            for aspect_name, exact_angle in ASPECTS.items():

                orb = abs(
                    distance - exact_angle
                )

                if orb <= max_orb:

                    aspects.append({
                        "planet1": planet1,
                        "planet2": planet2,
                        "aspect": aspect_name,
                        "angle": distance,
                        "orb": orb
                    })

    return aspects


def calculate_birth_chart(
    year,
    month,
    day,
    hour_utc,
    latitude,
    longitude
):
    julian_day = swe.julday(
        year,
        month,
        day,
        hour_utc
    )

    cusps, ascmc = swe.houses_ex(
        julian_day,
        latitude,
        longitude,
        b"P"
    )

    planets = {}

    for name, planet_id in PLANETS.items():

        position, _ = swe.calc_ut(
            julian_day,
            planet_id
        )

        position_next, _ = swe.calc_ut(
            julian_day + 0.01,
            planet_id
        )

        motion = position_next[0] - position[0]

        if motion > 180:
            motion -= 360

        if motion < -180:
            motion += 360

        longitude_position = position[0]

        house_number = next(
            i + 1
            for i in range(12)
            if (
                (
                    cusps[i]
                    <= longitude_position
                    < cusps[(i + 1) % 12]
                )
                if cusps[i] < cusps[(i + 1) % 12]
                else (
                    longitude_position >= cusps[i]
                    or longitude_position < cusps[(i + 1) % 12]
                )
            )
        )

        planets[name] = {
            "longitude": longitude_position,
            "zodiac": format_zodiac(longitude_position),
            "house": house_number,
            "retrograde": motion < 0
        }

    aspects = detect_aspects(planets)

    return {
        "calculation": {
            "zodiac": "Tropical",
            "house_system": "Placidus",
            "ephemeris": "Swiss Ephemeris"
        },

        "birth_data": {
            "year": year,
            "month": month,
            "day": day,
            "hour_utc": hour_utc,
            "latitude": latitude,
            "longitude": longitude
        },

        "julian_day": julian_day,

        "ascendant": ascmc[0],
        "ascendant_zodiac": format_zodiac(ascmc[0]),

        "mc": ascmc[1],
        "mc_zodiac": format_zodiac(ascmc[1]),

        "houses": list(cusps),

        "planets": planets,

        "aspects": aspects,
    }


def calculate_birth_chart_local(
    year,
    month,
    day,
    hour,
    minute,
    timezone_name,
    latitude,
    longitude
):
    utc_time = local_to_utc(
        year,
        month,
        day,
        hour,
        minute,
        timezone_name
    )

    hour_utc = (
        utc_time.hour
        + utc_time.minute / 60
        + utc_time.second / 3600
        + utc_time.microsecond / 3600000000
    )

    result = calculate_birth_chart(
        utc_time.year,
        utc_time.month,
        utc_time.day,
        hour_utc,
        latitude,
        longitude
    )

    result["birth_time_local"] = (
        f"{year:04d}-{month:02d}-{day:02d} "
        f"{hour:02d}:{minute:02d}"
    )

    result["birth_time_utc"] = utc_time.isoformat()

    result["timezone"] = timezone_name

    return result