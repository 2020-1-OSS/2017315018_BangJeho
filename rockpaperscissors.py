# list of play options
play = ["Rock", "Paper", "Scissors"]
# game rule
winning_rule = {"Rock": "Scissors", "Paper": "Rock",
                 "Scissors": "Papper"}
# assign a random play to the computer
computer = "Rock"
print('Computer: {}'.format(computer))
# get the user input
player = input("Rock,Paper, Scissors? ")
print('Player: {}'.format(player))
# tie
if player == computer:
     print("Tie!")
# you win
elif winning_rule[player] == computer:
     print("You win!")
# you lose
else:
     print("You lose!")
