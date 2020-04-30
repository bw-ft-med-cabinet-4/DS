from flask import Blueprint, render_template, redirect, jsonify, Response
import json
from bson import json_util
from strainrec_app.recommender import load_model, data
from strainrec_app.leafly_recommender import load_model as leafly_model
from strainrec_app.services.mongo_service import strains_collection

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
    strains_info = data.iloc[recommendations[0]
                             ].reset_index().to_json(orient='records', indent=2)

    print("RESULT:", strains_info)

    return jsonify(json.loads(strains_info))


@strains_routes.route("/api/v1/strains")
def api_strains():
    srecords = strains_collection.find({'isStub': False})
    resp = Response(json.dumps(
        {'data': list(srecords)}, default=json_util.default), mimetype='application/json')
    return resp


@strains_routes.route("/api/v1/recommend/<input_string>")
def api_recommend(input_string=None):
    input_str = str(input_string)
    print("INPUT: ", input_str)

    package = leafly_model()
    input_vec = package['tfidf'].transform([input_str])
    predictions = package['model'].kneighbors(input_vec.todense())
    recommendations = predictions[1]
    strains_info = data.iloc[recommendations[0]
                             ].reset_index().to_json(orient='records', indent=2)

    print("RESULT:", strains_info)

    return jsonify(json.loads(strains_info))
