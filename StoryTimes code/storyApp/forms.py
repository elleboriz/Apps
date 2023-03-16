from wtforms import StringField ,PasswordField , SubmitField
from wtforms.validators import DataRequired,Length , Email , EqualTo ,ValidationError
from flask_wtf import FlaskForm
from storyApp.models import User


class RegistrationForm(FlaskForm):


    username = StringField(label='Username' , validators = [Length(min=4 , max= 30,), DataRequired()])
    email = StringField(label='Email Address',  validators = [Email() , DataRequired()])
    password = PasswordField(label='New Password',validators =[Length(min=6) , DataRequired()])
    password_confirm = PasswordField(label="Confirm Password" , validators=[DataRequired(),EqualTo("password" , message="Sorry Passwords don't match")])
    submit = SubmitField(label="Create account")

    def validate_username(self , username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Sorry!! Username already exist, Please try a different Username')

    def validate_email_address(self , email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Sorry!! Email address already exist, Please try a different email address')

