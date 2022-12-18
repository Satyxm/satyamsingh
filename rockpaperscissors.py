import random

while True:
     choices = ["rock", "paper", "scissors"]
     player = None

     computer = random.choice(choices)

     while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

     if player == computer:
      print("computer: ", computer)
      print("player: ", player)
      print("Tie!")
     elif player == "rock":
      if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You Lose!")
      if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win!")
     elif player == "paper":
       if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win!")
     if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You Lose!")
     elif player == "scissors":
      if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win!")
      if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("You Lose!")

     play_again = input("Do you want to play again? (yes/no): ").lower()
     if play_again != "yes":
        break
print("byee")

