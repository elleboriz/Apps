from storyApp import app , db
from flask import render_template , request , flash ,redirect ,url_for
from storyApp.models import Story ,User
from storyApp.forms import RegistrationForm

@app.route("/")
@app.route("/homepage")
def StoryTimes_home():
    return render_template("home.html")


@app.route("/stories")
def StoryTimes_story():

    stories = Story.query.all()
    return render_template("stories.html",stories = stories)


@app.route("/register" , methods=["GET", "POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(form.username.data , form.email.data ,form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"welcome {user.username}" ," info")
        return redirect(url_for('StoryTimes_story'),200)
    else:
        return render_template("register.html", form = form)
