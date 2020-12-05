"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, jsonify
#from HackDuke import app

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(debug=True)