from storyApp import app
from flask import request , flash ,redirect ,url_for
from storyApp.models import Story 
from flask_login import current_user
from storyApp import db , ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
from os import path


class SPECIAL_FUNC():
    
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
class Route_func():
    def add_story(addstory_form):
        if not current_user.is_authenticated:
            flash('You are not Logged in , Login in Other to AddStory' , category='danger')
            
        
        else:
            file = request.files['image']
            filestatus = True
            story_title = addstory_form.title.data
            story_title = story_title.lower()
            
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
                    flash('New Post Added', category='success')
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
                    
                    
        
