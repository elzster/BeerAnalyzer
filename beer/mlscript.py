from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "static" / "df500.csv"


class BeerRecommender:
    def __init__(self, csv_path=CSV_PATH):
        self.csv_path = Path(csv_path)

        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")

        self.df = pd.read_csv(self.csv_path)

        self.df.columns = self.df.columns.str.strip()

        required_columns = [
            "beer_name",
            "beer_abv",
            "beer_style",
            "brewery_name",
            "combined_features",
        ]

        missing_columns = [
            column for column in required_columns
            if column not in self.df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns in df500.csv: {missing_columns}. "
                f"Available columns: {list(self.df.columns)}"
            )

        self.df = self.df.dropna(subset=["beer_name"]).reset_index(drop=True)

        self.df["combined_features"] = (
            self.df["combined_features"]
            .fillna("")
            .astype(str)
        )

        self.count_matrix = CountVectorizer(
            stop_words="english"
        ).fit_transform(self.df["combined_features"])

        self.cosine_sim = cosine_similarity(self.count_matrix)

    def get_index_from_title(self, beer_name):
        beer_name = str(beer_name).strip().lower()

        matches = self.df.index[
            self.df["beer_name"].astype(str).str.strip().str.lower() == beer_name
        ].tolist()

        if not matches:
            raise ValueError(f"Beer not found: {beer_name}")

        return matches[0]

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
            row = self.df.iloc[index]

            recommendations.append(
                {
                    "beer": row["beer_name"],
                    "similarity": round(float(score), 3),
                    "abv": row["beer_abv"],
                    "style": row["beer_style"],
                    "brewery": row["brewery_name"],
                }
            )

        return recommendations


recommender = BeerRecommender()


def similarity_model(parameter):
    return recommender.recommend(parameter)


def print_statement(parameter):
    recommendations = recommender.recommend(parameter)

    print(f"\nTop recommendations for '{parameter}':\n")

    for item in recommendations:
        print(
            f"{item['beer']} | "
            f"Similarity: {item['similarity']} | "
            f"ABV: {item['abv']} | "
            f"Style: {item['style']} | "
            f"Brewery: {item['brewery']}"
        )