from game import Score_display, game ,finalScore
from scores import scoreboard
options=["STONE","PAPER","SCISSOR"]
round = 1
print("Enter your name:")
Name=input()
computer=0
player=0

Score_display(computer,player,Name)
print("Hello",Name)
game(options,Name,round,computer,player)

Score = finalScore()
print()
print(">>>>>SCOREBOARD<<<<<")
print()
scoreboard(Name,Score)