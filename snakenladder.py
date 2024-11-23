# Snake n Ladder...

import random
def roll():
    dice=random.randint(1,6)
    return dice
def  snakeandladder():
    number=int(input("Enter the number of players: "))
    pos=[]
    for i in range(number):
        pos.append(0)
    while True:
        for i in range(number):
            input(f"Player {i+1}: Press enter to roll the dice ")
            rolldice=roll()
            print("You got",rolldice)
            newpos=pos[i]+rolldice
            if newpos>100:
                print(f"Movement to {newpos} not possible")
                print("Wait for next turn...\n")
            else:
                if newpos==15:
                    newpos=7
                    print("You have encountered Snake! Dropped to",newpos)
                elif newpos==23:
                    newpos=3
                    print("You have encountered Snake! Dropped to",newpos)
                elif newpos==46:
                    newpos = 12
                    print("You have encountered Snake! Dropped to",newpos)
                elif newpos==62:
                    newpos=35
                    print("You have encountered Snake! Dropped to",newpos)
                elif newpos==90:
                    newpos=1
                    print("You have encountered Snake! Dropped to ",newpos)
                elif newpos==3:
                    newpos=16
                    print("You have found a Ladder to",newpos)
                elif newpos==24:
                    newpos=82
                    print("You have found a Ladder to",newpos)
                elif newpos==32:
                    newpos=58
                    print("You have found a Ladder to",newpos)
                elif newpos==57:
                    newpos=73
                    print("You have found a Ladder to",newpos)
                elif newpos==68:
                    newpos=99
                    print("You have found a Ladder to",newpos)
                elif newpos==88:
                    newpos=91
                    print("You have found aLadder to",newpos)
                pos[i]=newpos
                print(f"Player {i+1} have moved to: {newpos}")
                print()
                if newpos==100:
                    print("\tGreat! You have reached 100.")
                    return
                  
snakeandladder()
