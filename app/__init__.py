from flask import Flask
from app import views
from app.database import db, migrate

def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.index_page)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    migrate.init_app(app, db)

    return app