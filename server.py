from flask import Flask, request
from random import randint
from waitress import serve

app = Flask(__name__)

@app.route("/national_id", methods=["POST"])
def national_id():
    """ Use to detect national ID from voice sample """
    # TODO use this
    # print(request.files.get('file').read())

    national_id = f"{randint(0, 1e14-1):013}"

@app.route("/detect_agree", methods=["POST"])
def detect_agree():
    """ Use to detect if the user agree to all terms and conditions from voice sample """
    # TODO use this
    # print(request.files.get('file').read())

    return randint(0, 100) > 10

@app.route("/address", methods=["POST"])
def address():
    """ Get the address, need to be called twice (home address and incident address) """
    # print(request.files.get('name').stream)
    # TODO get transcription from voice sample
    transcription = "12/3 ซอย ZZZ แขวง X เขต Y จังหวัด Z"
    
    return {
        ""
    }

if __name__ == "__main__":
    serve(app, port=5000)