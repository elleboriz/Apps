from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///story_db.db"
db = SQLAlchemy(app)

from storyApp import routes

