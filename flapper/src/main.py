from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template("index.html", users=users)
    else:
        return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username != "flapper":
        return render_template("auth_username_fail.html")
    
    if ' ' in password or 'or' in password or 'OR' in password or '-' in password:
        return render_template("auth_blacklist.html")

    try:
        if dbHandler.loginUser(username, password):
            return render_template("auth_success.html")
        else:
            return render_template("auth_pwd_fail.html")
    except Exception as e:
        return str(e)
