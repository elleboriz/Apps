from storyApp import app , db ,ALLOWED_EXTENSIONS
from flask import render_template ,  flash ,redirect ,url_for ,request 
from flask_login import login_user , logout_user  , current_user 
from storyApp.models import Story ,User 
from storyApp.forms import RegistrationForm , LoginForm ,LikeForm , DeslikeForm ,Add_storyForm
from storyApp.special_func import SPECIAL_FUNC
from werkzeug.utils import secure_filename
from os import path


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/stories", methods=["GET", "POST"])
def story_page():
    
    #impressions on story (like and deslike)
    
    like = LikeForm()
    deslike = DeslikeForm()
    addstory_form = Add_storyForm()
    if like.validate_on_submit() :        
        pass
    if deslike.validate_on_submit():
        pass
    if request.method == "POST" :
        if addstory_form.validate_on_submit() :
            new_story = Story(title = addstory_form.title.data , category = addstory_form.category.data, description = addstory_form.description.data, body=addstory_form.body.data )
            db.session.add(new_story)
            db.commit()
        
        
            
            
            redirect(url_for('story_page'))
    
    
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
    stories = Story.query.all() 
    addstory_form = Add_storyForm()
    
    if request.method == 'POST' : 
        if not current_user.is_authenticated:
            flash('You are not Logged in , Login in Other to AddStory' , category='danger')
            
        
        else:
            file = request.files['image']
            filestatus = True
            story_title = addstory_form.title.data
            if 'image' not in request.files or file.filename == '':
                filestatus = False
                flash('Story uploaded without cover image' , category='warning')
                
                
            if SPECIAL_FUNC.allowed_file(file.filename) and filestatus :
                filename = secure_filename(file.filename)
                file.save(path.join(app.config['UPLOAD_FOLDER'], filename))          
            
                new_story = Story(title = addstory_form.title.data , category = addstory_form.category.data, description = addstory_form.description.data, body=addstory_form.body.data , img = filename )
                db.session.add(new_story)
                
                
                new_story_obj = Story.query.filter_by(title = story_title).first()
                if(new_story_obj):
                    new_story_obj.uploaded_by = current_user.id
                    db.session.commit()
                    
                    return redirect(url_for('story_page'))
            else:
                new_story = Story(title = addstory_form.title.data , category = addstory_form.category.data, description = addstory_form.description.data, body=addstory_form.body.data )
                db.session.add(new_story)
                
            
            
                """_summary_  assigning ownership of each post to the user that uploaded it. using the story title to reference ownership for the user that posted it.

                Args:
                    None(_type_):instance of Add_storyForm() from POST request client .
                    _description_ 
                """
                #new_story_title =  request.form.get('addstory')
                new_story_obj = Story.query.filter_by(title = story_title).first()
                if(new_story_obj):
                    new_story_obj.uploaded_by = current_user.id
                    db.session.commit()
                    
                    return redirect(url_for('story_page'))
        
            
        
        
    return render_template('addstory.html', addstory_form=addstory_form , stories=stories)
    
    
