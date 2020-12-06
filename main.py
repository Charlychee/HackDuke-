"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, jsonify
#from HackDuke import app
import sqlite3 as sql
from sqlite import removeUser

app = Flask(__name__)


@app.route("/registration", methods=["POST", "GET"])
def submit_page():
    if request.method == "POST":
       email = request.form["email"]
       pwd = request.form["pwd"]
       name = request.form["name"]
       #dob = request.form["dob"]
       #diagnosis = request.form["diagnosis"]
       #purpose = request.form.getlist("purpose")
       #contact = request.form.getlist("contact")
       #upload = request.files['profilePic']
       with sql.connect("database.db") as con:
           cur = con.cursor()
           cur.execute("INSERT INTO users (email, pwd, name) VALUES (?,?,?)",(email, pwd, name) )
           con.commit()
    return render_template("registration.html")

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)


@app.route("/match", methods=["POST", "GET"])
def match_page():
    return render_template("match.html")

@app.route("/",methods=['GET', 'POST'])
def home_page():
    return render_template("home.html")

@app.route("/media",methods=['GET', 'POST'])
def media_page():
    return render_template("media.html")

@app.route("/delete/<name>",methods=['GET'])
def delete_user(name):
    removeUser(name)
    return name + ' will be removed from the table'

if __name__ == "__main__":
    app.run(debug=True)
