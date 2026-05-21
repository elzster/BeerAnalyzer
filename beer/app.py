from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

from .mlscript import recommender


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "static" / "df500.csv"

app = Flask(__name__)
app.config["SECRET_KEY"] = "7d441f27d441f27567d441f2b6176a"


def get_beer_list():
    beerlist = pd.read_csv(CSV_PATH)

    if "beer_name" not in beerlist.columns:
        raise ValueError("df500.csv must contain a 'beer_name' column.")

    return beerlist["beer_name"]


def render_recommendations(beer_name="Wachusett Larry"):
    beerlist1 = get_beer_list()

    try:
        case_list = recommender.recommend(beer_name, limit=5)
        error = None
    except ValueError:
        case_list = []
        error = f"Beer '{beer_name}' was not found. Please choose a beer from the list."

    result = {item["beer"]: item["similarity"] for item in case_list}
    result2 = {item["beer"]: item["abv"] for item in case_list}

    return render_template(
        "finaltable.html",
        result=result,
        result2=result2,
        beer_user_likes=beer_name,
        beerlist1=beerlist1,
        case_list=case_list,
        error=error,
    )


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


@app.route("/beer/", methods=["GET"])
def beer_default():
    return render_recommendations("Wachusett Larry")


@app.route("/beer/", methods=["POST"])
def beer_input():
    beer_name = request.form.get("mybeer", "Wachusett Larry").strip()

    if not beer_name:
        beer_name = "Wachusett Larry"

    return render_recommendations(beer_name)


if __name__ == "__main__":
    app.run(debug=True)
