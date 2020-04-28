from flask import Flask
import os
from strainrec_app.routes.strains_routes import strains_routes
# TODO: models.py
# from strainrec_app.models import db, migrate


def create_app():
    app = Flask(__name__)

    # app.config["SQLALCHEMY_DATABASE_URI"]
    # db.init_app(app)
    # migrate.init_app(app.db)

    app.register_blueprint(strains_routes)
    return app


if __name__ == "__name__":
    sr_app = create_app()
    sr_app.run(debug=True)
