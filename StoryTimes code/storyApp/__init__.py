from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///story_db.db"
app.config['SECRET_KEY'] = '0fdee5a425d992541bf7265c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from storyApp import routes


