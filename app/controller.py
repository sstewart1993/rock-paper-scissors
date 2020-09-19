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
@app.route('/submit/<choice>')
def submit(choice):
    player_choice = choice.lower()    
    computer_choice = get_computer_move()
    winner = get_winner(player_choice, computer_choice)
    return render_template("submit.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)
    # return render_template("submit.html", title="Move", players=players)
