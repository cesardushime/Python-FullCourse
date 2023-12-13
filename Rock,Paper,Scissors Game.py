import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()
    if player == computer:
        print("computer: ", computer)
        print("Player: ", player)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye! It's been a superb experience playing with you!!!")


