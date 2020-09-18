from app import app
from flask import render_template, request
from app.models.players_class import *
from app.models.players import *



@app.route("/")
def home():
    return render_template("index.html", title="Home", players=players)

