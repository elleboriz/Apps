from storyApp import db , bcrypt
from flask_bcrypt import Bcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    username = db.Column(db.String(length=15) , nullable=False,unique=True)
    email_address = db.Column(db.String(length=45) , nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60) , nullable=False)
    uploaded_stories = db.relationship("Story", backref="uploaded_by_user" , lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,password_to_encrypt):
        self.password_hash = bcrypt.generate_password_hash(password_to_encrypt)


class Story(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    uploaded_by = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.String(length=80), nullable=False)
    category = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(length=300) , nullable=True)
    body = db.Column(db.String(length=200), nullable=False , unique=True)
    img = db.Column(db.db.String())
    img_name = db.Column(db.String())
    mimetype = db.Column(db.String())

    def __repr__(self):
        return f"Story {self.title}"
