from flask import Flask, request
from random import randint
from waitress import serve
from datetime import datetime
from helper.address import split_address
from helper.date import parse_date

app = Flask(__name__)


@app.route("/national_id", methods=["POST"])
def national_id() -> str:
    """ Use to detect national ID from voice sample """
    # TODO use this
    # print(request.files.get('file').read())

    national_id = f"{randint(0, 1e13-1):013}"

    if len(national_id) != 13:
        return "national ID must have 13 digits", 400

    for digit in national_id:
        if not digit.isdigit():
            return "national ID must only contains number", 400

    return national_id


@app.route("/detect_agree", methods=["POST"])
def detect_agree() -> bool:
    """ Use to detect if the user agree to all terms and conditions from voice sample """
    # TODO use this
    # print(request.files.get('file').read())

    return randint(0, 100) > 10


@app.route("/address", methods=["POST"])
def address() -> dict[str, str]:
    """ Get the address from the voice sample, need to be called twice (home address and incident address) """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "12/3 ซอย ZZZ แขวง X เขต Y จังหวัด Z เลขไปรษณีย์ 99999"

    return split_address(transcription)


@app.route("/transcribe", methods=["POST"])
def transcribe() -> dict[str, str]:
    """ Get the transcription of the incident and the classification from the voice sample """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "โดนทุบหัว" + " bluh" * 40
    incident_type = "แย่งชิงทรัพย์"

    return {
        "transcription": transcription,
        "incident_type": incident_type,
    }


@app.route("/detect_gender", methods=["POST"])
def detect_gender() -> str:
    """ Get the gender from the voice sample """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "เพศ ชาย"

    gender = transcription \
        .replace("อื่นอื่น", "อื่นๆ").replace("เพศ", "").strip()

    if gender not in ['ชาย', 'หญิง', "อื่นๆ"]:
        return "invalid gender", 400

    return gender


@app.route("/detect_if_user_went", methods=["POST"])
def detect_if_user_went() -> bool:
    """ Detect if user went to the CIB from the voice sample """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "ไปมาแล้ว"

    if 'แล้ว' in transcription:
        return True

    if 'ยัง' in transcription:
        return False

    return "Cannot determine", 400


@app.route("/get_date", methods=["POST"])
def get_date() -> datetime:
    """ Get date from the voice sample """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "5 มกรา 2012"

    try:
        return parse_date(transcription)
    except Exception as e:
        return repr(e), 400


@app.route("/get_phone_provider", methods=["POST"])
def get_date() -> str:
    """ Get phone provider from the voice sample """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "true"

    provider = transcription.upper().strip()

    # TODO convert thai to english if needed

    if provider not in ['TRUE', 'DTAC', 'AIS']:
        return 'Cannot determine phone provider', 400

    return provider


if __name__ == "__main__":
    serve(app, port=5000)
