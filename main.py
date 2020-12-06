"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, jsonify
#from HackDuke import app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    diagnosis = db.Column(db.String(), nullable=False)
    purpose = db.Column(db.String(10))
    contact = db.Column(db.String(10))
    picture = db.Column(db.String(10), default='default.png')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.picture}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}"



@app.route("/registration", methods=["POST", "GET"])
def submit_page():
    if request.method == "POST":
       name = request.form["name"]
       dob = request.form["dob"]
       diagnosis = request.form["diagnosis"]
       purpose = request.form.getlist("purpose")
       contact = request.form.getlist("contact")
       upload = request.files['profilePic']
    return render_template("registration.html")


@app.route("/match", methods=["POST", "GET"])
def match_page():
    return render_template("match.html")

if __name__ == "__main__":
    app.run(debug=True)
