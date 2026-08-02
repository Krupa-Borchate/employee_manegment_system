from flask import Flask
from config import Config
from app.extentions import db, migrate

def create_app():
    app = Flask(__name__)


    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.employee import Employee

    @app.route("/")
    def home():
        return "<h1>Welcome to the Employee Management System</h1>"

    return app