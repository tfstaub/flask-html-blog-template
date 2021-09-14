from flaskext.markdown import Markdown
from app import app
from flask import render_template

Markdown(app)


@app.route("/")
def home():
    with open("app/main/home.md", "r") as md:
        content = md.read()
    return render_template("main.html", text = content)


@app.route("/blog")
def blog():
    with open("app/main/blog.md", "r") as md:
        content = md.read()
    return render_template("main.html", text = content)


@app.route("/about")
def about():
    with open("app/main/about.md", "r") as md:
        content = md.read()
    return render_template("main.html", text = content)


@app.route("/blog/post")
def post():
    with open("app/posts/post.md", "r") as md:
        content = md.read()
    return render_template("post.html", text = content)


@app.route("/blog/anotherpost")
def anotherpost():
    with open("app/posts/anotherpost.md", "r") as md:
        content = md.read()
    return render_template("post.html", text = content)
