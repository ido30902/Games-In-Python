import random

# Reload -  defend - shoot

def main():

    #integers
    player_choice = 0
    pc_choice = 0

    #objects
    player  = Player()
    pc = Player()

    #main loop
    while pc.isAlive and player.isAlive: # if the score for each one of the players is less then 3 the game continues

        printBorder()

        #player's choice + input check
        player_choice = playerInputCheck(player)

        #pc's random check + choice
        pc_choice = pcInputCheck(pc)

        #   Reload - 1
        #   Defend - 2
        #   Shoot -  3

        #checks the scenerio
        if pc_choice is 2:
            pc.num_of_defences = pc.num_of_defences + 1

        if player_choice is 2:
            player.num_of_defences = player.num_of_defences + 1

        if player_choice is 1:
            player.num_of_bullets = player.num_of_bullets + 1
            player.num_of_defences = 0

        if pc_choice is 1:
            pc.num_of_bullets = pc.num_of_bullets + 1
            pc.num_of_defences = 0

        if player_choice is 3 and pc_choice is 1:
            player.num_of_bullets = player.num_of_bullets - 1
            pc.isAlive = False
            print("\n PC had died, You have won the game!")

            if(checkIfWantsRestart()):
                restartGame()

        if pc_choice is 3 and player_choice is 1:
            player.num_of_bullets = player.num_of_bullets - 1
            player.isAlive = False
            print("\n Player had died")

            if(checkIfWantsRestart()):
                restartGame()

            if player_choice is 3 and pc_choice is 2:
                player.num_of_bullets = player.num_of_bullets - 1
                print("\n The PC was saved by the shield!")

            if pc_choice is 3 and player_choice is 2:
                player.num_of_bullets = player.num_of_bullets - 1
                print("\n The Player was saved by the shield!")

            if pc_choice is 3 and player_choice is 3:
                player.isAlive = False
                pc.isAlive = False
                print("\n Game ended, both players lost!")

                if(checkIfWantsRestart()):
                    restartGame()


        #prints the stats
        printStats(player,player_choice,player,pc)

#functions

def checkIfWantsRestart():
    ans = str(input(" Do you want a restart? y/n \n\n-"))

    while (ans is not "y") and (ans is not "n") and (ans is not "Y") and (ans is not "N"):
        ans = str(input(" Do you want a restart? y/n \n\n-"))

    if ans is "y" or ans is "Y":
        return True
    else:
        return False

#prints the player stats
def printStats(player):
    print("\n Number of bullets: " + str(player.num_of_bullets) + "\n Defended in a row: " + str(player.num_of_defences))

#prints a border
def printBorder():
    print("==============================================================================")
    print("==============================================================================")

#restarts the game
def restartGame(player, pc):
    #player restart
    player.num_of_bullets = 0
    player.isAlive = true
    player.num_of_defences = 0

    #pc restart
    pc.num_of_bullets = 0
    pc.isAlive = true
    pc.num_of_defences = 0

#checks the player's input
def playerInputCheck(player):
        player_choice = int(input("\n Make your choice!\n 1 - Reload\n 2 - defend\n 3 - Shoot\n My choice: "))

        while player_choice < 1 or player_choice > 3:  # Input check
            player_choice = int(input("\n Invalid choice! choose again: \n1 - Reload\n2 - defend\n3 - Shoot \n My choice: "))

        while player_choice is 3 and player.num_of_bullets is 0: #Cant shoot without bullets
            player_choice = int(input("\n You don't have ammo! \nchoose again: \n1 - Reload\n2 - defend\n3 - Shoot \n My choice: "))

        while player.num_of_defences is 3 and player_choice is 2: #too much defence blocker
            player_choice = int(input("\n You cant defend 3 times in a row!\nchoose again: \n1 - Reload\n2 - defend\n3 - Shoot \n  My choice: "))

        return player_choice

#checks the pc random
def pcInputCheck(pc):
    pc_choice = pc_choice = random.randint(0,3)

    while (pc_choice is 3) and pc.num_of_bullets <= 0: #shoots with no bullets
        pc_choice = random.randint(0,3)

    while (pc_choice is 2) and pc.num_of_defences is 3: #defends with 3 defenced previously
        pc_choice = random.randint(0,3)

    return pc_choice

#classes
class Player:
        def __init__(self):
            self.num_of_bullets = 0
            self.isAlive = True
            self.num_of_defences = 0

if __name__ == '__main__':
    main()
