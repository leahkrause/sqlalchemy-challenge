# sqlalchemy-challenge

# sqlalchemy-challenge
PART 1

First, create an engine from SQLAlchemy and load in Hawaii SQLite data.

Reflect existing database into new model and reflect the tables. View all the classes found and save references to them.

Create the session engine. 

EXPLORATORY PRECIPITATION ANALYSIS

Query the most recent date in the precipitation data set and the date one year from the most recent date.

Find the data for the range of these dates and save it as a DataFrame sorted by date. 

Plot this data in a Pandas bar graph.

Describe this data in a summary statistics table.

EXPLORATORY STATION ANALYSIS

Query the total number of stations in the station data.

Find the station that is the most active (has the most rows). List the stations and counts in descending order.

Calculate the lowest, highest, and average temperature from the most active station.

Query the last 12 months of temperature data and plot it as a histogram.

PART 2

Design a Flask API climate app with this data.

Start a homepage that links out to all pages (Precipitation, Stations, Tobs, Start, End)
