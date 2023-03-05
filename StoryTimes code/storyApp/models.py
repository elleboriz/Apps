from storyApp import db


class Story(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    title = db.Column(db.String(length=80), nullable=False)
    category = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False , unique=True)
    img = db.Column(db.LargeBinary)
    img_name = db.Column(db.String())
    mimetype = db.Column(db.String())

    def __repr__(self):
        return f"Story {self.title}"