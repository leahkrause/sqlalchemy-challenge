
# Import dependencies
from flask import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table 
measurement = Base.classes.measurement
station = Base.classes.station

# Flask set up
app = Flask(__name__)

# Homepage 
@app.route("/")
def homepage():
    return """Welcome to Leah's climate app. Please select from the below:
    <br><a> href="/api/v1.0/precipitation">Precipitation (JSON)</a>
    <br><a> href="/api/v1.0/stations">Stations (JSON)</a>
    <br><a> href="/api/v1.0/<start>">Start (JSON)</a>
    <br><a> href="/api/v1.0/<start>/<end>">Start and End (JSON)</a>
    """

@app.route("/api/v1.0/precipitation")
def precipitation()
