def split_address(transcription: str) -> dict[str, str]:
    """ split address into multiple parts """
    # TODO also split with diff keyword for area outside of Bangkok
    # split each section up
    # TODO tried using preset subdistrict and district info
    home_number, transcription = transcription.split("ซอย")
    alley, transcription = transcription.split("แขวง")
    subdistrict, transcription = transcription.split("เขต")
    district, transcription = transcription.split("จังหวัด")
    # remove all occurance of word related to area code and just use the number as area code
    transcription = transcription\
        .replace("เลขที่", "").replace("เลข", "").replace("ไปรษณีย์", "").strip()
    area_code_delim_idx = len(transcription)
    while transcription[area_code_delim_idx-1].isdigit():
        area_code_delim_idx -= 1
    province, area_code = transcription[:area_code_delim_idx], transcription[area_code_delim_idx:]

    return {
        "home_number": home_number.strip(),
        "alley": alley.strip(),
        "subdistrict": subdistrict.strip(),
        "district": district.strip(),
        "province": province.strip(),
        "area_code": area_code,
    }
