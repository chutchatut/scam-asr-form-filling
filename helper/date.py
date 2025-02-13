from datetime import datetime

MONTH_STR_TO_INT = {
    "มกรา": 1,
    "มกราคม": 1,
    "กุมภา": 2,
    "กุมภาพันธ์": 2,
    "มีนา": 3,
    "มีนาคม": 3,
    "เมษา": 4,
    "เมษายน": 4,
    "พฤษภา": 5,
    "พฤษภาคม": 5,
    "มิถุนา": 6,
    "มิถุนายน": 6,
    "กรกฎา": 7,
    "กรกฎาคม": 7,
    "สิงหา": 8,
    "สิงหาคม": 8,
    "กันยา": 9,
    "กันยายน": 9,
    "ตุลา": 10,
    "ตุลาคม": 10,
    "พฤศจิกา": 11,
    "พฤศจิกายน": 11,
    "ธันวา": 12,
    "ธันวาคม": 12,
}


def parse_date(transcription: str) -> datetime:
    parts = transcription.strip().split()

    if len(parts) != 3:
        raise Exception("incomplete date information")

    day, month, year = parts

    # TODO might need to convert date and year from text to int
    day = int(day)
    year = int(year)

    if month not in MONTH_STR_TO_INT:
        raise Exception('unknown month format')

    month = MONTH_STR_TO_INT[month]

    if year > 2400:
        year -= 543

    return datetime(year, month, day)
