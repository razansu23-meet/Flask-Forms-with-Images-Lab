from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
import pyrebase
import os

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

UPLOAD_FOLDER = 'static/images/posts'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html')


@app.route('/add_post')  # '/' for the default page
def add_post():
    return render_template('add_post.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
