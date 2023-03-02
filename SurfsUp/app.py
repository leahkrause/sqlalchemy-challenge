from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return """Welcome to Leah's climate app. Please select from the below:
    <br><a> href="/api/v1.0/precipitation">Precipitation (JSON)</a>
    <br><a> href="/api/v1.0/stations">Stations (JSON)</a>
    <br><a> href="/api/v1.0/<start>">Start (JSON)</a>
    <br><a> href="/api/v1.0/<start>/<end>">Start and End (JSON)</a>
    """

