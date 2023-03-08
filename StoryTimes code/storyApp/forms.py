from wtforms import Form , StringField ,PasswordField , SubmitField,validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4,max=25)])
    email = StringField('Email Address', [validators.Length(min=6,max=40)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message="Passwords doesn't match")
    ])
    password_confirm = PasswordField("Confirm Password")
    submit = SubmitField(label="Register")