# strainrec_app/recommender.py
import os
import pickle
import pandas as pd

from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

MODEL_FILEPATH = os.path.join(os.path.dirname(
    __file__), "..", "models", "latest_model.plk")


data = pd.read_csv(os.path.join(os.path.dirname(
    __file__), "..", "data", "strains_text.csv"))


def train_and_save_model():
    print("TRAINING THE MODEL...")
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    vectors = tfidf.fit_transform(data["Combined"])
    vectors = pd.DataFrame(vectors.todense())

    recommender = NearestNeighbors(n_neighbors=4, algorithm='kd_tree')

    model = recommender.fit(vectors)

    print("SAVING THE MODEL...")
    with open(MODEL_FILEPATH, "wb") as model_file:
        pickle.dump({"model": model, "tfidf": tfidf}, model_file)
    return model, tfidf


def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model


if __name__ == "__main__":
    print(data)

    train_and_save_model()

    package = load_model()
    recommender = package['model']
    print("RECOMMENDER:", recommender)
    input_vec = package['tfidf'].transform(['happy uplifted'])
    predictions = recommender.kneighbors(input_vec.todense())
    recommendations = predictions[1]
    strains_info = []
    for i in range(4):
        info = data.iloc[recommendations[0][i]]
        strains_info.append(info)

    print("RESULT:", strains_info)
