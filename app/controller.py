from app import app
from flask import render_template, request
from app.models.players_class import *
from app.models.players import *
import random


# CREATES HOME PAGE
@app.route("/")
def home():
    return render_template("index.html", title="Home", players=players)

@app.route("/computer")
def play_computer():
    return render_template("computer.html", title="Skynet", players=players)

@app.route("/player1")
def play_person():
    return render_template("player1.html", title= "Player1", players=players)


@app.route('/player1/<choice>')
def submit_player1(choice):
    player1_choice = choice.capitalize()
    return render_template("player2.html", player1_choice=player1_choice)

@app.route('/player2/<choice>')
def submit_player2(choice):
    submit_player1(choice)  
    player2_choice = choice.capitalize()
    winner = get_player_winner(submit_player1, player2_choice)
    return render_template("friends.html", winner=winner, player1_choice=submit_player1 , player2_choice=player2_choice)

@app.route('/submit/<choice>')
def submit(choice):
    player_choice = choice.capitalize()   
    computer_choice = get_computer_move()
    winner = get_computer_winner(player_choice, computer_choice)
    return render_template("submit.html", winner=winner, player_choice=player_choice, computer_choice=computer_choice)
