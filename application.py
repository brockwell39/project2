import os
import requests

from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    user = request.form.get("user")
    print(user)
    return jsonify({"success":True})
