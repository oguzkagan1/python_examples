#Phyton rock,paper,scissors game

import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
playing = True


while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

if player == computer:
    print("It's a tie!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "paper":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

else:
    print("You Lose!")
    



print(f"Player: {player}")
print(f"Computer: {computer}")