# list of play options
play = ["Rock", "Paper", "Scissors"]
# assign a random play to the computer
computer = "Rock"
print('Computer: {}'.format(computer))
# get the user input
player = "Paper"
print('Player: {}'.format(player))
# tie
if player == computer:
     print("Tie!")
# rock
elif player == "Rock":
     if computer == "Scissors":
         print("You win!")
     else:
         print("You lose!")
# paper
elif player == "Paper":
     if computer == "Rock":
         print("You win!")
     else:
         print("You lose!")
# scissors
elif player == "Scissors":
     if computer == "Paper":
         print("You win!")
     else:
         print("You lose!")
