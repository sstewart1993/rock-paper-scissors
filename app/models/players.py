from app.models.players_class import *
import random

player1 = Players("Steve", "rock")
player2 = Players("Rob", "scissors")

players = [player1, player2]
choice = ["rock", "paper", "scissors"]

#  FUNCTION TO CREATE A RANDOM COMPUTER SELECTION
def get_computer_move():
    choice = ["rock", "paper", "scissors"]
    return choice[random.randint(0,2)]

def get_winner(player_choice, computer_choice):
    winner = "computer"

    if player_choice == computer_choice:
        winner = "tie"
    if player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
    if player_choice == "paper" and computer_choice == "rock":
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