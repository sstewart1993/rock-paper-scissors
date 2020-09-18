from app import app
from flask import render_template, request
from app.models.players_class import *
from app.models.players import *


@app.route("/")
def home():
    return render_template("index.html", title="Home", players=players)

import random

while True:
    print("choose your weapon")
    player = input()
    player = player.lower() 
    print("my choice is ", player)

    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    print("player 2's choice is", computer_choice)

    if player in choices:
        if player == computer_choice:
             print("tie")
        if player == "rock":
            if computer_choice == "paper":
                print ("loser")
            elif computer_choice == "scissors":
                print ("winnner")

        if player == "paper":
            if computer_choice == "rock":
                print ("winner")
            elif computer_choice == "scissors":
                print ("loser")

        if player == "scissors":
            if computer_choice == "rock":
                print ("loser")
            elif computer_choice == "paper":
                print("winner")

    else:
        print("choose again weapon not avaiable")

    print("")