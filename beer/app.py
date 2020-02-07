# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import url_for
from sqlalchemy import func
from sqlalchemy import or_

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Maps Setup
#################################################
mapkey = os.environ.get('MAPKEY', '') or "CREATE MAPKEY ENV"

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

#Database Variables
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/brew.sqlite"

db = SQLAlchemy(app)
from .models import beerdata
Base = automap_base()
Base.prepare(db.engine, reflect=True)

###############################################
#########Html Routes for Web Server ###########
###############################################
####Landing Page####
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/scope/")
def scope():
    return render_template("scope.html")
@app.route("/analyst/")
def analyst():
    return render_template("analyst.html")
@app.route("/analysis/")
def analysis():
    return render_template("analysis.html")

##############################################
############Master Datafile Set ##############
# ##############################################
# @app.route("/datafile1/")
# def datafile1():
#     """Return the list of records in Table"""
#     # Use Pandas to perform the sql query
#     stmt = db.session.query(crashdata).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     json = df.to_json(orient='records')
#     return (json)

if __name__ == "__main__":
    app.run()