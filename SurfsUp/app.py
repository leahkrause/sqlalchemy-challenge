
# Import dependencies
from flask import Flask, jsonify
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
def precipitation():
    session = Session(engine)

    # Find the most recent date in the data set.
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    
    # Design a query to retrieve the last 12 months of precipitation data and plot the results. 
    # Starting from the most recent data point in the database. 
    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    data = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date > (year_ago)).order_by(measurement.date.desc())
  
    session.close()

    # Create a dictionary using date as the key and prcp as the value
    all_precipitation = []
    for date, prcp in data:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        all_precipitation.append(prcp_dict)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    # Find all distinct stations
    tot_stations = session.query(station).distinct()

    session.close()

    return jsonify(tot_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    # Query dates and temperature observations of the most-active station for the previous year of data
    sel = [station.station, func.count(measurement.station)]
    active_query = session.query(*sel).filter(station.station == measurement.station).group_by(station.station).\
    order_by(func.count(measurement.station).desc()).all()

    sel = [func.min(measurement.tobs),
      func.max(measurement.tobs),
      func.avg(measurement.tobs)]

    active_data = session.query(*sel).filter(measurement.station == 'USC00519281').all()

    last_year_data = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281', measurement.date >= year_ago).all()
    df_last_year = pd.DataFrame(last_year_data, columns=['date', 'temperature'])

    session.close()

    return jsonify(df_last_year)

if __name__ == '__main__':
    app.run(debug=True)


