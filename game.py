import random
options=["STONE","PAPER","SCISSOR"]
round = 1
print("Enter your name:")
Name=input()
computer=0
player=0
def checkStartCorrect(inpt):
    f = False
    if inpt!="":
        f = True
    return f

def Score_display() :
    print("Score :")
    print("Computer:",computer," ",Name,":",player)
print("Hello",Name)


def game() :
    print("Press <ENTER> to start")
    inp=input()

    if inp.upper() == "Q" :
        print("Are You sure to Quit ?    :   Y or N")
        dec = input()
        if dec.upper() == "Y":
            print("...OK...")
            exit()
        else :
            print("Redirecting...")
            game()
    elif checkStartCorrect(inp):
        print("....Wrong Input....")
        game()
    else:
        print("Game Rules:")
        print("You have to play 10 rounds....The one who scores more wins it!!!")
        print()
        Score_display()
        print()
        t = 10

        while(t>0):
            print("Press 1, 2 or 3 for the following:")
            print("1:Stone")
            print("2:Paper")
            print("3:Scissor")
            print()
            ch=int(input())
            print()
            comp_choice=random.choice(options)
            print("Computer chooses:",comp_choice)
            if ch==1:
                s="STONE"
                print(Name,"chooses:",s)
                if comp_choice=="STONE":
                    print("Same Pick")
                    print()
                    print('After Round -',round,':')
                    Score_display()
                    print()
                    t-=1
                    round+=1
                    continue
                elif comp_choice=="PAPER":
                    computer+=1
                    print("Computer Wins Round:",round)
                else:
                    player+=1
                    print("You Win Round:",round)
            elif ch==2:
                s="PAPER"
                print(Name,"chooses:",s)
                if comp_choice=="STONE":
                    player+=1
                    print("You Win Round:",round)
                elif comp_choice=="PAPER":
                    print("Same Pick")
                    print()
                    print('After Round -',round,':')
                    Score_display()
                    print()
                    t-=1
                    round+=1
                    continue
                else:
                    computer+=1
                    print("Computer Wins Round:",round)
            elif ch==3:
                s="SCISSOR"
                print(Name,"chooses:",s)
                if comp_choice=="STONE":
                    computer+=1
                    print("Computer Wins Round:",round)
                elif comp_choice=="PAPER":
                    player+=1
                    print("You Win Round:",round)
                else:
                    print("Same Pick")
                    print()
                    print('After Round -',round,':')
                    Score_display()
                    print()
                    t-=1
                    round+=1
                    continue
            else:
                print("Wrong Choice!!!")
                exit()
            print('After Round -',round,':')
            Score_display()
            print()
            t-=1
            round+=1
        print("Final Score:")
        print("Computer:",computer," ",Name,":",player)
        if player>computer:
            print(Name,"is winner!!!")
        elif computer>player:
            print("Computer is winner!!!")
        else:
            print("DRAW!!!")