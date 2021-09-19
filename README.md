# Flask HTML Markdown Blog Template

This template is used to create a blog to display markdown files as HTML leveraging the Flask framework.  

## Get Started

Clone repo.  
Create virtual environment.  
pip install -r requirements.txt  

### Run in Linux/MacOS

Set the environment variables  
export FLASK_APP=run.py  
export FLASK_ENV=development  

### Run in Windows

Set the environment variables  
set FLASK_APP=run.py  
set FLASK_ENV=development  

## Customize template

Add images for the site to app/static/img  
Add or modify css for the site by adding or modifying the files in app/static/img  
Add javascript for the site to app/static/js  

Update Title between {% block title %} {% endblock %} in app/templates/main.html and app/templates/post.html  

### Add a post

Add markdown file to app/posts  
Add an entry in app/main/blog.md for the post  
Update app/blog.py with a new route including the URI of your new post that is referenced by the entry in app/main/blog.md  

## References

[Markdown](https://pythonhosted.org/Flask-Markdown/)  
[Flask](https://flask.palletsprojects.com/en/2.0.x/)  