from flask import Blueprint, render_template, redirect, jsonify

# TODO: import model

strains_routes = Blueprint("strains_routes", __name__)


@strains_routes.route("/")
def home():
    return "home"


@strains_routes.route("/strains.json")
def strains():
    strains_records = [
        {'id': 1, 'name': "name1", 'description': "describe name1"}
    ]
    return jsonify(strains_records)


@strains_routes.route("/strains/recommend/<input_string>")
def recommend(input_string=None):
    input = {"input": str(input_string)}
    print(input)
    response = [
        input,
        {"recommend": "recommend string"}
    ]
    return jsonify(response)
