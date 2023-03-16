from storyApp import app , db
from flask import render_template ,  flash ,redirect ,url_for
from storyApp.models import Story ,User
from storyApp.forms import RegistrationForm

@app.route("/")
@app.route("/homepage")
def home_page():
    return render_template("home.html")


@app.route("/stories")
def story_page():

    stories = Story.query.all()
    return render_template("stories.html",stories = stories)


@app.route("/register" , methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit() :
        new_user = User(
            username = form.username.data ,
            email_address = form.email.data ,
            password = form.password.data
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('story_page'))

    if form.errors :
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template("register.html", form = form)
