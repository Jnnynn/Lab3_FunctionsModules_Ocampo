LAST_NAME = "OCAMPO"
SEED_NUM = 9
FAVORITE_ARTIST = "LANA DEL REY"


def telemetry_generator(last_name=LAST_NAME, seed_num=SEED_NUM, favorite_artist=FAVORITE_ARTIST, count=12):
    """Generate a student-specific telemetry stream using a surname, seed, and artist value."""
    name_value = sum(ord(char) for char in last_name.upper())
    artist_value = sum(ord(char) for char in favorite_artist.upper() if char.isalpha())
    base = (len(last_name) * seed_num) + (name_value % 20) + (artist_value % 30)

    for index in range(1, count + 1):
        reading = base + (index * 13) + (seed_num * 2)

        if index % 4 == 0:
            yield "INVALID"
        elif index % 5 == 0:
            yield "N/A"
        else:
            yield round(reading, 2)


def generate_telemetry_stream(last_name=LAST_NAME, seed_num=SEED_NUM, favorite_artist=FAVORITE_ARTIST, count=12):
    """Alias for compatibility with older and newer scripts."""
    return telemetry_generator(last_name, seed_num, favorite_artist, count)


def recursive_anomaly_analysis(value, threshold=120.0, depth=0):
    """Recursively reduce an abnormal reading until it reaches the base threshold."""
    if value <= threshold:
        return value, depth

    reduced_value = value - 10.0
    return recursive_anomaly_analysis(reduced_value, threshold, depth + 1)
