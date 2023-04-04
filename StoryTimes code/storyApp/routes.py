from storyApp import app , db 
from flask import render_template ,  flash ,redirect ,url_for ,request 
from flask_login import login_user , logout_user  ,current_user
from storyApp.models import Story ,User 
from storyApp.forms import RegistrationForm , LoginForm ,LikeForm , DeslikeForm ,Add_storyForm
from storyApp.special_func import  Routes_func 


@app.route("/",methods=["GET", "POST"])
def home_page():
    
    
    addstory_form = Add_storyForm()
    if addstory_form.validate_on_submit() :
        if current_user.is_authenticated:
            Routes_func.add_story(addstory_form)
            flash('New Post Added', category='info')
            return redirect(url_for('story_page')) 

    #render Stories
    stories = Story.query.all()
    
    return render_template("home.html",stories = stories ,addstory_form=addstory_form)


@app.route("/stories", methods=["GET", "POST"])
def story_page():
    like = LikeForm()
    deslike = DeslikeForm()
    addstory_form = Add_storyForm()
    
    
    #Add new story from StoryPage
    
    if addstory_form.validate_on_submit() :
        if current_user.is_authenticated:
            Routes_func.add_story(addstory_form)
            flash('New Post Added', category='info')
            return redirect(url_for('story_page')) 
        else:
            flash('You are not Logged in , Login in Other to AddStory' , category='danger')    
    
    
    #impressions on story (like and deslike)
    if like.validate_on_submit() :        
        pass
    if deslike.validate_on_submit():
        pass
    
    #render Stories
    stories = Story.query.all()
    
    return render_template("stories.html",stories = stories , like=like, deslike=deslike , addstory_form=addstory_form)


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
        
        Routes_func.loginto_account(form)
        return redirect(url_for('story_page'))

    if form.errors :
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template("register.html", form = form)

@app.route("/login" , methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    
    if form.validate_on_submit() and request.method == "POST" :
        Routes_func.loginto_account(form)
        return redirect(url_for('story_page'))
        
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
    stories = Story.query.all() 
    addstory_form = Add_storyForm()
    
      
    if request.method == 'POST' :
        if current_user.is_authenticated:
            Routes_func.add_story(addstory_form)
            flash('New Post Added', category='info')
            return redirect(url_for('story_page')) 
        else:
            flash('You are not Logged in , Login in Other to AddStory' , category='danger')     
   
    return render_template('addstory.html', addstory_form=addstory_form , stories=stories)
    
    
