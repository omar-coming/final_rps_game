from gameComponents import gameVars, game

#define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    #print("called winorlose", status)

    if status == "won":
        pre_message = "!!! -- YOU ARE KING IN THE CASTLE -- !!!"
        print(pre_message + "Play Again?")
    else:
        pre_message = "LOST TO A COMPUTER"
        print(pre_message + " dl0__0lb " + " ha ha ha ha ")
        print("Play Again?")

    choice = input("Y / N")

    if choice == "Y" or choice == "y":
        
        gameVars.player_lives = 5
        gameVars.computer_lives = 5
        gameVars.player = False

    elif choice == "N" or choice == "n":
        # exit message and quit
        print("Git gud son")
        exit()
    else:
        print("Make a valid choice - Y or N")
        # this is generating a bug
        choice = input("Y / N")