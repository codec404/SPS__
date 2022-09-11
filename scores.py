def scoreboard(name,score) :
    fWrite = open("Scores.txt","a")
    fWrite.write(name+"  :  "+str(score)+"\n")
    fWrite.close()
    fRead = open("Scores.txt","r")
    lines = fRead.readlines()

    for line in lines :
        print(line)
    fRead.close()