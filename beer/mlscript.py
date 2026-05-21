from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "static" / "df500.csv"


class BeerRecommender:
    def __init__(self, csv_path=CSV_PATH):
        self.df = pd.read_csv(csv_path).reset_index(drop=True)

        if "combined_features" not in self.df.columns:
            raise ValueError("df500.csv must contain a 'combined_features' column.")

        self.df["combined_features"] = self.df["combined_features"].fillna("")

        self.count_matrix = CountVectorizer().fit_transform(self.df["combined_features"])
        self.cosine_sim = cosine_similarity(self.count_matrix)

    def get_index_from_title(self, beer_name):
        matches = self.df.index[
            self.df["beer_name"].astype(str).str.lower() == str(beer_name).lower()
        ].tolist()

        if not matches:
            raise ValueError(f"Beer not found: {beer_name}")

        return matches[0]

    def get_title_from_index(self, index):
        return self.df.loc[index, "beer_name"]

    def get_abv_from_index(self, index):
        return self.df.loc[index, "beer_abv"]

    def get_beerstyle_from_index(self, index):
        return self.df.loc[index, "beer_style"]

    def get_brewery_from_index(self, index):
        return self.df.loc[index, "brewery_name"]

    def recommend(self, beer_name, limit=5):
        beer_index = self.get_index_from_title(beer_name)

        similar_beers = list(enumerate(self.cosine_sim[beer_index]))
        sorted_similar_beers = sorted(
            similar_beers,
            key=lambda item: item[1],
            reverse=True,
        )[1 : limit + 1]

        recommendations = []

        for index, score in sorted_similar_beers:
            recommendations.append(
                {
                    "beer": self.get_title_from_index(index),
                    "similarity": round(float(score), 2),
                    "abv": self.get_abv_from_index(index),
                    "style": self.get_beerstyle_from_index(index),
                    "brewery": self.get_brewery_from_index(index),
                }
            )

        return recommendations


recommender = BeerRecommender()


def similarity_model(parameter):
    return recommender.recommend(parameter)


def get_title_from_index(index):
    return recommender.get_title_from_index(index)


def get_index_from_title(beer_name):
    return recommender.get_index_from_title(beer_name)


def get_abv_from_index(index):
    return recommender.get_abv_from_index(index)


def get_beerstyle_from_index(index):
    return recommender.get_beerstyle_from_index(index)


def get_brewery_from_index(index):
    return recommender.get_brewery_from_index(index)


def print_statement(parameter):
    recommendations = recommender.recommend(parameter)

    print(f"The top 5 beers similar to {parameter} are:")

    for item in recommendations:
        print(
            f"Beer Name: {item['beer']}, "
            f"Similarity Score: {item['similarity']}, "
            f"ABV: {item['abv']}, "
            f"Style: {item['style']}, "
            f"Brewery: {item['brewery']}"
        )
