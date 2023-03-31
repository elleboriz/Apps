from storyApp import db , bcrypt ,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    print(int(user_id))
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
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

    def check_password_match(self, password_to_check):
        return bcrypt.check_password_hash(self.password_hash , password_to_check)


class Story(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    uploaded_by = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.String(length=80), nullable=False)
    category = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(length=300) , nullable=True)
    body = db.Column(db.String(length=200), nullable=False , unique=True)
    likes = db.Column(db.Integer() , nullable= False , default = 0 )
    deslikes = db.Column(db.Integer() , nullable= False , default = 0 )
    img = db.Column(db.db.String() ,nullable=True)
    img_name = db.Column(db.String() ,nullable=True)
    mimetype = db.Column(db.String() ,nullable=True)

    
    def addlike(self):
        self.likes=self.likes+1


    def __repr__(self):
        return f"Story {self.title}"
    
