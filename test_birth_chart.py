from birth_chart import calculate_birth_chart_local, local_to_utc


result = calculate_birth_chart_local(
    1990,
    3,
    15,
    18,
    45,
    "Asia/Tehran",
    35.6892,
    51.3890
)


assert result["ascendant_zodiac"]["sign"] == "Libra"
assert result["ascendant_zodiac"]["degree"] == 2

assert result["mc_zodiac"]["sign"] == "Cancer"
assert result["mc_zodiac"]["degree"] == 2


assert result["planets"]["Sun"]["house"] == 6
assert result["planets"]["Moon"]["house"] == 2
assert result["planets"]["Mercury"]["house"] == 6
assert result["planets"]["Venus"]["house"] == 5
assert result["planets"]["Mars"]["house"] == 4
assert result["planets"]["Jupiter"]["house"] == 9
assert result["planets"]["Saturn"]["house"] == 4
assert result["planets"]["Uranus"]["house"] == 4
assert result["planets"]["Neptune"]["house"] == 4
assert result["planets"]["Pluto"]["house"] == 2


sun_saturn = [
    aspect
    for aspect in result["aspects"]
    if aspect["planet1"] == "Sun"
    and aspect["planet2"] == "Saturn"
    and aspect["aspect"] == "Sextile"
]


assert len(sun_saturn) == 1
assert abs(sun_saturn[0]["orb"] - 1.4287) < 0.01


ny_dst = local_to_utc(
    2024,
    7,
    15,
    18,
    45,
    "America/New_York"
)


assert ny_dst.isoformat() == "2024-07-15T22:45:00+00:00"


mercury_retrograde = calculate_birth_chart_local(
    2024,
    4,
    15,
    12,
    0,
    "America/New_York",
    40.7128,
    -74.0060
)


assert mercury_retrograde["planets"]["Mercury"]["retrograde"] is True


print("Birth Chart Validation: PASSED")