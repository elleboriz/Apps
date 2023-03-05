from storyApp import app
from flask import render_template
from storyApp.models import Story


@app.route("/")
@app.route("/homepage")
def StoryTimes_home():
    return render_template("home.html")


@app.route("/stories")
def StoryTimes_story():

    stories = Story.query.all()
    return render_template("stories.html",stories = stories)
