THAI_NUM_TO_INT = {
    "ศูนย์": 0, "หนึ่ง": 1, "เอ็ด": 1, "สอง": 2,
    "สาม": 3, "สี่": 4, "ห้า": 5, "หก": 6,
    "เจ็ด": 7, "แปด": 8, "เก้า": 9,
}

THAI_MULT_TO_INT = {
    "สิบ": 10, "ร้อย": 100, "พัน": 1000, "หมื่น": 10000, "แสน": 100000, "ล้าน": 1000000
}


def split_first_number(text: str) -> tuple[int, str]:
    """ e.g. "สองสามสี่" => (2, "สามสี่") """
    for num in THAI_NUM_TO_INT:
        if text.startswith(num):
            return THAI_NUM_TO_INT[num], text[len(num):]
    return None, text


def split_first_mult(text: str) -> tuple[int, str]:
    """ e.g. "ร้อยห้าสิบ" => (100, "ห้าสิบ") """
    for mult in THAI_MULT_TO_INT:
        if text.startswith(mult):
            return THAI_MULT_TO_INT[mult], text[len(mult):]
    return None, text


def thai_text_to_number(text: str) -> int:
    ''' convert thai text of number to number '''

    text_backup = text
    text = text.replace(' ', '')
    if text[0].isnumeric():
        # already a number, e.g. "100"
        return int(text)

    out = 0

    has_mult = False
    for mult in THAI_MULT_TO_INT:
        if mult in text:
            has_mult = True
            break

    if has_mult:
        while text:
            # case with multiplier e.g. ห้าร้อยยี่สิบสาม
            num, text = split_first_number(text)
            # special case for shorthand ยี่x e.g. ยี่สอง
            if text.startswith('ยี่'):
                num = 2
                mult = 10
                text = text[len('ยี่'):]
                if text.startswith('สิบ'):
                    text = text[len('สิบ'):]
            else:
                mult, text = split_first_mult(text)

            if num is None and mult is None:
                raise Exception(f'cannot parse number: {text_backup}')
            if num is None:
                num = 1
            if mult is None:
                mult = 1
            out += num * mult

    else:
        # case without multiplier e.g. สองศูนย์สองสาม
        while text:
            out *= 10
            num, text = split_first_number(text)
            if num is None:
                raise Exception(f"cannot parse number: {text_backup}")
            out += num

    return out


if __name__ == "__main__":
    assert (thai_text_to_number("ห้าร้อยยี่สิบสาม") == 523)
    assert (thai_text_to_number("หนึ่งพันสามร้อยสิบหก") == 1316)
    assert (thai_text_to_number("สองล้านหนึ่งแสน") == 2100000)
    assert (thai_text_to_number("สองศูนย์สองสาม") == 2023)
    assert (thai_text_to_number("1234") == 1234)
