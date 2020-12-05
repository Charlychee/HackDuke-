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
       poption1 = request.form["poption1"]
       poption2 = request.form["poption2"]
       coption1 = request.form["coption1"]
       upload = request.files['profilePic']
       print(poption1)
       print(poption2)
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)