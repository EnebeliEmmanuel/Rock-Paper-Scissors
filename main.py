import random


def gameplay():
    
    # introduction to the rules of the game
    print("""
    Welcome to Rock, Paper, Scissors!!\n
    These are the rules of the game pay attention and goodluck:
    - Rock vs Paper = Paper wins
    - Rock vs Scissors = Rock wins
    - Paper vs Scissors = Scissors wins
        """)

    # list of available options
    options = ["R", "P", "S"]

    # prompt gamer to enter their choice
    # if user types R or P or S, the program will continue
    # if user types an invalid option, the program will prompt the user to enter a valid option
    gamer = input("Enter your choice: ")
    while gamer not in options:
        gamer = input("Please enter a valid response: ")


    # if gamer types in R, the gamer chooses rock
    # if gamer types in P, the gamer chooses paper
    # if gamer types in S, the gamer chooses scissor    
    if gamer == "R":
        gamer = "Rock"
    elif gamer == "P":
        gamer = "Paper"
    else:
        gamer = "Scissors"

    # computer selects randomly from the available options
    cpu = random.choice(options)

    # if computer chooses R, the computer chooses rock
    # if computer chooses P, the computer chooses paper
    # if computer chooses S, the computer chooses scissor
    if cpu == "R":
        cpu = "Rock"
    elif cpu == "P":
        cpu = "Paper"
    else:
        cpu = "Scissors"

    # print options chosen by the player and computer
    print(f"\nGamer ({gamer}) : CPU ({cpu})")


    # if both gamer and computer choose the same option, it is a tie
    # The game would restart until one of the gamers wins
    if gamer == cpu:
        print("It's a tie! You have to try again!")
        gameplay()

    # if gamer chooses rock and computer chooses paper, gamer wins
    # if gamer chooses rock and computer chooses scissors, gamer loses
    elif gamer == "Rock":
        if cpu == "Scissors":
            print(f"Rock smashes scissors! Gamer({gamer}) wins!\n")
        else:
            print(f"Paper covers rock! CPU({cpu}) wins!\n")

    # if gamer chooses paper and computer chooses rock, gamer wins
    # if gamer chooses paper and computer chooses scissors, gamer loses
    elif gamer == "Paper":
        if cpu == "Rock":
            print(f"Paper covers rock! Gamer({gamer}) wins!\n")
        else:
            print(f"Scissors cuts paper! CPU{(cpu)} wins!\n")

    # if gamer chooses scissors and computer chooses rock, gamer loses
    # if gamer chooses scissors and computer chooses paper, gamer wins
    elif cpu == "Paper":
        print(f"Scissors cuts paper! Gamer({gamer}) wins!\n")
    else:
        print(f"Rock smashes scissors! CPU({cpu}) wins!\n")
       
       
# function to start the game
gameplay() 