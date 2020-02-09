# import necessary libraries
import os
from flask import (Flask,render_template,jsonify,request,redirect,url_for)
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask import Flask, jsonify, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask import json
from flask import url_for
from sqlalchemy import func
from sqlalchemy import or_
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .mlscript import similarity_model, get_title_from_index, get_index_from_title,print_statement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#################################################
# Maps Setup
#################################################
mapkey = os.environ.get('MAPKEY', '') or "CREATE MAPKEY ENV"

#################################################
# Database Setup
#################################################
import os 
cd = os.getcwd()
# df_5000 = pd.read_csv(cd+"/beer/df500.csv")

from flask_sqlalchemy import SQLAlchemy

#Database Variables
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/brew.sqlite"

# df_5000 = pd.read_csv('df500.csv')

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

# @app.route('/form/')
# def my_form():
#     return render_template('form.html')


# @app.route('/function/<parameter>')
# def similarity_model(parameter):
#     cd = os.getcwd()
#     df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
#     count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
#     cosine_sim = cosine_similarity(count_matrix)
#     cosine_sim.shape
#     beer_user_likes = (parameter)
#     beer_index = get_index_from_title(beer_user_likes)
#     similar_beers = list( enumerate(cosine_sim[beer_index]) )
#     sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
#     i=0
#     beer_dict = []
#     sim_score = []
#     print(f"The top 5 beers similar to {beer_user_likes} are: ")
#     for i in range(len(sorted_similar_beers)):
#         beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
#         sim_score.append(sorted_similar_beers[i][1])
#         if i>=4:
#             break
#     mydict = (dict(zip(beer_dict, sim_score)))
    
#     return (mydict)





# @app.route('/beer/')
# def form():
#     return render_template('form.html',result=result)


#Testing (Route is Hard Coded)
@app.route('/beer/')
def input():

    # beer_variable = parameter.upper()
    parameter='Wachusett Larry'
    df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
    count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    cosine_sim.shape
    beer_user_likes = (parameter)
    beer_index = get_index_from_title(beer_user_likes)
    similar_beers = list( enumerate(cosine_sim[beer_index]) )
    sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
    i=0
    beer_dict = []
    sim_score = []
    print(f"The top 5 beers similar to {beer_user_likes} are: ")
    for i in range(len(sorted_similar_beers)):
        beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
        sim_score.append(sorted_similar_beers[i][1])
        if i>=4:
            break
    result = (dict(zip(beer_dict, sim_score)))
    
    return render_template("form.html", result=result)

###Testing    
# parameter = ''
@app.route('/signup', methods=['GET', 'POST']) 
def beer_parameter():
    parameter = request.form['email']
    print("The parameter is '" + parameter + "'")
    
    return render_template('form1.html', parameter=parameter)


#Testing (Route is Hard Coded)
@app.route('/testing/')
def input1():
    # parameter = resultfunction(form)
    # parameter = request.form['text']
    # beer_variable = parameter.upper()
    # parameter='Wachusett Larry'
    df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
    count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    cosine_sim.shape
    beer_user_likes = (parameter)
    beer_index = get_index_from_title(beer_user_likes)
    similar_beers = list( enumerate(cosine_sim[beer_index]) )
    sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
    i=0
    beer_dict = []
    sim_score = []
    print(f"The top 5 beers similar to {beer_user_likes} are: ")
    for i in range(len(sorted_similar_beers)):
        beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
        sim_score.append(sorted_similar_beers[i][1])
        if i>=4:
            break
    result = (dict(zip(beer_dict, sim_score)))
    
    return render_template("form2.html", result=result)
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