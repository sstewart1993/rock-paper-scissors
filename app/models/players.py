from app.models.players_class import *
import random

player1 = Players("Steve", "rock")
player2 = Players("Rob", "scissors")

players = [player1, player2]
choice = ["Rock", "Paper", "Scissors"]

#  FUNCTION TO CREATE A RANDOM COMPUTER SELECTION
def get_computer_move():
    choice = ["Rock", "Paper", "Scissors"]
    return choice[random.randint(0,2)]

def get_player_winner(player1_choice, player2_choice):
    winner = "player 2"

    if player1_choice == player2_choice:
        winner = "tie"
    elif player1_choice == "Rock" and player2_choice == "Scissors":
        winner = "player 1"
    elif player1_choice == "Scissors" and player2_choice == "Paper":
        winner = "player 1"
    elif player1_choice == "Paper" and player2_choice == "Rock":
        winner = "player 1"
    return winner


def get_computer_winner(player_choice, computer_choice):
    winner = "computer"

    if player_choice == computer_choice:
        winner = "tie"
    elif player_choice == "Rock" and computer_choice == "Scissors":
        winner = "player"
    elif player_choice == "Scissors" and computer_choice == "Paper":
        winner = "player"
    elif player_choice == "Paper" and computer_choice == "Rock":
        winner = "player"
    return winner






# FULL RUNNING RPS GAME FOR PYTHON BELOW


# while True:
# print("choose your weapon")
# player = input()
# player = player.lower() 
# print("my choice is ", player)

# choices = ["rock", "paper", "scissors"]

# computer_choice = random.choice(choices)
# print("player 2's choice is", computer_choice)

# if player in choices:
#     if player == computer_choice:
#          print("tie")
#     if player == "rock":
#         if computer_choice == "paper":
#             print ("loser")
#     elif computer_choice == "scissors":
#         print ("winnner")

#     if player == "paper":
#         if computer_choice == "rock":
#             print ("winner")
#         elif computer_choice == "scissors":
#             print ("loser")

#     if player == "scissors":
#         if computer_choice == "rock":
#             print ("loser")
#         elif computer_choice == "paper":
#             print("winner")

# else:
#     print("choose again weapon not avaiable")

# print("")