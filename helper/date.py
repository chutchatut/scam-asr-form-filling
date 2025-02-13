from datetime import datetime


def parse_date(transcription: str) -> datetime:
    parts = transcription.strip().split()

    if len(parts) != 3:
        raise Exception("incomplete date information")

    day, month, year = parts

    # TODO might need to convert date and year from text to int
    day = int(day)
    year = int(year)

    MONTH_STR_TO_INT = {
        "มกรา": 1,
        "มกราคม": 1,
        # TODO add more
    }

    if month not in MONTH_STR_TO_INT:
        raise Exception('unknown month format')

    month = MONTH_STR_TO_INT[month]

    if year > 2400:
        year -= 543

    return datetime(year, month, day)
