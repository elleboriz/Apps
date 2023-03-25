from wtforms import StringField ,PasswordField , SubmitField , TextAreaField ,SelectField ,FileField
from wtforms.validators import DataRequired,Length , Email , EqualTo ,ValidationError
from flask_wtf import FlaskForm
from storyApp.models import User


class RegistrationForm(FlaskForm):


    username = StringField(label='Username *' , validators = [Length(min=4 , max= 30,), DataRequired()])
    email = StringField(label='Email Address *',  validators = [Email() , DataRequired()])
    password = PasswordField(label='New Password *',validators =[Length(min=6) , DataRequired()])
    password_confirm = PasswordField(label="Confirm Password *" , validators=[DataRequired(),EqualTo("password" , message="Sorry Passwords don't match")])
    submit = SubmitField(label="Create account")

    def validate_username(self , username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Sorry!! Username already exist, Please try a different Username')

    def validate_email_address(self , email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Sorry!! Email address already exist, Please try a different email address')

class LoginForm(FlaskForm):
    username = StringField(label='Username *', validators=[Length(min=3 ,  message='username too short') , DataRequired()])
    password = StringField(label='Password *' , validators=[Length(min=6, message='Password too short') , DataRequired()])
    submit = SubmitField(label='Login')
    
 
class Add_storyForm(FlaskForm):
    title = StringField(label="Title *" , validators=[Length(min=3 , max=30) ,DataRequired() ] ) 
    description = TextAreaField(label="Description *" , validators=[DataRequired() ] ) 
    body = TextAreaField(label="Body *" , validators=[DataRequired()] ) 
    category = SelectField(label="Category *" , choices=['funny','wisdom','morals','love'],validators=[DataRequired()] ) 
    image = FileField(label="Cover image [ optional ]" , validators=[DataRequired()] ) 
    
    submit = SubmitField(label='Add Story')
    
class LikeForm(FlaskForm):
    submit = SubmitField(label='')

class DeslikeForm(FlaskForm):
    submit = SubmitField(label='') 
