import os
import requests

from flask import Flask,render_template,jsonify,request,redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Check in case JavaScript is disabled or fails
    if request.method == "POST":
        user = request.form.get("user")
        if user in users:
            error = "That username is taken"
            return render_template("error.html", error=error)
        elif user == "":
            error = "Please enter a username"
            return render_template("error.html", error=error)
        else:
            users.append(user)


    return render_template("chat.html", user=user)

@app.route("/check", methods=["POST"])
def check():
    user = request.form.get("user")
    if user in users:
        return jsonify({"success":False})
    else:
        return jsonify({"success":True})
