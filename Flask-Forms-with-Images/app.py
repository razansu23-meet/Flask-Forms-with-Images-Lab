from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
import pyrebase
import os

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

UPLOAD_FOLDER = 'static/images/fulls'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']



config = {
  "apiKey": "AIzaSyDI7jGVXg9tYZrnR-u97K8iYBfOzCVe2WM",
  "authDomain": "flask-images-lab.firebaseapp.com",
  "databaseURL": "https://flask-images-lab-default-rtdb.europe-west1.firebasedatabase.app/",
  "projectId": "flask-images-lab",
  "storageBucket": "flask-images-lab.appspot.com",
  "messagingSenderId": "242861158169",
  "appId": "1:242861158169:web:1ee20f4464290ba67a9f88",
  "measurementId": "G-PJDKZG0E33"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


# @app.route('/')  # '/' for the default page
# def all_posts():

#     return render_template('index.html')


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        name = request.form['name']
        photo = request.files['post']
        upload_file(photo)
        post = {"name": name, "photo": photo.filename}
        db.child("Posts").push(post)
        return render_template('index.html')
    else:
        return render_template('add_post.html')
@app.route('/')
def all_posts():
    posts = db.child("Posts").get().val()
    return render_template("index.html", posts = posts)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




def upload_file(file):
    if request.method == 'POST':
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(UPLOAD_FOLDER + "/" + filename)

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
