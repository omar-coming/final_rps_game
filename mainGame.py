#reimport variables from external file 
from gameComponents import gameVars, winLose, game


#run game
while gameVars.player is False:
    game.gamePlay()


#check player lives and ai lives

    if gameVars.player_lives is 0:
        winLose.winorlose("lost")

    elif gameVars.computer_lives is 0:
        winLose.winorlose("won")

    else:
        gameVars.player = False