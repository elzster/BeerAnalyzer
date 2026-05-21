from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

from .mlscript import recommender


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "static" / "df500.csv"

app = Flask(__name__)
app.config["SECRET_KEY"] = "beer-analyzer-secret-key"


def get_beer_list():
    beerlist = pd.read_csv(CSV_PATH)

    if "beer_name" not in beerlist.columns:
        raise ValueError("df500.csv must contain a 'beer_name' column.")

    return sorted(beerlist["beer_name"].dropna().unique())


def render_recommendations(beer_name="Wachusett Larry"):
    beerlist1 = get_beer_list()

    try:
        case_list = recommender.recommend(beer_name, limit=5)
        error = None
    except Exception:
        case_list = []
        error = (
            f"Beer '{beer_name}' was not found. "
            f"Please choose a beer from the list."
        )

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
    beer_name = request.form.get("mybeer", "").strip()

    if not beer_name:
        beer_name = "Wachusett Larry"

    return render_recommendations(beer_name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)