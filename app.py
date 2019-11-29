# Import dependencies.
import pandas as pd
import numpy as np
import datetime as dt
# Get the dependencies we need for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Add the code to import the dependencies that we need for Flask
from flask import Flask, jsonify
# Set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into our classes.
Base = automap_base()
# Reflect the database
Base.prepare(engine, reflect=True)
# Create a variable for each of the classes so that we can reference them later
measurement = Base.classes.measurement
station = Base.classes.station
# Create a session link from Python to our database
session = Session(engine)
# Define our Flask app
app = Flask(__name__)
# Define the welcome route
@app.route("/")
def welcome():
	return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
	)
