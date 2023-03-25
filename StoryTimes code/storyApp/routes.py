from storyApp import app , db
from flask import render_template ,  flash ,redirect ,url_for ,request
from flask_login import login_user , logout_user  , current_user
from storyApp.models import Story ,User 
from storyApp.forms import RegistrationForm , LoginForm ,LikeForm , DeslikeForm , Add_storyForm
from storyApp.special_func import *


@app.route("/")
@app.route("/homepage")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/stories", methods=["GET", "POST"])
def story_page():
    
    #impressions on story (like and deslike)
    like = LikeForm()
    deslike = DeslikeForm()
    if like.validate_on_submit() :        
        pass
    elif deslike.validate_on_submit():
        pass
    
    stories = Story.query.all()
    
    return render_template("stories.html",stories = stories , like=like, deslike=deslike)


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
        
        #login new registered user after registration and redirect to story page 
        
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_match(password_to_check = form.password.data):
            login_user(attempted_user)
        flash("Account created succesfully ", category='success')
        return redirect(url_for('story_page'))

    if form.errors :
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template("register.html", form = form)

@app.route("/login" , methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    
    if form.validate_on_submit() and request.method == "POST" :
        
        #"""verify that username in database by trying to query it """
        #  veryfy password of user using (check_password_match)function in models.py created  with bycrpt parameters
        
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_match(password_to_check = form.password.data):
            login_user(attempted_user)
            flash(f"welcome  {attempted_user.username}", category='info')
            return redirect(url_for('story_page'))

        else:
            flash(f'incorrect Username or Password', category="danger")
    if form.errors :
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You are logged out",category="info")
    return redirect(url_for("home_page"))

@app.route('/addstory', methods=['POST','GET'])
def addstory():
    form = Add_storyForm()
    return render_template('addstory.html', form=form)
