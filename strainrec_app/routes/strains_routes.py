from flask import Blueprint, render_template, redirect, jsonify
import json
from strainrec_app.recommender import load_model, data

strains_routes = Blueprint("strains_routes", __name__)


@strains_routes.route("/")
def home():
    return "home"


@strains_routes.route("/strains.json")
def strains():
    print(data)
    print(dir(data))
    strains_records = data.to_dict()
    return jsonify(strains_records)


@strains_routes.route("/strains/recommend/<input_string>")
def recommend(input_string=None):
    input = {"input": str(input_string)}
    print(input)

    package = load_model()
    input_vec = package['tfidf'].transform([str(input_string)])
    predictions = package['model'].kneighbors(input_vec.todense())
    recommendations = predictions[1]
    strains_info = []
    for i in range(4):
        info = data.iloc[recommendations[0][i]]
        strains_info.append(info)

    print("RESULT:", strains_info)

    return jsonify(str(strains_info))
