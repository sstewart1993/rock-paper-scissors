from app import app
from flask import render_template, request
from app.models.players_class import *
from app.models.players import *
import random


# CREATES HOME PAGE
@app.route("/")
def home():
    return render_template("index.html", title="Home", players=players)


#  CREATES A NEW SUBMIT PAGE LINKED IN WITH THE SUBMIT BUTTON 
@app.route("/submit")
def submit():
    return render_template("submit.html", title="Move", players=players)