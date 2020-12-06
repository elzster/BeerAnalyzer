# import necessary libraries
from flask import (Flask,render_template,jsonify,request,redirect,url_for)
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from flask import json
#Machine Learning Bits Imported into Flask Server
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .mlscript import similarity_model, get_title_from_index, get_index_from_title,print_statement, get_abv_from_index, get_beerstyle_from_index, get_brewery_from_index 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#################################################
# Database Setup
#################################################
import os 
cd = os.getcwd()

from sqlalchemy.orm import sessionmaker

#Database Variables
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/brew.sqlite"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost/beer_data"
db = SQLAlchemy(app)
from .models import beerdata
Base = automap_base()
Base.prepare(db.engine, reflect=True)

# ###############################################
# #########Html Routes for Web Server ###########
# ###############################################
# from beer import views

###Landing Page####
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

@app.route("/sentiment/")
def sentiment():
    return render_template("sentiment.html")

@app.route("/slow/<inputfield>")
def slow_input(inputfield):
    result = {}

    Session = sessionmaker(bind = db.engine)
    session = Session()
    
    WebCache = Base.classes["web_cache"]
    url = "/slow/"+ inputfield
    # check the database for the response
    found = session.query(WebCache.id).filter_by(url=url).count()
    # if found return response right away
    if(found > 0):
        record = session.query(WebCache).filter_by(url=url).first()
        result = json.loads(record.response)
        return render_template("slowpage.html", result=result)
        # otherwise do the critical section
    else:
        # this section is the critical section
        sleep(30)
        result["input"] = inputfield
        # ******* end of critical section ******

        
        resp = json.dumps(result)

        # c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')
        # print(Base.metadata.tables.keys())
        # print(Base.classes.keys())

        loaded = WebCache(url=url, response=resp)
        session.add(loaded)
        session.commit()
    
    return render_template("slowpage.html", result=result)


#Default Route that is Loaded Up into Script "Waschusett Larry"
@app.route('/beer/', defaults={'beer': 'Wachusett Larry'})
@app.route('/beer/<beer>')
def beer_input(beer):
    #loading up variables to use for MLscript
    beerlist = pd.read_csv(cd+"/beer/static/df500.csv")
    beerlist1 = beerlist['beer_name']
    
    #load up CSV for Matrix.
    df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
    count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    cosine_sim.shape
    beer_user_likes = (beer)
    beer_index = get_index_from_title(beer_user_likes)
    similar_beers = list( enumerate(cosine_sim[beer_index]) )
    sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
    i=0
    beer_dict = []
    sim_score = []
    abv_score = []
    beer = {}
    beer['beer'] ={}
    beer['similarity']={}
    beer['abv']={}
    beer['brewery']={}
    case_list=[]
    
    
    for i in range(len(sorted_similar_beers)):
        beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
        sim_score.append(sorted_similar_beers[i][1])
        abv_score.append(get_abv_from_index(sorted_similar_beers[i][0]))
        case = {'beer': get_title_from_index(sorted_similar_beers[i][0]), 'similarity': (sorted_similar_beers[i][1]).round(2), 'abv':(get_abv_from_index(sorted_similar_beers[i][0])), 'style':(get_beerstyle_from_index((sorted_similar_beers[i][0]))), 'brewery':(get_brewery_from_index((sorted_similar_beers[i][0]))) }
        case_list.append(case)
        if i>=4:
            break
    result = (dict(zip(beer_dict, sim_score)))
    result2 = dict(zip(beer_dict, abv_score))

    return render_template("finaltable.html", result=result, result2=result2, beer_user_likes=beer_user_likes, beerlist1=beerlist1, case_list=case_list)

#Testing (Route is Hard Coded)
@app.route('/beer/', methods=["POST"])
def beer_input1():

    beer = request.form['mybeer']
    
    beerlist = pd.read_csv(cd+"/beer/static/df500.csv")
    beerlist1 = beerlist['beer_name']
    

    df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
    count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    cosine_sim.shape
    beer_user_likes = (beer)
    beer_index = get_index_from_title(beer_user_likes)
    similar_beers = list( enumerate(cosine_sim[beer_index]) )
    sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
    i=0
    beer_dict = []
    sim_score = []
    abv_score = []
    beer = {}
    beer['beer'] ={}
    beer['similarity']={}
    beer['abv']={}
    case_list=[]

    for i in range(len(sorted_similar_beers)):
        beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
        sim_score.append(sorted_similar_beers[i][1])
        abv_score.append(get_abv_from_index(sorted_similar_beers[i][0]))
        case = {'beer': get_title_from_index(sorted_similar_beers[i][0]), 'similarity': (sorted_similar_beers[i][1]).round(2), 'abv':(get_abv_from_index(sorted_similar_beers[i][0])), 'style':(get_beerstyle_from_index((sorted_similar_beers[i][0]))), 'brewery':(get_brewery_from_index((sorted_similar_beers[i][0]))) }
        case_list.append(case)
        if i>=4:
            break
    result = dict(zip(beer_dict, sim_score))
    result2 = dict(zip(beer_dict, abv_score))

    return render_template("finaltable.html", result=result, result2=result2, beer_user_likes=beer_user_likes, beerlist1=beerlist1, case_list=case_list)

if __name__ == "__main__":
    app.run(debug=True)