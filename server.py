from flask import Flask, request
from random import randint
from waitress import serve
from helper.address import split_address

app = Flask(__name__)


@app.route("/national_id", methods=["POST"])
def national_id() -> str:
    """ Use to detect national ID from voice sample """
    # TODO use this
    # print(request.files.get('file').read())

    national_id = f"{randint(0, 1e14-1):013}"

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
    """ Get the address, need to be called twice (home address and incident address) """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "12/3 ซอย ZZZ แขวง X เขต Y จังหวัด Z เลขไปรษณีย์ 99999"

    return split_address(transcription)


if __name__ == "__main__":
    serve(app, port=5000)
