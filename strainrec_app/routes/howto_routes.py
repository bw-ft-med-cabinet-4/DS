from flask import Blueprint, render_template

howto_routes = Blueprint("howto_routes", __name__)


@howto_routes.route("/quickstart")
def getting_started():
    return render_template("quickstart.html")
