from random import randint

from gameComponents import gameVars, winLose, game

def gamePlay():

    # this is choice code
    print("R-O-C-K    P-A-P-E-R    S-C-I-S-S-O-R-S")
    print("----------------------------------------")
    print("Current Computer Lives: ", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Current Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
    print("----------------------------------------")
    print(" --- CHOOSE Y'UR WEAPON SOLDIER --- ")
    print("----------------------------------------")


#if input is other than choices, tell player to pick a suitable option

  
    gameVars.player = input("Choose rock paper or scissors: ")


    computerPlayer = gameVars.choices[randint(0,2)]


    # if player chooses to quit dont do anything
    # just exit

    if gameVars.player == "quit":
        print("You chose to quit")
        exit()

    #print output
    # line
    print("User chose: " + gameVars.player)

    #validate
    print("AI chose: " + computerPlayer)

    if(computerPlayer == gameVars.player):
        print("tie")

    elif(gameVars.player == "gun"):
        print("YOU ARE VICTOR, COMRAD")
        exit()
    
    # always check for negative conditions 
    elif(computerPlayer == "rock"):
        if(gameVars.player == "scissors"):
            gameVars.player_lives -= 1
            print("Round Lost, player lives: ", gameVars.player_lives)
        else:
            print("Round Won")
            gameVars.computer_lives -= 1

    elif(computerPlayer == "paper"):
        if(gameVars.player == "rock"):
            gameVars.player_lives -= 1
            print("Hand Lost, player lives:", gameVars.player_lives)
        else:
            print("Round Won")
            gameVars.computer_lives -= 1

    elif(computerPlayer == "scissors"):
        if(gameVars.player == "paper"):
            gameVars.player_lives -= 1
            print("Hand lost, player lives:", gameVars.player_lives)
        else:
            print("Round Won")
            gameVars.computer_lives -= 1