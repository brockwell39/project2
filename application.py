import os
import requests

from flask import Flask,render_template,jsonify,request,redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []
channelsi =[]
messages =["cat"]

@app.route("/", methods=["POST","GET"])
def index():
        return render_template("chat.html",channelsi=channelsi)



@app.route("/newuser", methods=["POST","GET"])
def newuser():
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
                return redirect("/chat")

        return render_template("index.html")

@app.route("/chat", methods=["POST","GET"])
def chat():
    print(channelsi)
    return render_template("chat.html",channelsi=channelsi)

@app.route("/channels/<string:channel_id>", methods=["POST","GET"])
def channels(channel_id):
    # Check in case JavaScript is disabled or fails
    return render_template("/channels.html",channelsi=channelsi)

@app.route("/channelcheck", methods=["POST","GET"])
def channelcheck():
    print("test")
    channel = request.form.get("channel")
    if channel in channelsi:
        return jsonify({"success":False})
    else:
        channelsi.append(channel)
        return jsonify({"success":True})


@app.route("/check", methods=["POST"])
def check():
    print("running")
    user = request.form.get("user")
    if user in users:
        return jsonify({"success":False})
    else:
        return jsonify({"success":True})

@socketio.on("chat")
def vote(data):
    message = data["message"]
    user = data["user"]
    message = message + "from" + user
    messages.append(message)
    print("mes",messages)
    print(user)
    emit("announce message", messages , broadcast=True)
