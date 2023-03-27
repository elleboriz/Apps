from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///story_db.db"
app.config['SECRET_KEY'] = '0fdee5a425d992541bf7265c'

UPLOAD_FOLDER = r'C:\Users\gmb\Documents\StoryTimes\storyApp\static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


#initializing routes to get all pages
from storyApp import routes




