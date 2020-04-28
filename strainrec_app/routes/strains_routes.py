from flask import Blueprint, render_template, redirect, jsonify

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
