import random
#python -m pip install "name" to download modules
def main():
    player_score = 0
    pc_score = 0

    #1 = rock, 2 = paper, 3 = scissors

    #border
    print("============================================================================================")
    print("============================================================================================")

    #input and input check
    while (player_score < 3) or (pc_score < 3): #if The score is less than 3 to each player stop the game
        player_choice = int(input("\nMake your choice!\n 1 - Rock\n 2 - paper\n 3 - scissors\n\n My choice:"))
        while player_choice < 0 or player_choice > 3: #Input check
            player_choice = int(input("Invalid choice! choose again: \n1 - Rock\n2 - paper\n3 - scissors\n\n My choice:"))

        #dispay of user choice
        if player_choice is 1:
            print("\n You chose Rock\n")
        if player_choice is 2:
            print("\n You chose Paper\n")
        if player_choice is 3:
            print("\n You chose Scissors\n")

        pc_choice = random.randint(0,3) #pc choice

        if player_choice is 1 and pc_choice is 2: #player rock, pc paper
            pc_score += 1
        if player_choice is 1 and pc_choice is 3: #player rock , pc scissors
            player_score += 1
        if player_choice is 2 and pc_choice is 1: #player paper, pc Rock
            player_score += 1
        if player_choice is 2 and pc_choice is 3: #player  paper , pc scissors
            pc_score += 1
        if player_choice is 3 and pc_choice is 1: #player scissors, pc rock
            pc_score += 1
        if player_choice is 3 and pc_choice is 2: #player scissors, pc paper
            player_score += 1


        #display of pc's choice
        if(pc_choice is 1): #pc choice output
            print(" The pc choice was - Rock")
        if (pc_choice is 2):
            print(" The pc choice was - Paper")
        if (pc_choice is 3):
            print(" The pc choice was - Scissors")

        print("\n player score: " +  str(player_score) + "\n pc score: " + str(pc_score) +"\n") #score print
        
        if (player_score is 3):
            print("The player has won!")
            break

        if (pc_score is 3):
            print("The PC has won!")
            break

        print("============================================================================================")
        print("============================================================================================")

if __name__ == "__main__":
        main()
