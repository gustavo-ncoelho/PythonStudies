import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None      #setar variavel player antes do while

    while player not in choices:    #se player não estiver em choices, repetir...
        player = input("rock, paper or scissors ?: ").lower()     #.lower para transformar o input em minusculo e ficar igual a lista choices

    def show():
        print("computer: ",computer)
        print("player: ",player)

    if player == computer:
        show()
        print("Tie!!!")
    elif player == "rock":
        if computer == "scissors":
            show()
            print("You WIN!!!")
        elif computer == "paper":
            show()
            print("You LOSE!!!!")
    elif player == "paper":
        if computer == "rock":
            show()
            print("You WIN!!!")
        elif computer == "scissors":
            show()
            print("You LOSE!!!!")
    elif player == "scissors":
        if computer == "paper":
            show()
            print("You WIN!!!")
        elif computer == "rock":
            show()
            print("You LOSE!!!!")
    
    playAgain = None
    while playAgain != "yes" and playAgain != "no":
        playAgain =  input("Do you want to play again ? (yes/no) ").lower()
    
    if playAgain != "yes":
        break

print("Bye, thanks for playing")
