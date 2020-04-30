from flask import Blueprint, render_template, redirect, jsonify
import json
from strainrec_app.recommender import load_model, data
from strainrec_app.services.mongo_service import strains_records as srecords

strains_routes = Blueprint("strains_routes", __name__)


@strains_routes.route("/")
def home():
    return render_template("home.html")


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
    strains_info = {}
    for i in range(4):
        info = data.iloc[recommendations[0][i]]
        strains_info[i] = info.to_json()

    print("RESULT:", strains_info)

    return json.dumps(strains_info)


@strains_routes.route("/api/v1/strains")
def api_strains():
    return jsonify(str(srecords))
